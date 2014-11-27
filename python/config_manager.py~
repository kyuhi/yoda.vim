import os
import imp

class ConfigManager( object ):
  '''\
  Manage compilation flags for each files of directories.
  The object of this class expect to be used singleton object.
  '''
  def __init__( self ):
    self._flags_of_filenames = {}
    self._default_basename = ''
    self._default_funcname = ''


  def Init( self, basename, funcname ):
    self._default_basename = basename
    self._default_funcname = funcname


  def Register( self, filename, param ):

    config_filename = self.ConfigFileForFileName( filename )
    if not config_filename: # file does not exist
      self._flags_of_filenames[ filename ] = None
      return False
    # execute function of module 
    module = None
    flags = None
    try:
      module = imp.load_source( 'yoda' + GenRandomName(), config_filename )
      flags = getattr( module, self._default_funcname )( param )
    except Exception as e: # failed to get flags of function
      self._flags_of_filenames[ filename ] = None
      raise Exception( 'failed to load file "{}". reason = {}'.format(
              config_filename, str(e) ) )
    finally:
      del module
    # validate flags
    if not IsListOfStrs( flags ):
      self._flags_of_filenames[ filename ] = None
      raise TypeError( 'flaga must be list of string' )

    # register flags of filename
    self._flags_of_filenames[ filename ] = flags
    return True


  def CompilationFlags( self, filename ):
    return self._flags_of_filenames.get( filename )


  def ConfigFileForFileName( self, filename ):
    return FindFileToUpperDirs( os.path.dirname( filename ),
                                self._default_basename )


def IsListOfStrs( any ):
  if not isinstance( any, list ):
    return False
  return all( isinstance(obj, str) for obj in any )


def FindFileToUpperDirs( rootdir, basename ):
  for d in ParentDirs( rootdir ):
    path = os.path.join( d, basename )
    if os.path.isfile( path ):
      return path
  return ''


def ParentDirs( dirname ):
  while True:
    yield dirname
    parent = os.path.dirname( dirname )
    if parent == dirname:
      raise StopIteration
    dirname = parent


def GenRandomName( n=8 ):
  import string, random
  if n > 0: n -= 1
  letters = string.ascii_letters + string.digits
  name = ''.join( random.sample( letters, n ) )
  return random.choice( string.ascii_letters ) + name


# vim:et:ts=2 sts=2 sw=2
