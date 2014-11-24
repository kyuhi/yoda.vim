import vim
import sys

py_version = sys.version_info[0]
if py_version >= 3:
    unicode = str


# the function is taken from 'jedi-vim'
# TODO: paste the Licence
class VimStr( unicode ):
  __slots__ = []
  def __new__( cls, obj, encoding='utf-8' ):
    if py_version == 3 or isinstance( obj, unicode ):
      return unicode.__new__( cls, obj )
    else:
      return unicode.__new__( cls, obj, encoding )

  def __repr__(self):
    if unicode is str: s = self
    else: s = self.encode( 'utf-8' )
    return '"{}"'.format( s.replace('\\', '\\\\').replace('"', r'\"') )


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
      return VimStr( result )
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
    vim.command( VimStr( commandstr ) )

  def Eval( self, eval_str ):
    return vim.eval( VimStr( eval_str ) )

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
