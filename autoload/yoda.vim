let s:save_cpo = &cpo
set cpo&vim

if !has( 'python' ) && !has( 'python3' )
  echomsg
  \   "No python support available. "
  \ . "Compile VIM --with-python 2 or 3 if you want to use yoda."
  let s:failed_inited = 1
elseif v:version < 704
  echomsg
  \ 'yoda.vim required VIM(7.4 or above). Code completion OFF'
  let s:failed_inited = 1
endif


" yoda.options {{{1

" Snippet:
" snippet engine name. now support 'ultisnips'
let g:yoda_snippet_engine = 
\ get( g:, 'yoda_snippet_engine', '' )
" enable insert spaces in parenthes
let g:yoda_snippet_space_in_parenthes =
\ get( g:, 'yoda_snippet_space_in_parenthes', 0 )

" Key Mappings:
" key for trigger in completion.
let g:yoda_super_trigger_key =
\ get( g:, 'yoda_super_trigger_key', "<Tab>" )

" Clang:
" filename to clang dynamic library.
let g:yoda_clang_library =
\ get( g:, 'yoda_clang_library', '' )
let g:yoda_greedy_reparsing = 
\ get( g:, 'yoda_greedy_reparsing', 1 )
let g:yoda_shutup_when_loaded =
\ get( g:, 'yoda_shutup_when_loaded', 0 )

" Goto:
" how to open new window when user go to other buffer.
let g:yoda_window_split_behavior =
\ get( g:, 'yoda_window_split_behavior', 'split' ) " (edit | split | vsplit)


" Configuration File:
" base name of python configuration file.
let g:yoda_config_basename =
\ get( g:, 'yoda_config_basename', '.yoda_config.py' )
" function name to be called in python configuration file.
let g:yoda_config_funcname =
\ get( g:, 'yoda_config_funcname', 'Flags' ) 
" argument of function in python configuration file.
let g:yoda_config_pass_arg =
\ get( g:, 'yoda_config_pass_arg', 'expand("%:p")' ) " filename of curernt
                                                      " buffer


" yoda.filetype {{{1


" plugin starting point.
" called when C-fammily buffers is opened.
func! yoda#on_filetype()

  if exists('s:failed_inited') && s:failed_inited
    return
  endif

  augroup Yoda " set autocommand for the buffer
    " update clang translation unit periodically
    au CursorHold <buffer> call s:vim_on_cursor_hold_normal_mode()
    au CursorHoldI <buffer> call s:vim_on_cursor_hold_insert_mode()
    au InsertLeave <buffer> call s:vim_on_insert_leave()
    " TODO: what is version above?
    au CompleteDone <buffer> call s:vim_on_complete_done()
  augroup end

  " set mapping
  let b:yoda_snip_map = s:map_store_new( g:yoda_super_trigger_key, 'i' )

  setlocal omnifunc=yoda#omni_complete

  " set commands in current buffer
  command! -nargs=? -complete=customlist,s:goto_command_complete -buffer
  \        YodaGoto call s:goto( <f-args> )
  command! -buffer YodaShowErrors call s:show_errors()
  command! -buffer YodaDescription call s:show_description()

  try
    " evaluate argument of function in vim context.
    let config_arg = eval( g:yoda_config_pass_arg )
    YodaPY yoda_vim.VimOnFileType( vim.eval("config_arg") )
  catch /.*/
    call s:echohl('ErrorMsg',
    \             'errors in eval( g:yoda_config_pass_arg )\n\t' . v:exception )
  endtry

endfunc


" yoda.complete {{{1

" to be set omnifunc=
func! yoda#omni_complete( findstart, base )
  if a:findstart
    YodaPY vim.command( 'return {}'.format( yoda_vim.CompleteStart() ) )
  else
    YodaPY vim.command( 'let do_map = {}'.format( yoda_vim.ShouldSnip() ) )
    if do_map
      let funcname = 'vim_on_expand_snippet_pre'
      call b:yoda_snip_map.push(
      \       s:printf( '<c-r>=<SID>%s()<return>', funcname ) )
    endif
    YodaPY vim.command(
    \ 'return {}'.format( yoda_vim.Complete( vim.eval( 'a:base' ) ) ) )
  endif
endfunc


" yoda.trackings {{{1

func! s:vim_on_complete_done()
  call b:yoda_snip_map.pop()
  YodaPY yoda_vim.VimOnCompleteDone()
endfunc


func! s:vim_on_cursor_hold_insert_mode()
  YodaPY yoda_vim.VimOnIdle( False )
endfunc


func! s:vim_on_cursor_hold_normal_mode()
  YodaPY yoda_vim.VimOnIdle( True )
endfunc


func! s:vim_on_insert_leave()
  YodaPY yoda_vim.VimOnIdle( False )
endfunc


func! s:vim_on_expand_snippet_pre()
  " Stop monitoring as we'll trigger a snippet
  if pumvisible()
    " Trigger the snippet
    YodaPY vim.command( 'let success = {}'.format( yoda_vim.TriggerSnip() ) )
    return success ? "" : "\<c-y>"
  endif
  return ''
endfun


func! s:map_store_new( key, mode )

  let map_stack = {
  \ 'key' : a:key,
  \ 'mode' : a:mode,
  \ 'original' : maparg( a:key, a:mode ) }

  func! map_stack.push( new_map ) dict
    exec s:printf( 'silent %snoremap <buffer> <silent> %s %s',
    \ self.mode, self.key, a:new_map )
    let self.new_map = a:new_map
  endfunc

  func! map_stack.pop() dict
    if self.original != ''
      exec s:printf( 'silent %snoremap <buffer> <silent> %s %s',
      \ self.mode, self.key, self.original)
    else
      exec s:printf( 'silent %sunmap <buffer> <silent> %s', self.mode, self.key )
    endif
  endfunc

  return map_stack

endfunc


" yoda.quickfix {{{1


func! s:show_errors()
  let qflist = yoda#diagnostic_qflist()
  call setqflist( qflist )
  if empty( qflist )
    cclose
  else
    copen
  endif
endfunc


func! yoda#diagnostic_qflist()
  YodaPY vim.command( 'return {}'.format( yoda_vim.DiagnosticQfList() ) )
endfunc


" yoda.goto {{{1


func! s:goto_command_complete( arg_lead, cmd_line, cursor_pos )
  let candidates = ['Definition', 'Declaration']
  return filter( candidates, 'v:val =~ "^' . a:arg_lead . '"' )
endfunc


func! s:goto( ... )
  if !len( a:000 )
    let where = 'Declaration'
  else
    let where = a:1
  endif

  let location = yoda#location_to( where )
  try
    if empty( location )
      call s:echohl( 'WarningMsg', 'could not find location "%s"', where )
      return ''
    endif
    " location exists
    if bufnr('%') != location.bufnr
      call s:edit( location.filename, g:yoda_window_split_behavior )
    else " found location in the current window
      normal! m'
    endif
    " set cursor for location
    call cursor( location.lnum, location.col )
    " set line at center of window
    normal! zz
  catch /^Vim\%((\a\+)\)\=:E37/
    call s:echohl( 'WarningMsg',
    \              "Failed to goto! Set vim option 'hidden' if you want to go "
    \               "other buffer without saving current buffer." )
  endtry
  return ''

endfunc


func! yoda#location_to( where )
  YodaPY vim.command(
  \ 'return {}'.format( yoda_vim.LocationTo( vim.eval( 'a:where' ) ) ) )
endfunc


" yoda.misc {{{1


func! s:show_description()
  YodaPY yoda_vim.Description()
endfunc


" vim.helper {{{1


func! s:echohl(hl, format, ...)
  try
    exec 'echohl ' . a:hl
    let lines = call( 's:printf', [ 'yoda.vim: ' . a:format ] + a:000 )
    for line in split( lines, "\n" )
      echomsg line
    endfor
  finally
    echohl None
  endtry
endfunc


func! s:printf( format, ... )
  " built-in printf() requires 2 or more argumetns
  if empty(a:000)
    let fmtargs = [a:format . '%s', ''] 
  else
    let fmtargs = [a:format] + a:000
  endif
  return call( 'printf', fmtargs )
endfunc


func! s:exec( format, ... )
  " execute the given command in printf format
  execute call( 's:printf', [ a:format ] + a:000 )
endfunc


func! s:edit( filename, ... )
  let fbufnr = bufnr( a:filename )
  let winnr = bufwinnr( fbufnr )
  if winnr != -1 " window of filename exist so move cursor to the window.
    call s:exec( '%dwincmd w', winnr )
    return
  endif
  let edit_mode = len( a:000 ) > 0 ? a:1 : 'edit'
  for pat in [ '^e\%[dit]$', '^sp\%[lit]$', '^vs\%[plit]$' ]
    if edit_mode =~# pat
      call s:exec( '%s %s', edit_mode, escape( a:filename, '\ ' ) )
      return
    endif
  endfor
  call s:echohl( 'ErrorMsg', 'logic error: invalid mode "%s"', edit_mode )
endfunc


" script.init {{{1


let s:script_directory = escape( expand( '<sfile>:p:h:h' ), '\' )


func! s:init_python_module()
  if exists('s:failed_inited') && s:failed_inited
    delfunction yoda#omni_complete
    delfunction yoda#diagnostic_qflist
    delfunction yoda#location_to
    augroup YodaPlugin
      autocmd!
    augroup END
    return
  endif

  if has( 'python' )
    command! -nargs=1 YodaPY python <args>
  else " python3
    command! -nargs=1 YodaPY python3 <args>
  endif
  YodaPY import sys
  exe 'YodaPY sys.path.insert(0, "' . s:script_directory . '/python")'
  YodaPY import yoda_vim
  YodaPY sys.path.pop( 0 )
  YodaPY vim.command( 'return {}'.format( yoda_vim.VimOnAutoLoad() ) )

endfunc


" load python module
call s:init_python_module()


let &cpo = s:save_cpo
unlet s:save_cpo

" vim:et:ts=2 sts=2 sw=2
