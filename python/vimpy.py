import vim
import sys

py_version = sys.version_info[0]
if py_version >= 3:
    unicode = str
is_py3 = py_version == 3

### The software uses a function part of code snippts of [jedi-vim](https://github.com/davidhalter/jedi-vim) for python/vim unicode support.
# The MIT License (MIT) 

# Copyright (c) 2013 David Halter and others, see [AUTHORS.txt](https://github.com/davidhalter/jedi-vim/AUTHORS.txt)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
class PythonToVimStr(unicode):

  """ Vim has a different string implementation of single quotes """
  __slots__ = []

  def __new__(cls, obj, encoding='UTF-8'):
    if is_py3 or isinstance(obj, unicode):
      return unicode.__new__(cls, obj)
    else:
      return unicode.__new__(cls, obj, encoding)

  def __repr__(self):
    # this is totally stupid and makes no sense but vim/python unicode
    # support is pretty bad. don't ask how I came up with this... It just
    # works...
    # It seems to be related to that bug: http://bugs.python.org/issue5876
    if unicode is str:
      s = self
    else:
      s = self.encode('UTF-8')
    return '"%s"' % s.replace('\\', '\\\\').replace('"', r'\"')
### end


class VimPy( object ):

  def __getattr__( self, key ):
    caller = lambda *args: self.Call( key, *args )
    setattr( self, key, caller )
    return caller

  def Return( self, func ):
    import functools
    @functools.wraps( func )
    def wrapper( *args, **kwargs ):
      return VimPy.Py2Vim( func( *args, **kwargs ) )
    return wrapper

  @staticmethod
  def Py2Vim( result ):
    if isinstance( result, str ):
      return PythonToVimStr( result )
    elif isinstance( result, (int, float) ):
      return result
    elif isinstance( result, dict ):
      return dict( ( VimPy.Py2Vim( k ), VimPy.Py2Vim( v ) )
                     for k, v in result.items() )
    elif isinstance( result, list ) or hasattr( result, '__iter__' ):
      return list( VimPy.Py2Vim( item ) for item in result )
    elif None is result:
      return 0
    elif isinstance( result, bool ):
      return int( result )
    raise TypeError( 'invalid type {}'.format( type(result) ) )

  @property
  def Exception( self ):
    return vim.error

  @property
  def Line( self ):
    return vim.current.line

  @Line.setter
  def Line( self, line ):
    vim.current.line = line

  @property
  def LineNum( self ):
    return vim.current.window.cursor[0]

  @LineNum.setter
  def LineNum( self, line_num ):
    vim.current.window.cursor = line_num, vim.current.window.cursor[1]

  @property
  def ColNum( self ):
    return vim.current.window.cursor[1]

  @ColNum.setter
  def ColNum( self, col_num ):
    vim.current.window.cursor = vim.current.window.cursor[0], col_num

  @property
  def Buffer( self ):
    return '\n'.join( vim.current.buffer[:] + ['\n'] )

  @property
  def BufferAsList( self ):
    return vim.current.buffer[:]

  @property
  def FileName( self ):
    return vim.current.buffer.name

  def Command( self, commandstr ):
    vim.command( PythonToVimStr( commandstr ) )

  def Eval( self, eval_str ):
    return vim.eval( PythonToVimStr( eval_str ) )

  def Call( self, funcname, *args ):
    args_str = ','.join( repr( VimPy.Py2Vim(a) ) for a in args )
    return vim.eval( funcname + '(' + args_str + ')' )

  def Get( self, name ):
    try:
      return int( vim.eval( name ) )
    except ValueError:
      return vim.eval( name )

  def Set( self, key, value ):
    vim.command( 'let {} = {}'.format( key, repr( VimPy.Py2Vim(value) ) ) )

# vim:et:ts=2 sts=2 sw=2
