A VIM plug-in for completion using libclang
===========================================

Yoda-vim is a Vim plug-in for code completion using libclang. Yoda-vim's features are:

- Fast code completion for C/C++ and Objective-C/C++.
- Load compilation options using your python configuration file influenced by [YouCompleteMe](https://github.com/Valloric/YouCompleteMe).
- Jump to definition or declaration under the cursor of the editing file.
- Show code diagnostics in Vim's `quickfix-window` or you can use it via API as you want.
- Automatically insert variable segments, substring of text of candidate
supporting snake case and camel case, by one keystroke in completion (Like XCode behaivior).
- Support code snippets if you have installed [ultisnips](https://github.com/SirVer/ultisnips).
- Works on python2 and python3.

Below gif picture demonstrates the variable segments insertion with `<tab>` key.  
![variable segments demo](http://i.imgur.com/AR2mvgl.gif)


There are various code completion plug-ins using [clang](http://clang.llvm.org)
like [clang_complete](https://github.com/Rip-Rip/clang_complete),
[YouCompleteMe](https://github.com/Valloric/YouCompleteMe), etc.
However, these are usefull, why did I make this plug-in and who should use this?
- I want to write Objective-C code in Vim.
- I want to reduce typing when searching completion.
- I want to use multi-byte string in code.
- My Vim compiled with +python3.
- clang_complete does not support ignorecase completon.
- YouCompleteMe forces fuzzy completion, but I want just use clang's completion engine.
- Many of the completion plug-ins with the similar settings like popupmenu,
preview window, etc. This causes too long `.vimrc` and to spend time users to
write similar settings. I think plug-ins should be compatible with Vim's option,
or delegate to a special purpose plug-in when Vim does not have such features.


Requirements
------------
- Yoda.vim has tested in linux and MacOSX platform.
- Vim version 7.4 or above and has compiled with +python or +python3.
- [libclang.(so | dylib)](http://clang.llvm.org) (3.5 is recommended.)
- [ultisnips](https://github.com/SirVer/ultisnips) (Optional: Expand snippets like function arguments, template parameters, etc)


Quick Start
-----------
To use yoda-vim for completions, you have to do are folowings:
  1. Add yoda-vim in Vim runtime path manually or using plug-in manager like [Vundle](https://github.com/gmarik/Vundle.vim).
  2. Tell yoda-vim where a clang dynamic library is.
  3. Write python configuration file of `.yoda_config.py` for your project.

Python configuration file is a python file, default basename is
`.yoda_config.py` set by `g:yoda_config_basename`, should give clang
compilation flags of the editing file.  Yoda-vim search the file in the
directory or above it in the hierachy when a new C-fammily file read. And it
will call function, default name is `Flags` set by `g:yoda_config_funcname`,
using vim's information as it's argument, you can set it via
`g:yoda_config_pass_arg`, to give clang the flags. Folowing is an example.

### A Recipe For Configuration

In your `.vimrc`.
```vim
" Set full path of clang library path.
" You do not have to set this configuration if you have installed `llvm-config` in your $PATH.
" For more ditails, see option 'g:yoda_clang_library'.
let g:yoda_clang_library = '/path/to/clang-library'

" Set snippet engine if ultisnips is in your Vim runtime
let g:yoda_snippet_engine = 'ultisnips'

" Specify the function argument to give it `.yoda_config.py`.
" NOTE: This example set string of dict. You can also set any evaluatable strings
" like global functions, list, etc. (default is `'expand("%:p")'`)
let g:yoda_config_pass_arg = 
\  "{'filename' : expand('%:p'),"
\ . "'filetype' : &l:filetype}"
```

In `.yoda_config.py`.
```python
import os

def Flags( fileinfo ):
  '''
  The function is called when yoda-vim read a new C-fammily file.
  It has to return compilation flags for clang, may return only flags related
  to syntax.
  It can return None if you want to disable the completion in the editing file.
  '''
  filename = fileinfo['filename']
  filetype = fileinfo['filetype']

  # Disable completion if `filename` is above your home directory.
  # NOTE: This is an example. You can remove this block as you want.
  if not filename.startswith( os.path.expanduser('~/') ):
    return None

  # Get compilation flags related to a `filetype`.
  # NOTE: Clang does not know filetype of editing file. So you should tell
  # clang its filetype using compilation flags, e.g. '-x', 'LANG(c++, c, etc.)'
  # and '-std=WHAT(c99, c++, etc.)'.
  # Because this is an example, you should add suitable compilation flags
  # for your project.
  common_flags = ['-Wall', '-I' + os.path.dirname( filename )]
  ft_flags = dict( 
    c=['-x', 'c', '-std=c99'],
    cpp=['-x', 'c++', '-std=c++11'],
    objc=['-x', 'objective-c', '-std=c99', '-fobjcarc'],
    objcpp=['-x', 'objective-c++', '-std=c++11', '-fobjcarc'],
  )
  return common_flags + ft_flags[ filetype ]
```

Commands
--------
### The `:YodaGoto [where]` command
Go to the location to definition or declaration under the cursor if possible.
The argument of `where` is where to jump. It is supposed to be `'Definition'`
or `'Declaration'`.  If no arguments are given. Go to the declaration.


### The `:YodaShowErrors` command
Set quickfix list of diagnostics in current buffer and open its window.
If you want to know about quickfix, See `:help quickfix`.


Options
-------
### The `g:yoda_clang_library` option
This option specifies a path to a clang dynamic library file. 
If the option is not set. The followings are used for searching the library.
  1. Tries to search the library in the directory using `llvm-config --libdir` if possible.
  2. Tries to search it in the directories of `$LD_LIBRARY_PATH`.
  3. Discontinue the searching.

Type: str  
Default: `''`  


### The `g:yoda_super_trigger_key` option
This option controls the key mapping used to trigger the first completion string
in completion popup menu. How to insert text has multiple state.
  1. If snippet is enabled and inserted text matches completion exactly, expand its snippet.
  2. If completion candidate is not selected and only one candidate exists,
insert this text.
  3. If completion candidate is not selected, insert text to next variable segments (XCode like behaivior).

Type: str  
Default:`'<Tab>'`


### The `g:yoda_window_split_behavior` option
This option controls how to open a new window when `:YodaGoto` command is invoked.

Type: str  
Default: `'split'`  
Supported behaiviors: `'edit'`, `'split'`, `'vsplit'`


### The `g:yoda_config_basename` option
This option specifies a basename of python configuration file.

Type: str  
Default: `'.yoda_config.py'`

### The `g:yoda_config_funcname` option
This option specifies a name of function in python configuration file to be used
to set compilation flags for current buffer.

Type: str  
Default: `'Flags'`


### The `g:yoda_config_pass_arg` option
This option is used to pass argument for function in python configuration file.
The option evaluate when new buffer is opened.

Type: str  
Default: `'expand("%:p")'`


### The `g:yoda_snippet_engine` option
This option select a snippet engine to use expand placeholder of completion.

Supported snippet engines: `"ultisnips"`  
Type: str  
Default:`''`


### The `g:yoda_snippet_space_in_parenthes` option
This option enable to insert spaces in parenthes when snippet trigger.

Type: int  
Default: `0`


Functions
---------
### The `yoda#diagnostic_qflist()` function
Get diagnostics of quick fix list of current buffer.
If you want to know about its format, See `:help setqflist()`.

Return: list

### The `yoda#location_to( where )` function
Get location under the current cursor.

Return: dict  
Argument `where`: where to location (str)  
Supported locations: `'Definition'`, `'Declaration'`

TODO
----
- Add more platforms tested (Yoda.vim has been tested on Ubuntu, MacOSX).
- Yoda.vim can crash while parsing.
- Yoda.vim consume large memory.
- Support any string encodings. (It has tested only UTF-8).

License
-------
This software is licensed under the [MIT license](http://opensource.org/licenses/MIT)  
Copyright (C) 2014 by Kaika Yuhi

This plug-in includes a function part of code snippets from [jedi-vim](https://github.com/davidhalter/jedi-vim) for python/vim unicode support.
The jedi-vim is also licensed under the MIT license. See [LICENSE.txt](https://github.com/davidhalter/jedi-vim/blob/master/LICENSE.txt).
