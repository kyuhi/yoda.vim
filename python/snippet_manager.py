import re

class SnippetManager( object ):
  def __init__( self ):
    self.snippet_engines = dict( ultisnips=UltiSnipsSnip )
    self.snippet = _NopSnip()

  def Get( self ):
    return self.snippet

  def Init( self, engine_name ):
    if engine_name not in self.snippet_engines:
      return
    if engine_name == 'ultisnips':
      try:
        from UltiSnips import UltiSnips_Manager
        UltiSnipsSnip.Manager = UltiSnips_Manager
        self.snippet = UltiSnipsSnip()
      except ImportError:
        raise ImportError( 'Ultisnips snippet not found' )
    else:
      self.snippet = self.snippet_engines[ engine_name ]



# Snippet class requires to define method Trigger().
# Trigger() method expands given placeholder text if expandable.
# return 1 if placeholder is expanded otherwise 0.
class _NopSnip( object ):
  def Trigger( self ):
    return 0

  def CanSnip( self ):
    return False


class UltiSnipsSnip( _NopSnip ):
  RX = re.compile( r'(\{#[^{]*#\})' )
  RX_IN = re.compile( r'\{#([^{]*)#\}' )
  Manager = None # to be expected to assign `UltiSnips_Manager`

  def CanSnip( self ):
    return True

  def Trigger( self, pre, placeholder, post ):
    self.Manager.expand_anon( pre + self.yoda2US( placeholder ) + post )
    return 1

  def yoda2US( self, placeholder ):
    # make yoda placeholder into ultisnips syntax
    results = []
    count = 1
    for w in self.RX.split( placeholder ):
      m = self.RX_IN.match( w )
      if m:
        w = '${{{}:{}}}'.format( count, m.group(1) )
        count += 1
      results.append( w )
    return ''.join( results )


