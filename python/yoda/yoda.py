#!/usr/bin/env python
from __future__ import print_function
import cindex_def
import ctypes as C
import sys

### compatibirity 2 and 3 ### {{{1
is_py3 = sys.version_info[ 0 ] >= 3
if is_py3:
  xrange = range
  unicode = str


def tobytes( contents ):
  if is_py3:
    return unicode.encode( contents ) if isinstance( contents, unicode ) else contents
  else:
    return contents


def tostr( contents ):
  if is_py3:
    return bytes.decode( contents )
  else:
    return contents


### request helper ### {{{1
class RequestWrap( object ):

  def __init__( self, data ):
    self.data = data
    self.converted_data = dict()

  def __getitem__( self, key ):
    if key in self.converted_data:
        return self.converted_data[ key ]
    if key == 'compilation_flags':
      self.converted_data[ key ] = \
          RequestWrap.convert_compilation_flags( self.data[ key ] )
    elif key == 'unsaved_files':
      self.converted_data[ key ] = \
          RequestWrap.convert_unsaved_file( self.data[ key ] )
    else:
      value = RequestWrap.convert_if_unicode( self.data[ key ] )
      self.converted_data[ key ] = value
    return self.converted_data[ key ]

  @staticmethod
  def convert_if_unicode( value ):
    if isinstance( value, unicode ):
      return tobytes( value )
    else:
      return value

  @staticmethod
  def convert_compilation_flags( flagslist ):
    nflags = len(flagslist)
    if not nflags:
      return None
    flags = (C.c_char_p * nflags)()
    for i, f in enumerate( flagslist ):
      flags[i] = tobytes( f )
    return flags

  @staticmethod
  def convert_unsaved_file( filelist ):
    if not filelist:
      return None
    unsaved = ( cindex_def.CXUnsavedFile * len( filelist ) )()
    for i, f in enumerate( filelist ):
      contents = tobytes( f[1] )
      unsaved[i].Filename = tobytes( f[0] )
      unsaved[i].Contents = contents
      unsaved[i].Length = len(contents)
    return unsaved

  @staticmethod
  def convert_if_needed( request_data ):
    if isinstance( request_data, RequestWrap ):
      return request_data
    else:
      return RequestWrap( request_data )


### cindex helper ### {{{1
def cx2str( cx_string ):
  s = L.clang_getCString( cx_string )
  L.clang_disposeString( cx_string )
  if s is None:
    return ''
  else:
    return tostr( s )


### result for client ### {{{1
class CursorKindInfo( object ):
  @classmethod
  def _register_kinds( cls ):
    CursorKindInfo.cursor_kind_map = {}
    for k in dir( cindex_def ):
      if not k.startswith( 'CXCursor_' ):
        continue
      CursorKindInfo.cursor_kind_map[ getattr( cindex_def, k ) ] = \
          '[' + k[ len( 'CXCursor_' ) : ] + ']'

  @classmethod
  def kind_str( cls, k ):
    return cls.cursor_kind_map[ k ]

CursorKindInfo._register_kinds()

  
class CompleteInfo( object ):

  __slots__ = ( 'result_type', 'spelling', 'placeholder',
                'syntax_except_return_type', 'kind' )

  CK_INFO = cindex_def.CXCompletionChunk_Informative
  CK_RESULT = cindex_def.CXCompletionChunk_ResultType
  CK_TEXT = cindex_def.CXCompletionChunk_TypedText
  CK_PLACEHOLDER = cindex_def.CXCompletionChunk_Placeholder
  PLACEHOLDER_ST = '{#'
  PLACEHOLDER_EN = '#}'

  def __init__( self, result_type, spelling, placeholder,
                syntax_except_return_type, kind ):
    self.result_type = result_type
    self.spelling = spelling
    self.placeholder = placeholder
    self.syntax_except_return_type = syntax_except_return_type
    self.kind = kind

  def has_placeholder( self ):
    return self.placeholder != self.spelling

  @property
  def full_info(self):
    'full information of the syntax'
    if self.result_type:
      return self.result_type + ' ' + self.syntax_except_return_type
    else:
      return self.syntax_except_return_type

  @staticmethod
  def make( completion_result ):
    result_type = ''
    spelling = ''
    placeholder = []
    syntax_except_return_type = []

    completion_string = completion_result.CompletionString

    for i in range( L.clang_getNumCompletionChunks( completion_string ) ):

      k = L.clang_getCompletionChunkKind( completion_string, i )
      text = cx2str( L.clang_getCompletionChunkText( completion_string, i ) )
      if k == CompleteInfo.CK_INFO:
        continue
      if k == CompleteInfo.CK_RESULT:
        result_type = text
        continue
      if k == CompleteInfo.CK_TEXT:
        spelling += text
      if k == CompleteInfo.CK_PLACEHOLDER:
        placeholder.append(
          CompleteInfo.PLACEHOLDER_ST + text + CompleteInfo.PLACEHOLDER_EN )
      else:
        placeholder.append(text)
      syntax_except_return_type.append(text)

    return CompleteInfo(
                result_type,
                spelling,
                ''.join( placeholder ),
                ''.join( syntax_except_return_type ),
                CursorKindInfo.kind_str( completion_result.CursorKind ) )


class LocationInfo( object ):
  def __init__(self, location):
    assert isinstance(location, Location)
    self.filename = location.filename
    self.line_num = location.line_num
    self.column_num = location.column_num

  def __repr__(self):
    return 'LocationInfo@{}:{}:{}'.format(
        self.filename, self.line_num, self.column_num)


class DiagnosticInfo(object):

  SEVERITY_MAP = {
    cindex_def.CXDiagnostic_Ignored : 'I',
    cindex_def.CXDiagnostic_Note : 'N',
    cindex_def.CXDiagnostic_Warning : 'W',
    cindex_def.CXDiagnostic_Error : 'E',
    cindex_def.CXDiagnostic_Fatal : 'E',
  }

  def __init__( self, location_info, text, kind ):
    self.location_info = location_info
    self.text = text
    self.kind = kind

  @staticmethod
  def make( diagnostic ):
    assert isinstance( diagnostic, Diagnostic )
    kind = DiagnosticInfo.SEVERITY_MAP.get( diagnostic.severity, 'I' )
    text = diagnostic.spelling
    location_info = LocationInfo( diagnostic.location )
    return DiagnosticInfo( location_info, text, kind )

  def __repr__( self ):
    return 'Diagnostic@{}:\'{}\':"{}"'.format(
        self.location_info, self.kind, self.text )
              

### cindex wrapper ### {{{1
class CIndexWrap( object ):

  def __init__( self, obj ):
    self._as_parameter_ = self.obj = obj


class Index( CIndexWrap ):

  def __del__( self ):
    L.clang_disposeIndex( self )

 ### entry point of this script
  @staticmethod
  def make():
    return Index( L.clang_createIndex(0, 0) )

  def translation_unit( self, request_data ):
    if not hasattr( self, '_translation_units_fn_map' ):
      self._translation_units_fn_map = dict()
    filename = request_data['filename']
    if filename not in self._translation_units_fn_map:
      self._translation_units_fn_map[ filename ] = \
          TranslationUnit.make( self, request_data )
    return self._translation_units_fn_map[ filename ]


class TranslationUnit( CIndexWrap ):

  @staticmethod
  def defalut_flags():
    return L.clang_defaultEditingTranslationUnitOptions()

  @staticmethod
  def default_completion_flags():
    return cindex_def.CXCodeComplete_IncludeMacros

  def __del__( self ):
    L.clang_disposeTranslationUnit( self )

  @staticmethod
  def make( index, request_data ):
    request_data = RequestWrap.convert_if_needed( request_data )
    tu = TranslationUnit( L.clang_parseTranslationUnit( 
        index,
        request_data['filename'],
        request_data['compilation_flags'],
        request_data['num_compilation_flags'],
        request_data['unsaved_files'],
        request_data['num_unsaved_flies'],
        TranslationUnit.defalut_flags() ) )
    tu.reparse( request_data )
    return tu

  ### parsing methods
  def reparse( self, request_data ):
    request_data = RequestWrap.convert_if_needed( request_data )
    L.clang_reparseTranslationUnit(
        self,
        request_data['num_unsaved_flies'],
        request_data['unsaved_files'],
        TranslationUnit.defalut_flags() )

  ### code completion methods
  def code_completions( self, request_data ):
    request_data = RequestWrap.convert_if_needed( request_data )
    ptr = L.clang_codeCompleteAt(
        self,
        request_data['filename'],
        request_data['line_num'],
        request_data['column_num'],
        request_data['unsaved_files'],
        request_data['num_unsaved_flies'],
        TranslationUnit.default_completion_flags() )
    return CodeCompletionResults( ptr )

  ### diagnostic methods
  def diagnostics( self, request_data ):
    request_data = RequestWrap.convert_if_needed( request_data )
    self.reparse( request_data )
    n = L.clang_getNumDiagnostics( self )
    diags = ( L.clang_getDiagnostic( self, i ) for i in range( n ) )
    diags = ( Diagnostic( d ) for d in diags )
    return [ DiagnosticInfo.make( d ) for d in diags ]

  ### cursor methods
  def _cursor( self, request_data ):
    location = Location.make(
        self,
        request_data['filename'],
        request_data['line_num'],
        request_data['column_num'] )
    return Cursor.make( self, location )

  def declaration_location_info( self, request_data ):
    request_data = RequestWrap.convert_if_needed( request_data )
    cursor = self._cursor( request_data )
    if not cursor: return None
    return LocationInfo( cursor.get_referenced().location )

  def definition_location_info( self, request_data ):
    request_data = RequestWrap.convert_if_needed( request_data )
    cursor = self._cursor( request_data )
    if not cursor: return None
    return LocationInfo( cursor.get_definition().location )


class CodeCompletionResults( CIndexWrap ):

  def __init__( self, ptr ):
    assert isinstance( ptr, C.POINTER( cindex_def.CXCodeCompleteResults ) ) \
    and ptr
    self.obj = self._as_parameter_ = ptr
    self._sorted = False

  def sort( self ):
    if not self._sorted:
      L.clang_sortCodeCompletionResults(
          self.obj.contents.Results, self.obj.contents.NumResults )
      self._sorted = True

  def __del__( self ):
    L.clang_disposeCodeCompleteResults( self )

  def __len__( self ):
    return int( self.obj.contents.NumResults )

  def __getitem__( self, index ):
    if len( self ) <= index:
      raise IndexError
    return CompleteInfo.make( self.obj.contents.Results[ index ] )

  def search( self, query ):
    self.sort()
    pos = self.binsearch( query )
    if pos >= 0:
      return self[ pos ]
    else:
      return None

  def iterate( self, query='' ):
    left, right = self.binrange( query )
    for i in xrange( left, right ):
      yield CompleteInfo.make( self.obj.contents.Results[i] )

  def binrange( self, query ):
    self.sort()
    if query:
      nextq = query[:-1] + chr( ord( query[-1] ) + 1 )
      if nextq[-1] > 'z':
        nextq = query[:-1] + chr( 0x7f )
      left  = self.bisect_left( query )
      right = self.bisect_right( nextq )
      assert left >= 0 and len( self ) >= left
      assert right >= 0 and len( self ) >= right
      return left, right
    else:
      return 0, len( self )

  ### searching ###
  def binsearch( self, query, lo=0, hi=None ):
    if lo < 0:
      raise ValueError('lo must be non-negative')
    if hi is None:
      hi = len( self )
    cmp_query = _ClangCmpKey( query )
    p = self.bisect_left( cmp_query, lo, hi )
    if p != hi and _ClangCmpKey( self[ p ].spelling ) == cmp_query:
      while p != hi and _ClangCmpKey( self[ p ].spelling ) == cmp_query:
        if self[ p ].spelling == query:
          return p
        p += 1
      return -1
    else:
      return -1

  def bisect_left( self, query, lo=0, hi=None ):
    if lo < 0:
      raise ValueError('lo must be non-negative')
    if hi is None:
      hi = len( self )
    query = _ClangCmpKey( query )
    while lo < hi:
      mid = (lo+hi)//2
      key = _ClangCmpKey( self[ mid ].spelling )
      if key < query: lo = mid+1
      else: hi = mid
    return lo

  def bisect_right( self, query, lo=0, hi=None ):
    if lo < 0:
      raise ValueError('lo must be non-negative')
    if hi is None:
      hi = len( self )
    query = _ClangCmpKey( query )
    while lo < hi:
      mid = (lo+hi)//2
      key = _ClangCmpKey( self[ mid ].spelling )
      if query < key: hi = mid
      else: lo = mid+1
    return lo


def _ClangCmpKey( s ):
  # clang sort the code-completion results in case-insensitive alphabetical
  # order. Non alphabetical characters are preordered from it.
  import string
  non_letters = ''.join( sorted( string.punctuation + string.digits ) )
  non_letters_repl = ''.join( chr(i) for i in range( len( non_letters ) ) )
  if is_py3:
    trans = unicode.maketrans( non_letters      + string.ascii_lowercase,
                               non_letters_repl + string.ascii_uppercase )
  else:
    trans = string.maketrans( non_letters      + string.ascii_lowercase,
                               non_letters_repl + string.ascii_uppercase )
  # cache trans
  global _ClangCmpKey
  _ClangCmpKey = lambda x: x.translate( trans )
  return _ClangCmpKey( s )


class Location( CIndexWrap ):

  def __init__( self, cx_location ):
    assert isinstance( cx_location, cindex_def.CXSourceLocation )
    self.obj = self._as_parameter_ = cx_location
    self._instantiated = False

  def _instantiate_once( self ):
    if self._instantiated:
      return
    line_p, col_p = ( C.c_uint * 1 )(), ( C.c_uint * 1 )()
    offset_p = ( C.c_uint * 1 )()
    cx_file_p = ( cindex_def.CXFile * 1 )()
    L.clang_getInstantiationLocation( self, cx_file_p, line_p, col_p, offset_p )
    self._filename = cx2str( L.clang_getFileName( cx_file_p[0] ) )
    # cast requires because element of pointer returns long type value.
    self._line_num, self._column_num = int(line_p[0]), int(col_p[0])
    self._offset_num = int(offset_p[0])
    # noting to do after the call
    self._instantiated = True

  @property
  def line_num( self ):
    self._instantiate_once()
    return self._line_num

  @property
  def column_num( self ):
    self._instantiate_once()
    return self._column_num

  @property
  def offset_num( self ):
    self._instantiate_once()
    return self._offset_num

  @property
  def filename( self ):
    self._instantiate_once()
    return self._filename

  @staticmethod
  def make( tu, filename, line_num, column_num ):
    assert isinstance( tu, TranslationUnit ) and tu
    cxfile = L.clang_getFile( tu, filename )
    cx_location = L.clang_getLocation( tu, cxfile, line_num, column_num )
    return Location( cx_location )
    
  def __repr__( self ):
    return 'Location@{}:{}:{}'.format(
        self.filename, self.line_num, self.column_num )


class Cursor( CIndexWrap ):

  def __init__( self, cx_cursor ):
    assert isinstance( cx_cursor, cindex_def.CXCursor )
    self.obj = self._as_parameter_ = cx_cursor

  @staticmethod
  def make( tu, location ):
    assert isinstance( tu, TranslationUnit ) and tu
    assert isinstance( location, Location )
    cx_cursor = L.clang_getCursor( tu, location )
    return Cursor( cx_cursor )

  def __len__( self ): # for use 'if' statement __bool__ (3x) and __nonzero__ (2x)
    return 0 if int( L.clang_Cursor_isNull( self ) ) else 1

  @property
  def location( self ):
    return Location( L.clang_getCursorLocation( self ) )

  def get_referenced( self ):
    return Cursor( L.clang_getCursorReferenced( self ) )

  def get_definition( self ):
    return Cursor( L.clang_getCursorDefinition( self ) )


class Diagnostic( CIndexWrap ):

  def __init__( self, cx_diagnostic ):
    assert isinstance( cx_diagnostic, cindex_def.CXDiagnostic ) \
    and cx_diagnostic
    self.obj = self._as_parameter_ = cx_diagnostic

  def __del__( self ):
    L.clang_disposeDiagnostic( self )

  @property
  def severity( self ):
    return L.clang_getDiagnosticSeverity( self )

  @property
  def location( self ):
    return Location( L.clang_getDiagnosticLocation( self ) )

  @property
  def spelling( self ):
    return cx2str( L.clang_getDiagnosticSpelling( self ) )


### version ###
def Version():
  return cx2str( L.clang_getClangVersion() )


### starting point ### {{{1
L = None
def Initialize( library_path ):
  # load library 
  global L
  L = C.cdll.LoadLibrary( library_path )
  for name, argtypes, restype in cindex_def._function_infos:
      f = getattr( L, name, None )
      if not f: continue # TODO: version check
      f.argtypes = argtypes
      f.restype  = restype

# vim:et:ts=2 sts=2 sw=2
