### import {{{1
import re, os, sys, threading, collections
import vimpy
import config_manager
import snippet_manager

### compatibility of python 2 and 3 ### {{{1


if vimpy.py_version >= 3:
  # we must add module dir in system paths in python3.
  yoda_dir = os.path.join( os.path.dirname(__file__), 'yoda' )
  assert os.path.exists( yoda_dir )
  sys.path.insert( 0, yoda_dir )
  import yoda
  sys.path.pop( 0 )
else: # python2
  from yoda import yoda


### vim state ###{{{1


class _State( object ):

  '''\
  State object manage the vim status, thread and validate request for
  index.
  '''

  def __init__( self ):
    self._lock = threading.Lock()
    self._fatal_message = ''
    self.complete_start = 0
    self.config_manager = config_manager.ConfigManager()
    self.snippet_manager = snippet_manager.SnippetManager()
    self.interfaces = []
    self.includes_of_filenames = collections.defaultdict( set )
    self.completions = None


  ### initialize ###
  def Init( self ):
    self.config_manager.Init( Vim.Get( 'g:yoda_config_basename' ),
                              Vim.Get( 'g:yoda_config_funcname' ) )
    try:
      self.snippet_manager.Init( Vim.Get( 'g:yoda_snippet_engine' ) )
    except ImportError as e:
      EchoHL( 'ModeMsg', str(e) )


  ### manage buffer ###
  def IsValid( self, silent=False ):
    def echohl( msg ):
      if not silent: EchoHL( 'ModeMsg', msg )

    flags = self.config_manager.CompilationFlags( Vim.FileName )
    if None is Index:
      echohl( 'Completion is OFF.' )
      return False
    elif None is flags:
      echohl( 'No compilation flags found. '
              'To give clang compliation flags, see :help yoda-quick-start.' )
      return False
    elif self._fatal_message:
      echohl( self._fatal_message )
      self._fatal_message = None
      return False
    return True


  ### fatal state ####
  def SetFatal( self, message ):
    self._fatal_message = message


  ### threading ###
  def Lock( self ):
    return self._lock


  def IsParsing( self ):
    if not self._lock.acquire( False ):
      return True
    else:
      self._lock.release()
      return False


  ### request data ###
  def RequestData( self ):
    compilation_flags = self.config_manager.CompilationFlags( Vim.FileName )
    unsaved_files = [ ( Vim.FileName, Vim.Buffer ) ]
    # vim cursor line starts from 1, but it's column starts from 0!
    return dict(
        filename = Vim.FileName,
        line_num = Vim.LineNum,
        column_num = Vim.ColNum+1,
        unsaved_files = unsaved_files,
        num_unsaved_flies = len( unsaved_files ),
        compilation_flags = compilation_flags,
        num_compilation_flags = len( compilation_flags ) )


### autocmd ### {{{1


State = _State()
Index = None
Vim = vimpy.VimPy()


def VimOnAutoLoad():
  global Index
  try:
    library_filename = _FindClangLibrary( Vim.Get( 'g:yoda_clang_library' ) )
    if not Vim.Get( 'g:yoda_clang_library' ):
      Vim.Set( 'g:yoda_clang_library', library_filename )
    State.Init()
    if not library_filename:
      EchoHL( 'ModeMsg',
          'g:yoda_clang_library({}) is not set or is invalid. Disable completion. '
          'See :help yoda-quick-start'.format( library_filename ) )
      return 0
    yoda.Initialize( library_filename )
    Index = yoda.Index.make()
  except Exception:
    import traceback
    EchoHL( 'WarningMsg',
            '\n[failed to load clang library]\nreason: {}'.format(
            traceback.format_exc() ) )
    return 0
  return 1


def VimOnFileType( config_param ):
  try: # validate configuration file
    if not State.config_manager.Register( Vim.FileName, config_param ):
      return 0
  except Exception as e:
    EchoHL( 'ErrorMsg', '\nerrors in configuration file\nreason:\n{}'
                        .format( str(e) ) )
    return 0

  if not State.IsValid():
    return

  if not Vim.Get( 'g:yoda_shutup_when_loaded' ):
    EchoHL( 'ModeMsg',
            'load configuration file @{}'.format(
              State.config_manager.ConfigFileForFileName( Vim.FileName ) ) )

  if not State.IsValid():
    return 0

  _ReparseInBackground( True )
  return 1


def VimOnIdle( force ):
  return _ReparseInBackground( force )


def _ReparseInBackground( force ):

  force = Vim.Get( 'g:yoda_greedy_reparsing' ) or force

  if not State.IsValid(silent=True):
    return 0
  if not force and State.IsParsing():
    return 0

  ### check include Experimental:
  includes = set()
  include_rx = re.compile( r'\s*#\s*include\s+[<"](.+)[>"]' )
  for line in Vim.BufferAsList:
    m = include_rx.match( line )
    if m:
      includes.add( m.group(1) )
  past_includes = State.includes_of_filenames[ Vim.FileName ]
  State.includes_of_filenames[ Vim.FileName ] = includes
  if not len( past_includes ^ includes ) and not force:
    return 0

  ### create deamon thread to reparse translation unit
  def reparse( request_data ):
    with State.Lock():
      try:
        tu = Index.translation_unit( request_data )
        tu.reparse( request_data )
      except Exception: ### XXX: the exception must catch!!
        import traceback
        msg = ('\nerror occured in "{}" background thread\n'
               'reason:').format( '_ReparseInBackground()' )
        State.SetFatal( msg + traceback.format_exc() )

  request_data = State.RequestData()
  update_deamon = threading.Thread( target=reparse, args=( request_data, ) )
  update_deamon.daemon = True
  update_deamon.start()

  return 1


### complete ### {{{1


def CompleteStart():

  if not State.IsValid():
    return -1

  l_line = Vim.Line[ : Vim.ColNum ]
  if vimpy.py_version == 2: # TODO: Surrogate pair
    l_line = l_line.decode( 'utf-8' )
  match = re.search( r'(\w+)$', l_line, re.UNICODE )
  State.complete_start = match.start() if match else Vim.ColNum
  return State.complete_start


def Complete( base ):

  if not State.IsValid():
    return []

  if State.IsParsing():
    EchoHL( 'ModeMsg', 'yoda is still parsing. no compeletions yet.' )
    return []

  with State.Lock():
    request_data = State.RequestData()
    tu = Index.translation_unit( request_data )
    State.completions = tu.code_completions( request_data )

  # reduce completions and convert it into list of vim dicts
  completions = State.completions.iterate( base )
  completions = _ConvertFilterCompletions( completions, base )

  # add completions and check to stop completion periodically.
  for i, x in enumerate( completions ):
    if i % 10000 == 0: # TODO: improve performance
      Vim.Command('sleep 100m')
      if Vim.complete_check() != '0':
        break
    Vim.complete_add( x )

  return []


def VimOnCompleteDone():
  State.completions = None


### goto ### {{{1


def LocationTo( kind ):
  'get location to kind'

  if not State.IsValid():
    return {}

  # dict contains translation unit functions of location kinds.
  location_func = dict(
      Declaration = lambda tu, req: tu.declaration_location_info( req ),
      Definition  = lambda tu, req: tu.definition_location_info( req )
  )[ kind ]

  with State.Lock(): # get location
    request_data = State.RequestData()
    tu = Index.translation_unit( request_data )
    location_info = location_func( tu, request_data )

  if not location_info or not location_info.filename:
    return {}

  # convert location_info to vim dict
  return Vim.Py2Vim(
    dict(
      filename = location_info.filename,
      bufnr = Vim.bufnr( location_info.filename ),
      lnum = location_info.line_num,
      col = location_info.column_num
  ) )


### diagnostics ### {{{1


def DiagnosticQfList():
  'get diagnostic quickfix list of current buffer'

  if not State.IsValid():
    return []

  with State.Lock():
    request_data = State.RequestData()
    tu = Index.translation_unit( request_data )
    diagnostics = tu.diagnostics( request_data )

  # converter of diagnostic
  def make( diagnostic ):
    loc = diagnostic.location_info
    return dict(
        bufnr = Vim.bufnr( loc.filename, 1 ),
        lnum = loc.line_num,
        col = loc.column_num,
        text = diagnostic.text,
        type = diagnostic.kind )

  # predicate of diagnostics
  def pred( diagnostic ):
    if diagnostic.kind in ('E', 'W'):
      return True
    return False 

  # filter and map
  return Vim.Py2Vim( make( d ) for d in diagnostics if pred( d ) )


### snippet ### {{{1


def ShouldSnip():
  'whether current state can snippet'
  if not State.IsValid():
    return 0
  return int( State.snippet_manager.Get().CanSnip() )



def TriggerSnip(): ###
  '''
  Trigger snippet which is selected completion of placeholder in insert mode.
  '''
  def divided_by( s, *positions ):
    pos = 0
    result = []
    for p in positions:
      assert pos <= p
      result.append( s[pos:p] )
      pos = p
    result.append( s[pos:] )
    return tuple( result )


  if not State.IsValid() or not State.completions: # this will not return 0
    return 0

  # back up current line for exceptions.
  backup_line = Vim.Line
  backup_colnum = Vim.ColNum
  pre, query, post = divided_by( backup_line, State.complete_start, backup_colnum )

  # vim has prepared to get placeholder for query.
  completions = State.completions

  # search the first completion candidate is matched query.
  # TODO: c++ function overrides have not supported yet.
  completion_info = completions.search( query )
  if not completion_info or not completion_info.has_placeholder():
    # set current line as non query. because clang won't return completions if
    # valid candidate inserted.
    Vim.Line = pre + post
    Vim.ColNum = State.complete_start
    if _FeedKeysForCompletions( completions, query, pre, post ):
      return 1
    else:
      Vim.Line = backup_line
      Vim.ColNum = backup_colnum
      return 0

  # trigger the placeholder.
  placeholder = _FormatPlaceHolder( completion_info.placeholder )
  snip = State.snippet_manager.Get()
  success = 0
  try:
    # trigger snippet. if exception raise or it returns 0, restore current
    # line and return 0(fairure) otherwise return 1(success).
    Vim.Line = ''
    if snip.Trigger( pre, placeholder, post ):
      success = 1
    else:
      success = 1
  except Exception as e:
    EchoHL( 'ErrorMsg', str(e) )
  finally:
    if not success: # error has occured. restore current line
      Vim.Line = backup_line
      Vim.ColNum = backup_colnum
    return success


def _FormatPlaceHolder( placeholder ):

  if not Vim.Get( 'g:yoda_snippet_space_in_parenthes' ):
    return placeholder

  def repl_paren( match ):
    p = match.group(1)
    return '{} {} {}'.format( p[0], p[1:-1], p[-1] )

  reduced = placeholder
  rxs = [ re.compile( r'(\(\{#.*?#\}\))' ), re.compile( r'(<\{#.*?#\}>)' ) ]
  for rx in rxs:
    reduced = rx.sub( repl_paren, reduced )
  return reduced


def _FeedKeysForCompletions( completions, query, pre, post ):
  'return True if inserted.'
  def cased_next( s, query ):
    res = s[ : len( query ) ]
    cases = re.split( r'([A-Z][A-Z]*[a-z]*)|(_)', s[ len(res): ] )
    for case in [ c for c in cases if c ]:
      res += case
      break
    return ''.join( res )

  def feedkeys( s ):
    Vim.feedkeys( s, 'n' )
    # Vim.Line = pre + s + post
    # Vim.ColNum = len( pre+s )

  left, right = completions.binrange( query )
  if left < right \
  and completions[ left ].spelling == completions[ right-1 ].spelling:
    # only one completions
    feedkeys( completions[ left ].spelling )
    return True
  elif (right-left) >= 2: # two or more completions
    keys = cased_next( completions[ left ].spelling, query )
    if keys == query or not keys:
      return False
    else:
      feedkeys( keys )
      return True
  return False


### version ### {{{1
def Description():
  if State.IsValid():
    EchoHL('ModeMsg',
           '\nlibarary @{}\n{}\npython version {}\nflags {}'.format(
           Vim.Get('g:yoda_clang_library'),
           yoda.Version(),
           '.'.join( map( str, sys.version_info ) ),
           State.config_manager.CompilationFlags( Vim.FileName ) ) )


### vim helper ### {{{1
def EchoHL( hl, message ):
  return Vim.Call( 's:echohl', hl, message )


### find clang library ###{{{1
def _FindClangLibrary( library_path ):
  'helper function to find clang library file'

  def validate( libpath ):
    if libpath and os.path.exists( libpath ):
      return libpath
    return ''

  # platform dependent dynamic library name
  import platform
  sysname = platform.system()
  def lib_basename():
    d = dict( Darwin='libclang.dylib', Windows='libclang.dll' )
    return d.get( sysname, 'libclang.so' )

  if library_path:
    library_path = os.path.expanduser( library_path )
    if os.path.isdir( library_path ):
      library_path = os.path.join( library_path, lib_basename() )
    return validate( library_path )
  else:
    # try to find library using command `llvm-config`.
    if Vim.executable( 'llvm-config' ) != '0':
      dirname = Vim.system( 'llvm-config --libdir 2>/dev/null' ).strip()
      library_path = os.path.join( dirname, lib_basename() )
    # try to find library using environment variable $LD_LIBRARY_PATH
    elif Vim.Get( '$LD_LIBRARY_PATH' ):
      for dirname in Vim.Get( '$LD_LIBRARY_PATH' ).split( os.pathsep ):
        libfile = os.path.join( dirname, lib_basename() )
        if os.path.exists( libfile ):
          library_path = libfile
          break
    return validate( library_path )


### convert completions ### {{{1
def _ConvertFilterCompletions( completions, query ):
  '''
  Filter completions by query and convert completions into vim completion
  format.
  '''
  # decide how to reduce the completions
  ignorecase = Vim.Get( '&l:ignorecase' )
  if ignorecase:
    query = query.upper()
    starts_with = lambda x, q: x.upper().startswith( q )
  else:
    starts_with = lambda x, q: x.startswith( q )

  # filter and convert completions
  def convert( stack, icase ):
    result = stack.popleft()
    infos = [result.full_info]
    while stack:
      infos.append( stack.popleft().full_info )
    return dict( word  = result.spelling,
                 # abbr  = result.syntax_except_return_type,
                 # menu  = result.result_type,
                 info  = '\n'.join( infos ),
                 menu  = result.kind,
                 dup   = 1,
                 icase = icase )

  # collect same spellings for c++ name overrided functions.
  # NOTE: `completions` suppose to be sorted.
  same_spellings = collections.deque()
  for x in completions:
    spelling = x.spelling
    if not starts_with( spelling, query ):
      continue
    if same_spellings and same_spellings[0].spelling != spelling:
      yield convert( same_spellings, ignorecase )
    same_spellings.append( x )
  if same_spellings:
    yield convert( same_spellings, ignorecase )


### set __all__ ### {{{1
__all__ = [
  'VimOnAutoLoad',
  'VimOnFileType',
  'VimOnIdle',
  'VimOnCompleteDone',
  'CompleteStart',
  'Complete',
  'LocationTo',
  'DiagnosticQfList',
  'ShouldSnip',
  'TriggerSnip',
  'Description',
]
# vim:et:ts=2 sts=2 sw=2
