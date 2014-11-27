if has( 'g:loaded_yoda' ) && g:loaded_yoda != 0
    finish
endif

augroup YodaPlugin
    autocmd!
    autocmd FileType c,cpp,objc,objcpp :call yoda#on_filetype()
augroup END

let g:loaded_yoda = 1
