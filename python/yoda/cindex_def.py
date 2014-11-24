from ctypes import c_long, c_char_p, c_ulonglong, c_uint, CFUNCTYPE, c_void_p, c_ulong, c_longlong, c_int, POINTER, Structure

CXErrorCode = c_uint # enum
CXError_Success = 0
CXError_Failure = 1
CXError_Crashed = 2
CXError_InvalidArguments = 3
CXError_ASTReadError = 4

CXAvailabilityKind = c_uint # enum
CXAvailability_Available = 0
CXAvailability_Deprecated = 1
CXAvailability_NotAvailable = 2
CXAvailability_NotAccessible = 3

CXGlobalOptFlags = c_uint # enum
CXGlobalOpt_None = 0
CXGlobalOpt_ThreadBackgroundPriorityForIndexing = 1
CXGlobalOpt_ThreadBackgroundPriorityForEditing = 2
CXGlobalOpt_ThreadBackgroundPriorityForAll = 3

CXDiagnosticSeverity = c_uint # enum
CXDiagnostic_Ignored = 0
CXDiagnostic_Note = 1
CXDiagnostic_Warning = 2
CXDiagnostic_Error = 3
CXDiagnostic_Fatal = 4

CXLoadDiag_Error = c_uint # enum
CXLoadDiag_None = 0
CXLoadDiag_Unknown = 1
CXLoadDiag_CannotLoad = 2
CXLoadDiag_InvalidFile = 3

CXDiagnosticDisplayOptions = c_uint # enum
CXDiagnostic_DisplaySourceLocation = 1
CXDiagnostic_DisplayColumn = 2
CXDiagnostic_DisplaySourceRanges = 4
CXDiagnostic_DisplayOption = 8
CXDiagnostic_DisplayCategoryId = 16
CXDiagnostic_DisplayCategoryName = 32

CXTranslationUnit_Flags = c_uint # enum
CXTranslationUnit_None = 0
CXTranslationUnit_DetailedPreprocessingRecord = 1
CXTranslationUnit_Incomplete = 2
CXTranslationUnit_PrecompiledPreamble = 4
CXTranslationUnit_CacheCompletionResults = 8
CXTranslationUnit_ForSerialization = 16
CXTranslationUnit_CXXChainedPCH = 32
CXTranslationUnit_SkipFunctionBodies = 64
CXTranslationUnit_IncludeBriefCommentsInCodeCompletion = 128

CXSaveTranslationUnit_Flags = c_uint # enum
CXSaveTranslationUnit_None = 0

CXSaveError = c_uint # enum
CXSaveError_None = 0
CXSaveError_Unknown = 1
CXSaveError_TranslationErrors = 2
CXSaveError_InvalidTU = 3

CXReparse_Flags = c_uint # enum
CXReparse_None = 0

CXTUResourceUsageKind = c_uint # enum
CXTUResourceUsage_AST = 1
CXTUResourceUsage_Identifiers = 2
CXTUResourceUsage_Selectors = 3
CXTUResourceUsage_GlobalCompletionResults = 4
CXTUResourceUsage_SourceManagerContentCache = 5
CXTUResourceUsage_AST_SideTables = 6
CXTUResourceUsage_SourceManager_Membuffer_Malloc = 7
CXTUResourceUsage_SourceManager_Membuffer_MMap = 8
CXTUResourceUsage_ExternalASTSource_Membuffer_Malloc = 9
CXTUResourceUsage_ExternalASTSource_Membuffer_MMap = 10
CXTUResourceUsage_Preprocessor = 11
CXTUResourceUsage_PreprocessingRecord = 12
CXTUResourceUsage_SourceManager_DataStructures = 13
CXTUResourceUsage_Preprocessor_HeaderSearch = 14
CXTUResourceUsage_MEMORY_IN_BYTES_BEGIN = 1
CXTUResourceUsage_MEMORY_IN_BYTES_END = 14
CXTUResourceUsage_First = 1
CXTUResourceUsage_Last = 14

CXCursorKind = c_uint # enum
CXCursor_UnexposedDecl = 1
CXCursor_StructDecl = 2
CXCursor_UnionDecl = 3
CXCursor_ClassDecl = 4
CXCursor_EnumDecl = 5
CXCursor_FieldDecl = 6
CXCursor_EnumConstantDecl = 7
CXCursor_FunctionDecl = 8
CXCursor_VarDecl = 9
CXCursor_ParmDecl = 10
CXCursor_ObjCInterfaceDecl = 11
CXCursor_ObjCCategoryDecl = 12
CXCursor_ObjCProtocolDecl = 13
CXCursor_ObjCPropertyDecl = 14
CXCursor_ObjCIvarDecl = 15
CXCursor_ObjCInstanceMethodDecl = 16
CXCursor_ObjCClassMethodDecl = 17
CXCursor_ObjCImplementationDecl = 18
CXCursor_ObjCCategoryImplDecl = 19
CXCursor_TypedefDecl = 20
CXCursor_CXXMethod = 21
CXCursor_Namespace = 22
CXCursor_LinkageSpec = 23
CXCursor_Constructor = 24
CXCursor_Destructor = 25
CXCursor_ConversionFunction = 26
CXCursor_TemplateTypeParameter = 27
CXCursor_NonTypeTemplateParameter = 28
CXCursor_TemplateTemplateParameter = 29
CXCursor_FunctionTemplate = 30
CXCursor_ClassTemplate = 31
CXCursor_ClassTemplatePartialSpecialization = 32
CXCursor_NamespaceAlias = 33
CXCursor_UsingDirective = 34
CXCursor_UsingDeclaration = 35
CXCursor_TypeAliasDecl = 36
CXCursor_ObjCSynthesizeDecl = 37
CXCursor_ObjCDynamicDecl = 38
CXCursor_CXXAccessSpecifier = 39
CXCursor_FirstDecl = 1
CXCursor_LastDecl = 39
CXCursor_FirstRef = 40
CXCursor_ObjCSuperClassRef = 40
CXCursor_ObjCProtocolRef = 41
CXCursor_ObjCClassRef = 42
CXCursor_TypeRef = 43
CXCursor_CXXBaseSpecifier = 44
CXCursor_TemplateRef = 45
CXCursor_NamespaceRef = 46
CXCursor_MemberRef = 47
CXCursor_LabelRef = 48
CXCursor_OverloadedDeclRef = 49
CXCursor_VariableRef = 50
CXCursor_LastRef = 50
CXCursor_FirstInvalid = 70
CXCursor_InvalidFile = 70
CXCursor_NoDeclFound = 71
CXCursor_NotImplemented = 72
CXCursor_InvalidCode = 73
CXCursor_LastInvalid = 73
CXCursor_FirstExpr = 100
CXCursor_UnexposedExpr = 100
CXCursor_DeclRefExpr = 101
CXCursor_MemberRefExpr = 102
CXCursor_CallExpr = 103
CXCursor_ObjCMessageExpr = 104
CXCursor_BlockExpr = 105
CXCursor_IntegerLiteral = 106
CXCursor_FloatingLiteral = 107
CXCursor_ImaginaryLiteral = 108
CXCursor_StringLiteral = 109
CXCursor_CharacterLiteral = 110
CXCursor_ParenExpr = 111
CXCursor_UnaryOperator = 112
CXCursor_ArraySubscriptExpr = 113
CXCursor_BinaryOperator = 114
CXCursor_CompoundAssignOperator = 115
CXCursor_ConditionalOperator = 116
CXCursor_CStyleCastExpr = 117
CXCursor_CompoundLiteralExpr = 118
CXCursor_InitListExpr = 119
CXCursor_AddrLabelExpr = 120
CXCursor_StmtExpr = 121
CXCursor_GenericSelectionExpr = 122
CXCursor_GNUNullExpr = 123
CXCursor_CXXStaticCastExpr = 124
CXCursor_CXXDynamicCastExpr = 125
CXCursor_CXXReinterpretCastExpr = 126
CXCursor_CXXConstCastExpr = 127
CXCursor_CXXFunctionalCastExpr = 128
CXCursor_CXXTypeidExpr = 129
CXCursor_CXXBoolLiteralExpr = 130
CXCursor_CXXNullPtrLiteralExpr = 131
CXCursor_CXXThisExpr = 132
CXCursor_CXXThrowExpr = 133
CXCursor_CXXNewExpr = 134
CXCursor_CXXDeleteExpr = 135
CXCursor_UnaryExpr = 136
CXCursor_ObjCStringLiteral = 137
CXCursor_ObjCEncodeExpr = 138
CXCursor_ObjCSelectorExpr = 139
CXCursor_ObjCProtocolExpr = 140
CXCursor_ObjCBridgedCastExpr = 141
CXCursor_PackExpansionExpr = 142
CXCursor_SizeOfPackExpr = 143
CXCursor_LambdaExpr = 144
CXCursor_ObjCBoolLiteralExpr = 145
CXCursor_ObjCSelfExpr = 146
CXCursor_LastExpr = 146
CXCursor_FirstStmt = 200
CXCursor_UnexposedStmt = 200
CXCursor_LabelStmt = 201
CXCursor_CompoundStmt = 202
CXCursor_CaseStmt = 203
CXCursor_DefaultStmt = 204
CXCursor_IfStmt = 205
CXCursor_SwitchStmt = 206
CXCursor_WhileStmt = 207
CXCursor_DoStmt = 208
CXCursor_ForStmt = 209
CXCursor_GotoStmt = 210
CXCursor_IndirectGotoStmt = 211
CXCursor_ContinueStmt = 212
CXCursor_BreakStmt = 213
CXCursor_ReturnStmt = 214
CXCursor_GCCAsmStmt = 215
CXCursor_AsmStmt = 215
CXCursor_ObjCAtTryStmt = 216
CXCursor_ObjCAtCatchStmt = 217
CXCursor_ObjCAtFinallyStmt = 218
CXCursor_ObjCAtThrowStmt = 219
CXCursor_ObjCAtSynchronizedStmt = 220
CXCursor_ObjCAutoreleasePoolStmt = 221
CXCursor_ObjCForCollectionStmt = 222
CXCursor_CXXCatchStmt = 223
CXCursor_CXXTryStmt = 224
CXCursor_CXXForRangeStmt = 225
CXCursor_SEHTryStmt = 226
CXCursor_SEHExceptStmt = 227
CXCursor_SEHFinallyStmt = 228
CXCursor_MSAsmStmt = 229
CXCursor_NullStmt = 230
CXCursor_DeclStmt = 231
CXCursor_OMPParallelDirective = 232
CXCursor_OMPSimdDirective = 233
CXCursor_OMPForDirective = 234
CXCursor_OMPSectionsDirective = 235
CXCursor_OMPSectionDirective = 236
CXCursor_OMPSingleDirective = 237
CXCursor_OMPParallelForDirective = 238
CXCursor_OMPParallelSectionsDirective = 239
CXCursor_OMPTaskDirective = 240
CXCursor_OMPMasterDirective = 241
CXCursor_OMPCriticalDirective = 242
CXCursor_OMPTaskyieldDirective = 243
CXCursor_OMPBarrierDirective = 244
CXCursor_OMPTaskwaitDirective = 245
CXCursor_OMPFlushDirective = 246
CXCursor_SEHLeaveStmt = 247
CXCursor_LastStmt = 247
CXCursor_TranslationUnit = 300
CXCursor_FirstAttr = 400
CXCursor_UnexposedAttr = 400
CXCursor_IBActionAttr = 401
CXCursor_IBOutletAttr = 402
CXCursor_IBOutletCollectionAttr = 403
CXCursor_CXXFinalAttr = 404
CXCursor_CXXOverrideAttr = 405
CXCursor_AnnotateAttr = 406
CXCursor_AsmLabelAttr = 407
CXCursor_PackedAttr = 408
CXCursor_PureAttr = 409
CXCursor_ConstAttr = 410
CXCursor_NoDuplicateAttr = 411
CXCursor_CUDAConstantAttr = 412
CXCursor_CUDADeviceAttr = 413
CXCursor_CUDAGlobalAttr = 414
CXCursor_CUDAHostAttr = 415
CXCursor_LastAttr = 415
CXCursor_PreprocessingDirective = 500
CXCursor_MacroDefinition = 501
CXCursor_MacroExpansion = 502
CXCursor_MacroInstantiation = 502
CXCursor_InclusionDirective = 503
CXCursor_FirstPreprocessing = 500
CXCursor_LastPreprocessing = 503
CXCursor_ModuleImportDecl = 600
CXCursor_FirstExtraDecl = 600
CXCursor_LastExtraDecl = 600

CXLinkageKind = c_uint # enum
CXLinkage_Invalid = 0
CXLinkage_NoLinkage = 1
CXLinkage_Internal = 2
CXLinkage_UniqueExternal = 3
CXLinkage_External = 4

CXLanguageKind = c_uint # enum
CXLanguage_Invalid = 0
CXLanguage_C = 1
CXLanguage_ObjC = 2
CXLanguage_CPlusPlus = 3

CXTypeKind = c_uint # enum
CXType_Invalid = 0
CXType_Unexposed = 1
CXType_Void = 2
CXType_Bool = 3
CXType_Char_U = 4
CXType_UChar = 5
CXType_Char16 = 6
CXType_Char32 = 7
CXType_UShort = 8
CXType_UInt = 9
CXType_ULong = 10
CXType_ULongLong = 11
CXType_UInt128 = 12
CXType_Char_S = 13
CXType_SChar = 14
CXType_WChar = 15
CXType_Short = 16
CXType_Int = 17
CXType_Long = 18
CXType_LongLong = 19
CXType_Int128 = 20
CXType_Float = 21
CXType_Double = 22
CXType_LongDouble = 23
CXType_NullPtr = 24
CXType_Overload = 25
CXType_Dependent = 26
CXType_ObjCId = 27
CXType_ObjCClass = 28
CXType_ObjCSel = 29
CXType_FirstBuiltin = 2
CXType_LastBuiltin = 29
CXType_Complex = 100
CXType_Pointer = 101
CXType_BlockPointer = 102
CXType_LValueReference = 103
CXType_RValueReference = 104
CXType_Record = 105
CXType_Enum = 106
CXType_Typedef = 107
CXType_ObjCInterface = 108
CXType_ObjCObjectPointer = 109
CXType_FunctionNoProto = 110
CXType_FunctionProto = 111
CXType_ConstantArray = 112
CXType_Vector = 113
CXType_IncompleteArray = 114
CXType_VariableArray = 115
CXType_DependentSizedArray = 116
CXType_MemberPointer = 117

CXCallingConv = c_uint # enum
CXCallingConv_Default = 0
CXCallingConv_C = 1
CXCallingConv_X86StdCall = 2
CXCallingConv_X86FastCall = 3
CXCallingConv_X86ThisCall = 4
CXCallingConv_X86Pascal = 5
CXCallingConv_AAPCS = 6
CXCallingConv_AAPCS_VFP = 7
CXCallingConv_PnaclCall = 8
CXCallingConv_IntelOclBicc = 9
CXCallingConv_X86_64Win64 = 10
CXCallingConv_X86_64SysV = 11
CXCallingConv_Invalid = 100
CXCallingConv_Unexposed = 200

CXTypeLayoutError = c_int # enum
CXTypeLayoutError_Invalid = -1
CXTypeLayoutError_Incomplete = -2
CXTypeLayoutError_Dependent = -3
CXTypeLayoutError_NotConstantSize = -4
CXTypeLayoutError_InvalidFieldName = -5

CXRefQualifierKind = c_uint # enum
CXRefQualifier_None = 0
CXRefQualifier_LValue = 1
CXRefQualifier_RValue = 2

CX_CXXAccessSpecifier = c_uint # enum
CX_CXXInvalidAccessSpecifier = 0
CX_CXXPublic = 1
CX_CXXProtected = 2
CX_CXXPrivate = 3

CXChildVisitResult = c_uint # enum
CXChildVisit_Break = 0
CXChildVisit_Continue = 1
CXChildVisit_Recurse = 2

CXObjCPropertyAttrKind = c_uint # enum
CXObjCPropertyAttr_noattr = 0
CXObjCPropertyAttr_readonly = 1
CXObjCPropertyAttr_getter = 2
CXObjCPropertyAttr_assign = 4
CXObjCPropertyAttr_readwrite = 8
CXObjCPropertyAttr_retain = 16
CXObjCPropertyAttr_copy = 32
CXObjCPropertyAttr_nonatomic = 64
CXObjCPropertyAttr_setter = 128
CXObjCPropertyAttr_atomic = 256
CXObjCPropertyAttr_weak = 512
CXObjCPropertyAttr_strong = 1024
CXObjCPropertyAttr_unsafe_unretained = 2048

CXObjCDeclQualifierKind = c_uint # enum
CXObjCDeclQualifier_None = 0
CXObjCDeclQualifier_In = 1
CXObjCDeclQualifier_Inout = 2
CXObjCDeclQualifier_Out = 4
CXObjCDeclQualifier_Bycopy = 8
CXObjCDeclQualifier_Byref = 16
CXObjCDeclQualifier_Oneway = 32

CXNameRefFlags = c_uint # enum
CXNameRange_WantQualifier = 1
CXNameRange_WantTemplateArgs = 2
CXNameRange_WantSinglePiece = 4

CXTokenKind = c_uint # enum
CXToken_Punctuation = 0
CXToken_Keyword = 1
CXToken_Identifier = 2
CXToken_Literal = 3
CXToken_Comment = 4

CXCompletionChunkKind = c_uint # enum
CXCompletionChunk_Optional = 0
CXCompletionChunk_TypedText = 1
CXCompletionChunk_Text = 2
CXCompletionChunk_Placeholder = 3
CXCompletionChunk_Informative = 4
CXCompletionChunk_CurrentParameter = 5
CXCompletionChunk_LeftParen = 6
CXCompletionChunk_RightParen = 7
CXCompletionChunk_LeftBracket = 8
CXCompletionChunk_RightBracket = 9
CXCompletionChunk_LeftBrace = 10
CXCompletionChunk_RightBrace = 11
CXCompletionChunk_LeftAngle = 12
CXCompletionChunk_RightAngle = 13
CXCompletionChunk_Comma = 14
CXCompletionChunk_ResultType = 15
CXCompletionChunk_Colon = 16
CXCompletionChunk_SemiColon = 17
CXCompletionChunk_Equal = 18
CXCompletionChunk_HorizontalSpace = 19
CXCompletionChunk_VerticalSpace = 20

CXCodeComplete_Flags = c_uint # enum
CXCodeComplete_IncludeMacros = 1
CXCodeComplete_IncludeCodePatterns = 2
CXCodeComplete_IncludeBriefComments = 4

CXCompletionContext = c_uint # enum
CXCompletionContext_Unexposed = 0
CXCompletionContext_AnyType = 1
CXCompletionContext_AnyValue = 2
CXCompletionContext_ObjCObjectValue = 4
CXCompletionContext_ObjCSelectorValue = 8
CXCompletionContext_CXXClassTypeValue = 16
CXCompletionContext_DotMemberAccess = 32
CXCompletionContext_ArrowMemberAccess = 64
CXCompletionContext_ObjCPropertyAccess = 128
CXCompletionContext_EnumTag = 256
CXCompletionContext_UnionTag = 512
CXCompletionContext_StructTag = 1024
CXCompletionContext_ClassTag = 2048
CXCompletionContext_Namespace = 4096
CXCompletionContext_NestedNameSpecifier = 8192
CXCompletionContext_ObjCInterface = 16384
CXCompletionContext_ObjCProtocol = 32768
CXCompletionContext_ObjCCategory = 65536
CXCompletionContext_ObjCInstanceMessage = 131072
CXCompletionContext_ObjCClassMessage = 262144
CXCompletionContext_ObjCSelectorName = 524288
CXCompletionContext_MacroName = 1048576
CXCompletionContext_NaturalLanguage = 2097152
CXCompletionContext_Unknown = 4194303

CXVisitorResult = c_uint # enum
CXVisit_Break = 0
CXVisit_Continue = 1

CXResult = c_uint # enum
CXResult_Success = 0
CXResult_Invalid = 1
CXResult_VisitBreak = 2

CXIdxEntityKind = c_uint # enum
CXIdxEntity_Unexposed = 0
CXIdxEntity_Typedef = 1
CXIdxEntity_Function = 2
CXIdxEntity_Variable = 3
CXIdxEntity_Field = 4
CXIdxEntity_EnumConstant = 5
CXIdxEntity_ObjCClass = 6
CXIdxEntity_ObjCProtocol = 7
CXIdxEntity_ObjCCategory = 8
CXIdxEntity_ObjCInstanceMethod = 9
CXIdxEntity_ObjCClassMethod = 10
CXIdxEntity_ObjCProperty = 11
CXIdxEntity_ObjCIvar = 12
CXIdxEntity_Enum = 13
CXIdxEntity_Struct = 14
CXIdxEntity_Union = 15
CXIdxEntity_CXXClass = 16
CXIdxEntity_CXXNamespace = 17
CXIdxEntity_CXXNamespaceAlias = 18
CXIdxEntity_CXXStaticVariable = 19
CXIdxEntity_CXXStaticMethod = 20
CXIdxEntity_CXXInstanceMethod = 21
CXIdxEntity_CXXConstructor = 22
CXIdxEntity_CXXDestructor = 23
CXIdxEntity_CXXConversionFunction = 24
CXIdxEntity_CXXTypeAlias = 25
CXIdxEntity_CXXInterface = 26

CXIdxEntityLanguage = c_uint # enum
CXIdxEntityLang_None = 0
CXIdxEntityLang_C = 1
CXIdxEntityLang_ObjC = 2
CXIdxEntityLang_CXX = 3

CXIdxEntityCXXTemplateKind = c_uint # enum
CXIdxEntity_NonTemplate = 0
CXIdxEntity_Template = 1
CXIdxEntity_TemplatePartialSpecialization = 2
CXIdxEntity_TemplateSpecialization = 3

CXIdxAttrKind = c_uint # enum
CXIdxAttr_Unexposed = 0
CXIdxAttr_IBAction = 1
CXIdxAttr_IBOutlet = 2
CXIdxAttr_IBOutletCollection = 3

CXIdxDeclInfoFlags = c_uint # enum
CXIdxDeclFlag_Skipped = 1

CXIdxObjCContainerKind = c_uint # enum
CXIdxObjCContainer_ForwardRef = 0
CXIdxObjCContainer_Interface = 1
CXIdxObjCContainer_Implementation = 2

CXIdxEntityRefKind = c_uint # enum
CXIdxEntityRef_Direct = 1
CXIdxEntityRef_Implicit = 2

CXIndexOptFlags = c_uint # enum
CXIndexOpt_None = 0
CXIndexOpt_SuppressRedundantRefs = 1
CXIndexOpt_IndexFunctionLocalSymbols = 2
CXIndexOpt_IndexImplicitTemplateInstantiations = 4
CXIndexOpt_SuppressWarnings = 8
CXIndexOpt_SkipParsedBodiesInSession = 16

CXCommentKind = c_uint # enum
CXComment_Null = 0
CXComment_Text = 1
CXComment_InlineCommand = 2
CXComment_HTMLStartTag = 3
CXComment_HTMLEndTag = 4
CXComment_Paragraph = 5
CXComment_BlockCommand = 6
CXComment_ParamCommand = 7
CXComment_TParamCommand = 8
CXComment_VerbatimBlockCommand = 9
CXComment_VerbatimBlockLine = 10
CXComment_VerbatimLine = 11
CXComment_FullComment = 12

CXCommentInlineCommandRenderKind = c_uint # enum
CXCommentInlineCommandRenderKind_Normal = 0
CXCommentInlineCommandRenderKind_Bold = 1
CXCommentInlineCommandRenderKind_Monospaced = 2
CXCommentInlineCommandRenderKind_Emphasized = 3

CXCommentParamPassDirection = c_uint # enum
CXCommentParamPassDirection_In = 0
CXCommentParamPassDirection_Out = 1
CXCommentParamPassDirection_InOut = 2

time_t = c_long

class CXString(Structure):
  _fields_ = [("data", POINTER(c_void_p)),
              ("private_flags", c_uint)]

class CXVirtualFileOverlayImpl(Structure):
  pass # opaque structure

CXVirtualFileOverlay = POINTER(CXVirtualFileOverlayImpl)

class CXModuleMapDescriptorImpl(Structure):
  pass # opaque structure

CXModuleMapDescriptor = POINTER(CXModuleMapDescriptorImpl)

CXIndex = POINTER(c_void_p)

class CXTranslationUnitImpl(Structure):
  pass # opaque structure

CXTranslationUnit = POINTER(CXTranslationUnitImpl)

CXClientData = POINTER(c_void_p)

class CXUnsavedFile(Structure):
  _fields_ = [("Filename", c_char_p),
              ("Contents", c_char_p),
              ("Length", c_ulong)]

class CXVersion(Structure):
  _fields_ = [("Major", c_int),
              ("Minor", c_int),
              ("Subminor", c_int)]

CXFile = POINTER(c_void_p)

class CXFileUniqueID(Structure):
  _fields_ = [("data", c_ulonglong * 3)]

class CXSourceLocation(Structure):
  _fields_ = [("ptr_data", POINTER(c_void_p) * 2),
              ("int_data", c_uint)]

class CXSourceRange(Structure):
  _fields_ = [("ptr_data", POINTER(c_void_p) * 2),
              ("begin_int_data", c_uint),
              ("end_int_data", c_uint)]

class CXSourceRangeList(Structure):
  _fields_ = [("count", c_uint),
              ("ranges", POINTER(CXSourceRange))]

CXDiagnostic = POINTER(c_void_p)

CXDiagnosticSet = POINTER(c_void_p)

class CXTUResourceUsageEntry(Structure):
  _fields_ = [("kind", CXTUResourceUsageKind),
              ("amount", c_ulong)]

class CXTUResourceUsage(Structure):
  _fields_ = [("data", POINTER(c_void_p)),
              ("numEntries", c_uint),
              ("entries", POINTER(CXTUResourceUsageEntry))]

class CXCursor(Structure):
  _fields_ = [("kind", CXCursorKind),
              ("xdata", c_int),
              ("data", POINTER(c_void_p) * 3)]

class CXPlatformAvailability(Structure):
  _fields_ = [("Platform", CXString),
              ("Introduced", CXVersion),
              ("Deprecated", CXVersion),
              ("Obsoleted", CXVersion),
              ("Unavailable", c_int),
              ("Message", CXString)]

class CXCursorSetImpl(Structure):
  pass # opaque structure

CXCursorSet = POINTER(CXCursorSetImpl)

class CXType(Structure):
  _fields_ = [("kind", CXTypeKind),
              ("data", POINTER(c_void_p) * 2)]

CXCursorVisitor = CFUNCTYPE(c_uint, CXCursor, CXCursor, CXClientData)

CXModule = POINTER(c_void_p)

CXTokenKind = CXTokenKind

class CXToken(Structure):
  _fields_ = [("int_data", c_uint * 4),
              ("ptr_data", POINTER(c_void_p))]

CXCompletionString = POINTER(c_void_p)

class CXCompletionResult(Structure):
  _fields_ = [("CursorKind", CXCursorKind),
              ("CompletionString", CXCompletionString)]

class CXCodeCompleteResults(Structure):
  _fields_ = [("Results", POINTER(CXCompletionResult)),
              ("NumResults", c_uint)]

CXInclusionVisitor = CFUNCTYPE(None, CXFile, POINTER(CXSourceLocation), c_uint, CXClientData)

CXRemapping = POINTER(c_void_p)

class CXCursorAndRangeVisitor(Structure):
  _fields_ = [("context", POINTER(c_void_p)),
              ("visit", CFUNCTYPE(c_uint, POINTER(c_void_p), CXCursor, CXSourceRange))]

CXIdxClientFile = POINTER(c_void_p)

CXIdxClientEntity = POINTER(c_void_p)

CXIdxClientContainer = POINTER(c_void_p)

CXIdxClientASTFile = POINTER(c_void_p)

class CXIdxLoc(Structure):
  _fields_ = [("ptr_data", POINTER(c_void_p) * 2),
              ("int_data", c_uint)]

class CXIdxIncludedFileInfo(Structure):
  _fields_ = [("hashLoc", CXIdxLoc),
              ("filename", c_char_p),
              ("file", CXFile),
              ("isImport", c_int),
              ("isAngled", c_int),
              ("isModuleImport", c_int)]

class CXIdxImportedASTFileInfo(Structure):
  _fields_ = [("file", CXFile),
              ("module", CXModule),
              ("loc", CXIdxLoc),
              ("isImplicit", c_int)]

class CXIdxAttrInfo(Structure):
  _fields_ = [("kind", CXIdxAttrKind),
              ("cursor", CXCursor),
              ("loc", CXIdxLoc)]

class CXIdxEntityInfo(Structure):
  _fields_ = [("kind", CXIdxEntityKind),
              ("templateKind", CXIdxEntityCXXTemplateKind),
              ("lang", CXIdxEntityLanguage),
              ("name", c_char_p),
              ("USR", c_char_p),
              ("cursor", CXCursor),
              ("attributes", POINTER(POINTER(CXIdxAttrInfo))),
              ("numAttributes", c_uint)]

class CXIdxContainerInfo(Structure):
  _fields_ = [("cursor", CXCursor)]

class CXIdxIBOutletCollectionAttrInfo(Structure):
  _fields_ = [("attrInfo", POINTER(CXIdxAttrInfo)),
              ("objcClass", POINTER(CXIdxEntityInfo)),
              ("classCursor", CXCursor),
              ("classLoc", CXIdxLoc)]

class CXIdxDeclInfo(Structure):
  _fields_ = [("entityInfo", POINTER(CXIdxEntityInfo)),
              ("cursor", CXCursor),
              ("loc", CXIdxLoc),
              ("semanticContainer", POINTER(CXIdxContainerInfo)),
              ("lexicalContainer", POINTER(CXIdxContainerInfo)),
              ("isRedeclaration", c_int),
              ("isDefinition", c_int),
              ("isContainer", c_int),
              ("declAsContainer", POINTER(CXIdxContainerInfo)),
              ("isImplicit", c_int),
              ("attributes", POINTER(POINTER(CXIdxAttrInfo))),
              ("numAttributes", c_uint),
              ("flags", c_uint)]

class CXIdxObjCContainerDeclInfo(Structure):
  _fields_ = [("declInfo", POINTER(CXIdxDeclInfo)),
              ("kind", CXIdxObjCContainerKind)]

class CXIdxBaseClassInfo(Structure):
  _fields_ = [("base", POINTER(CXIdxEntityInfo)),
              ("cursor", CXCursor),
              ("loc", CXIdxLoc)]

class CXIdxObjCProtocolRefInfo(Structure):
  _fields_ = [("protocol", POINTER(CXIdxEntityInfo)),
              ("cursor", CXCursor),
              ("loc", CXIdxLoc)]

class CXIdxObjCProtocolRefListInfo(Structure):
  _fields_ = [("protocols", POINTER(POINTER(CXIdxObjCProtocolRefInfo))),
              ("numProtocols", c_uint)]

class CXIdxObjCInterfaceDeclInfo(Structure):
  _fields_ = [("containerInfo", POINTER(CXIdxObjCContainerDeclInfo)),
              ("superInfo", POINTER(CXIdxBaseClassInfo)),
              ("protocols", POINTER(CXIdxObjCProtocolRefListInfo))]

class CXIdxObjCCategoryDeclInfo(Structure):
  _fields_ = [("containerInfo", POINTER(CXIdxObjCContainerDeclInfo)),
              ("objcClass", POINTER(CXIdxEntityInfo)),
              ("classCursor", CXCursor),
              ("classLoc", CXIdxLoc),
              ("protocols", POINTER(CXIdxObjCProtocolRefListInfo))]

class CXIdxObjCPropertyDeclInfo(Structure):
  _fields_ = [("declInfo", POINTER(CXIdxDeclInfo)),
              ("getter", POINTER(CXIdxEntityInfo)),
              ("setter", POINTER(CXIdxEntityInfo))]

class CXIdxCXXClassDeclInfo(Structure):
  _fields_ = [("declInfo", POINTER(CXIdxDeclInfo)),
              ("bases", POINTER(POINTER(CXIdxBaseClassInfo))),
              ("numBases", c_uint)]

class CXIdxEntityRefInfo(Structure):
  _fields_ = [("kind", CXIdxEntityRefKind),
              ("cursor", CXCursor),
              ("loc", CXIdxLoc),
              ("referencedEntity", POINTER(CXIdxEntityInfo)),
              ("parentEntity", POINTER(CXIdxEntityInfo)),
              ("container", POINTER(CXIdxContainerInfo))]

class IndexerCallbacks(Structure):
  _fields_ = [("abortQuery", CFUNCTYPE(None, CXClientData, POINTER(c_void_p))),
              ("diagnostic", CFUNCTYPE(None, CXClientData, CXDiagnosticSet, POINTER(c_void_p))),
              ("enteredMainFile", CFUNCTYPE(CXIdxClientFile, CXClientData, CXFile, POINTER(c_void_p))),
              ("ppIncludedFile", CFUNCTYPE(CXIdxClientFile, CXClientData, POINTER(CXIdxIncludedFileInfo))),
              ("importedASTFile", CFUNCTYPE(CXIdxClientASTFile, CXClientData, POINTER(CXIdxImportedASTFileInfo))),
              ("startedTranslationUnit", CFUNCTYPE(CXIdxClientContainer, CXClientData, POINTER(c_void_p))),
              ("indexDeclaration", CFUNCTYPE(None, CXClientData, POINTER(CXIdxDeclInfo))),
              ("indexEntityReference", CFUNCTYPE(None, CXClientData, POINTER(CXIdxEntityRefInfo)))]

CXIndexAction = POINTER(c_void_p)

class CXComment(Structure):
  _fields_ = [("ASTNode", POINTER(c_void_p)),
              ("TranslationUnit", CXTranslationUnit)]

_function_infos = (
  ("clang_getCString",
    [CXString],
    c_char_p),
  ("clang_disposeString",
    [CXString],
    None),
  ("clang_getBuildSessionTimestamp",
    [],
    c_ulonglong),
  ("clang_VirtualFileOverlay_create",
    [c_uint],
    CXVirtualFileOverlay),
  ("clang_VirtualFileOverlay_addFileMapping",
    [CXVirtualFileOverlay, c_char_p, c_char_p],
    CXErrorCode),
  ("clang_VirtualFileOverlay_setCaseSensitivity",
    [CXVirtualFileOverlay, c_int],
    CXErrorCode),
  ("clang_VirtualFileOverlay_writeToBuffer",
    [CXVirtualFileOverlay, c_uint, POINTER(c_char_p), POINTER(c_uint)],
    CXErrorCode),
  ("clang_VirtualFileOverlay_dispose",
    [CXVirtualFileOverlay],
    None),
  ("clang_ModuleMapDescriptor_create",
    [c_uint],
    CXModuleMapDescriptor),
  ("clang_ModuleMapDescriptor_setFrameworkModuleName",
    [CXModuleMapDescriptor, c_char_p],
    CXErrorCode),
  ("clang_ModuleMapDescriptor_setUmbrellaHeader",
    [CXModuleMapDescriptor, c_char_p],
    CXErrorCode),
  ("clang_ModuleMapDescriptor_writeToBuffer",
    [CXModuleMapDescriptor, c_uint, POINTER(c_char_p), POINTER(c_uint)],
    CXErrorCode),
  ("clang_ModuleMapDescriptor_dispose",
    [CXModuleMapDescriptor],
    None),
  ("clang_createIndex",
    [c_int, c_int],
    CXIndex),
  ("clang_disposeIndex",
    [CXIndex],
    None),
  ("clang_CXIndex_setGlobalOptions",
    [CXIndex, c_uint],
    None),
  ("clang_CXIndex_getGlobalOptions",
    [CXIndex],
    c_uint),
  ("clang_getFileName",
    [CXFile],
    CXString),
  ("clang_getFileTime",
    [CXFile],
    time_t),
  ("clang_getFileUniqueID",
    [CXFile, POINTER(CXFileUniqueID)],
    c_int),
  ("clang_isFileMultipleIncludeGuarded",
    [CXTranslationUnit, CXFile],
    c_uint),
  ("clang_getFile",
    [CXTranslationUnit, c_char_p],
    CXFile),
  ("clang_getNullLocation",
    [],
    CXSourceLocation),
  ("clang_equalLocations",
    [CXSourceLocation, CXSourceLocation],
    c_uint),
  ("clang_getLocation",
    [CXTranslationUnit, CXFile, c_uint, c_uint],
    CXSourceLocation),
  ("clang_getLocationForOffset",
    [CXTranslationUnit, CXFile, c_uint],
    CXSourceLocation),
  ("clang_Location_isInSystemHeader",
    [CXSourceLocation],
    c_int),
  ("clang_Location_isFromMainFile",
    [CXSourceLocation],
    c_int),
  ("clang_getNullRange",
    [],
    CXSourceRange),
  ("clang_getRange",
    [CXSourceLocation, CXSourceLocation],
    CXSourceRange),
  ("clang_equalRanges",
    [CXSourceRange, CXSourceRange],
    c_uint),
  ("clang_Range_isNull",
    [CXSourceRange],
    c_int),
  ("clang_getExpansionLocation",
    [CXSourceLocation, POINTER(CXFile), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)],
    None),
  ("clang_getPresumedLocation",
    [CXSourceLocation, POINTER(CXString), POINTER(c_uint), POINTER(c_uint)],
    None),
  ("clang_getInstantiationLocation",
    [CXSourceLocation, POINTER(CXFile), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)],
    None),
  ("clang_getSpellingLocation",
    [CXSourceLocation, POINTER(CXFile), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)],
    None),
  ("clang_getFileLocation",
    [CXSourceLocation, POINTER(CXFile), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)],
    None),
  ("clang_getRangeStart",
    [CXSourceRange],
    CXSourceLocation),
  ("clang_getRangeEnd",
    [CXSourceRange],
    CXSourceLocation),
  ("clang_getSkippedRanges",
    [CXTranslationUnit, CXFile],
    POINTER(CXSourceRangeList)),
  ("clang_disposeSourceRangeList",
    [POINTER(CXSourceRangeList)],
    None),
  ("clang_getNumDiagnosticsInSet",
    [CXDiagnosticSet],
    c_uint),
  ("clang_getDiagnosticInSet",
    [CXDiagnosticSet, c_uint],
    CXDiagnostic),
  ("clang_loadDiagnostics",
    [c_char_p, POINTER(CXLoadDiag_Error), POINTER(CXString)],
    CXDiagnosticSet),
  ("clang_disposeDiagnosticSet",
    [CXDiagnosticSet],
    None),
  ("clang_getChildDiagnostics",
    [CXDiagnostic],
    CXDiagnosticSet),
  ("clang_getNumDiagnostics",
    [CXTranslationUnit],
    c_uint),
  ("clang_getDiagnostic",
    [CXTranslationUnit, c_uint],
    CXDiagnostic),
  ("clang_getDiagnosticSetFromTU",
    [CXTranslationUnit],
    CXDiagnosticSet),
  ("clang_disposeDiagnostic",
    [CXDiagnostic],
    None),
  ("clang_formatDiagnostic",
    [CXDiagnostic, c_uint],
    CXString),
  ("clang_defaultDiagnosticDisplayOptions",
    [],
    c_uint),
  ("clang_getDiagnosticSeverity",
    [CXDiagnostic],
    CXDiagnosticSeverity),
  ("clang_getDiagnosticLocation",
    [CXDiagnostic],
    CXSourceLocation),
  ("clang_getDiagnosticSpelling",
    [CXDiagnostic],
    CXString),
  ("clang_getDiagnosticOption",
    [CXDiagnostic, POINTER(CXString)],
    CXString),
  ("clang_getDiagnosticCategory",
    [CXDiagnostic],
    c_uint),
  ("clang_getDiagnosticCategoryName",
    [c_uint],
    CXString),
  ("clang_getDiagnosticCategoryText",
    [CXDiagnostic],
    CXString),
  ("clang_getDiagnosticNumRanges",
    [CXDiagnostic],
    c_uint),
  ("clang_getDiagnosticRange",
    [CXDiagnostic, c_uint],
    CXSourceRange),
  ("clang_getDiagnosticNumFixIts",
    [CXDiagnostic],
    c_uint),
  ("clang_getDiagnosticFixIt",
    [CXDiagnostic, c_uint, POINTER(CXSourceRange)],
    CXString),
  ("clang_getTranslationUnitSpelling",
    [CXTranslationUnit],
    CXString),
  ("clang_createTranslationUnitFromSourceFile",
    [CXIndex, c_char_p, c_int, POINTER(c_char_p), c_uint, POINTER(CXUnsavedFile)],
    CXTranslationUnit),
  ("clang_createTranslationUnit",
    [CXIndex, c_char_p],
    CXTranslationUnit),
  ("clang_createTranslationUnit2",
    [CXIndex, c_char_p, POINTER(CXTranslationUnit)],
    CXErrorCode),
  ("clang_defaultEditingTranslationUnitOptions",
    [],
    c_uint),
  ("clang_parseTranslationUnit",
    [CXIndex, c_char_p, POINTER(c_char_p), c_int, POINTER(CXUnsavedFile), c_uint, c_uint],
    CXTranslationUnit),
  ("clang_parseTranslationUnit2",
    [CXIndex, c_char_p, POINTER(c_char_p), c_int, POINTER(CXUnsavedFile), c_uint, c_uint, POINTER(CXTranslationUnit)],
    CXErrorCode),
  ("clang_defaultSaveOptions",
    [CXTranslationUnit],
    c_uint),
  ("clang_saveTranslationUnit",
    [CXTranslationUnit, c_char_p, c_uint],
    c_int),
  ("clang_disposeTranslationUnit",
    [CXTranslationUnit],
    None),
  ("clang_defaultReparseOptions",
    [CXTranslationUnit],
    c_uint),
  ("clang_reparseTranslationUnit",
    [CXTranslationUnit, c_uint, POINTER(CXUnsavedFile), c_uint],
    c_int),
  ("clang_getTUResourceUsageName",
    [CXTUResourceUsageKind],
    c_char_p),
  ("clang_getCXTUResourceUsage",
    [CXTranslationUnit],
    CXTUResourceUsage),
  ("clang_disposeCXTUResourceUsage",
    [CXTUResourceUsage],
    None),
  ("clang_getNullCursor",
    [],
    CXCursor),
  ("clang_getTranslationUnitCursor",
    [CXTranslationUnit],
    CXCursor),
  ("clang_equalCursors",
    [CXCursor, CXCursor],
    c_uint),
  ("clang_Cursor_isNull",
    [CXCursor],
    c_int),
  ("clang_hashCursor",
    [CXCursor],
    c_uint),
  ("clang_getCursorKind",
    [CXCursor],
    CXCursorKind),
  ("clang_isDeclaration",
    [CXCursorKind],
    c_uint),
  ("clang_isReference",
    [CXCursorKind],
    c_uint),
  ("clang_isExpression",
    [CXCursorKind],
    c_uint),
  ("clang_isStatement",
    [CXCursorKind],
    c_uint),
  ("clang_isAttribute",
    [CXCursorKind],
    c_uint),
  ("clang_isInvalid",
    [CXCursorKind],
    c_uint),
  ("clang_isTranslationUnit",
    [CXCursorKind],
    c_uint),
  ("clang_isPreprocessing",
    [CXCursorKind],
    c_uint),
  ("clang_isUnexposed",
    [CXCursorKind],
    c_uint),
  ("clang_getCursorLinkage",
    [CXCursor],
    CXLinkageKind),
  ("clang_getCursorAvailability",
    [CXCursor],
    CXAvailabilityKind),
  ("clang_getCursorPlatformAvailability",
    [CXCursor, POINTER(c_int), POINTER(CXString), POINTER(c_int), POINTER(CXString), POINTER(CXPlatformAvailability), c_int],
    c_int),
  ("clang_disposeCXPlatformAvailability",
    [POINTER(CXPlatformAvailability)],
    None),
  ("clang_getCursorLanguage",
    [CXCursor],
    CXLanguageKind),
  ("clang_Cursor_getTranslationUnit",
    [CXCursor],
    CXTranslationUnit),
  ("clang_createCXCursorSet",
    [],
    CXCursorSet),
  ("clang_disposeCXCursorSet",
    [CXCursorSet],
    None),
  ("clang_CXCursorSet_contains",
    [CXCursorSet, CXCursor],
    c_uint),
  ("clang_CXCursorSet_insert",
    [CXCursorSet, CXCursor],
    c_uint),
  ("clang_getCursorSemanticParent",
    [CXCursor],
    CXCursor),
  ("clang_getCursorLexicalParent",
    [CXCursor],
    CXCursor),
  ("clang_getOverriddenCursors",
    [CXCursor, POINTER(POINTER(CXCursor)), POINTER(c_uint)],
    None),
  ("clang_disposeOverriddenCursors",
    [POINTER(CXCursor)],
    None),
  ("clang_getIncludedFile",
    [CXCursor],
    CXFile),
  ("clang_getCursor",
    [CXTranslationUnit, CXSourceLocation],
    CXCursor),
  ("clang_getCursorLocation",
    [CXCursor],
    CXSourceLocation),
  ("clang_getCursorExtent",
    [CXCursor],
    CXSourceRange),
  ("clang_getCursorType",
    [CXCursor],
    CXType),
  ("clang_getTypeSpelling",
    [CXType],
    CXString),
  ("clang_getTypedefDeclUnderlyingType",
    [CXCursor],
    CXType),
  ("clang_getEnumDeclIntegerType",
    [CXCursor],
    CXType),
  ("clang_getEnumConstantDeclValue",
    [CXCursor],
    c_longlong),
  ("clang_getEnumConstantDeclUnsignedValue",
    [CXCursor],
    c_ulonglong),
  ("clang_getFieldDeclBitWidth",
    [CXCursor],
    c_int),
  ("clang_Cursor_getNumArguments",
    [CXCursor],
    c_int),
  ("clang_Cursor_getArgument",
    [CXCursor, c_uint],
    CXCursor),
  ("clang_equalTypes",
    [CXType, CXType],
    c_uint),
  ("clang_getCanonicalType",
    [CXType],
    CXType),
  ("clang_isConstQualifiedType",
    [CXType],
    c_uint),
  ("clang_isVolatileQualifiedType",
    [CXType],
    c_uint),
  ("clang_isRestrictQualifiedType",
    [CXType],
    c_uint),
  ("clang_getPointeeType",
    [CXType],
    CXType),
  ("clang_getTypeDeclaration",
    [CXType],
    CXCursor),
  ("clang_getDeclObjCTypeEncoding",
    [CXCursor],
    CXString),
  ("clang_getTypeKindSpelling",
    [CXTypeKind],
    CXString),
  ("clang_getFunctionTypeCallingConv",
    [CXType],
    CXCallingConv),
  ("clang_getResultType",
    [CXType],
    CXType),
  ("clang_getNumArgTypes",
    [CXType],
    c_int),
  ("clang_getArgType",
    [CXType, c_uint],
    CXType),
  ("clang_isFunctionTypeVariadic",
    [CXType],
    c_uint),
  ("clang_getCursorResultType",
    [CXCursor],
    CXType),
  ("clang_isPODType",
    [CXType],
    c_uint),
  ("clang_getElementType",
    [CXType],
    CXType),
  ("clang_getNumElements",
    [CXType],
    c_longlong),
  ("clang_getArrayElementType",
    [CXType],
    CXType),
  ("clang_getArraySize",
    [CXType],
    c_longlong),
  ("clang_Type_getAlignOf",
    [CXType],
    c_longlong),
  ("clang_Type_getClassType",
    [CXType],
    CXType),
  ("clang_Type_getSizeOf",
    [CXType],
    c_longlong),
  ("clang_Type_getOffsetOf",
    [CXType, c_char_p],
    c_longlong),
  ("clang_Type_getNumTemplateArguments",
    [CXType],
    c_int),
  ("clang_Type_getTemplateArgumentAsType",
    [CXType, c_uint],
    CXType),
  ("clang_Type_getCXXRefQualifier",
    [CXType],
    CXRefQualifierKind),
  ("clang_Cursor_isBitField",
    [CXCursor],
    c_uint),
  ("clang_isVirtualBase",
    [CXCursor],
    c_uint),
  ("clang_getCXXAccessSpecifier",
    [CXCursor],
    CX_CXXAccessSpecifier),
  ("clang_getNumOverloadedDecls",
    [CXCursor],
    c_uint),
  ("clang_getOverloadedDecl",
    [CXCursor, c_uint],
    CXCursor),
  ("clang_getIBOutletCollectionType",
    [CXCursor],
    CXType),
  ("clang_visitChildren",
    [CXCursor, CXCursorVisitor, CXClientData],
    c_uint),
  ("clang_getCursorUSR",
    [CXCursor],
    CXString),
  ("clang_constructUSR_ObjCClass",
    [c_char_p],
    CXString),
  ("clang_constructUSR_ObjCCategory",
    [c_char_p, c_char_p],
    CXString),
  ("clang_constructUSR_ObjCProtocol",
    [c_char_p],
    CXString),
  ("clang_constructUSR_ObjCIvar",
    [c_char_p, CXString],
    CXString),
  ("clang_constructUSR_ObjCMethod",
    [c_char_p, c_uint, CXString],
    CXString),
  ("clang_constructUSR_ObjCProperty",
    [c_char_p, CXString],
    CXString),
  ("clang_getCursorSpelling",
    [CXCursor],
    CXString),
  ("clang_Cursor_getSpellingNameRange",
    [CXCursor, c_uint, c_uint],
    CXSourceRange),
  ("clang_getCursorDisplayName",
    [CXCursor],
    CXString),
  ("clang_getCursorReferenced",
    [CXCursor],
    CXCursor),
  ("clang_getCursorDefinition",
    [CXCursor],
    CXCursor),
  ("clang_isCursorDefinition",
    [CXCursor],
    c_uint),
  ("clang_getCanonicalCursor",
    [CXCursor],
    CXCursor),
  ("clang_Cursor_getObjCSelectorIndex",
    [CXCursor],
    c_int),
  ("clang_Cursor_isDynamicCall",
    [CXCursor],
    c_int),
  ("clang_Cursor_getReceiverType",
    [CXCursor],
    CXType),
  ("clang_Cursor_getObjCPropertyAttributes",
    [CXCursor, c_uint],
    c_uint),
  ("clang_Cursor_getObjCDeclQualifiers",
    [CXCursor],
    c_uint),
  ("clang_Cursor_isObjCOptional",
    [CXCursor],
    c_uint),
  ("clang_Cursor_isVariadic",
    [CXCursor],
    c_uint),
  ("clang_Cursor_getCommentRange",
    [CXCursor],
    CXSourceRange),
  ("clang_Cursor_getRawCommentText",
    [CXCursor],
    CXString),
  ("clang_Cursor_getBriefCommentText",
    [CXCursor],
    CXString),
  ("clang_Cursor_getModule",
    [CXCursor],
    CXModule),
  ("clang_getModuleForFile",
    [CXTranslationUnit, CXFile],
    CXModule),
  ("clang_Module_getASTFile",
    [CXModule],
    CXFile),
  ("clang_Module_getParent",
    [CXModule],
    CXModule),
  ("clang_Module_getName",
    [CXModule],
    CXString),
  ("clang_Module_getFullName",
    [CXModule],
    CXString),
  ("clang_Module_isSystem",
    [CXModule],
    c_int),
  ("clang_Module_getNumTopLevelHeaders",
    [CXTranslationUnit, CXModule],
    c_uint),
  ("clang_Module_getTopLevelHeader",
    [CXTranslationUnit, CXModule, c_uint],
    CXFile),
  ("clang_CXXMethod_isPureVirtual",
    [CXCursor],
    c_uint),
  ("clang_CXXMethod_isStatic",
    [CXCursor],
    c_uint),
  ("clang_CXXMethod_isVirtual",
    [CXCursor],
    c_uint),
  ("clang_CXXMethod_isConst",
    [CXCursor],
    c_uint),
  ("clang_getTemplateCursorKind",
    [CXCursor],
    CXCursorKind),
  ("clang_getSpecializedCursorTemplate",
    [CXCursor],
    CXCursor),
  ("clang_getCursorReferenceNameRange",
    [CXCursor, c_uint, c_uint],
    CXSourceRange),
  ("clang_getTokenKind",
    [CXToken],
    CXTokenKind),
  ("clang_getTokenSpelling",
    [CXTranslationUnit, CXToken],
    CXString),
  ("clang_getTokenLocation",
    [CXTranslationUnit, CXToken],
    CXSourceLocation),
  ("clang_getTokenExtent",
    [CXTranslationUnit, CXToken],
    CXSourceRange),
  ("clang_tokenize",
    [CXTranslationUnit, CXSourceRange, POINTER(POINTER(CXToken)), POINTER(c_uint)],
    None),
  ("clang_annotateTokens",
    [CXTranslationUnit, POINTER(CXToken), c_uint, POINTER(CXCursor)],
    None),
  ("clang_disposeTokens",
    [CXTranslationUnit, POINTER(CXToken), c_uint],
    None),
  ("clang_getCursorKindSpelling",
    [CXCursorKind],
    CXString),
  ("clang_getDefinitionSpellingAndExtent",
    [CXCursor, POINTER(c_char_p), POINTER(c_char_p), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)],
    None),
  ("clang_enableStackTraces",
    [],
    None),
  ("clang_executeOnThread",
    [CFUNCTYPE(None, POINTER(c_void_p)), POINTER(c_void_p), c_uint],
    None),
  ("clang_getCompletionChunkKind",
    [CXCompletionString, c_uint],
    CXCompletionChunkKind),
  ("clang_getCompletionChunkText",
    [CXCompletionString, c_uint],
    CXString),
  ("clang_getCompletionChunkCompletionString",
    [CXCompletionString, c_uint],
    CXCompletionString),
  ("clang_getNumCompletionChunks",
    [CXCompletionString],
    c_uint),
  ("clang_getCompletionPriority",
    [CXCompletionString],
    c_uint),
  ("clang_getCompletionAvailability",
    [CXCompletionString],
    CXAvailabilityKind),
  ("clang_getCompletionNumAnnotations",
    [CXCompletionString],
    c_uint),
  ("clang_getCompletionAnnotation",
    [CXCompletionString, c_uint],
    CXString),
  ("clang_getCompletionParent",
    [CXCompletionString, POINTER(CXCursorKind)],
    CXString),
  ("clang_getCompletionBriefComment",
    [CXCompletionString],
    CXString),
  ("clang_getCursorCompletionString",
    [CXCursor],
    CXCompletionString),
  ("clang_defaultCodeCompleteOptions",
    [],
    c_uint),
  ("clang_codeCompleteAt",
    [CXTranslationUnit, c_char_p, c_uint, c_uint, POINTER(CXUnsavedFile), c_uint, c_uint],
    POINTER(CXCodeCompleteResults)),
  ("clang_sortCodeCompletionResults",
    [POINTER(CXCompletionResult), c_uint],
    None),
  ("clang_disposeCodeCompleteResults",
    [POINTER(CXCodeCompleteResults)],
    None),
  ("clang_codeCompleteGetNumDiagnostics",
    [POINTER(CXCodeCompleteResults)],
    c_uint),
  ("clang_codeCompleteGetDiagnostic",
    [POINTER(CXCodeCompleteResults), c_uint],
    CXDiagnostic),
  ("clang_codeCompleteGetContexts",
    [POINTER(CXCodeCompleteResults)],
    c_ulonglong),
  ("clang_codeCompleteGetContainerKind",
    [POINTER(CXCodeCompleteResults), POINTER(c_uint)],
    CXCursorKind),
  ("clang_codeCompleteGetContainerUSR",
    [POINTER(CXCodeCompleteResults)],
    CXString),
  ("clang_codeCompleteGetObjCSelector",
    [POINTER(CXCodeCompleteResults)],
    CXString),
  ("clang_getClangVersion",
    [],
    CXString),
  ("clang_toggleCrashRecovery",
    [c_uint],
    None),
  ("clang_getInclusions",
    [CXTranslationUnit, CXInclusionVisitor, CXClientData],
    None),
  ("clang_getRemappings",
    [c_char_p],
    CXRemapping),
  ("clang_getRemappingsFromFileList",
    [POINTER(c_char_p), c_uint],
    CXRemapping),
  ("clang_remap_getNumFiles",
    [CXRemapping],
    c_uint),
  ("clang_remap_getFilenames",
    [CXRemapping, c_uint, POINTER(CXString), POINTER(CXString)],
    None),
  ("clang_remap_dispose",
    [CXRemapping],
    None),
  ("clang_findReferencesInFile",
    [CXCursor, CXFile, CXCursorAndRangeVisitor],
    CXResult),
  ("clang_findIncludesInFile",
    [CXTranslationUnit, CXFile, CXCursorAndRangeVisitor],
    CXResult),
  ("clang_index_isEntityObjCContainerKind",
    [CXIdxEntityKind],
    c_int),
  ("clang_index_getObjCContainerDeclInfo",
    [POINTER(CXIdxDeclInfo)],
    POINTER(CXIdxObjCContainerDeclInfo)),
  ("clang_index_getObjCInterfaceDeclInfo",
    [POINTER(CXIdxDeclInfo)],
    POINTER(CXIdxObjCInterfaceDeclInfo)),
  ("clang_index_getObjCCategoryDeclInfo",
    [POINTER(CXIdxDeclInfo)],
    POINTER(CXIdxObjCCategoryDeclInfo)),
  ("clang_index_getObjCProtocolRefListInfo",
    [POINTER(CXIdxDeclInfo)],
    POINTER(CXIdxObjCProtocolRefListInfo)),
  ("clang_index_getObjCPropertyDeclInfo",
    [POINTER(CXIdxDeclInfo)],
    POINTER(CXIdxObjCPropertyDeclInfo)),
  ("clang_index_getIBOutletCollectionAttrInfo",
    [POINTER(CXIdxAttrInfo)],
    POINTER(CXIdxIBOutletCollectionAttrInfo)),
  ("clang_index_getCXXClassDeclInfo",
    [POINTER(CXIdxDeclInfo)],
    POINTER(CXIdxCXXClassDeclInfo)),
  ("clang_index_getClientContainer",
    [POINTER(CXIdxContainerInfo)],
    CXIdxClientContainer),
  ("clang_index_setClientContainer",
    [POINTER(CXIdxContainerInfo), CXIdxClientContainer],
    None),
  ("clang_index_getClientEntity",
    [POINTER(CXIdxEntityInfo)],
    CXIdxClientEntity),
  ("clang_index_setClientEntity",
    [POINTER(CXIdxEntityInfo), CXIdxClientEntity],
    None),
  ("clang_IndexAction_create",
    [CXIndex],
    CXIndexAction),
  ("clang_IndexAction_dispose",
    [CXIndexAction],
    None),
  ("clang_indexSourceFile",
    [CXIndexAction, CXClientData, POINTER(IndexerCallbacks), c_uint, c_uint, c_char_p, POINTER(c_char_p), c_int, POINTER(CXUnsavedFile), c_uint, POINTER(CXTranslationUnit), c_uint],
    c_int),
  ("clang_indexTranslationUnit",
    [CXIndexAction, CXClientData, POINTER(IndexerCallbacks), c_uint, c_uint, CXTranslationUnit],
    c_int),
  ("clang_indexLoc_getFileLocation",
    [CXIdxLoc, POINTER(CXIdxClientFile), POINTER(CXFile), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)],
    None),
  ("clang_indexLoc_getCXSourceLocation",
    [CXIdxLoc],
    CXSourceLocation),
  ("clang_Cursor_getParsedComment",
    [CXCursor],
    CXComment),
  ("clang_Comment_getKind",
    [CXComment],
    CXCommentKind),
  ("clang_Comment_getNumChildren",
    [CXComment],
    c_uint),
  ("clang_Comment_getChild",
    [CXComment, c_uint],
    CXComment),
  ("clang_Comment_isWhitespace",
    [CXComment],
    c_uint),
  ("clang_InlineContentComment_hasTrailingNewline",
    [CXComment],
    c_uint),
  ("clang_TextComment_getText",
    [CXComment],
    CXString),
  ("clang_InlineCommandComment_getCommandName",
    [CXComment],
    CXString),
  ("clang_InlineCommandComment_getRenderKind",
    [CXComment],
    CXCommentInlineCommandRenderKind),
  ("clang_InlineCommandComment_getNumArgs",
    [CXComment],
    c_uint),
  ("clang_InlineCommandComment_getArgText",
    [CXComment, c_uint],
    CXString),
  ("clang_HTMLTagComment_getTagName",
    [CXComment],
    CXString),
  ("clang_HTMLStartTagComment_isSelfClosing",
    [CXComment],
    c_uint),
  ("clang_HTMLStartTag_getNumAttrs",
    [CXComment],
    c_uint),
  ("clang_HTMLStartTag_getAttrName",
    [CXComment, c_uint],
    CXString),
  ("clang_HTMLStartTag_getAttrValue",
    [CXComment, c_uint],
    CXString),
  ("clang_BlockCommandComment_getCommandName",
    [CXComment],
    CXString),
  ("clang_BlockCommandComment_getNumArgs",
    [CXComment],
    c_uint),
  ("clang_BlockCommandComment_getArgText",
    [CXComment, c_uint],
    CXString),
  ("clang_BlockCommandComment_getParagraph",
    [CXComment],
    CXComment),
  ("clang_ParamCommandComment_getParamName",
    [CXComment],
    CXString),
  ("clang_ParamCommandComment_isParamIndexValid",
    [CXComment],
    c_uint),
  ("clang_ParamCommandComment_getParamIndex",
    [CXComment],
    c_uint),
  ("clang_ParamCommandComment_isDirectionExplicit",
    [CXComment],
    c_uint),
  ("clang_ParamCommandComment_getDirection",
    [CXComment],
    CXCommentParamPassDirection),
  ("clang_TParamCommandComment_getParamName",
    [CXComment],
    CXString),
  ("clang_TParamCommandComment_isParamPositionValid",
    [CXComment],
    c_uint),
  ("clang_TParamCommandComment_getDepth",
    [CXComment],
    c_uint),
  ("clang_TParamCommandComment_getIndex",
    [CXComment, c_uint],
    c_uint),
  ("clang_VerbatimBlockLineComment_getText",
    [CXComment],
    CXString),
  ("clang_VerbatimLineComment_getText",
    [CXComment],
    CXString),
  ("clang_HTMLTagComment_getAsString",
    [CXComment],
    CXString),
  ("clang_FullComment_getAsHTML",
    [CXComment],
    CXString),
  ("clang_FullComment_getAsXML",
    [CXComment],
    CXString),
)

