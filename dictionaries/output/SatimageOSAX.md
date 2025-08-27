# Satimage OSAX: AppleScript/JSX

## Table of Contents

### Applescript types
#### Commands
- [find text obsolete](#find_text_obsolete)
- [replace obsolete](#replace_obsolete)
- [extract string](#extract_string)
- [findxmlstag](#findxmlstag)
- [gziptext](#gziptext)
- [gunziptext](#gunziptext)
#### Classs
- [reference](#reference)
- [byte](#byte)
- [point](#point)
- [location reference](#location_reference)
- [alias](#alias)
- [file specification](#file_specification)
### Satimage Text Additions
#### Commands
- [find text](#find_text)
- [change](#change)
- [re_compile](#re_compile)
- [splittext](#splittext)
- [filter text](#filter_text)
- [file offset](#file_offset)
- [readtext](#readtext)
- [writetext](#writetext)
- [uppercase](#uppercase)
- [lowercase](#lowercase)
- [titlecase](#titlecase)
- [format](#format)
- [atof](#atof)
- [atoi](#atoi)
- [encode entities](#encode_entities)
- [resolve entities](#resolve_entities)
- [escapeURL](#escapeurl)
- [unescapeURL](#unescapeurl)
- [normalize unicode](#normalize_unicode)
- [transform unicode](#transform_unicode)
- [hash](#hash)
- [join](#join)
- [printf](#printf)
- [strftime](#strftime)
- [strptime](#strptime)
#### Record Types
- [matchrecord](#matchrecord)
### Satimage File Additions
#### Commands
- [alias description for](#alias_description_for)
- [navchoose file](#navchoose_file)
- [navchoose folder](#navchoose_folder)
- [navchoose object](#navchoose_object)
- [navchoose volume](#navchoose_volume)
- [navask save](#navask_save)
- [navchoose file name](#navchoose_file_name)
- [navnew folder](#navnew_folder)
- [URL info for](#url_info_for)
- [absoluteURL](#absoluteurl)
- [relativeURL](#relativeurl)
- [list files](#list_files)
- [glob](#glob)
- [backup](#backup)
#### Classs
- [URL information](#url_information)
### Resource Suite
#### Commands
- [load resource](#load_resource)
- [list resources](#list_resources)
- [get resource name](#get_resource_name)
### Mathematical Functions
#### Commands
- [abs](#abs)
- [acos](#acos)
- [acosh](#acosh)
- [asin](#asin)
- [asinh](#asinh)
- [atan](#atan)
- [atan2](#atan2)
- [atanh](#atanh)
- [ceil](#ceil)
- [cosh](#cosh)
- [cos](#cos)
- [erf](#erf)
- [erfc](#erfc)
- [exp](#exp)
- [floor](#floor)
- [gamma](#gamma)
- [hypot](#hypot)
- [lgamma](#lgamma)
- [ln](#ln)
- [log10](#log10)
- [sin](#sin)
- [sinh](#sinh)
- [sqr](#sqr)
- [sqrt](#sqrt)
- [tan](#tan)
- [tanh](#tanh)
- [trunc](#trunc)
### Arrays
#### Commands
- [createarray](#createarray)
- [creatematrix](#creatematrix)
- [randomarray](#randomarray)
- [replacemissingvalue](#replacemissingvalue)
- [removemissingvalue](#removemissingvalue)
- [extractitem](#extractitem)
- [extractarray](#extractarray)
- [changearray](#changearray)
- [insertarray](#insertarray)
- [resamplematrix](#resamplematrix)
- [reversearray](#reversearray)
- [multlist](#multlist)
- [divlist](#divlist)
- [addlist](#addlist)
- [sublist](#sublist)
- [runningsum](#runningsum)
- [statlist](#statlist)
- [histogram](#histogram)
- [evalformula](#evalformula)
- [maskarray](#maskarray)
- [listvariables](#listvariables)
- [smootharray](#smootharray)
- [filter](#filter)
- [evalpolynomial](#evalpolynomial)
- [roots of](#roots_of)
- [composepolynomial](#composepolynomial)
- [pade approximant](#pade_approximant)
- [fitpolynomial](#fitpolynomial)
- [fitrational](#fitrational)
- [read binary](#read_binary)
- [write binary](#write_binary)
- [find peaks](#find_peaks)
- [arrays auto filling](#arrays_auto_filling)
#### Record Types
- [matrix](#matrix)
- [fitrecord](#fitrecord)
- [statsrecord](#statsrecord)
#### Value Types
- [array of real](#array_of_real)
- [list of real](#list_of_real)
- [list of integer](#list_of_integer)
- [polynomial](#polynomial)
### Array and List Utilities
#### Commands
- [sortlist](#sortlist)
- [masklist](#masklist)
- [topological sort](#topological_sort)
- [suppress item](#suppress_item)
- [exclude items](#exclude_items)
- [keep items](#keep_items)
- [special concat](#special_concat)
### Satimage XML DOM
#### Commands
- [XMLOpen](#xmlopen)
- [XMLClose](#xmlclose)
- [XMLRoot](#xmlroot)
- [XMLCount](#xmlcount)
- [XMLCountElement](#xmlcountelement)
- [XMLChild](#xmlchild)
- [XMLElement](#xmlelement)
- [XMLParent](#xmlparent)
- [XMLNextSibling](#xmlnextsibling)
- [XMLNextElement](#xmlnextelement)
- [XMLPrevSibling](#xmlprevsibling)
- [XMLPrevElement](#xmlprevelement)
- [XMLTagName](#xmltagname)
- [XMLGetAttribute](#xmlgetattribute)
- [XMLSetAttribute](#xmlsetattribute)
- [XMLRemoveAttribute](#xmlremoveattribute)
- [XMLRemove](#xmlremove)
- [XMLRemoveChildren](#xmlremovechildren)
- [XMLExists](#xmlexists)
- [XMLNewChild](#xmlnewchild)
- [XMLNewSibling](#xmlnewsibling)
- [XMLNodeInfo](#xmlnodeinfo)
- [XMLDisplayXML](#xmldisplayxml)
- [XMLSetXML](#xmlsetxml)
- [XMLGetText](#xmlgettext)
- [XMLSetText](#xmlsettext)
- [XMLAppendText](#xmlappendtext)
- [XMLGetNameSpace](#xmlgetnamespace)
- [XMLGetNameSpaces](#xmlgetnamespaces)
- [XMLGetNameSpaceFromPrefix](#xmlgetnamespacefromprefix)
- [XMLAddNamespace](#xmladdnamespace)
- [XMLFind](#xmlfind)
- [XMLFindText](#xmlfindtext)
- [XMLRegexp](#xmlregexp)
- [XMLBase](#xmlbase)
- [XMLSetBase](#xmlsetbase)
- [XMLAbsoluteURL](#xmlabsoluteurl)
- [XMLRelativeURL](#xmlrelativeurl)
- [XMLError](#xmlerror)
#### Classs
- [anything](#anything)
- [dictionary](#dictionary)
- [alias](#alias)
- [file specification](#file_specification)
#### Record Types
- [namespace](#namespace)
- [NodeInfo](#nodeinfo)
#### Value Types
- [XMLRef](#xmlref)
### XML XPath, XSLT
#### Commands
- [XMLXPath](#xmlxpath)
- [XMLSetContext](#xmlsetcontext)
- [XMLGetContext](#xmlgetcontext)
- [XMLGetNodePath](#xmlgetnodepath)
- [XMLXPointer](#xmlxpointer)
- [XMLEscapeXPointer](#xmlescapexpointer)
- [XMLGetXPointer](#xmlgetxpointer)
- [XMLTransform](#xmltransform)
- [XMLCompile](#xmlcompile)
- [XMLNewIndex](#xmlnewindex)
- [XMLLookup](#xmllookup)
- [XMLEntries](#xmlentries)
- [XMLIndexDocument](#xmlindexdocument)
- [XMLStrings](#xmlstrings)
- [XMLLocalize](#xmllocalize)
#### Record Types
- [XPathRef](#xpathref)
### XML Documents
#### Commands
- [XMLURL](#xmlurl)
- [XMLSetURL](#xmlseturl)
- [XMLDocument](#xmldocument)
- [XMLCatalog](#xmlcatalog)
- [XMLCloneDocument](#xmlclonedocument)
- [XMLXInclude](#xmlxinclude)
- [XMLGetEncoding](#xmlgetencoding)
- [XMLSetEncoding](#xmlsetencoding)
- [XMLSetIndentString](#xmlsetindentstring)
- [XMLSave](#xmlsave)
- [XMLErrorLevel](#xmlerrorlevel)
- [XMLExtendedChar](#xmlextendedchar)
- [XMLListDocuments](#xmllistdocuments)
- [XMLSetDocID](#xmlsetdocid)
- [XMLGetDocByID](#xmlgetdocbyid)
- [XMLc14n](#xmlc14n)
- [XMLSetExtras](#xmlsetextras)
- [XMLGetExtras](#xmlgetextras)
### XML Validation
#### Commands
- [XMLValidate](#xmlvalidate)
- [XMLSchema](#xmlschema)
- [XMLRelaxNG](#xmlrelaxng)
- [XMLCheckDTD](#xmlcheckdtd)
- [XMLGetByID](#xmlgetbyid)
- [XMLGetxmlID](#xmlgetxmlid)
- [XMLValidName](#xmlvalidname)
- [XMLValidNCName](#xmlvalidncname)
- [XMLDu](#xmldu)
- [XMLGetID](#xmlgetid)
- [XMLFromID](#xmlfromid)
### Satimage PropertyList Additions
#### Commands
- [PlistNew](#plistnew)
- [PlistOpen](#plistopen)
- [PlistClose](#plistclose)
- [PlistRetain](#plistretain)
- [PlistSave](#plistsave)
- [PlistBinaryFormat](#plistbinaryformat)
- [PlistCount](#plistcount)
- [PlistChild](#plistchild)
- [PlistType](#plisttype)
- [PlistGet](#plistget)
- [PlistGetXML](#plistgetxml)
- [PlistGetKeys](#plistgetkeys)
- [PlistSet](#plistset)
- [PlistNewChild](#plistnewchild)
- [PlistRemoveChild](#plistremovechild)
- [PlistEqual](#plistequal)
- [PlistExist](#plistexist)
- [PlistMatch](#plistmatch)
- [PlistURL](#plisturl)
- [PlistDocument](#plistdocument)
- [PlistListDocuments](#plistlistdocuments)
- [PlistAdd](#plistadd)
- [PlistToJSON](#plisttojson)
- [PlistToJavaScript](#plisttojavascript)
- [PlistFromJSON](#plistfromjson)
- [PlistSetDocID](#plistsetdocid)
- [PlistGetDocByID](#plistgetdocbyid)
- [PlistGetID](#plistgetid)
- [PlistFromID](#plistfromid)
#### Value Types
- [CFRef](#cfref)
### Satimage Pool Additions
#### Commands
- [SetPool](#setpool)
- [DeletePool](#deletepool)
- [GetPool](#getpool)
### XNF Additions
#### Commands
- [XNFOpen](#xnfopen)
- [XNFSaveBundle](#xnfsavebundle)
- [XNFNewDataSet](#xnfnewdataset)
- [XNFGetDataSet](#xnfgetdataset)
- [XNFGetDimensions](#xnfgetdimensions)
- [XNFNewArray](#xnfnewarray)
- [XNFNewFileData](#xnfnewfiledata)
- [XNFGetArray](#xnfgetarray)
- [XNFSetScale](#xnfsetscale)
- [XNFSetScaleReference](#xnfsetscalereference)
- [XNFSetScaleRange](#xnfsetscalerange)
- [XNFGetScales](#xnfgetscales)
- [XNFGetArray3D](#xnfgetarray3d)
- [XNFRemove](#xnfremove)
### 
#### Commands
- [XMLCookie](#xmlcookie)
- [XMLRegisterScheme](#xmlregisterscheme)
- [XMLDisplayEntity](#xmldisplayentity)
- [XMLResolveScheme](#xmlresolvescheme)
- [PlistCopy](#plistcopy)
- [ExtractBinary](#extractbinary)
- [XMLObsolete](#xmlobsolete)
- [XMLGetTextObso](#xmlgettextobso)
- [XMLGetAttributeObso](#xmlgetattributeobso)
- [XMLTagNameObso](#xmltagnameobso)
- [XMLFullTagName](#xmlfulltagname)
- [XMLDisplayXMLObso](#xmldisplayxmlobso)
- [XMLNodeInfoObso](#xmlnodeinfoobso)
- [XMLSetTagName](#xmlsettagname)
- [XMLRemoveNamespace](#xmlremovenamespace)
- [ListPools](#listpools)
- [XMLXPathCompile](#xmlxpathcompile)
- [XMLGetNode at line](#xmlgetnode_at_line)
- [XMLParseCURIE](#xmlparsecurie)
- [XMLGetArray](#xmlgetarray)
- [XMLSetArray](#xmlsetarray)
### Linear algebra
#### Commands
- [currentEndianess](#currentendianess)
- [transpose](#transpose)
- [multmatrix](#multmatrix)
- [invertmatrix](#invertmatrix)
- [solve linear system](#solve_linear_system)
- [compute eigenvalues](#compute_eigenvalues)
- [LUdecomposition](#ludecomposition)
- [pivot](#pivot)
- [compute determinant](#compute_determinant)
#### Classs
- [anything](#anything)
- [array of real](#array_of_real)
- [matrix](#matrix)
- [dimensions](#dimensions)
- [scale](#scale)
- [number of field](#number_of_field)
- [alias](#alias)
- [file specification](#file_specification)
- [bounding rectangle](#bounding_rectangle)
- [XMLRef](#xmlref)
#### Record Types
- [Lapack result](#lapack_result)
### FFT and convolution
#### Commands
- [fft1d](#fft1d)
- [fft2d](#fft2d)
- [filterarray](#filterarray)
- [convolve](#convolve)
- [correlate](#correlate)
- [interpolate](#interpolate)
### Image files
#### Commands
- [imagefile bounds](#imagefile_bounds)
- [convert imagefile](#convert_imagefile)
- [create grayimagefile](#create_grayimagefile)
- [particles](#particles)
### 3D array handling
#### Commands
- [open3D](#open3d)
- [close3D](#close3d)
- [info3D](#info3d)
- [contents3D](#contents3d)
- [list3D](#list3d)
- [rename3D](#rename3d)
- [extract3D](#extract3d)
- [isosurface](#isosurface)
- [streamline](#streamline)
#### Value Types
- [Array3DRef](#array3dref)
### FITS
#### Commands
- [FITSOpen](#fitsopen)
- [FITSClose](#fitsclose)
- [FITSCount](#fitscount)
- [FITSMovein](#fitsmovein)
- [FITSInfo](#fitsinfo)
- [FITSPlist](#fitsplist)
- [FITSReadImage](#fitsreadimage)
- [FITSTableInfo](#fitstableinfo)
- [FITSReadTable](#fitsreadtable)
- [FITSExtractimage](#fitsextractimage)
#### Classs
- [kind](#kind)
- [alias](#alias)
- [array of real](#array_of_real)
- [dimensions](#dimensions)
- [matrix](#matrix)
### Files and folders suite
#### Commands
- [filenew](#filenew)
- [mkdir](#mkdir)
- [filecopy](#filecopy)
- [filemove](#filemove)
- [fileremove](#fileremove)
- [filegetname](#filegetname)
- [filerename](#filerename)
- [mkstemp](#mkstemp)
- [mkdtemp](#mkdtemp)
- [chmod](#chmod)
#### Classs
- [alias](#alias)
- [file specification](#file_specification)
### Symlink suite
#### Commands
- [create symlink](#create_symlink)
- [testsymlink](#testsymlink)
- [readlink](#readlink)


## Applescript types

**Description:** None

<a name="find_text_obsolete"></a>
```yaml
---
type: command
name: find text obsolete
suite: Applescript types
---
```

## Command: find text obsolete

**Description:** find text literally or using regular expression syntax.

### Direct Parameter
- **Description:** the substring to search for
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in |  | string | No |
| case sensitive | default true | boolean | Yes |
| regexp | default false | boolean | Yes |
| using | the pattern to generate the string (regexp) | string | Yes |

### Result
- **Description:** {first character index,last  character index}
- **Types:** list of integer
<a name="replace_obsolete"></a>
```yaml
---
type: command
name: replace obsolete
suite: Applescript types
---
```

## Command: replace obsolete

**Description:** replace all occurences of a substring

### Direct Parameter
- **Description:** the substring to search for
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | the replacement string | string | No |
| in | a string or a file path | anything | No |
| case sensitive | default true | boolean | Yes |
| regexp | default false | boolean | Yes |

### Result
- **Description:** the new string
- **Types:** anything
<a name="extract_string"></a>
```yaml
---
type: command
name: extract string
suite: Applescript types
---
```

## Command: extract string

**Description:** extract a substring out of a string. Same as AppleScript's expression "text i thru j of s". Not Unicode-compliant.

### Direct Parameter
- **Description:** the original string
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | index of the first character. Default: 1. Negative numbers index characters backwards. | integer | Yes |
| to | index of the last character. Default: -1. Negative numbers index characters backwards. | integer | Yes |

### Result
- **Description:** the substring
- **Types:** string
<a name="findxmlstag"></a>
```yaml
---
type: command
name: findxmlstag
suite: Applescript types
---
```

## Command: findxmlstag

### Direct Parameter
- **Description:** the offset
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the offset | integer | No |

### Result
- **Description:** the range
- **Types:** integer
<a name="gziptext"></a>
```yaml
---
type: command
name: gziptext
suite: Applescript types
---
```

## Command: gziptext

### Direct Parameter
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| encoding | a IANA charset name ("MACINTOSH", "UTF-8", "UTF-16", "ISO-8859-1"…). Default: "UTF-8" | string | Yes |
| missing char | characters that cannot be converted to the specified encoding are represented with this character. Default: gziptext returns an error if it encounters an untranslatable character | string | Yes |

### Result
- **Types:** gzip
<a name="gunziptext"></a>
```yaml
---
type: command
name: gunziptext
suite: Applescript types
---
```

## Command: gunziptext

### Direct Parameter
- **Types:** gzip
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| encoding | a IANA charset name ("MACINTOSH", "UTF-8", "UTF-16", "ISO-8859-1"…). Default: "UTF-8" | string | Yes |

### Result
- **Types:** data
<a name="reference"></a>
```yaml
---
type: class
name: reference
suite: Applescript types
---
```

## Class: reference

<a name="byte"></a>
```yaml
---
type: class
name: byte
suite: Applescript types
---
```

## Class: byte

<a name="point"></a>
```yaml
---
type: class
name: point
suite: Applescript types
---
```

## Class: point

<a name="location_reference"></a>
```yaml
---
type: class
name: location reference
suite: Applescript types
---
```

## Class: location reference

<a name="alias"></a>
```yaml
---
type: class
name: alias
suite: Applescript types
---
```

## Class: alias

<a name="file_specification"></a>
```yaml
---
type: class
name: file specification
suite: Applescript types
---
```

## Class: file specification

## Satimage Text Additions

**Description:** mailto:support@satimage-software.com

<a name="find_text"></a>
```yaml
---
type: command
name: find text
suite: Satimage Text Additions
---
```

## Command: find text

**Description:** find text literally or using regular expression syntax.

### Sample Code
### Direct Parameter
- **Description:** the substring to search for
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | a string or an alias | string | No |
| starting at | default: 0 | integer | Yes |
| for | length of text after starting | integer | Yes |
| case sensitive | default true | boolean | Yes |
| regexp | use regular expression, default false | boolean | Yes |
| backward | default false. Irrelevant with regexp | boolean | Yes |
| diacritic sensitive | default true. Irrelevant with regexp | boolean | Yes |
| whole word | default false. Irrelevant with regexp | boolean | Yes |
| regexpflag | a subset of {"IGNORECASE", "EXTEND", "MULTILINE", "SINGLELINE", "FIND LONGEST", "FIND NOT EMPTY", "DONT CAPTURE GROUP", "NOTBOL", "NOTEOL", "NEWLINE IN NEGATIVE CC"}; default {} | string | Yes |
| using | the pattern to generate the string (regexp only). Useful for constructs with backward references in regexp, ex.: using "name: \\1". This parameter may be an integer n (between 0 and 9). Equivalent to  "\\n" but matchPos and matchLen correspond to the position of the reference. using may be a list, in this case matchResult is a list of strings | string, integer, string | Yes |
| all occurrences | returns a list of all occurrences. Default: false | boolean | Yes |
| string result | return only the matching string instead of the whole record | boolean | Yes |
| syntax | the syntax for regular expressions. Relevant if regexp parameter is true. A string among ("POSIX" | "POSIX_EXTENDED" | "EMACS" | "GREP" | "GNU_REGEX" | "JAVA" | "PERL" | "RUBY"). Default: "RUBY" | string | Yes |
| options | list of  shortcuts:  'a' for "all occurrences", 'r' for "regexp", 's' for "string result", 'c' for "not case sensitive", 'd' for "not diacritic sensitive". For instance "ras" stands for for "with regexp, all occurrences and string result". | string | Yes |

### Result
- **Description:** according to "all occurrences" and "string result" parameters
- **Types:** matchrecord, matchrecord, string, string
<a name="change"></a>
```yaml
---
type: command
name: change
suite: Satimage Text Additions
---
```

## Command: change

**Description:** replace all occurrences of a substring

### Sample Code
### Direct Parameter
- **Description:** the substring(s) to search for
- **Types:** string, string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| into | the replacement string(s). If regexp is true, it may contain backward references | string, string | No |
| in |  | string, string, alias | No |
| starting at | default: 0 | integer | Yes |
| for | length of text after starting | integer | Yes |
| case sensitive | default true | boolean | Yes |
| regexp | default false | boolean | Yes |
| diacritic sensitive | default true. Irrelevant with regexp | boolean | Yes |
| whole word | default false. Irrelevant with regexp | boolean | Yes |
| regexpflag | see the documentation for find text | string | Yes |
| syntax | see the documentation for find text | string | Yes |
| verbatim | default: false (regexp only). If verbatim, the replacement string ("into" parameter) is not interpreted | boolean | Yes |
| only backreference | (regexp only). An integer in  (0,9) or a name corresponding to a named backreterence of the direct parameter. Default: 0, replace the matched substring  by the "into" parameter; otherwise replace only the provided backreference. | integer, string | Yes |
| options | list of  shortcuts (see  "find text") | string | Yes |

### Result
- **Description:** the new string if the "in" parameter is a string, otherwise the number of changes performed in the file
- **Types:** anything
<a name="re_compile"></a>
```yaml
---
type: command
name: re_compile
suite: Satimage Text Additions
---
```

## Command: re_compile

**Description:** check a regular expression

### Direct Parameter
- **Description:** the regular expression
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| syntax | the syntax for regular expressions. Relevant if regexp parameter is true. A string among ("POSIX" | "POSIX_EXTENDED" | "EMACS" | "GREP" | "GNU_REGEX" | "JAVA" | "PERL" | "RUBY"). Default: "RUBY" | string | Yes |

<a name="splittext"></a>
```yaml
---
type: command
name: splittext
suite: Satimage Text Additions
---
```

## Command: splittext

**Description:** split a text according to a given separator pattern. Optional matching parameters work like with the "find text" command

### Direct Parameter
- **Description:** the string to split
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | the separator | string | No |
| case sensitive | default true | boolean | Yes |
| regexp | consider the separator pattern as a        regular expression, default false | boolean | Yes |
| diacritic sensitive | default true. Irrelevant with regexp | boolean | Yes |
| whole word | consider only whole word separators. default false. Irrelevant with regexp | boolean | Yes |
| options | list of  shortcuts (see  "find text") | string | Yes |

### Result
- **Description:** the splitted text. If no separator found, the returned list contains one element: the original string.
- **Types:** string
<a name="filter_text"></a>
```yaml
---
type: command
name: filter text
suite: Satimage Text Additions
---
```

## Command: filter text

**Description:** parse a string (or a text file) into  a property list

### Sample Code
### Direct Parameter
- **Description:** the pattern
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | a string or an alias | string | No |
| key | the pattern to generate the keys in the plist | string | No |
| using | the pattern to generate the strings of the plist. Default: "\\0" | string | Yes |
| as | list or string. Default: string, the plist contains for each key a concatenation of the matches separated by a linefeed character (or the provided separator). Otherwise the plist contains for each key an array of matches. | type | Yes |
| duplicates | relevant if the "as" parameter is list. Without duplicates, only new strings are added. Default: true | boolean | Yes |
| separator | relevant if the "as" parameter is string. Default: linefeed | string | Yes |
| case sensitive | default: true | boolean | Yes |
| whole word |  | boolean | Yes |
| regexpflag | like in the find text command | string | Yes |
| syntax | like in the find text command | string | Yes |
| into | the file destination for the plist or an existing plist (see the XMLLib.osax dictionary). Default: filter text returns the property list as string | file, CFRef | Yes |

### Result
- **Description:** the XML data if the into parameter is missing
- **Types:** string
<a name="file_offset"></a>
```yaml
---
type: command
name: file offset
suite: Satimage Text Additions
---
```

## Command: file offset

**Description:** find a string in a file and return the offset in byte.

### Direct Parameter
- **Description:** the character(s) to find
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in |  | alias | No |
| starting at | the initial offset in byte | integer | Yes |
| encoding | a IANA charset name ("MACINTOSH", "UTF-8", "UTF-16", "ISO-8859-1", "windows-1252"…). Default: "UTF-8" | string | Yes |
| inclusive | default: false. If true, the offset includes the requested string | boolean | Yes |

### Result
- **Types:** integer
<a name="readtext"></a>
```yaml
---
type: command
name: readtext
suite: Satimage Text Additions
---
```

## Command: readtext

**Description:** read a text file. readtext is aware of the presence of BOM.

### Direct Parameter
- **Description:** or an url
- **Types:** alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for | the maximum number of bytes to read | integer | Yes |
| starting at | the initial offset in byte | integer | Yes |
| encoding | a IANA charset name ("MACINTOSH", "UTF-8", "UTF-16", "ISO-8859-1", "windows-1252"…) | string | Yes |
| redirect | redirects automatically (http). Default: true | boolean | Yes |
| timeout | default : 10 seconds | real | Yes |

### Result
- **Types:** string
<a name="writetext"></a>
```yaml
---
type: command
name: writetext
suite: Satimage Text Additions
---
```

## Command: writetext

**Description:** write a string in a file.

### Direct Parameter
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | or an url | file | No |
| append | default: false. If true, append the string at the end of the file | boolean | Yes |
| encoding | a IANA charset name ("MACINTOSH", "UTF-8", "UTF-16", "ISO-8859-1", "windows-1252"…). Default: "UTF-8" | string | Yes |
| missing char | characters that cannot be converted to the specified encoding are represented with this character. Default: writetext returns an error if it encounters an untranslatable character | string | Yes |

### Result
- **Types:** string
<a name="uppercase"></a>
```yaml
---
type: command
name: uppercase
suite: Satimage Text Additions
---
```

## Command: uppercase

**Description:** move to uppercase.

### Direct Parameter
- **Description:** the original string(s)
- **Types:** string, string
### Result
- **Description:** the uppercase string(s)
- **Types:** string, string
<a name="lowercase"></a>
```yaml
---
type: command
name: lowercase
suite: Satimage Text Additions
---
```

## Command: lowercase

**Description:** move to lowercase.

### Direct Parameter
- **Description:** the original string(s)
- **Types:** string, string
### Result
- **Description:** the lowercase string(s)
- **Types:** string, string
<a name="titlecase"></a>
```yaml
---
type: command
name: titlecase
suite: Satimage Text Additions
---
```

## Command: titlecase

### Direct Parameter
- **Description:** the original string(s)
- **Types:** string, string
### Result
- **Description:** the capitalized string(s)
- **Types:** string, string
<a name="format"></a>
```yaml
---
type: command
name: format
suite: Satimage Text Additions
---
```

## Command: format

**Description:** format a real number using a specification string. Ex: format pi into "##.##"->"3.14". '0' instead of '#' forces trailing zeros. '^' adds a space. "+f1;-f2;f3" provides formats for numbers >0, <0, =0. Encapsulate custom strings with "'".

### Direct Parameter
- **Description:** the number
- **Types:** real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| into | the formatting string, using #,^,O,.,%,',(,),+,- | string | No |
| underflow test | switch to scientific format if the number is too small with respect to the formatting string (default: false) | boolean | Yes |

### Result
- **Description:** the formatted number
- **Types:** string
<a name="atof"></a>
```yaml
---
type: command
name: atof
suite: Satimage Text Additions
---
```

## Command: atof

**Description:** convert a string into a number. Ex: atof "1.5"

### Direct Parameter
- **Types:** string, string
### Result
- **Types:** real, real
<a name="atoi"></a>
```yaml
---
type: command
name: atoi
suite: Satimage Text Additions
---
```

## Command: atoi

**Description:** convert a string into an integer. Ex: atoi "0xa0" -> 160

### Direct Parameter
- **Types:** string, string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base | the base value, between 2 and 36 | integer | Yes |

### Result
- **Types:** integer, integer
<a name="encode_entities"></a>
```yaml
---
type: command
name: encode entities
suite: Satimage Text Additions
---
```

## Command: encode entities

**Description:** substitutes the 5 reserved XML characters found in the direct parameter with the corresponding XML entities.

### Sample Code
### Direct Parameter
- **Types:** string
### Result
- **Types:** string
<a name="resolve_entities"></a>
```yaml
---
type: command
name: resolve entities
suite: Satimage Text Additions
---
```

## Command: resolve entities

**Description:** substitutes the XML character entities found in the direct parameter (not the html entities such as &eacute;) with the corresponding Unicode characters.

### Sample Code
### Direct Parameter
- **Types:** string
### Result
- **Types:** string
<a name="escapeurl"></a>
```yaml
---
type: command
name: escapeURL
suite: Satimage Text Additions
---
```

## Command: escapeURL

**Description:** encode a URI by replacing each instance of certain characters by one, two, or three escape sequences representing the UTF-8 encoding of the character

### Direct Parameter
- **Description:** a URI or a URI component
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| escaping | additional characters to escape. Default "". To translate URI component (for a GET request for instance) into legal URI component use ";,/?:@&=+$" | string | Yes |

### Result
- **Description:** a legal URI
- **Types:** string
<a name="unescapeurl"></a>
```yaml
---
type: command
name: unescapeURL
suite: Satimage Text Additions
---
```

## Command: unescapeURL

**Description:** decode a URI previously encoded with "escapeURL".

### Direct Parameter
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| keeping | characters to leave escaped. Default "". | string | Yes |

### Result
- **Types:** string
<a name="normalize_unicode"></a>
```yaml
---
type: command
name: normalize unicode
suite: Satimage Text Additions
---
```

## Command: normalize unicode

**Description:** normalize Unicode text (canonical composition or decomposition)

### Direct Parameter
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| decomposition | want canonical decomposition. default: false. For example, HFS Plus converts all file names to decomposed Unicode, while Macintosh keyboards generally produce precomposed Unicode. | boolean | Yes |

### Result
- **Types:** string
<a name="transform_unicode"></a>
```yaml
---
type: command
name: transform unicode
suite: Satimage Text Additions
---
```

## Command: transform unicode

**Description:** transform Unicode text 

### Sample Code
### Direct Parameter
- **Types:** string, string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | any valid ICU transform ID (see http://userguide.icu-project.org/transforms/general) | string | No |
| inverse | inverse transformation requested. Default: false | boolean | Yes |

### Result
- **Types:** string, string
<a name="hash"></a>
```yaml
---
type: command
name: hash
suite: Satimage Text Additions
---
```

## Command: hash

**Description:** normalize (KD) and hash a string

### Direct Parameter
- **Types:** string
### Result
- **Types:** integer
<a name="join"></a>
```yaml
---
type: command
name: join
suite: Satimage Text Additions
---
```

## Command: join

**Description:** coerce as Unicode text

### Direct Parameter
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | the text delimiter | string | No |

### Result
- **Types:** string
<a name="printf"></a>
```yaml
---
type: command
name: printf
suite: Satimage Text Additions
---
```

## Command: printf

**Description:** format a string like the C function printf.

### Sample Code
### Direct Parameter
- **Description:** the format string
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| parameters |  | anything | No |

### Result
- **Description:** the formatted string
- **Types:** string
<a name="strftime"></a>
```yaml
---
type: command
name: strftime
suite: Satimage Text Additions
---
```

## Command: strftime

**Description:** format a date using a specification string like in the C function strftime.

### Sample Code
### Direct Parameter
- **Types:** date, date
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| into | the formatting string. To obtain ISO 8601 dates, use "%FT%TZ" or "%GW%V-%uT%TZ" (using the 'with GMT' parameter) | string | No |
| GMT | if true, output date as GMT. Default: false, the ouput date is local. | boolean | Yes |

### Result
- **Description:** the formatted date
- **Types:** string
<a name="strptime"></a>
```yaml
---
type: command
name: strptime
suite: Satimage Text Additions
---
```

## Command: strptime

**Description:** Reverse of strftime.

### Sample Code
### Direct Parameter
- **Description:** the date string(s)
- **Types:** string, string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| encoding | the format of the date corresponding to the into parameter of strftime. | string | No |
| GMT | the intput date string is GMT (if unspecified by the format). Default: false | boolean | Yes |
| as | date or real (seconds since January 1 2001). Default: date | type | Yes |

### Result
- **Description:** the date
- **Types:** date, real
<a name="matchrecord"></a>
```yaml
---
type: record-type
name: matchrecord
suite: Satimage Text Additions
---
```

## Record Type: matchrecord

**Description:** the record returned by "find text"

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| matchPos | offset of the first character found | integer | read/write |
| matchLen | length of the match | integer | read/write |
| matchResult | the matched string (possibly formatted according to the "using" parameter)} | string, string | read/write |

## Satimage File Additions

**Description:** None

<a name="alias_description_for"></a>
```yaml
---
type: command
name: alias description for
suite: Satimage File Additions
---
```

## Command: alias description for

**Description:** resolve the alias file

### Direct Parameter
- **Types:** alias
### Result
- **Description:** the original item
- **Types:** string
<a name="navchoose_file"></a>
```yaml
---
type: command
name: navchoose file
suite: Satimage File Additions
---
```

## Command: navchoose file

**Description:** choose file with navigation services

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with prompt | a prompt to be displayed in the file chooser | string | Yes |
| of type | restrict the files shown to only these file types | string | Yes |
| starting at | the default file or folder | alias | Yes |
| multiple files | allow multiple files selection (default true) | boolean | Yes |
| show packages | (default true) | boolean | Yes |
| open packages | (default false) | boolean | Yes |
| of extension | list of allowed file extensions | string | Yes |
| invisibles | Show invisible files and folders? (default is false) | boolean | Yes |
| key | associate a key to the folder that the user will select. If no 'starting at' parameter is provided, assume the corresponding folder as the default folder. | integer | Yes |

### Result
- **Description:** the chosen files
- **Types:** alias
<a name="navchoose_folder"></a>
```yaml
---
type: command
name: navchoose folder
suite: Satimage File Additions
---
```

## Command: navchoose folder

**Description:** choose folder with navigation services

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with prompt | a prompt to be displayed in the folder chooser | string | Yes |
| starting at | the default folder | alias | Yes |
| multiple files | allow multiple folders selection (default true) | boolean | Yes |
| open packages | (default false) | boolean | Yes |
| key | associate a key to the folder that the user will select. If no 'starting at' parameter is provided, assume the corresponding folder as the default folder. | integer | Yes |

### Result
- **Description:** the chosen folders
- **Types:** alias
<a name="navchoose_object"></a>
```yaml
---
type: command
name: navchoose object
suite: Satimage File Additions
---
```

## Command: navchoose object

**Description:** choose file or folder with navigation services

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with prompt | a prompt to be displayed in the folder chooser | string | Yes |
| starting at | the default folder | alias | Yes |
| multiple files | allow multiple objects selection (default true) | boolean | Yes |
| show packages | (default true) | boolean | Yes |
| open packages | (default false) | boolean | Yes |
| key | associate a key to the folder that the user will select. If no 'starting at' parameter is provided, assume the corresponding folder as the default folder. | integer | Yes |

### Result
- **Description:** the chosen objects
- **Types:** alias
<a name="navchoose_volume"></a>
```yaml
---
type: command
name: navchoose volume
suite: Satimage File Additions
---
```

## Command: navchoose volume

**Description:** choose volume with navigation services

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with prompt | a prompt to be displayed in the folder chooser | string | Yes |
| starting at | the default folder | alias | Yes |

### Result
- **Description:** the chosen folders
- **Types:** alias
<a name="navask_save"></a>
```yaml
---
type: command
name: navask save
suite: Satimage File Additions
---
```

## Command: navask save

**Description:** prompt for save

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| file name | name of the file | string | Yes |
| action | 1 = before closing, 2 = before quitting, 0 = none | integer | Yes |

### Result
- **Description:** 1 save, 2 cancel, 3 don't save
- **Types:** integer
<a name="navchoose_file_name"></a>
```yaml
---
type: command
name: navchoose file name
suite: Satimage File Additions
---
```

## Command: navchoose file name

**Description:** Get a new file specification from the user, without creating the file. Uses navigation services

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with prompt | the text to display in the file creation dialog box | string | Yes |
| default name | the default name for the new file | string | Yes |
| with menu | list of menu items | string | Yes |
| menu index | index of the menu item to display | integer | Yes |
| starting at | the default folder | alias | Yes |
| show packages | (default true) | boolean | Yes |
| open packages | (default false) | boolean | Yes |
| key | associate a key to the folder that the user will select, and assume the corresponding folder as the default folder. | integer | Yes |

### Result
- **Description:** the file the user specified
- **Types:** file specification
<a name="navnew_folder"></a>
```yaml
---
type: command
name: navnew folder
suite: Satimage File Additions
---
```

## Command: navnew folder

**Description:** Get a new folder specification from the user. Uses navigation services

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with prompt | the text to display in the file creation dialog box | string | Yes |
| starting at | the default folder | alias | Yes |
| open packages | (default false) | boolean | Yes |
| key | associate a key to the folder that the user will select, and assume the corresponding folder as the default folder. | integer | Yes |

### Result
- **Description:** the folder the user specified
- **Types:** file specification
<a name="url_info_for"></a>
```yaml
---
type: command
name: URL info for
suite: Satimage File Additions
---
```

## Command: URL info for

**Description:** Parse an URL and returns an URL information record

### Direct Parameter
- **Description:** an URL or an alias
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| size | Return the size of the file or folder? (default is false) | boolean | Yes |

### Result
- **Types:** URL information
<a name="absoluteurl"></a>
```yaml
---
type: command
name: absoluteURL
suite: Satimage File Additions
---
```

## Command: absoluteURL

**Description:** resolve a relative URL using a base URL or coerce an alias, a posix path or a URL.

### Sample Code
### Direct Parameter
- **Description:** a relative URL or  an alias, a posix path (starting with / or ~) (Or a list of such.)
- **Types:** string, alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the base URL  | string, alias | Yes |
| as | Unicode text, alias, unix path, path... | type | Yes |

### Result
- **Types:** string, alias
<a name="relativeurl"></a>
```yaml
---
type: command
name: relativeURL
suite: Satimage File Additions
---
```

## Command: relativeURL

**Description:** translate an URL into the most suitable relative URL with respect to a given base.

### Direct Parameter
- **Description:** an absolute URL
- **Types:** string, alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the base URL | string, alias | No |

### Result
- **Description:** a relative or absolute URL
- **Types:** string
<a name="list_files"></a>
```yaml
---
type: command
name: list files
suite: Satimage File Additions
---
```

## Command: list files

**Description:** make a list of the files contained in the folder

### Sample Code
### Direct Parameter
- **Description:** a folder
- **Types:** alias, string, alias, string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| recursively | default: true. If false, list files and folders. | boolean | Yes |
| invisibles | default: false | boolean | Yes |
| of extension | the required file extension(s) | string | Yes |
| conforming to | the requested Universal Type Identifier(s) (UTI) | string | Yes |
| not conforming to | the forbidden Universal Type Identifier(s) (UTI) | string | Yes |
| starting with |  | string | Yes |
| ignoring packages | consider packages as folders. Default: false | boolean | Yes |
| after | list only files whose modification date is after the after date parameter | date | Yes |
| before | list only files whose modification date is before the before date parameter | date | Yes |
| names only | default: false | boolean | Yes |
| as | string (URL), alias, unix path, path... | type | Yes |

### Result
- **Types:** string, alias
<a name="glob"></a>
```yaml
---
type: command
name: glob
suite: Satimage File Additions
---
```

## Command: glob

**Description:** list  the files or the folders matching a unix pathname pattern

### Direct Parameter
- **Description:** the pattern
- **Types:** string, string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the working directory. By default, the direct parameter must be a full posix path pattern | alias | Yes |
| invisibles | default: false | boolean | Yes |
| of extension | the required file extension(s) | string | Yes |
| not conforming to | the forbidden Universal Type Identifier(s) (UTI) | string | Yes |
| after | list only items whose modification date is after the after date parameter | date | Yes |
| before | list only items whose modification date is before the before date parameter | date | Yes |
| names only | default: false | boolean | Yes |
| as | string (URL), alias, unix path, path... | type | Yes |

### Result
- **Types:** string, alias
<a name="backup"></a>
```yaml
---
type: command
name: backup
suite: Satimage File Additions
---
```

## Command: backup

**Description:** synchronizes 2 folders

### Direct Parameter
- **Description:** the source folder
- **Types:** file specification
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| onto | the destination folder | file specification | No |
| level | 0: report only, 1: synchronize folders, 2 : synchronize and report. Default 0.  | integer | Yes |
| after | files older than this date are not considered. | date | Yes |
| recursively | recursively synchronize subfolders. Default true. | boolean | Yes |
| except folders | names of folders to be omitted | string | Yes |
| except extensions | file extensions to be omitted | string | Yes |
| only extensions | consider only these file extensions | string | Yes |

### Result
- **Description:** the (optional) report
- **Types:** string
<a name="url_information"></a>
```yaml
---
type: class
name: URL information
suite: Satimage File Additions
---
```

## Class: URL information

**Description:** Reply record for the ‘URL info for’ command

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| scheme | the access scheme | Unicode text | read/write |
| host | the host specified by this URL | Unicode text | read/write |
| path | the (escaped) location of the target on the host | Unicode text | read/write |
| unix path | the (unescaped) location of the target on the host | Unicode text | read/write |
| name | the name of the item | Unicode text | read/write |
| user name | the user name by which to access this URL | Unicode text | read/write |
| password | the password by which to access this URL | Unicode text | read/write |
| name extension | the name extension of the URL | Unicode text | read/write |
| url parameters |  | Unicode text | read/write |
| url query |  | Unicode text | read/write |
| url fragment |  | Unicode text | read/write |
| type identifier | the item’s type identifier | Unicode text | read/write |

## Resource Suite

**Description:** Utilities to read and write resources from/to a file.

<a name="load_resource"></a>
```yaml
---
type: command
name: load resource
suite: Resource Suite
---
```

## Command: load resource

**Description:** get the resource of the given type and id from the specified file

### Direct Parameter
- **Description:** index of the desired resource
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| type | type of the desired resource | string | No |
| from | file to read from | alias | No |
| as | an AppleScript type for the returned result | type | Yes |

### Result
- **Description:** any AppleScript data that is stored  in the resource: data, object specification, reference, etc.
- **Types:** anything
<a name="list_resources"></a>
```yaml
---
type: command
name: list resources
suite: Resource Suite
---
```

## Command: list resources

**Description:** return the list of the ids of the resources of the specified type stored in the specified file

### Direct Parameter
- **Description:** type of desired resources
- **Types:** type
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | file to read from | file specification | No |

### Result
- **Description:** the list of ids
- **Types:** anything
<a name="get_resource_name"></a>
```yaml
---
type: command
name: get resource name
suite: Resource Suite
---
```

## Command: get resource name

**Description:** return the name of the resource of the specified type and id from the specified file

### Direct Parameter
- **Description:** index of the desired resource
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| type | type of the desired resource | type | No |
| from | file to read from | file specification | No |

### Result
- **Description:** the name of the resource
- **Types:** string
## Mathematical Functions

**Description:** Some mathematical functions. Most functions support as their direct parameter (and return) a list or an array of real. Notice: you may need more parentheses than is intuitive. Ex: cos(a) - b returns cos(a - b), so you may want to write (cos(a)) - b.

<a name="abs"></a>
```yaml
---
type: command
name: abs
suite: Mathematical Functions
---
```

## Command: abs

**Description:** absolute value of direct parameter 

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="acos"></a>
```yaml
---
type: command
name: acos
suite: Mathematical Functions
---
```

## Command: acos

**Description:** arc cosine of direct parameter 

### Direct Parameter
- **Description:** -1 <= x <= 1
- **Types:** real
### Result
- **Description:** in radians
- **Types:** real
<a name="acosh"></a>
```yaml
---
type: command
name: acosh
suite: Mathematical Functions
---
```

## Command: acosh

**Description:** hyperbolic arc cosine of direct parameter

### Direct Parameter
- **Description:** a positive number
- **Types:** real
### Result
- **Types:** real
<a name="asin"></a>
```yaml
---
type: command
name: asin
suite: Mathematical Functions
---
```

## Command: asin

**Description:** arc sine of direct parameter

### Direct Parameter
- **Description:** -1 <= x <= 1
- **Types:** real
### Result
- **Description:** in radians
- **Types:** real
<a name="asinh"></a>
```yaml
---
type: command
name: asinh
suite: Mathematical Functions
---
```

## Command: asinh

**Description:** hyperbolic arc sine of direct parameter

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="atan"></a>
```yaml
---
type: command
name: atan
suite: Mathematical Functions
---
```

## Command: atan

**Description:** arc tangent of direct parameter

### Direct Parameter
- **Types:** real
### Result
- **Description:** in radians
- **Types:** real
<a name="atan2"></a>
```yaml
---
type: command
name: atan2
suite: Mathematical Functions
---
```

## Command: atan2

**Description:** the angle of the line whose direction is the vector (x , y)

### Direct Parameter
- **Description:** 2 real numbers : y (ordinate) and x (abscissa)
- **Types:** list of real
### Result
- **Description:** in radians
- **Types:** real
<a name="atanh"></a>
```yaml
---
type: command
name: atanh
suite: Mathematical Functions
---
```

## Command: atanh

**Description:** hyperbolic arc tangent of direct parameter

### Direct Parameter
- **Description:** -1 < x < 1
- **Types:** real
### Result
- **Types:** real
<a name="ceil"></a>
```yaml
---
type: command
name: ceil
suite: Mathematical Functions
---
```

## Command: ceil

**Description:** round up

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="cosh"></a>
```yaml
---
type: command
name: cosh
suite: Mathematical Functions
---
```

## Command: cosh

**Description:** hyperbolic cosine of direct parameter

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="cos"></a>
```yaml
---
type: command
name: cos
suite: Mathematical Functions
---
```

## Command: cos

**Description:** cosine of direct parameter

### Direct Parameter
- **Description:** the angle (in radians). If the angle is in degrees, multiply it by pi / 180 before taking the cosine.
- **Types:** real
### Result
- **Types:** real
<a name="erf"></a>
```yaml
---
type: command
name: erf
suite: Mathematical Functions
---
```

## Command: erf

**Description:** the error function

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="erfc"></a>
```yaml
---
type: command
name: erfc
suite: Mathematical Functions
---
```

## Command: erfc

**Description:** the complementary error function

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="exp"></a>
```yaml
---
type: command
name: exp
suite: Mathematical Functions
---
```

## Command: exp

**Description:** exponential of direct parameter

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="floor"></a>
```yaml
---
type: command
name: floor
suite: Mathematical Functions
---
```

## Command: floor

**Description:** round down

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="gamma"></a>
```yaml
---
type: command
name: gamma
suite: Mathematical Functions
---
```

## Command: gamma

**Description:** the gamma function

### Direct Parameter
- **Description:** a positive number
- **Types:** real
### Result
- **Types:** real
<a name="hypot"></a>
```yaml
---
type: command
name: hypot
suite: Mathematical Functions
---
```

## Command: hypot

**Description:** the square root of the sum of the squares of its arguments

### Direct Parameter
- **Description:** 2 real numbers
- **Types:** list of real
### Result
- **Types:** real
<a name="lgamma"></a>
```yaml
---
type: command
name: lgamma
suite: Mathematical Functions
---
```

## Command: lgamma

**Description:** base-e logarithm of the absolute value of gamma

### Direct Parameter
- **Description:** a positive number
- **Types:** real
### Result
- **Types:** real
<a name="ln"></a>
```yaml
---
type: command
name: ln
suite: Mathematical Functions
---
```

## Command: ln

**Description:** base-e logarithm of direct parameter

### Direct Parameter
- **Description:** a positive real
- **Types:** real
### Result
- **Types:** real
<a name="log10"></a>
```yaml
---
type: command
name: log10
suite: Mathematical Functions
---
```

## Command: log10

**Description:** decimal logarithm of direct parameter

### Direct Parameter
- **Description:** a positive real
- **Types:** real
### Result
- **Types:** real
<a name="sin"></a>
```yaml
---
type: command
name: sin
suite: Mathematical Functions
---
```

## Command: sin

**Description:** sine of direct parameter

### Direct Parameter
- **Description:** the angle (in radians)
- **Types:** real
### Result
- **Types:** real
<a name="sinh"></a>
```yaml
---
type: command
name: sinh
suite: Mathematical Functions
---
```

## Command: sinh

**Description:** hyperbolic sine of direct parameter

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="sqr"></a>
```yaml
---
type: command
name: sqr
suite: Mathematical Functions
---
```

## Command: sqr

**Description:** square of direct parameter

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="sqrt"></a>
```yaml
---
type: command
name: sqrt
suite: Mathematical Functions
---
```

## Command: sqrt

**Description:** square root of direct parameter

### Direct Parameter
- **Description:** a positive number
- **Types:** real
### Result
- **Types:** real
<a name="tan"></a>
```yaml
---
type: command
name: tan
suite: Mathematical Functions
---
```

## Command: tan

**Description:** tangent of direct parameter

### Direct Parameter
- **Description:** the angle (in radians)
- **Types:** real
### Result
- **Types:** real
<a name="tanh"></a>
```yaml
---
type: command
name: tanh
suite: Mathematical Functions
---
```

## Command: tanh

**Description:** hyperbolic tangent of direct parameter

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
<a name="trunc"></a>
```yaml
---
type: command
name: trunc
suite: Mathematical Functions
---
```

## Command: trunc

**Description:** round toward zero

### Direct Parameter
- **Types:** real
### Result
- **Types:** real
## Arrays

**Description:** 

<a name="createarray"></a>
```yaml
---
type: command
name: createarray
suite: Arrays
---
```

## Command: createarray

**Description:** create an array of real 

### Sample Code
### Direct Parameter
- **Description:** the requested size of the array
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| range | {min,max} | list of real | Yes |

### Result
- **Types:** array of real
<a name="creatematrix"></a>
```yaml
---
type: command
name: creatematrix
suite: Arrays
---
```

## Command: creatematrix

**Description:** create an array of real of size ncols*nrows 

### Sample Code
### Direct Parameter
- **Description:** "1": array of 1.0, "x": array of x values, "y": array of y values, "d": diagonal square matrix
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| ncols | or a list of real with the "x" option, will make an array with identical rows | integer | No |
| nrows | or a list of real with the "y" option, will make an array with identical columns | integer | No |
| range | a range {min,max} for the "x" and "y" options | list of real | Yes |
| diagonal | the diagonal values for the "d" option. You can also provide a real, in which case the matrix dimensions are specified by ncols=nrows. Default: 1.0 (identity matrix). | array of real | Yes |
| as | array of real or matrix, default: array of real | type | Yes |

### Result
- **Description:** or matrix
- **Types:** array of real
<a name="randomarray"></a>
```yaml
---
type: command
name: randomarray
suite: Arrays
---
```

## Command: randomarray

**Description:** create a random array of real

### Sample Code
### Direct Parameter
- **Description:** the requested size of the array
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| range | {min,max} | list of real | Yes |
| seed |  | integer | Yes |

### Result
- **Types:** array of real
<a name="replacemissingvalue"></a>
```yaml
---
type: command
name: replacemissingvalue
suite: Arrays
---
```

## Command: replacemissingvalue

**Description:** replace missing values (or NaN's) in a list, or an array of real, or a list of such.

### Sample Code
### Direct Parameter
- **Description:** or a list of arrays
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with |  | real | No |

### Result
- **Description:** or a list of arrays
- **Types:** array of real
<a name="removemissingvalue"></a>
```yaml
---
type: command
name: removemissingvalue
suite: Arrays
---
```

## Command: removemissingvalue

**Description:** delete missing values (or NaN's)from a list or an array of real

### Direct Parameter
- **Types:** list, array of real
### Result
- **Types:** list
<a name="extractitem"></a>
```yaml
---
type: command
name: extractitem
suite: Arrays
---
```

## Command: extractitem

**Description:** (obsolete: use extractarray instead)

### Direct Parameter
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| thru |  | integer | Yes |
| step |  | integer | Yes |
| in |  | array of real | No |
| blocksize |  | integer | Yes |
| as |  | type | Yes |

### Result
- **Types:** array of real
<a name="extractarray"></a>
```yaml
---
type: command
name: extractarray
suite: Arrays
---
```

## Command: extractarray

**Description:** extract values from an array of real

### Sample Code
### Direct Parameter
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the first item to read or a list of indexes (in which case, the "for", "step" and "blocksize" parameters are not taken into account). 1-based. Default 1 | integer | Yes |
| for | the number of blocks to read. If <0 then read as many blocks as possible. Default 1. Pass -1 in order to extract all available values | integer | Yes |
| blocksize | size of the block to read at each step. blocksize must be smaller than step | integer | Yes |
| step | the interval between the beginnings of successive blocks to read. Must be larger than blocksize. Default: blocksize | integer | Yes |
| as | default is array of real, you can provide small real or real for 1 item | type | Yes |

### Result
- **Types:** array of real
<a name="changearray"></a>
```yaml
---
type: command
name: changearray
suite: Arrays
---
```

## Command: changearray

**Description:** change items in an array of real

### Sample Code
### Direct Parameter
- **Description:** the array to modify
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the index of the first item to change (1 based) or a list of indexes (in which case, the "step" and "blocksize" parameters are not taken into account). default: 1 | integer | Yes |
| into | the new values | array of real | No |
| blocksize | size of the blocks to copy at each step. The "into" parameter must have a size multiple of blocksize. Default: 1 | integer | Yes |
| step | the interval between the beginnings of successive blocks to write. Must be larger than blocksize. Default: blocksize | integer | Yes |

### Result
- **Types:** array of real
<a name="insertarray"></a>
```yaml
---
type: command
name: insertarray
suite: Arrays
---
```

## Command: insertarray

**Description:** insert items into an array of real

### Sample Code
### Direct Parameter
- **Description:** the values to insert
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| into | the array to modify | array of real | No |
| at | the index of the first item to insert (0: at the beginning) or a list of indexes of the same size as the direct parameter (in which case, the "for", "step" and "blocksize" parameters are not taken into account). default -1 (insert values at the end) | integer | Yes |
| for | number of blocks to insert. default 1 | integer | Yes |
| step | the number of values between each insertion. default 0 | integer | Yes |
| blocksize | size of the blocks to insert after each step. The direct parameter must have a size multiple of blocksize. Default: 1 if "for" is defined, else the size of the direct parameter. | integer | Yes |

### Result
- **Types:** array of real
<a name="resamplematrix"></a>
```yaml
---
type: command
name: resamplematrix
suite: Arrays
---
```

## Command: resamplematrix

**Description:** resample a matrix. The incoming matrix is divided into rectangular blocks. Each block may be replaced by its mean value or by another statistical value.

### Sample Code
### Direct Parameter
- **Description:** the matrix to resample
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| blocksize | {i,j}, defines the horizontal and vertical sizes of the blocks used for resampling. i and j may be integers (identical blocks) or lists of integers (irregular grid, the items of the lists define the successive sizes of the blocks). | list of integer | No |
| wanted | the following strings or a list of such: "mean", "minimum", "maximum", "stdev", "missing value", "sum", "median", "dispersion". Specify the statistical function computed on each block. Default: "mean". | string | Yes |

### Result
- **Description:** the resampled matrix, or a list of matrices if 'wanted' is a list. The dimensions of the resampled matrix correspond to the numbers of blocks defined with 'blocksize'.
- **Types:** matrix
<a name="reversearray"></a>
```yaml
---
type: command
name: reversearray
suite: Arrays
---
```

## Command: reversearray

**Description:** returns reverse of the direct parameter.

### Sample Code
### Direct Parameter
- **Description:** ... or an array of real
- **Types:** list of real
### Result
- **Types:** array of real
<a name="multlist"></a>
```yaml
---
type: command
name: multlist
suite: Arrays
---
```

## Command: multlist

**Description:** performs the product of the parameters. Each parameter may be a list, an array of real, a matrix or a number. multlist {x1,x2...} with {y1,y2...} returns {x1.y1, x2.y2, ...}; multlist x with {y1,y2...} returns {x.y1, x.y2, ...}

### Direct Parameter
- **Types:** list of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with |  | list of real | No |

### Result
- **Types:** list of real
<a name="divlist"></a>
```yaml
---
type: command
name: divlist
suite: Arrays
---
```

## Command: divlist

**Description:** same as multlist, but for quotient

### Direct Parameter
- **Types:** list of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with |  | list of real | No |

### Result
- **Types:** list of real
<a name="addlist"></a>
```yaml
---
type: command
name: addlist
suite: Arrays
---
```

## Command: addlist

**Description:** same as multlist, but for sums

### Direct Parameter
- **Types:** list of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with |  | list of real | No |

### Result
- **Types:** list of real
<a name="sublist"></a>
```yaml
---
type: command
name: sublist
suite: Arrays
---
```

## Command: sublist

**Description:** same as multlist, but for subtraction

### Direct Parameter
- **Types:** list of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with |  | list of real | No |

### Result
- **Types:** list of real
<a name="runningsum"></a>
```yaml
---
type: command
name: runningsum
suite: Arrays
---
```

## Command: runningsum

**Description:** returns the running sum of an array of real

### Sample Code
### Direct Parameter
- **Types:** array of real
### Result
- **Types:** array of real
<a name="statlist"></a>
```yaml
---
type: command
name: statlist
suite: Arrays
---
```

## Command: statlist

**Description:** returns as a record the min, max, min index, max index, mean, sum, standard deviation, variance.

### Sample Code
### Direct Parameter
- **Description:** ... or an array of real
- **Types:** list of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| kurtosis | if true, statlist compute also skewness, kurtosis and median calculations. | boolean | Yes |

### Result
- **Types:** statsrecord
<a name="histogram"></a>
```yaml
---
type: command
name: histogram
suite: Arrays
---
```

## Command: histogram

**Description:** given an array of real numbers, return a list of 2 arrays : {sampling values,frequencies}

### Sample Code
### Direct Parameter
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| samples | number of intervals. If the parameter is missing  histogram builds a raw histogram {sampling values,frequencies} | integer | Yes |
| minimum | lower bound of the intervals | real | Yes |
| maximum | upper bound of the intervals | real | Yes |

### Result
- **Description:** {sampling values,frequencies}
- **Types:** list of array of real
<a name="evalformula"></a>
```yaml
---
type: command
name: evalformula
suite: Arrays
---
```

## Command: evalformula

**Description:** apply C-like mathematical expressions to arrays of real. Ex: evalformula "a*x^2+y^2" with {"a",2.4,"x",anarray,"y",anotherarray} (or by using a record: evalformula "a*x^2+y^2" with {a:2.4,x:anarray,y:anotherarray})

### Sample Code
### Direct Parameter
- **Description:** the formula to compute
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | the definition of the variables occurring in the formula. If a list, an alternation of reference names (strings) and data (number, list of numbers or array of real). Prefer lists because you can't use reserved words with records. | list, record | No |
| as | matrix or array of real: the requested type if parameters are matrices. Default: array of real | type | No |

### Result
- **Description:** or real
- **Types:** array of real
<a name="maskarray"></a>
```yaml
---
type: command
name: maskarray
suite: Arrays
---
```

## Command: maskarray

**Description:** suppress items (or rows) out of an array of real (or a matrix) with respect to a mask of 0's and 1's.

### Sample Code
### Direct Parameter
- **Description:** the array(s) or matrix to be filtered. For a matrix, the rows are deleted.
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | the filter: an array of real, 0's mean that the corresponding items are to be deleted in the direct object(s). | array of real | No |

### Result
- **Description:** the resulting array(s) or matrix
- **Types:** array of real
<a name="listvariables"></a>
```yaml
---
type: command
name: listvariables
suite: Arrays
---
```

## Command: listvariables

### Direct Parameter
- **Description:** a formula
- **Types:** string
### Result
- **Description:** the list of all input variables of the direct formula
- **Types:** string
<a name="smootharray"></a>
```yaml
---
type: command
name: smootharray
suite: Arrays
---
```

## Command: smootharray

**Description:** smooth an array by applying a [1 2 1] filter. First and last value are left unchanged.

### Direct Parameter
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for | how many times the smooth is applied | integer | No |

### Result
- **Description:** the smoothed array. It has the same size as the direct parameter
- **Types:** array of real
<a name="filter"></a>
```yaml
---
type: command
name: filter
suite: Arrays
---
```

## Command: filter

### Direct Parameter
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | a list of 9 real numbers representing the 3x3 convolution matrix | array of real | No |
| reduced | the resulting matrix is smaller (the 2 extremal columns and rows are removed. Default true.) | boolean | Yes |

### Result
- **Types:** matrix
<a name="evalpolynomial"></a>
```yaml
---
type: command
name: evalpolynomial
suite: Arrays
---
```

## Command: evalpolynomial

### Sample Code
### Direct Parameter
- **Description:** the polynomial, given as the list of its coefficients, 0th degree (constant term) first. Or an array of real coerced with "as polynomial"
- **Types:** list of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | or array of real | real | No |

### Result
- **Types:** real
<a name="roots_of"></a>
```yaml
---
type: command
name: roots of
suite: Arrays
---
```

## Command: roots of

### Sample Code
### Direct Parameter
- **Description:** the polynomial, given as the list of its coefficients, 0th degree (constant term) first
- **Types:** list of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| complex | default : false. Also compute the complex roots | boolean | Yes |

### Result
- **Description:** roots of the polynomial. Complex roots are returned as a list of 2 real numbers
- **Types:** list of real
<a name="composepolynomial"></a>
```yaml
---
type: command
name: composepolynomial
suite: Arrays
---
```

## Command: composepolynomial

**Description:** you can provide arrays of real instead of polynomials

### Direct Parameter
- **Description:** or an array of real: the polynomial P(X), given as the list of its coefficients, 0th degree (constant term) first.
- **Types:** polynomial
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | Q(X) | polynomial | No |

### Result
- **Description:** P(Q(X))
- **Types:** polynomial
<a name="pade_approximant"></a>
```yaml
---
type: command
name: pade approximant
suite: Arrays
---
```

## Command: pade approximant

**Description:** given a polynomial P(X), compute the Padé approximant as the rational function NUM(X)/DEN(X). NUM and DEN are polynomials and the constant term of DEN is 1.

### Direct Parameter
- **Description:** or an array of real: the polynomial P(X), given as the list of its coefficients, 0th degree (constant term) first.
- **Types:** polynomial
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| numerator | the requested degree for NUM(X) | integer | No |
| denominator | the requested degree for DEN(X) | integer | No |

### Result
- **Description:** {NUM(X), DEN(X)}
- **Types:** polynomial
<a name="fitpolynomial"></a>
```yaml
---
type: command
name: fitpolynomial
suite: Arrays
---
```

## Command: fitpolynomial

**Description:** given two arrays of real {x,y} returns the best polynomial fit y=P(x)

### Sample Code
### Direct Parameter
- **Description:** a list of two arrays of real {x,y}
- **Types:** list of array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| degree | the degree of the resulting polynomial | integer | No |
| number formatting | the format string for the formula output. If you don't specify this parameter, no fit string will be provided in the result record. | string | Yes |
| constraints | a list of constraints. Each constraint is a list of  degree+2 real numbers (a0,a1..,b) ensuring an affine relation between the coefficient of the polynomial: a0*c0+..=b, where (c0,..) are the coefficients of the polynomial | list | Yes |

### Result
- **Types:** fitrecord
<a name="fitrational"></a>
```yaml
---
type: command
name: fitrational
suite: Arrays
---
```

## Command: fitrational

**Description:** given two arrays of real {x,y} returns the best rational fit y=NUM(x)/DEN(x). NUM and DEN are polynomials and the constant term of DEN is 1.

### Direct Parameter
- **Description:** a list of two arrays of real {x,y}
- **Types:** list of array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| numerator | the requested degree for NUM(X) | integer | No |
| denominator | the requested degree for DEN(X) | integer | No |
| number formatting | the format string for the formula output. If you don't specify this parameter, no fit string will be provided in the result record. | string | Yes |

### Result
- **Description:** where fit result if a list of 2 polynomials.
- **Types:** fitrecord
<a name="read_binary"></a>
```yaml
---
type: command
name: read binary
suite: Arrays
---
```

## Command: read binary

**Description:** read a file of real or small real

### Direct Parameter
- **Description:** the file
- **Types:** file specification
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | the format of the data file: real (8 bytes), small real (4 bytes), integer (4 bytes), small integer (2 bytes), or byte (1 byte) | type | No |
| skip | the number of leading bytes to skip | integer | Yes |
| step | the offset between two consecutive readings | integer | Yes |
| blocksize | the size of the blocks in the "as" unit. Default 1 | integer | Yes |
| length | the number of blocks to read | integer | Yes |
| big endian | is the file encoded as big endian or little endian? Default: system endianess (false on mac intel). | boolean | Yes |
| signed | Only for integer types. Are they signed or unsigned? Default: true. | boolean | Yes |

### Result
- **Types:** array of real
<a name="write_binary"></a>
```yaml
---
type: command
name: write binary
suite: Arrays
---
```

## Command: write binary

**Description:** write the data into a binary file (encoded as big endian)

### Direct Parameter
- **Description:** the file
- **Types:** file specification
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with data |  | array of real | No |
| starting at | offset in bytes, default: append data at the end of the file | integer | Yes |
| as | the format of the data to be saved: real (8 bytes), small real (4 bytes), integer (4 bytes), small integer (2 bytes), or byte (1 byte). Default: real. | type | Yes |
| big endian | is the file encoded as big endian or little endian? Default: system endianess (false on mac intel). | boolean | Yes |

<a name="find_peaks"></a>
```yaml
---
type: command
name: find peaks
suite: Arrays
---
```

## Command: find peaks

**Description:** Find the peaks (indexes of local min and max values) of an array of real. A minimum height of peaks can be provided.

### Direct Parameter
- **Description:** the input data
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| delta | the minimum height of a peak. Default:0.0 | real | No |
| lookformaxfirst | search a maximum first. Default true. | boolean | No |

### Result
- **Description:** {list of max's indices, list of min's indices}. Indices are 1-based. Use it with extractarray to get list of values.
- **Types:** integer
<a name="arrays_auto_filling"></a>
```yaml
---
type: command
name: arrays auto filling
suite: Arrays
---
```

## Command: arrays auto filling

**Description:** defines the behavior when two arrays of real should have the same length: O: fails if lengths are differents, 1: fills the shortest array with NaNs, -1: shrinks the largest array.

### Direct Parameter
- **Description:** the new setting
- **Types:** integer
### Result
- **Description:** the previous setting
- **Types:** integer
<a name="matrix"></a>
```yaml
---
type: record-type
name: matrix
suite: Arrays
---
```

## Record Type: matrix

**Description:** An AppleScript representation of a 2D array of real numbers as a record:

### Sample Code
### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| ncols | the number of columns | integer | read/write |
| nrows | the number of rows | integer | read/write |
| array of real | the data, as an array of real or as a standard AppleScript list of real numbers. Ordering: the first numbers are the data for the first row. | array of real | read/write |

<a name="fitrecord"></a>
```yaml
---
type: record-type
name: fitrecord
suite: Arrays
---
```

## Record Type: fitrecord

**Description:** result of "fitpolynomial"

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| fit error | the mean error | real | read/write |
| fit result | the list of the coefficients (constant term first) | anything | read/write |
| fit string | the polynomial formula as text | string | read/write |

<a name="statsrecord"></a>
```yaml
---
type: record-type
name: statsrecord
suite: Arrays
---
```

## Record Type: statsrecord

**Description:** result of "statlist"

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| maximum |  | real | read/write |
| minimum |  | real | read/write |
| sum |  | real | read/write |
| mean |  | real | read/write |
| variance |  | real | read/write |
| stdev |  | real | read/write |
| median |  | real | read/write |
| skewness |  | real | read/write |
| kurtosis |  | real | read/write |
| maximum index |  | integer | read/write |
| minimum index |  | integer | read/write |

<a name="array_of_real"></a>
```yaml
---
type: value-type
name: array of real
suite: Arrays
---
```

## Value Type: array of real

**Description:** a packed list of real. Can be coerced to an AppleScript list with "as list of real" or "as list of integer". Conversely, a list of real may be translated using "as array of real" for fast computation.

### Sample Code
<a name="list_of_real"></a>
```yaml
---
type: value-type
name: list of real
suite: Arrays
---
```

## Value Type: list of real

**Description:** an abstract type provided to coerce arrays of real into list of real

<a name="list_of_integer"></a>
```yaml
---
type: value-type
name: list of integer
suite: Arrays
---
```

## Value Type: list of integer

**Description:** an abstract type provided to coerce arrays of real into list of integer

<a name="polynomial"></a>
```yaml
---
type: value-type
name: polynomial
suite: Arrays
---
```

## Value Type: polynomial

**Description:** list of its coefficients, 0th degree first. Supports "as string" and "as list of real" coercions.

## Array and List Utilities

**Description:** 

<a name="sortlist"></a>
```yaml
---
type: command
name: sortlist
suite: Array and List Utilities
---
```

## Command: sortlist

**Description:** sort a list of numbers (or an array of real) or a list of strings or a list of dates. Missing values of the input list are always returned at the end of the resulting list. Can also sort a list of lists: lists are sorted either asynchronously or synchronously if the 'with respect to' parameter is specified. Sortlist is stable.

### Sample Code
### Direct Parameter
- **Description:** the list to sort (or a list of lists)
- **Types:** anything
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with respect to | index of the list used as the sort criterion. Relevant only if the direct parameter is a list of lists: requests a synchronous sort. If this parameter is not specified, each list is sorted separately. This parameter may be a list of integer corresponding to a list of criteria in decreasing priority order. Of course, the lists that does not correspond to a criterium are reordered and do not need to be homogeneous | integer | Yes |
| ascending | default true. May be a list if "with respect to" is already a list. | boolean | Yes |
| remove duplicates | if true, remove duplicate values. Default false | boolean | Yes |
| comparison | only relevant for list of string. 1 case insensitive, 2 compare numerically, 1+4 force ordering ('A'<'a'<'B'). Default 0 | integer | Yes |

### Result
- **Description:** the sorted list (or lists)
- **Types:** anything
<a name="masklist"></a>
```yaml
---
type: command
name: masklist
suite: Array and List Utilities
---
```

## Command: masklist

**Description:** suppress items out of a list (or replace items) with respect to a mask of 0's and 1's. See also 'suppress item'

### Sample Code
### Direct Parameter
- **Description:** the list to be filtered.
- **Types:** list of any
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | the filter: an array of real, or a list of integers, 0's mean that the corresponding items are to be deleted (or replaced if substitute is present) in the direct object(s). | array of real | No |
| substitute |  | any | Yes |

### Result
- **Description:** the resulting list
- **Types:** list of any
<a name="topological_sort"></a>
```yaml
---
type: command
name: topological sort
suite: Array and List Utilities
---
```

## Command: topological sort

**Description:** given a list of vertices and partial ordering providing provided by either the parameter edges or the parameter dependencies, topological sort returns a ordered list or an error if the ordering is not suitable

### Sample Code
### Direct Parameter
- **Description:** the vertices. Optional with the edges parameter
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| edges | {{v1,v2},{v3,v4},..}. Each ordered pair corresponds to an oriented edge (that is v1>v2). This parameter can also be provided as a list {v1,v2v3,v4,,..} | list | Yes |
| dependencies | if there are n vertices, dependencies is a list of n list of vertices. The ith list contains the vertices known as larger that the ith vertex | list | Yes |

### Result
- **Description:** a ordered list of vertices {v1,v2,...}
- **Types:** integer
<a name="suppress_item"></a>
```yaml
---
type: command
name: suppress item
suite: Array and List Utilities
---
```

## Command: suppress item

**Description:** delete a list of items from a list or a record. 

### Sample Code
### Direct Parameter
- **Description:** a list of indices or a list of keywords. Use quotes around custom properties, and also around 4-characters codes. (If you don't know what this means, you don't need it).
- **Types:** anything
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from |  | list, record | No |

### Result
- **Description:** according to the "from" parameter
- **Types:** list, record
<a name="exclude_items"></a>
```yaml
---
type: command
name: exclude items
suite: Array and List Utilities
---
```

## Command: exclude items

**Description:** remove strings from a list of strings. A list equivalent of the set difference.

### Sample Code
### Direct Parameter
- **Description:** the list of strings to remove from the input list
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the input list | string | No |
| with respect to | rank of the list (of string) used for the filter process. Other input lists may be lists of anything. Relevant only if the 'from' parameter is a list of lists. Default: 1 | integer | Yes |
| case sensitive | default true | boolean | Yes |

### Result
- **Description:** the cleaned input list, or a list of cleaned lists if the 'from' parameter is a list of lists.
- **Types:** list
<a name="keep_items"></a>
```yaml
---
type: command
name: keep items
suite: Array and List Utilities
---
```

## Command: keep items

**Description:** remove strings from a list of strings. A list equivalent of the set intersection.

### Sample Code
### Direct Parameter
- **Description:** the list of the strings to keep
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | (or list of list). The input list | string | No |
| with respect to | rank of the list (of string) used for the filter process. Other input lists may be lists of anything. Relevant only if the 'from' parameter is a list of lists. Default: 1 | integer | Yes |
| case sensitive | default true | boolean | Yes |

### Result
- **Description:** the cleaned input list, or a list of cleaned lists if the 'from' parameter is a list of lists.
- **Types:** list
<a name="special_concat"></a>
```yaml
---
type: command
name: special concat
suite: Array and List Utilities
---
```

## Command: special concat

**Description:** concatenate {a_ppty:X, …} and {a_ppty:Y, …} into {a_ppty:Z, …}, where Z is X & Y (resp. X + Y) if X,Y are lists (resp. numbers). Also merges tabulated string arrays side to side (in other terms, adds columns).

### Sample Code
### Direct Parameter
- **Description:** the record
- **Types:** record
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | the additional data | record | No |

### Result
- **Types:** record
## Satimage XML DOM

**Description:** An AppleScript implementation of the DOM. Uses the Libxml2 open source project.

<a name="xmlopen"></a>
```yaml
---
type: command
name: XMLOpen
suite: Satimage XML DOM
---
```

## Command: XMLOpen

**Description:** open an XML file and parse it. Must be balanced with a XMLClose at the end of the job. Alternatively, use to "from string" parameter to provide the xml data as a string

### Sample Code
### Direct Parameter
- **Description:** a file containing xml data or an url
- **Types:** alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from string | a string containing xml data | text | Yes |
| keep blanks | default false | boolean | Yes |
| load external DTD | default: according to the standalone declaration (http://www.w3.org/TR/2008/REC-xml-20081126/#sec-rmd) | boolean | Yes |
| substitute entities | default false | boolean | Yes |
| validate | validate with respect to its dtd; default false. Support XML Catalogs (http://www.oasis-open.org/committees/entity/spec-2001-08-06.html) at "/etc/xml/catalog" or "/Library/DTDs/catalog" | boolean | Yes |
| html4 | require the HTML4 lax parsing. Default: false | boolean | Yes |
| xmlscript | parse the script tags even if HTML4 is true. Produce faithful xml when scripts are escaped with CDATA sections. Default: false | boolean | Yes |
| noCDATA | if true, encountered CDATA sections are translated into text node. Default: false | boolean | Yes |
| verbose | default false | boolean | Yes |
| failure level | a number between 1 and 3. 3: fail only on fatal errors, 2: fail on xml recoverable errors, 1: fail on warnings. The default is provided by the XMLErrorLevel command. | integer | Yes |
| in pool | the name of the group where the new document is created. Default: the current pool. At launch the current pool is "". | string | Yes |
| POST | Default false.  The method of the http request. Relevant for http URLs with query. XMLOpen automatically adds the Content-Type header field and build the request body | boolean | Yes |
| query | the query is usually available thru the direct parameter after a question mark.  In some cases (with http POST method), this is not possible and the query may be supplied thru this parameter in conjunction with the POST parameter | string | Yes |
| header | the http extra headers of the request: a record or a propertylist containing a dict. Relevant for http URLs | string | Yes |
| bypassing namespace | default false. Bypass the default namespaces. | boolean | Yes |
| encoding | relevant only for invalid documents | string | Yes |

### Result
- **Description:** a reference to the XML parsed document, required by all the other XML commands
- **Types:** XMLRef
<a name="xmlclose"></a>
```yaml
---
type: command
name: XMLClose
suite: Satimage XML DOM
---
```

## Command: XMLClose

**Description:** release memory, associated XMLRefs are no longer valid.

### Direct Parameter
- **Types:** XMLRef
<a name="xmlroot"></a>
```yaml
---
type: command
name: XMLRoot
suite: Satimage XML DOM
---
```

## Command: XMLRoot

**Description:** get the root of the XML document.

### Direct Parameter
- **Description:** the document
- **Types:** XMLRef
### Result
- **Description:** the root element
- **Types:** XMLRef
<a name="xmlcount"></a>
```yaml
---
type: command
name: XMLCount
suite: Satimage XML DOM
---
```

## Command: XMLCount

**Description:** count children in the given XML object.

### Sample Code
### Direct Parameter
- **Description:** an XML object
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| all nodes | if false XMLCount omits non-element nodes. Default true. | boolean | Yes |

### Result
- **Description:** the number of children
- **Types:** integer
<a name="xmlcountelement"></a>
```yaml
---
type: command
name: XMLCountElement
suite: Satimage XML DOM
---
```

## Command: XMLCountElement

**Description:** count elements in the given XML object. Equivalent to XMLCount without all nodes

### Direct Parameter
- **Description:** an XML object
- **Types:** XMLRef
### Result
- **Description:** the number of children
- **Types:** integer
<a name="xmlchild"></a>
```yaml
---
type: command
name: XMLChild
suite: Satimage XML DOM
---
```

## Command: XMLChild

**Description:** provide access to children of a given XML object.

### Sample Code
### Direct Parameter
- **Description:** the parent
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| index | 1..XMLCount, index of the requested child | integer | No |
| all nodes | if false XMLChild omits non-element nodes. Default true. | boolean | Yes |

### Result
- **Description:** the child
- **Types:** XMLRef
<a name="xmlelement"></a>
```yaml
---
type: command
name: XMLElement
suite: Satimage XML DOM
---
```

## Command: XMLElement

**Description:** equivalent to XMLChild without all nodes.

### Direct Parameter
- **Description:** the parent
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| index | 1..XMLCountElement, index of the requested child | integer | No |

### Result
- **Description:** the child
- **Types:** XMLRef
<a name="xmlparent"></a>
```yaml
---
type: command
name: XMLParent
suite: Satimage XML DOM
---
```

## Command: XMLParent

**Description:** return the parent of an object.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Result
- **Description:** the parent(s)
- **Types:** XMLRef, XMLRef
<a name="xmlnextsibling"></a>
```yaml
---
type: command
name: XMLNextSibling
suite: Satimage XML DOM
---
```

## Command: XMLNextSibling

**Description:** return the next sibling of an object.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| all nodes | if false XMLNextSibling omits non-element nodes. Default true. | boolean | Yes |

### Result
- **Description:** the next sibling
- **Types:** XMLRef, XMLRef
<a name="xmlnextelement"></a>
```yaml
---
type: command
name: XMLNextElement
suite: Satimage XML DOM
---
```

## Command: XMLNextElement

**Description:** equivalent to XMLNextSibling without all nodes.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Result
- **Description:** the next sibling element
- **Types:** XMLRef, XMLRef
<a name="xmlprevsibling"></a>
```yaml
---
type: command
name: XMLPrevSibling
suite: Satimage XML DOM
---
```

## Command: XMLPrevSibling

**Description:** return the previous sibling of an object.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| all nodes | if false XMLPrevSibling omits non-element nodes. Default true. | boolean | Yes |

### Result
- **Description:** the previous sibling
- **Types:** XMLRef, XMLRef
<a name="xmlprevelement"></a>
```yaml
---
type: command
name: XMLPrevElement
suite: Satimage XML DOM
---
```

## Command: XMLPrevElement

**Description:** equivalent to XMLPrevSibling without all nodes.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Result
- **Description:** the previous sibling element
- **Types:** XMLRef, XMLRef
<a name="xmltagname"></a>
```yaml
---
type: command
name: XMLTagName
suite: Satimage XML DOM
---
```

## Command: XMLTagName

**Description:** return the name of the element.

### Sample Code
### Direct Parameter
- **Types:** XMLRef, XMLRef
### Result
- **Types:** string, string
<a name="xmlgetattribute"></a>
```yaml
---
type: command
name: XMLGetAttribute
suite: Satimage XML DOM
---
```

## Command: XMLGetAttribute

**Description:** return the contents of an attribute.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the name of the attribute | string | No |
| namespace | the namespace URL.  For instance, to retrieve an xml:lang attribute this parameter must be "http://www.w3.org/XML/1998/namespace" and the name parameter must be "lang" | string | Yes |

### Result
- **Types:** string, string
<a name="xmlsetattribute"></a>
```yaml
---
type: command
name: XMLSetAttribute
suite: Satimage XML DOM
---
```

## Command: XMLSetAttribute

**Description:** set (or create) an attribute.

### Sample Code
### Direct Parameter
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the name of the attribute | string, string | No |
| to | the contents of the attribute. | string, string | No |
| namespace | the namespace URL | string | Yes |
| suppressing | default: false. If true and the "to" parameter is a list containing missing values, then XMLSetAttribute removes the corresponding attributes. Otherwise these values are ignored | boolean | Yes |

<a name="xmlremoveattribute"></a>
```yaml
---
type: command
name: XMLRemoveAttribute
suite: Satimage XML DOM
---
```

## Command: XMLRemoveAttribute

**Description:** remove an attribute.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the name of the attribute | string, string | No |
| namespace | the namespace URL | string | Yes |

<a name="xmlremove"></a>
```yaml
---
type: command
name: XMLRemove
suite: Satimage XML DOM
---
```

## Command: XMLRemove

**Description:** delete an object. The reference to this object (or to any contained object) is no more valid.

### Direct Parameter
- **Description:** the object to delete
- **Types:** XMLRef, XMLRef
<a name="xmlremovechildren"></a>
```yaml
---
type: command
name: XMLRemoveChildren
suite: Satimage XML DOM
---
```

## Command: XMLRemoveChildren

**Description:** delete all children.

### Direct Parameter
- **Types:** XMLRef, XMLRef
<a name="xmlexists"></a>
```yaml
---
type: command
name: XMLExists
suite: Satimage XML DOM
---
```

## Command: XMLExists

**Description:** Test if an XMLRef is valid.

### Direct Parameter
- **Description:** the object(s) to test
- **Types:** XMLRef, XMLRef
### Result
- **Types:** boolean, boolean
<a name="xmlnewchild"></a>
```yaml
---
type: command
name: XMLNewChild
suite: Satimage XML DOM
---
```

## Command: XMLNewChild

**Description:** create a new child in a given object.

### Sample Code
### Direct Parameter
- **Description:** the XML string describing the new child or the XMLRef(s) to clone
- **Types:** string, XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| keep blanks | default false | boolean | Yes |
| at | the parent | XMLRef | No |
| nsclean | remove the redundant namespaces. Default: true. | boolean | Yes |

### Result
- **Description:** a reference to the newly created object(s)
- **Types:** XMLRef, XMLRef
<a name="xmlnewsibling"></a>
```yaml
---
type: command
name: XMLNewSibling
suite: Satimage XML DOM
---
```

## Command: XMLNewSibling

**Description:** create a new object beside a given object.

### Sample Code
### Direct Parameter
- **Description:** the XML string describing the new object or the XMLRef(s) to clone
- **Types:** string, XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| keep blanks | default false | boolean | Yes |
| after | insert new object after this one | XMLRef | Yes |
| before | insert new object before this one | XMLRef | Yes |

### Result
- **Description:** a reference to the newly created object(s)
- **Types:** XMLRef, XMLRef
<a name="xmlnodeinfo"></a>
```yaml
---
type: command
name: XMLNodeInfo
suite: Satimage XML DOM
---
```

## Command: XMLNodeInfo

**Description:** return node information.

### Sample Code
### Direct Parameter
- **Description:** the XML object to display. If the direct parameter is an alias (or a string), XMLNodeInfo attempts to retrieve the root node or the DOCTYPE node of the file (XMLNodeInfo does not check the whole file)
- **Types:** XMLRef, alias, string
### Result
- **Description:** a record containing the name, the kind and the dictionary (attributes) of the object
- **Types:** NodeInfo
<a name="xmldisplayxml"></a>
```yaml
---
type: command
name: XMLDisplayXML
suite: Satimage XML DOM
---
```

## Command: XMLDisplayXML

**Description:** return an XML object as a string.

### Direct Parameter
- **Description:** the XML object to display
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| formatting | add returns and tabs for legibility. Default: true. | boolean | Yes |
| xml declaration | require the xml declaration (relevant only if the direct parameter is a document). Default: true | boolean | Yes |
| nsclean | append the implicit namespaces. Default: true. | boolean | Yes |
| html4 | require compatible HTML4 output (relevant only if the direct parameter is a document). Default: false | boolean | Yes |
| encoding | change the xml declaration or the html charset. However, the result of XMLDisplayXML is always an AppleScript string (Unicode text) | string | Yes |

### Result
- **Types:** string, string
<a name="xmlsetxml"></a>
```yaml
---
type: command
name: XMLSetXML
suite: Satimage XML DOM
---
```

## Command: XMLSetXML

**Description:** set the contents of an element or text node.

### Sample Code
### Direct Parameter
- **Description:** an XML object.
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the text description for the new contents of the node (or for the new nodes if the direct parameter is a text node). | string | No |

<a name="xmlgettext"></a>
```yaml
---
type: command
name: XMLGetText
suite: Satimage XML DOM
---
```

## Command: XMLGetText

**Description:** return the textual contents of a node.

### Sample Code
### Direct Parameter
- **Description:** an XML object containing a simple text node.
- **Types:** XMLRef, XMLRef
### Result
- **Types:** string, string
<a name="xmlsettext"></a>
```yaml
---
type: command
name: XMLSetText
suite: Satimage XML DOM
---
```

## Command: XMLSetText

**Description:** set the textual contents of an element or text node.

### Sample Code
### Direct Parameter
- **Description:** if it is an element node, its content will be replaced by a unique text node
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | copied as is ; in particular the entities are not interpreted. | string, string | No |
| suppressing | default: false. If true and the "to" parameter is a list containing missing values, then XMLSetText removes (attribute or text) or empties (element) the corresponding nodes. Otherwise these values are ignored | boolean | Yes |

<a name="xmlappendtext"></a>
```yaml
---
type: command
name: XMLAppendText
suite: Satimage XML DOM
---
```

## Command: XMLAppendText

**Description:** append text to an element or text node.

### Sample Code
### Direct Parameter
- **Description:** the string to append
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | if necessary, a new text node wil be appended at the end of this node | XMLRef, XMLRef | No |

<a name="xmlgetnamespace"></a>
```yaml
---
type: command
name: XMLGetNameSpace
suite: Satimage XML DOM
---
```

## Command: XMLGetNameSpace

**Description:** return the namespace of a given element.

### Direct Parameter
- **Description:**  an XML element or attribute
- **Types:** XMLRef
### Result
- **Types:** namespace
<a name="xmlgetnamespaces"></a>
```yaml
---
type: command
name: XMLGetNameSpaces
suite: Satimage XML DOM
---
```

## Command: XMLGetNameSpaces

**Description:** search all the namespaces in the scope of a given node.

### Direct Parameter
- **Description:**  an XML node
- **Types:** XMLRef
### Result
- **Types:** namespace
<a name="xmlgetnamespacefromprefix"></a>
```yaml
---
type: command
name: XMLGetNameSpaceFromPrefix
suite: Satimage XML DOM
---
```

## Command: XMLGetNameSpaceFromPrefix

**Description:** return the URL associated to a given prefix in the scope of a given node.

### Direct Parameter
- **Description:**  an XML node
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| prefix |  | text | No |

### Result
- **Types:** text
<a name="xmladdnamespace"></a>
```yaml
---
type: command
name: XMLAddNamespace
suite: Satimage XML DOM
---
```

## Command: XMLAddNamespace

**Description:** add a namespace declaration in an XML element.

### Direct Parameter
- **Types:** namespace
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | an XML element | XMLRef | No |

<a name="xmlfind"></a>
```yaml
---
type: command
name: XMLFind
suite: Satimage XML DOM
---
```

## Command: XMLFind

**Description:** select a child (or children) satisfying a simple criterion: the name of the XML element and/or the key and value of an attribute. XMLFind is a poor man's XMLXPath suitable (and fast) for simple queries and is not aware of the namespace specifiers

### Direct Parameter
- **Description:** the parent where the search occurs
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the name of the element | string | Yes |
| key | the key of the attribute | string | Yes |
| value | the value of the attribute | string | Yes |
| all occurrences | returns a list of all occurrences. Default : false | boolean | Yes |

### Result
- **Description:** or a list of XMLRefs with all occurrences
- **Types:** XMLRef
<a name="xmlfindtext"></a>
```yaml
---
type: command
name: XMLFindText
suite: Satimage XML DOM
---
```

## Command: XMLFindText

**Description:** find a string in text nodes

### Direct Parameter
- **Description:** the string to find
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the tree node where the search begins | XMLRef, XMLRef | No |
| all occurrences | returns a list of all occurrences. Default: false | boolean | Yes |

### Result
- **Description:** the text node found or a list if "all occurrences" is true. Use XMLParent to retrieve the element node.
- **Types:** XMLRef
<a name="xmlregexp"></a>
```yaml
---
type: command
name: XMLRegexp
suite: Satimage XML DOM
---
```

## Command: XMLRegexp

**Description:** find text nodes conforming (or not conforming) to a given regular expression pattern

### Sample Code
### Direct Parameter
- **Description:** the pattern
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the tree node where the search begins | XMLRef, XMLRef | No |
| all occurrences | returns a list of all occurrences. Default: false | boolean | Yes |
| conforming | if false returns the text nodes not conforming to the pattern. Default: true | boolean | Yes |

### Result
- **Description:** the text node found or a list if "all occurrences" is true. Use XMLParent to retrieve the element node.
- **Types:** XMLRef
<a name="xmlbase"></a>
```yaml
---
type: command
name: XMLBase
suite: Satimage XML DOM
---
```

## Command: XMLBase

**Description:** get the base URL of a node.

### Direct Parameter
- **Description:** a node
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | string, alias... | type | Yes |

### Result
- **Description:** the effective base of the node, not the xml:base attribute.
- **Types:** string
<a name="xmlsetbase"></a>
```yaml
---
type: command
name: XMLSetBase
suite: Satimage XML DOM
---
```

## Command: XMLSetBase

**Description:** set the xml:base attribute of a node.

### Direct Parameter
- **Description:** a node
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | or alias. Passing "" remove the xml:base attribute of the node | string | No |

<a name="xmlabsoluteurl"></a>
```yaml
---
type: command
name: XMLAbsoluteURL
suite: Satimage XML DOM
---
```

## Command: XMLAbsoluteURL

**Description:** resolve a relative URL using a node base (or an absolute URL).

### Direct Parameter
- **Description:** a (possibly) relative URL
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the node providing the base URL (or an absolute URL) | XMLRef | No |
| as | string, alias... | type | Yes |

### Result
- **Description:** an absolute URL
- **Types:** string
<a name="xmlrelativeurl"></a>
```yaml
---
type: command
name: XMLRelativeURL
suite: Satimage XML DOM
---
```

## Command: XMLRelativeURL

**Description:** translate an URL into the most suitable relative URL with respect to a given base.

### Direct Parameter
- **Description:** an absolute URL
- **Types:** string, alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the node providing the base URL (or an absolute URL) | XMLRef | No |

### Result
- **Description:** a relative or absolute URL
- **Types:** string
<a name="xmlerror"></a>
```yaml
---
type: command
name: XMLError
suite: Satimage XML DOM
---
```

## Command: XMLError

**Description:** the full text of the last error occurred (debugging)

### Result
- **Types:** string
<a name="anything"></a>
```yaml
---
type: class
name: anything
suite: Satimage XML DOM
---
```

## Class: anything

**Description:** any class or reference

<a name="dictionary"></a>
```yaml
---
type: class
name: dictionary
suite: Satimage XML DOM
---
```

## Class: dictionary

<a name="alias"></a>
```yaml
---
type: class
name: alias
suite: Satimage XML DOM
---
```

## Class: alias

<a name="file_specification"></a>
```yaml
---
type: class
name: file specification
suite: Satimage XML DOM
---
```

## Class: file specification

<a name="namespace"></a>
```yaml
---
type: record-type
name: namespace
suite: Satimage XML DOM
---
```

## Record Type: namespace

**Description:** the AppleScript format of an XML namespace.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| nsprefix | the prefix of the namespace. | string | read/write |
| nsurl | the uri of the namespace. | string | read/write |

<a name="nodeinfo"></a>
```yaml
---
type: record-type
name: NodeInfo
suite: Satimage XML DOM
---
```

## Record Type: NodeInfo

**Description:** type returned by XMLNodeInfo.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| kind | XML class of the element : ELEMENT_NODE, TEXT_NODE, ATTRIBUTE_NODE, DOCUMENT_NODE... | string | read/write |
| name | tag of the element for element node. | string | read/write |
| attribute | a list of attribute name, attribute value. | string | read/write |
| namespace | optional. namespace of the element. | namespace | read/write |
| hasDTD | for document node only. | boolean | read/write |
| SystemID | the system ID of the DTD (document node only). | string | read/write |
| ExternalID | the external ID of the DTD (document node only). | string | read/write |
| standalone | (document node only). | boolean | read/write |
| paragraph | the line index of the node in the file | integer | read/write |

<a name="xmlref"></a>
```yaml
---
type: value-type
name: XMLRef
suite: Satimage XML DOM
---
```

## Value Type: XMLRef

**Description:** an opaque reference to an XML node. Initial XMLRefs must be created with XMLOpen.

## XML XPath, XSLT

**Description:** An AppleScript implementation of XPath, and XSLT.

<a name="xmlxpath"></a>
```yaml
---
type: command
name: XMLXPath
suite: XML XPath, XSLT
---
```

## Command: XMLXPath

**Description:** select an object (or objects) satisfying an xpath request. 

### Sample Code
### Direct Parameter
- **Description:** the starting point for the path
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | the xpath expression | string | No |
| namespace | {nsprefix:theName, nsurl:thehref} or a list of records. Or use XMLSetContext. | namespace, namespace | Yes |
| xpath variables | an even list {varname1,value1,…}. The XPath expression may refer to such a variable by $varname1. Alternatively, xpath variables may be a record {var1:value1,...} | list | Yes |

### Result
- **Description:** the selected objects
- **Types:** XMLRef
<a name="xmlsetcontext"></a>
```yaml
---
type: command
name: XMLSetContext
suite: XML XPath, XSLT
---
```

## Command: XMLSetContext

**Description:** set the default context for future xpath requests.

### Sample Code
### Direct Parameter
- **Description:**  an XML document
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| namespace | a list of {nsprefix:theName, nsurl:thehref}. If nsurl is "" the pair is removed. Further calls to XMLXPath may omit the "namespace" parameter | namespace | Yes |
| xpath variables | a list {varname1 ,value1,…}. Further XMLXPath expressions may refer to such a variable by $varname1. If value1 is "missing value" the variable "varname1" becomes undefined.  Alternatively, "xpath variables" may be a record {var1:value1,...} | string, record | Yes |

<a name="xmlgetcontext"></a>
```yaml
---
type: command
name: XMLGetContext
suite: XML XPath, XSLT
---
```

## Command: XMLGetContext

**Description:** get the xpath context.

### Direct Parameter
- **Description:**  an XML document
- **Types:** XMLRef
### Result
- **Types:** record
<a name="xmlgetnodepath"></a>
```yaml
---
type: command
name: XMLGetNodePath
suite: XML XPath, XSLT
---
```

## Command: XMLGetNodePath

**Description:** return a valid xpath for an object.

### Sample Code
### Direct Parameter
- **Description:** the node
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | starting point for the path | XMLRef | Yes |

### Result
- **Description:** the path
- **Types:** string
<a name="xmlxpointer"></a>
```yaml
---
type: command
name: XMLXPointer
suite: XML XPath, XSLT
---
```

## Command: XMLXPointer

**Description:** resolve a reference to a XML fragment. "XMLXPointer"  can open the targeted XML file only if the "read permission" parameter is not false.

### Sample Code
### Direct Parameter
- **Description:** the link: "[absoluteOrRelativeUrl]#anID" (the file must have been opened with "XMLOpen" using the validate option) or "[absoluteOrRelativeUrl]#xpointer(xpathExpression)"
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| baseURL | the base URL in order to resolve a relative URL. Alternatively may be provided by the "from" parameter  | string | Yes |
| from | for non-local links and relative URLs, define the base URL for the link. For local links (starting with #) and relative xpathExpression: the element where the search begins | XMLRef | Yes |
| in pool | the name of the group where the open document can be found. By default XMLXPointer use the pool of the "from" parameter or the current pool | string | Yes |
| namespace | {nsprefix:theName, nsurl:thehref} or a list of records to resolve the xpath expression | namespace, namespace | Yes |
| read permission | default true. Open a new document if necessary. If true (or missing) the following parameters may be useful. | boolean | Yes |
| keep blanks | default false | boolean | Yes |
| substitute entities | default false | boolean | Yes |
| validate | validate with respect to its dtd; default false | boolean | Yes |
| failure level | a number between 1 and 3. 3: fail only on fatal errors, 2: fail on xml recoverable errors, 1: fail on warnings. The default is provided by the XMLErrorLevel command. | integer | Yes |

### Result
- **Description:** the objects linked
- **Types:** XMLRef
<a name="xmlescapexpointer"></a>
```yaml
---
type: command
name: XMLEscapeXPointer
suite: XML XPath, XSLT
---
```

## Command: XMLEscapeXPointer

**Description:** return a valid string value for an xpath predicate.

### Direct Parameter
- **Description:** the string
- **Types:** string
### Result
- **Description:** the escaped string
- **Types:** string
<a name="xmlgetxpointer"></a>
```yaml
---
type: command
name: XMLGetXPointer
suite: XML XPath, XSLT
---
```

## Command: XMLGetXPointer

**Description:** return a valid xpointer for an object.

### Direct Parameter
- **Description:** the node
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| suffix | an xpath expression to append as the last path(s) of the xpointer | string | No |

### Result
- **Description:** the xpointer
- **Types:** string
<a name="xmltransform"></a>
```yaml
---
type: command
name: XMLTransform
suite: XML XPath, XSLT
---
```

## Command: XMLTransform

**Description:** transform an XML document (or a node) according to a given XSLT stylesheet.

### Sample Code
### Direct Parameter
- **Description:** the XML document to transform (or a node)
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | (or an XMLRef) the stylesheet. If this parameter is missing, XMLTransform will attempt to find in the direct parameter a processing instruction providing a stylesheet: <?xml-stylesheet type='…' href='... '?>. The type attribute must be 'text/xsl' or 'application/xml' or 'text/xml' | string | Yes |
| xsl params | a list {varname1 ,value1,…}. Set the values of the global xsl:param elements of the stylesheet or create new xsl global variables. The values are strings interpreted as xpath expressions. Thus a raw string parameter must be quoted like in {s:"'hello'"}. As there is no escaping in xsl, raw string parameters can more simply be provided with the "xsl string params" parameter. Alternatively, "xsl params" may be a record {var1 ,value1,…} | record, string | Yes |
| xsl string params | like xsl params, but the string values are automatically quoted | list | Yes |
| in | a file path for the result | file specification | Yes |
| as | XMLRef or string or CFRef. Default: XMLRef | type | Yes |
| in pool | the name of the group where the new document must be created. Default: the current pool. At launch the current pool is "". | string | Yes |

### Result
- **Description:**  or no result if the "in" parameter is present. A reference to the newly created document (resp. string) if the "as" parameter is XMLRef (resp. string) or a property list if the "as" parameter is CFRef (and the resulting data are actually valid XML data for a property list)
- **Types:** XMLRef, string, CFRef
<a name="xmlcompile"></a>
```yaml
---
type: command
name: XMLCompile
suite: XML XPath, XSLT
---
```

## Command: XMLCompile

**Description:** compile an XML document into a XSLT stylesheet for faster transformations. The resulting stylesheet is stored within the document and will be used in future XMLTransform calls

### Direct Parameter
- **Description:** the XML document
- **Types:** XMLRef
<a name="xmlnewindex"></a>
```yaml
---
type: command
name: XMLNewIndex
suite: XML XPath, XSLT
---
```

## Command: XMLNewIndex

**Description:** create an index for XMLLookup. XMLNewIndex returns an error if its evaluation results in an empty index

### Sample Code
### Direct Parameter
- **Description:** the name of the index
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| match | an XPath expression for the selected items | string | No |
| use | an XPath expression for the identifier of the items in the index | string | No |
| at | the document or the node to apply the match | XMLRef | No |
| namespace | {nsprefix:theName, nsurl:thehref} or a list of records. Or use XMLSetContext. | namespace, namespace | Yes |
| xpath variables | a list {varname1 ,value1,…}. The XPath expression may refer to such a variable by $varname1.  Alternatively, "xpath variables" may be a record {var1 :value1,…} | list | Yes |

<a name="xmllookup"></a>
```yaml
---
type: command
name: XMLLookup
suite: XML XPath, XSLT
---
```

## Command: XMLLookup

**Description:** retrieve a list of nodes associated to an index and a key

### Sample Code
### Direct Parameter
- **Description:** the entry to find in the index
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | the name of the index. XMLLookup returns an error if there is no index with the given name | string | No |
| at | the document (or a node of the document) holding the index | XMLRef | No |

### Result
- **Description:** an empty list if there is no entry in the index corresponding to the direct parameter
- **Types:** XMLRef
<a name="xmlentries"></a>
```yaml
---
type: command
name: XMLEntries
suite: XML XPath, XSLT
---
```

## Command: XMLEntries

**Description:** return the list of the keys in an index created with XMLNewIndex

### Direct Parameter
- **Description:** the name of the index
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the document containing the index | XMLRef | No |
| duplicate match | if true (resp. false) retrieves only the entries corresponding to multiple matches (resp. single match). Default: return all entries | boolean | Yes |

### Result
- **Types:** string
<a name="xmlindexdocument"></a>
```yaml
---
type: command
name: XMLIndexDocument
suite: XML XPath, XSLT
---
```

## Command: XMLIndexDocument

**Description:** index or re-index a document. May be useful to speed up XMLTransform or XMLXPath when some expressions involve node ordering.

### Direct Parameter
- **Description:** the XML document to index
- **Types:** XMLRef
<a name="xmlstrings"></a>
```yaml
---
type: command
name: XMLStrings
suite: XML XPath, XSLT
---
```

## Command: XMLStrings

### Direct Parameter
- **Description:** or a list
- **Types:** XMLRef, XMLRef, XMLRef
### Result
- **Types:** text
<a name="xmllocalize"></a>
```yaml
---
type: command
name: XMLLocalize
suite: XML XPath, XSLT
---
```

## Command: XMLLocalize

### Sample Code
### Direct Parameter
- **Description:** or a list
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | the .strings file | alias | No |

<a name="xpathref"></a>
```yaml
---
type: record-type
name: XPathRef
suite: XML XPath, XSLT
---
```

## Record Type: XPathRef

**Description:** A record defining a list of XMLRef by providing a node and an xpath string. Such a record may be used instead of a list of XMLRef.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| XMLRef | the starting node | XMLRef | read/write |
| xpath pattern | an xpath expression defining a node set. | string | read/write |
| namespace | (optional) definition of the prefixes used in the xpath expression. | namespace | read/write |
| xpath variables | (optional) an even list {varname1,value1,…}. varname1 is a string and value1 should be a string, a number, a boolean or a (list of ) CFRef . The XPath expression may refer to such a variable by $varname1. Alternatively, xpath variables may be a record {var1:value1,...} | any, record | read/write |

## XML Documents

**Description:** Commands to handle XML documents and global settings.

<a name="xmlurl"></a>
```yaml
---
type: command
name: XMLURL
suite: XML Documents
---
```

## Command: XMLURL

**Description:** get the path to the XML document.

### Direct Parameter
- **Description:** the document
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | string, alias... | type | Yes |
| parent | return the parent folder. Default: false | boolean | Yes |

### Result
- **Types:** file specification
<a name="xmlseturl"></a>
```yaml
---
type: command
name: XMLSetURL
suite: XML Documents
---
```

## Command: XMLSetURL

### Direct Parameter
- **Description:** a node
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to |  | alias | No |

<a name="xmldocument"></a>
```yaml
---
type: command
name: XMLDocument
suite: XML Documents
---
```

## Command: XMLDocument

**Description:** get the opened XML document from the file URL.

### Direct Parameter
- **Types:** file specification
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in pool | Default: the current pool. At launch the current pool is "". | string | Yes |

### Result
- **Description:** the document
- **Types:** XMLRef
<a name="xmlcatalog"></a>
```yaml
---
type: command
name: XMLCatalog
suite: XML Documents
---
```

## Command: XMLCatalog

**Description:** resolve a PUBLIC or SYSTEM ID or a URI with respect to the available catalogs

### Sample Code
### Direct Parameter
- **Types:** string
### Result
- **Description:** a URL
- **Types:** string
<a name="xmlclonedocument"></a>
```yaml
---
type: command
name: XMLCloneDocument
suite: XML Documents
---
```

## Command: XMLCloneDocument

**Description:** create a clone of the direct parameter (except for the url)

### Direct Parameter
- **Description:** a document
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in pool | Default: the current pool. | string | Yes |

### Result
- **Description:** the newly created document
- **Types:** XMLRef
<a name="xmlxinclude"></a>
```yaml
---
type: command
name: XMLXInclude
suite: XML Documents
---
```

## Command: XMLXInclude

**Description:** XInclude processing

### Sample Code
### Direct Parameter
- **Description:** a document
- **Types:** XMLRef
### Result
- **Description:** the number of includes processed
- **Types:** integer
<a name="xmlgetencoding"></a>
```yaml
---
type: command
name: XMLGetEncoding
suite: XML Documents
---
```

## Command: XMLGetEncoding

**Description:** return the encoding of the XML document.

### Direct Parameter
- **Description:** the document
- **Types:** XMLRef
### Result
- **Types:** string
<a name="xmlsetencoding"></a>
```yaml
---
type: command
name: XMLSetEncoding
suite: XML Documents
---
```

## Command: XMLSetEncoding

**Description:** set the encoding of the XML document. The encoding will be used by XMLSave.

### Sample Code
### Direct Parameter
- **Description:** the document
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | "UTF-8", "ASCII", "UTF-16", "ISO-8859-1"... "ISO-8859-9", "ISO-2022-JP", "SHIFT_JIS" or "EUC-JP". | string | No |

<a name="xmlsetindentstring"></a>
```yaml
---
type: command
name: XMLSetIndentString
suite: XML Documents
---
```

## Command: XMLSetIndentString

**Description:** set the default indent string. The indent string is used by XMLSave and XMLDisplayXML.

### Direct Parameter
- **Description:** a string containing spaces or tabs
- **Types:** string
### Result
- **Description:** the previous indent string
- **Types:** string
<a name="xmlsave"></a>
```yaml
---
type: command
name: XMLSave
suite: XML Documents
---
```

## Command: XMLSave

**Description:** save an XML document.

### Sample Code
### Direct Parameter
- **Description:** the XML object to save
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the file path | file specification | Yes |
| formatting | add returns and tabs for legibility. Default: true. | boolean | Yes |
| html4 | require compatible HTML4 output. Default: false | boolean | Yes |
| xml declaration | require the xml declaration. Default: true | boolean | Yes |
| encoding |  | string | Yes |

<a name="xmlerrorlevel"></a>
```yaml
---
type: command
name: XMLErrorLevel
suite: XML Documents
---
```

## Command: XMLErrorLevel

### Direct Parameter
- **Description:** the requested error level. 1 fails on warnings. 2 fails on XML recoverable errors. 3 fails on fatal errors. Set to 2 at the beginning
- **Types:** integer
### Result
- **Description:** the previous setting
- **Types:** integer
<a name="xmlextendedchar"></a>
```yaml
---
type: command
name: XMLExtendedChar
suite: XML Documents
---
```

## Command: XMLExtendedChar

**Description:** toggle between the 1.0 and the 1.1 XML recommendation for character definition.

### Direct Parameter
- **Description:** if true the extended character set (including all positive characters smaller than 32) of the 1.1 XML recommendation is in use.
- **Types:** boolean
### Result
- **Description:** the previous setting
- **Types:** boolean
<a name="xmllistdocuments"></a>
```yaml
---
type: command
name: XMLListDocuments
suite: XML Documents
---
```

## Command: XMLListDocuments

### Direct Parameter
- **Description:** the pool. Default: the current pool.
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | XMLListDocuments as string returns the url of the xmldocuments instead of their references | anything | Yes |

### Result
- **Description:** the opened xmldocuments
- **Types:** XMLRef
<a name="xmlsetdocid"></a>
```yaml
---
type: command
name: XMLSetDocID
suite: XML Documents
---
```

## Command: XMLSetDocID

**Description:** set an identifier to an existing document. Avoid many problems with the AppleScript's global variables

### Direct Parameter
- **Description:** the XML document
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to |  | string | No |

### Result
- **Description:** the previous ID
- **Types:** string
<a name="xmlgetdocbyid"></a>
```yaml
---
type: command
name: XMLGetDocByID
suite: XML Documents
---
```

## Command: XMLGetDocByID

**Description:** retrieve a document by identifier

### Direct Parameter
- **Description:** the identifier
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in pool | Default: the current pool. | string | Yes |

### Result
- **Types:** XMLRef
<a name="xmlc14n"></a>
```yaml
---
type: command
name: XMLc14n
suite: XML Documents
---
```

## Command: XMLc14n

**Description:** Canonicalization of an XML document

### Sample Code
### Direct Parameter
- **Description:** the XML document or a list of XMLRef or an XPathRef
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the destination file | alias | Yes |
| comments | include comments. Default true | boolean | Yes |
| nodelist | the set of nodes to output. Default all nodes. | XMLRef | Yes |
| exclusive | exclusive canonicalization. Default false | boolean | Yes |
| inclusive prefixes | list of inclusive prefixes (relevant if exclusive is true). | string | Yes |
| digest | "SHA1" or "MD5". If this parameter is provided, returns a digest using the specified algorithm. The result is base64-encoded if the "in" parameter is not provided. | string | Yes |

### Result
- **Description:** if the "in" parameter is not provided.
- **Types:** string
<a name="xmlsetextras"></a>
```yaml
---
type: command
name: XMLSetExtras
suite: XML Documents
---
```

## Command: XMLSetExtras

**Description:** associate any AppleScript contents with a document. This utility command is at the scripter's convenience and has no effect on the XML part of the document

### Direct Parameter
- **Description:** the XML document
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to |  | anything | No |

<a name="xmlgetextras"></a>
```yaml
---
type: command
name: XMLGetExtras
suite: XML Documents
---
```

## Command: XMLGetExtras

**Description:** retrieve the extras of a document

### Direct Parameter
- **Description:** the XML document
- **Types:** XMLRef
### Result
- **Types:** anything
## XML Validation

**Description:** Validation of documents and DTDs

<a name="xmlvalidate"></a>
```yaml
---
type: command
name: XMLValidate
suite: XML Validation
---
```

## Command: XMLValidate

**Description:** validate a document with respect to its DTD or a given dtd.

### Sample Code
### Direct Parameter
- **Description:** the document or the element to validate
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| against | a dtd | alias | Yes |
| verbose | default false | boolean | Yes |
| failure level | a number between 1 and 2. 2: fail on recoverable xml errors, 1: fail on warnings. Default: 2 | integer | Yes |

<a name="xmlschema"></a>
```yaml
---
type: command
name: XMLSchema
suite: XML Validation
---
```

## Command: XMLSchema

**Description:** validate a schema or a document with respect to a schema

### Direct Parameter
- **Description:** the document. If this parameter is missing, XMLSchema attempts to validate the schema provided in the "with respect to" parameter
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with respect to | the url of the schema. May be also provided as text or XMLRef. If this parameter is missing, XMLSchema uses the attributes "noNamespaceSchemaLocation" or "SchemaLocation" in the namespace "http://www.w3.org/2001/XMLSchema-instance" | alias | Yes |

<a name="xmlrelaxng"></a>
```yaml
---
type: command
name: XMLRelaxNG
suite: XML Validation
---
```

## Command: XMLRelaxNG

**Description:** validate a relaxNG schema or a document with respect to a relaxNG schema

### Direct Parameter
- **Description:** the document. If this parameter is missing, XMLRelaxNG attempts to validate the relaxNG schema provided in the "with respect to" parameter
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with respect to | the url of the relaxNG schema. May be also provided as text or XMLRef. | alias | No |

<a name="xmlcheckdtd"></a>
```yaml
---
type: command
name: XMLCheckDTD
suite: XML Validation
---
```

## Command: XMLCheckDTD

**Description:** check the syntax of a given DTD.

### Direct Parameter
- **Description:** the DTD's URL or alias, or the text of the DTD
- **Types:** anything
<a name="xmlgetbyid"></a>
```yaml
---
type: command
name: XMLGetByID
suite: XML Validation
---
```

## Command: XMLGetByID

**Description:** retrieve an element by ID. i.e. this element has an attribute xml:id or an attribute declared as an ID is the DTD of the document. In this later case, the document must have been opened with validate. XMLGetByID x xmlid "aa" is a shortcut for XMLPath x with "id('aa')".

### Direct Parameter
- **Description:** a valid XMLRef
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| xmlid | id of the element(s) | XMLRef, XMLRef | No |

### Result
- **Description:** according to the xmlid parameter
- **Types:** XMLRef, XMLRef
<a name="xmlgetxmlid"></a>
```yaml
---
type: command
name: XMLGetxmlID
suite: XML Validation
---
```

## Command: XMLGetxmlID

**Description:** return a string corresponding to an xml:id attribute or to the ID attribute according to the dtd; otherwise XMLGetxmlID returns an error 

### Direct Parameter
- **Description:** a valid XMLRef (corresponding to an element)
- **Types:** XMLRef
### Result
- **Description:** the ID
- **Types:** string
<a name="xmlvalidname"></a>
```yaml
---
type: command
name: XMLValidName
suite: XML Validation
---
```

## Command: XMLValidName

**Description:** check the validity of an XML Name (http://www.w3.org/TR/REC-xml/#NT-Name)

### Direct Parameter
- **Description:** the name(s)
- **Types:** string, string
### Result
- **Types:** boolean
<a name="xmlvalidncname"></a>
```yaml
---
type: command
name: XMLValidNCName
suite: XML Validation
---
```

## Command: XMLValidNCName

**Description:** check the validity of an XML NCName (http://www.w3.org/TR/2009/REC-xml-names-20091208/#NT-NCName)

### Direct Parameter
- **Description:** the name(s)
- **Types:** string, string
### Result
- **Types:** boolean
<a name="xmldu"></a>
```yaml
---
type: command
name: XMLDu
suite: XML Validation
---
```

## Command: XMLDu

**Description:** sum up the structure of a node

### Direct Parameter
- **Types:** XMLRef
### Result
- **Description:** a textual representation of the tree
- **Types:** string
<a name="xmlgetid"></a>
```yaml
---
type: command
name: XMLGetID
suite: XML Validation
---
```

## Command: XMLGetID

### Direct Parameter
- **Description:** a reference to an element of the XML document
- **Types:** CFRef
### Result
- **Description:** the ID of the XML document
- **Types:** integer
<a name="xmlfromid"></a>
```yaml
---
type: command
name: XMLFromID
suite: XML Validation
---
```

## Command: XMLFromID

### Direct Parameter
- **Description:** the ID of the XML document
- **Types:** integer
### Result
- **Description:** a reference to an element of the XML document
- **Types:** CFRef
## Satimage PropertyList Additions

**Description:** An AppleScript interface to property lists.

### Sample Code
<a name="plistnew"></a>
```yaml
---
type: command
name: PlistNew
suite: Satimage PropertyList Additions
---
```

## Command: PlistNew

**Description:** create a new PropertyList with the contents of the direct parameter. Must be balanced with a PlistClose at the end of the job.

### Direct Parameter
- **Description:** any AppleScript type, usually, a record or a list. Default: an empty record.
- **Types:** anything
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| typed | if false, write as raw base64 data. Default: true. Use false when storing complex types (such as alias) to allow other software to use the p-list (for instance, when changing a Preference p-list). If false, specify the type with 'as' when using PlistGet. | boolean | Yes |
| in pool | the name of the group where the plist document is created. Default: the current pool. At launch the current pool is "". | string | Yes |

### Result
- **Description:** a reference to the property list, required by the other PropertyList commands
- **Types:** CFRef
<a name="plistopen"></a>
```yaml
---
type: command
name: PlistOpen
suite: Satimage PropertyList Additions
---
```

## Command: PlistOpen

**Description:** open a property list file and parse it. Must be balanced with a PlistClose at the end of the job.

### Direct Parameter
- **Types:** alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from string | a string containing xml data | text | Yes |
| in pool | the name of the group where the plist document is created. Default: the current pool. At launch the current pool is "". | string | Yes |

### Result
- **Description:** a reference to the parsed property list, required by the other PropertyList commands
- **Types:** CFRef
<a name="plistclose"></a>
```yaml
---
type: command
name: PlistClose
suite: Satimage PropertyList Additions
---
```

## Command: PlistClose

**Description:** release memory, associated CFRefs are no more valid.

### Direct Parameter
- **Types:** CFRef
<a name="plistretain"></a>
```yaml
---
type: command
name: PlistRetain
suite: Satimage PropertyList Additions
---
```

## Command: PlistRetain

### Direct Parameter
- **Types:** CFRef
<a name="plistsave"></a>
```yaml
---
type: command
name: PlistSave
suite: Satimage PropertyList Additions
---
```

## Command: PlistSave

**Description:** save a Plist.

### Direct Parameter
- **Description:** the Plist to save
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the file path | file specification | Yes |
| binary | default: false | boolean | Yes |

<a name="plistbinaryformat"></a>
```yaml
---
type: command
name: PlistBinaryFormat
suite: Satimage PropertyList Additions
---
```

## Command: PlistBinaryFormat

**Description:** is the plist in a binary file format?

### Direct Parameter
- **Description:** the Plist
- **Types:** CFRef
### Result
- **Types:** boolean
<a name="plistcount"></a>
```yaml
---
type: command
name: PlistCount
suite: Satimage PropertyList Additions
---
```

## Command: PlistCount

**Description:** count children in the given CFRef.

### Direct Parameter
- **Description:** an CFRef
- **Types:** CFRef, CFRef
### Result
- **Description:** the number of children
- **Types:** integer, integer
<a name="plistchild"></a>
```yaml
---
type: command
name: PlistChild
suite: Satimage PropertyList Additions
---
```

## Command: PlistChild

**Description:** provide access to children of a given CFRef. Similar to PlistGet, but return a CFRef. Provide either a  "index", or a "key", or a "using" parameter. Only the direct parameter or "key", or "index" may be a list. If there is no specifier, PlistChild returns all the children.

### Direct Parameter
- **Description:** the parent: an array or a dictionary
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| index | 1..PlistCount, index of the requested child | integer | Yes |
| key | relevant only if the direct parameter is a dictionary | string | Yes |
| using | a selecting path. A valid path contains sequences of keys (for dictionaries) separated with slashes, and indices (for arrays) inside brackets. Example: "key1/key2[4]/key3[2]" | string | Yes |

### Result
- **Description:** the child or a list if one parameter is a list
- **Types:** CFRef
<a name="plisttype"></a>
```yaml
---
type: command
name: PlistType
suite: Satimage PropertyList Additions
---
```

## Command: PlistType

**Description:** return the type of a CFRef (the tag's name).

### Direct Parameter
- **Description:** the CFobject to display
- **Types:** CFRef
### Result
- **Types:** string
<a name="plistget"></a>
```yaml
---
type: command
name: PlistGet
suite: Satimage PropertyList Additions
---
```

## Command: PlistGet

**Description:** Similar to PlistChild, but return actual contents. Can be used with direct parameter alone to retrieve the contents of a CFRef. Only one of the parameters "key", "index" or "using" can be specified. Only the direct parameter or "key", or "index" may be a list.

### Direct Parameter
- **Description:** the CFRef to display
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | for base64 data stored 'without typed', the AppleScript type. | string | Yes |
| index | 1..PlistCount, index of the requested child | integer | Yes |
| key |  | string | Yes |
| using | a path. See the PlistChild command. | string | Yes |

### Result
- **Description:** or a list if one parameter is a list
- **Types:** anything
<a name="plistgetxml"></a>
```yaml
---
type: command
name: PlistGetXML
suite: Satimage PropertyList Additions
---
```

## Command: PlistGetXML

**Description:** return the contents of a CFRef as xml data.

### Direct Parameter
- **Description:** the CFRef to display
- **Types:** CFRef
### Result
- **Types:** string
<a name="plistgetkeys"></a>
```yaml
---
type: command
name: PlistGetKeys
suite: Satimage PropertyList Additions
---
```

## Command: PlistGetKeys

**Description:** return the list of keys in a dictionary.

### Direct Parameter
- **Description:** the dictionary
- **Types:** CFRef
### Result
- **Types:** string
<a name="plistset"></a>
```yaml
---
type: command
name: PlistSet
suite: Satimage PropertyList Additions
---
```

## Command: PlistSet

**Description:** equivalent to PlistNewChild on dictionaries. Use PlistSet to modify an existing element in an array.

### Sample Code
### Direct Parameter
- **Description:** the parent: an array or a dictionary
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| index | 1..PlistCount, index of the requested child | integer, integer | Yes |
| key |  | string, string | Yes |
| using | a path. See the PlistChild command. | string | Yes |
| to | any AppleScript content or a CFRef. Be aware of self-references when you use CFRef | anything | No |
| suppressing | default: true. If true and the "to" parameter is a list containing missing values, then XMLSetAttribute removes the corresponding attributes. Otherwise these values are ignored | boolean | Yes |
| typed | irrelevant with CFRefs. Default: true. If false, write as raw base64 data. Use false to store complex types (eg alias) for use by other software (eg, when editing a Preference file). If false, specify the type with 'as' when using PlistGet. | boolean | Yes |

<a name="plistnewchild"></a>
```yaml
---
type: command
name: PlistNewChild
suite: Satimage PropertyList Additions
---
```

## Command: PlistNewChild

**Description:** create a new child in a given object (array or dictionary). You must use PlistSet to modify an existing element of an array.

### Direct Parameter
- **Description:** any AppleScript content or a CFRef. Be aware of self-references when you use CFRef. Default: an empty record.
- **Types:** anything
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the container: an array or a dictionary | CFRef | No |
| index | 1..(PlistCount+1), index of the new child | integer | Yes |
| key | requested if CFRef is a dictionary | string | Yes |
| using | a path. See the PlistChild command. | string | Yes |
| typed | see the PlistSet command. | boolean | Yes |

### Result
- **Description:** the child
- **Types:** CFRef
<a name="plistremovechild"></a>
```yaml
---
type: command
name: PlistRemoveChild
suite: Satimage PropertyList Additions
---
```

## Command: PlistRemoveChild

**Description:** delete an object. The reference to this object (or to any object it may contain) is no longer valid. Future use of this reference may crash XMLLib.

### Direct Parameter
- **Description:** the container: an array or a dictionary
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| index | 1..PlistCount, index of the requested child | integer | Yes |
| key | the key of the requested child | string, string | Yes |
| using | a path. See the PlistChild command. | string | Yes |

<a name="plistequal"></a>
```yaml
---
type: command
name: PlistEqual
suite: Satimage PropertyList Additions
---
```

## Command: PlistEqual

**Description:** compare the contents of two plist. Return true if equal.

### Direct Parameter
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to |  | CFRef | No |

### Result
- **Types:** boolean
<a name="plistexist"></a>
```yaml
---
type: command
name: PlistExist
suite: Satimage PropertyList Additions
---
```

## Command: PlistExist

**Description:** match a value in an array (or a dictionary).

### Direct Parameter
- **Description:** a value
- **Types:** any
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | an array (or a dictionary) | CFRef | No |
| several values | is the direct parameter a list of values. Default: false | boolean | No |

### Result
- **Description:** the available indices (1 based) or the available keys
- **Types:** integer, string
<a name="plistmatch"></a>
```yaml
---
type: command
name: PlistMatch
suite: Satimage PropertyList Additions
---
```

## Command: PlistMatch

**Description:** return a list of dictionaries containing a given key or a given (key, value) pair.

### Direct Parameter
- **Description:** an array containing dictionaries
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| key | the key to match. For a more complex request, omit this parameter and provide the "using" parameter | string | No |
| using | a selecting path (see PlistChild) | string | Yes |
| value | the requested value of the key | string, real, boolean | Yes |

### Result
- **Types:** CFRef
<a name="plisturl"></a>
```yaml
---
type: command
name: PlistURL
suite: Satimage PropertyList Additions
---
```

## Command: PlistURL

**Description:** get the path to the plist document.

### Direct Parameter
- **Description:** the document
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as |  | type | Yes |
| parent | return the parent folder. Default: false | boolean | Yes |

### Result
- **Types:** file specification
<a name="plistdocument"></a>
```yaml
---
type: command
name: PlistDocument
suite: Satimage PropertyList Additions
---
```

## Command: PlistDocument

**Description:** retrieve the already opened plist from the file URL.

### Direct Parameter
- **Types:** file specification
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in pool | Default: the current pool. At launch the current pool is "". | string | Yes |

### Result
- **Description:** the plist
- **Types:** CFRef
<a name="plistlistdocuments"></a>
```yaml
---
type: command
name: PlistListDocuments
suite: Satimage PropertyList Additions
---
```

## Command: PlistListDocuments

**Description:** List the opened plist documents

### Direct Parameter
- **Description:** the pool. Default: the current pool
- **Types:** string
### Result
- **Description:** the property lists opened in the specified pool.
- **Types:** CFRef
<a name="plistadd"></a>
```yaml
---
type: command
name: PlistAdd
suite: Satimage PropertyList Additions
---
```

## Command: PlistAdd

**Description:** concatenate arrays or dictionaries. "PlistAdd x after y" (resp. "PlistAdd x before y") works like the Applescript statement "set y to y & x" (resp. "set y to x & y") 

### Direct Parameter
- **Description:** of the same type as the "after" or "before" parameter. May alternatively be a list or a record
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| after | the array or the dictionary to modify | CFRef | Yes |
| before | the array or the dictionary to modify | CFRef | Yes |

<a name="plisttojson"></a>
```yaml
---
type: command
name: PlistToJSON
suite: Satimage PropertyList Additions
---
```

## Command: PlistToJSON

**Description:** transform a plist into a JSON

### Sample Code
### Direct Parameter
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| formatting | add returns and tabs for legibility. Default: false. | boolean | Yes |
| replacer | a JavaScript function for the optional callback of JSON.stringify. | string | Yes |

### Result
- **Types:** string
<a name="plisttojavascript"></a>
```yaml
---
type: command
name: PlistToJavaScript
suite: Satimage PropertyList Additions
---
```

## Command: PlistToJavaScript

### Direct Parameter
- **Types:** CFRef
### Result
- **Types:** string
<a name="plistfromjson"></a>
```yaml
---
type: command
name: PlistFromJSON
suite: Satimage PropertyList Additions
---
```

## Command: PlistFromJSON

**Description:** transform a JSON into a plist

### Direct Parameter
- **Description:** the JSON
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in pool | the name of the group where the plist document is created. Default: the current pool. | string | Yes |

### Result
- **Types:** CFRef
<a name="plistsetdocid"></a>
```yaml
---
type: command
name: PlistSetDocID
suite: Satimage PropertyList Additions
---
```

## Command: PlistSetDocID

**Description:** set an identifier to an existing plist

### Direct Parameter
- **Description:** the XML document
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to |  | string | No |

### Result
- **Description:** the previous ID
- **Types:** string
<a name="plistgetdocbyid"></a>
```yaml
---
type: command
name: PlistGetDocByID
suite: Satimage PropertyList Additions
---
```

## Command: PlistGetDocByID

**Description:** retrieve a plist by identifier. Avoid many problems with the AppleScript's global variables

### Direct Parameter
- **Description:** the identifier
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in pool | Default: the current pool. | string | Yes |

### Result
- **Types:** CFRef
<a name="plistgetid"></a>
```yaml
---
type: command
name: PlistGetID
suite: Satimage PropertyList Additions
---
```

## Command: PlistGetID

### Direct Parameter
- **Description:** a reference to the property list
- **Types:** CFRef
### Result
- **Description:** the ID of the property list
- **Types:** integer
<a name="plistfromid"></a>
```yaml
---
type: command
name: PlistFromID
suite: Satimage PropertyList Additions
---
```

## Command: PlistFromID

### Direct Parameter
- **Description:** the ID of the property list
- **Types:** integer
### Result
- **Description:** a reference to the property list
- **Types:** CFRef
<a name="cfref"></a>
```yaml
---
type: value-type
name: CFRef
suite: Satimage PropertyList Additions
---
```

## Value Type: CFRef

**Description:** an opaque reference to a property list element. Initial CFRefs must be created with PlistNew or PlistOpen.

## Satimage Pool Additions

**Description:** Pool management. Optional features that you can use to manage groups of XML documents or PList's, protect their privacy, and dispose of them when suitable.

<a name="setpool"></a>
```yaml
---
type: command
name: SetPool
suite: Satimage Pool Additions
---
```

## Command: SetPool

**Description:** Set the new default pool. Further "XMLOpen", "XMLListDocuments", "PlistOpen", "PlistNew" and "PlistListDocuments" will occur in this pool

### Direct Parameter
- **Description:** name of the new default pool
- **Types:** string
### Result
- **Description:** the previous default pool.
- **Types:** string
<a name="deletepool"></a>
```yaml
---
type: command
name: DeletePool
suite: Satimage Pool Additions
---
```

## Command: DeletePool

**Description:** release all documents in the specified pool.

### Direct Parameter
- **Description:** name of the pool. Default: the default pool.
- **Types:** string
<a name="getpool"></a>
```yaml
---
type: command
name: GetPool
suite: Satimage Pool Additions
---
```

## Command: GetPool

**Description:** return the name of the pool containing the document

### Direct Parameter
- **Description:** an XML document (XMLRef) or a plist document (CFRef)
- **Types:** anything
### Result
- **Description:** the name of the pool.
- **Types:** string
## XNF Additions

**Description:** 

### Sample Code
<a name="xnfopen"></a>
```yaml
---
type: command
name: XNFOpen
suite: XNF Additions
---
```

## Command: XNFOpen

**Description:** open an xnf bundle or create a new xnf bundle if the file does not exist. Must be balanced with a XMLClose (or DeletePool) at the end of the job. XNFOpen equivalent to XMLOpen but expects a bundle path instead of a file path.

### Sample Code
### Direct Parameter
- **Description:** usually with a file name ending with".xnf"
- **Types:** file
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in pool | the name of the group where the new document is created. Default: the current pool. At launch the current pool is "". | string | Yes |

### Result
- **Description:** a reference to the table of contents. Call XMLClose to release the memory
- **Types:** XMLRef
<a name="xnfsavebundle"></a>
```yaml
---
type: command
name: XNFSaveBundle
suite: XNF Additions
---
```

## Command: XNFSaveBundle

**Description:** save the TOC of the XNF bundle (like XMLSave does) and update the modification date of the bundle

### Sample Code
### Direct Parameter
- **Description:** an XMLRef returned by XNFOpen
- **Types:** XMLRef
<a name="xnfnewdataset"></a>
```yaml
---
type: command
name: XNFNewDataSet
suite: XNF Additions
---
```

## Command: XNFNewDataSet

**Description:** create a new dataset with a given id and given dimensions

### Sample Code
### Direct Parameter
- **Description:** id of the new dataset
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| dimensions | a list {dim1, ... dimn} of integers | integer | No |
| scale | a list of scale | array of real | Yes |
| at | usually the XML document returned by XNFOpen | XMLRef | No |

### Result
- **Description:** the resulting node
- **Types:** XMLRef
<a name="xnfgetdataset"></a>
```yaml
---
type: command
name: XNFGetDataSet
suite: XNF Additions
---
```

## Command: XNFGetDataSet

**Description:** retrieve an reference to a dataset by id. XNFGetDataSet thexnf xmlid "aa" is a shortcut for XMLPath thexnf with "id('aa')"

### Direct Parameter
- **Description:** an XMLRef returned by XNFOpen
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| xmlid | id of the dataset | string | No |

### Result
- **Description:** a dataset
- **Types:** XMLRef
<a name="xnfgetdimensions"></a>
```yaml
---
type: command
name: XNFGetDimensions
suite: XNF Additions
---
```

## Command: XNFGetDimensions

**Description:** retrieve the dimensions of a dataset. 

### Direct Parameter
- **Description:** a dataset
- **Types:** XMLRef
### Result
- **Description:** the list of the dimensions {n1,...}
- **Types:** any
<a name="xnfnewarray"></a>
```yaml
---
type: command
name: XNFNewArray
suite: XNF Additions
---
```

## Command: XNFNewArray

**Description:** add an array to a dataset

### Direct Parameter
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | a dataset returned by XNFNewDataSet or XNFGetDataSet | XMLRef | No |
| as | the requested format for the data in the file: "real32" | "real64" | "uint8" | "uint16" | "uint32" | "sint8" | "sint16" | "sint32" | "complex64" | "complex32". Default: "real64" | string | Yes |
| big endian | the requested byteorder. Default: system byte order. | boolean | Yes |

### Result
- **Description:** the resulting node
- **Types:** XMLRef
<a name="xnfnewfiledata"></a>
```yaml
---
type: command
name: XNFNewFileData
suite: XNF Additions
---
```

## Command: XNFNewFileData

**Description:** add an array already stored in a binary file to a dataset

### Direct Parameter
- **Description:** an alias or a string for an absolute or relative URL
- **Types:** any
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | a node returned by XNFNewDataSet or XNFGetDataSet | XMLRef | No |
| starting at | offset of the data in bytes. Default 0 | integer | Yes |
| as | the format of the data in the file: "real32" | "real64" | "uint8" | "uint16" | "uint32" | "sint8" | "sint16" | "sint32" | "complex64" | "complex32" | string | No |
| big endian | is the file encoded as big endian or little endian? Default: system byte order. | boolean | Yes |

### Result
- **Description:** the resulting node
- **Types:** XMLRef
<a name="xnfgetarray"></a>
```yaml
---
type: command
name: XNFGetArray
suite: XNF Additions
---
```

## Command: XNFGetArray

**Description:** retrieve an array or a sub-array. If "start" and "length" are present XNFGetArray returns a sub-array of possibly lower dimensionality if some length is 1.

### Direct Parameter
- **Description:** a dataset
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| index | index of the array inside the dataset. Default 1 | integer | Yes |
| start | for each dimension of the dataset, the first element to read. 1-based | integer | Yes |
| length | for each dimension of the dataset, number of elements to read | integer | Yes |
| part | for complex arrays, choose a string in the set "r" (real part),  "i" (imaginary part),  "m" (modulus) or  "p" (phase) | string | Yes |
| as | pass 'record' to get the result as a record {dimensions:{...}, array of real: ...} | type | Yes |

### Result
- **Description:** or record
- **Types:** array of real
<a name="xnfsetscale"></a>
```yaml
---
type: command
name: XNFSetScale
suite: XNF Additions
---
```

## Command: XNFSetScale

**Description:** set the scale of the specified axis to a list of real

### Direct Parameter
- **Description:** index of the axis in the dataset
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | a node returned by XNFNewDataSet or XNFGetDataSet | XMLRef | No |
| to |  | array of real | No |
| as | the requested format for the data in the file: "real32" | "real64" | "uint8" | "uint16" | "uint32" | "sint8" | "sint16" | "sint32". Default: "real64" | string | Yes |
| big endian | the requested byteorder. Default: system byte order. | boolean | Yes |

<a name="xnfsetscalereference"></a>
```yaml
---
type: command
name: XNFSetScaleReference
suite: XNF Additions
---
```

## Command: XNFSetScaleReference

**Description:** set the scale of the specified axis to a reference of some 1-D dataset

### Direct Parameter
- **Description:** index of the axis in the dataset
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | a node returned by XNFNewDataSet or XNFGetDataSet | XMLRef | No |
| to | the id of an existing dataset | string | No |

<a name="xnfsetscalerange"></a>
```yaml
---
type: command
name: XNFSetScaleRange
suite: XNF Additions
---
```

## Command: XNFSetScaleRange

**Description:** set the scale of the specified axis to a range

### Direct Parameter
- **Description:** index of the axis in the dataset
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | a node returned by XNFNewDataSet or XNFGetDataSet | XMLRef | No |
| to | a list {start,step} | real | No |

<a name="xnfgetscales"></a>
```yaml
---
type: command
name: XNFGetScales
suite: XNF Additions
---
```

## Command: XNFGetScales

**Description:** retrieve the scales of dataset. If "start" and "length" are present XNFGetScales returns the scales corresponding to the sub-array returned by XNFGetArray

### Direct Parameter
- **Description:** a dataset
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| start | for each dimension of the dataset, the first element to read. 1-based | integer | Yes |
| length | for each dimension of the dataset, number of elements to read | integer | Yes |

### Result
- **Types:** array of real
<a name="xnfgetarray3d"></a>
```yaml
---
type: command
name: XNFGetArray3D
suite: XNF Additions
---
```

## Command: XNFGetArray3D

**Description:** see Numerics.osax about Array3DRef

### Direct Parameter
- **Description:** a 3-D dataset
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| index | index of the array inside the dataset. Default 1 | integer | Yes |
| name | the name of the new Array3DRef | string | Yes |
| part | for complex arrays, choose a string in the set "r" (real part),  "i" (imaginary part),  "m" (modulus) or  "p" (phase) | string | Yes |

### Result
- **Types:** Array3DRef
<a name="xnfremove"></a>
```yaml
---
type: command
name: XNFRemove
suite: XNF Additions
---
```

## Command: XNFRemove

**Description:** delete a dataset or an array

### Direct Parameter
- **Description:** the object to delete
- **Types:** XMLRef
## 

**Description:** None

<a name="xmlcookie"></a>
```yaml
---
type: command
name: XMLCookie
suite: 
---
```

## Command: XMLCookie

**Description:** store a cookie for a given host. This cookie is reused in forthcoming XMLOpen commands

### Direct Parameter
- **Description:** the value of the cookie. If the parameter is missing, XMLCookie silently returns the current value of the cookie
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the http (or https) URL providing the host | string | No |

### Result
- **Description:** the previous value of the cookie
- **Types:** string
<a name="xmlregisterscheme"></a>
```yaml
---
type: command
name: XMLRegisterScheme
suite: 
---
```

## Command: XMLRegisterScheme

**Description:** register a URI scheme with an AppleScript callback. A cousin of rewriteURL

### Direct Parameter
- **Description:** the scheme
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| subroutine | the name of the AppleScript callback. The callback takes a string (URI) argument and returns a string (URI) | string | No |

<a name="xmldisplayentity"></a>
```yaml
---
type: command
name: XMLDisplayEntity
suite: 
---
```

## Command: XMLDisplayEntity

### Direct Parameter
- **Description:** the entity name
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | a document with a dtd | XMLRef | No |

### Result
- **Types:** string
<a name="xmlresolvescheme"></a>
```yaml
---
type: command
name: XMLResolveScheme
suite: 
---
```

## Command: XMLResolveScheme

**Description:** translate an URL as soon as a corresponding callback has been installed with XMLRegisterScheme

### Direct Parameter
- **Description:** the original URL
- **Types:** string
### Result
- **Description:** the translated URL
- **Types:** string
<a name="plistcopy"></a>
```yaml
---
type: command
name: PlistCopy
suite: 
---
```

## Command: PlistCopy

**Description:** copy a dictionary or an array to another one. The 2 parameters must have the same type.

### Direct Parameter
- **Description:** a dictionary or an array
- **Types:** CFRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | a dictionary or an array | CFRef | No |

<a name="extractbinary"></a>
```yaml
---
type: command
name: ExtractBinary
suite: 
---
```

## Command: ExtractBinary

### Direct Parameter
- **Description:** the file
- **Types:** file specification
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| skip | the number of leading bytes to skip | integer | Yes |
| big endian | is the file encoded as big endian or little endian? Default: system endianess (false on mac intel). | boolean | Yes |
| as | the format of the data in the file: "real32" | "real64" | "uint8" | "uint16" | "uint32" | "sint8" | "sint16" | "sint32" | "complex64" | "complex32" | string | No |
| dimensions | the dimensions of the array | integer | No |
| start | for each dimension of the array, the first element to read. 1-based | integer | No |
| length | for each dimension of the array, number of elements to read | integer | No |

### Result
- **Types:** array of real, record
<a name="xmlobsolete"></a>
```yaml
---
type: command
name: XMLObsolete
suite: 
---
```

## Command: XMLObsolete

### Direct Parameter
- **Types:** boolean
### Result
- **Types:** boolean
<a name="xmlgettextobso"></a>
```yaml
---
type: command
name: XMLGetTextObso
suite: 
---
```

## Command: XMLGetTextObso

**Description:** return the textual contents of a node.

### Direct Parameter
- **Description:** an XML object containing a simple text node.
- **Types:** XMLRef
### Result
- **Types:** string
<a name="xmlgetattributeobso"></a>
```yaml
---
type: command
name: XMLGetAttributeObso
suite: 
---
```

## Command: XMLGetAttributeObso

**Description:** return the contents of an attribute.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the name of the attribute | string | No |
| namespace | the namespace URL | string | Yes |

### Result
- **Types:** string
<a name="xmltagnameobso"></a>
```yaml
---
type: command
name: XMLTagNameObso
suite: 
---
```

## Command: XMLTagNameObso

**Description:** return the name of the element.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Result
- **Types:** string
<a name="xmlfulltagname"></a>
```yaml
---
type: command
name: XMLFullTagName
suite: 
---
```

## Command: XMLFullTagName

**Description:** return the name of the element.

### Direct Parameter
- **Types:** XMLRef, XMLRef
### Result
- **Types:** string
<a name="xmldisplayxmlobso"></a>
```yaml
---
type: command
name: XMLDisplayXMLObso
suite: 
---
```

## Command: XMLDisplayXMLObso

**Description:** return an XML object as a string.

### Direct Parameter
- **Description:** (or a list of XMLRef) the XML object to display
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| formatting | add returns and tabs for legibility. Default: true. | boolean | Yes |

### Result
- **Description:** (or a list of text)
- **Types:** string
<a name="xmlnodeinfoobso"></a>
```yaml
---
type: command
name: XMLNodeInfoObso
suite: 
---
```

## Command: XMLNodeInfoObso

**Description:** return node information.

### Direct Parameter
- **Description:** the XML object to display
- **Types:** XMLRef
### Result
- **Description:** a record containing the name, the kind and the dictionary (attributes) of the object
- **Types:** NodeInfo
<a name="xmlsettagname"></a>
```yaml
---
type: command
name: XMLSetTagName
suite: 
---
```

## Command: XMLSetTagName

### Direct Parameter
- **Description:** the XML object to display
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the new name | string | No |

<a name="xmlremovenamespace"></a>
```yaml
---
type: command
name: XMLRemoveNamespace
suite: 
---
```

## Command: XMLRemoveNamespace

### Direct Parameter
- **Types:** namespace
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at |  | XMLRef | No |

<a name="listpools"></a>
```yaml
---
type: command
name: ListPools
suite: 
---
```

## Command: ListPools

### Result
- **Types:** string
<a name="xmlxpathcompile"></a>
```yaml
---
type: command
name: XMLXPathCompile
suite: 
---
```

## Command: XMLXPathCompile

### Direct Parameter
- **Description:** an xpath expression
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in |  | XMLRef | No |

### Result
- **Types:** integer
<a name="xmlgetnode_at_line"></a>
```yaml
---
type: command
name: XMLGetNode at line
suite: 
---
```

## Command: XMLGetNode at line

### Direct Parameter
- **Description:** the line index
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in |  | XMLRef | No |

### Result
- **Types:** XMLRef
<a name="xmlparsecurie"></a>
```yaml
---
type: command
name: XMLParseCURIE
suite: 
---
```

## Command: XMLParseCURIE

**Description:** return the non-abreviated URI corresponding to the data parameter or the value of an attribute (if name and/or namespace are specified) or the text contents of an element (no data and no name)

### Direct Parameter
- **Description:** an element or an attribute
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the name of the attribute containing the CURIE | string | Yes |
| namespace | the namespace URL of the attribute | string | Yes |
| data | any CURIE (http://www.w3.org/TR/curie/) to be expanded in the context of the direct parameter | string | Yes |

### Result
- **Types:** string
<a name="xmlgetarray"></a>
```yaml
---
type: command
name: XMLGetArray
suite: 
---
```

## Command: XMLGetArray

### Sample Code
### Direct Parameter
- **Types:** XMLRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| start | the index of the first element to read. 1-based, default 1 | integer | Yes |
| length | number of elements to read. Default: read until the end. | integer | Yes |

### Result
- **Types:** array of real
<a name="xmlsetarray"></a>
```yaml
---
type: command
name: XMLSetArray
suite: 
---
```

## Command: XMLSetArray

### Direct Parameter
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | an element node | XMLRef | No |
| href | the binary file to use | alias | No |
| as | the requested format for the data in the file: "real32" | "real64" | "uint8" | "uint16" | "uint32" | "sint8" | "sint16" | "sint32" | "complex64" | "complex32". Default: "real64" | string | Yes |
| big endian | the requested byteorder. Default: system byte order. | boolean | Yes |

## Linear algebra

**Description:** real vectors and real matrices must be provided as "array of real" and "matrix" (see the Satimage.osax). Complex vectors and matrices must be provided as list of 2 arrays of real or 2 matrices.

<a name="currentendianess"></a>
```yaml
---
type: command
name: currentEndianess
suite: Linear algebra
---
```

## Command: currentEndianess

### Result
- **Description:** return true means big endian
- **Types:** boolean
<a name="transpose"></a>
```yaml
---
type: command
name: transpose
suite: Linear algebra
---
```

## Command: transpose

**Description:** transpose a matrix. Provide a list of two matrices to transpose a complex matrix

### Direct Parameter
- **Description:** the matrix
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| adjoint | For complex matrix only: request the adjoint of the direct parameter. Default: true | boolean | Yes |

### Result
- **Description:** the transposed matrix
- **Types:** matrix
<a name="multmatrix"></a>
```yaml
---
type: command
name: multmatrix
suite: Linear algebra
---
```

## Command: multmatrix

**Description:** matrix x matrix, vector x matrix, matrix x vector, vector x vector (scalar product). Here vector stands for array of real. Provide a list of two matrices to define a complex matrix

### Direct Parameter
- **Description:** array of real or matrix
- **Types:** anything
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | array of real or matrix | anything | No |

### Result
- **Description:** real, array of real or matrix
- **Types:** anything
<a name="invertmatrix"></a>
```yaml
---
type: command
name: invertmatrix
suite: Linear algebra
---
```

## Command: invertmatrix

**Description:** invert a matrix

### Direct Parameter
- **Description:** a matrix or a list of two matrices {A_real,A_imag}
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| positive | false: general matrix, true: positive symmetric or Hermitian matrix. default: false | boolean | Yes |

### Result
- **Description:** return the inverse matrix (with ipiv). Determinant is always calculated
- **Types:** record
<a name="solve_linear_system"></a>
```yaml
---
type: command
name: solve linear system
suite: Linear algebra
---
```

## Command: solve linear system

**Description:** Solve X for the linear system AX=B

### Direct Parameter
- **Description:** a matrix or a list of two matrices {A_real,A_imag}
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| RHS | B as array of real or a matrix representing the vectors in columns {B1,B2, ...} (for complex a list of two arrays of real or a list of two matrices) | array of real | No |
| symmetry | false: general matrix, true: symmetric or Hermitian matrix. default: false | boolean | Yes |
| positive | true for definite positive matrix. default: false | boolean | Yes |

### Result
- **Description:** or a matrix if "RHS" is a matrix. Errors with small positive number n means minor n of A is not positive
- **Types:** array of real
<a name="compute_eigenvalues"></a>
```yaml
---
type: command
name: compute eigenvalues
suite: Linear algebra
---
```

## Command: compute eigenvalues

**Description:** compute eigenvalues and eigenvectors of a matrix

### Direct Parameter
- **Description:** a square matrix
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| eigenvects | true: compute the eigenvectors. default: false | boolean | Yes |
| Vtype | used when eigenvects are required for non symmetric matrices. 0:right, 1:left, 2:both eigenvects. default: 0 | integer | Yes |
| symmetry | false: general matrix, true: symmetric or Hermitian matrix. default: false | boolean | Yes |
| conquer | false: standard driver, true: use divide-and-conquer driver in case of symmetric inputs. default: true | boolean | Yes |
| irange | a list of two integers {i1,i2}: eigenvalues (eigenvectors) from i1 to i2 are computed | list of integer | Yes |
| erange | the lower VL and upper VU bounds of the interval to be searched for eigenvalues. VL < VU | list of real | Yes |
| RHS | Solve the generalized problem with right hand side: Ax = lamba Bx. If symmetry is true, RHS has to be symmetric definite positive and Itype describes the following cases. Itype=1: Ax = lamba Bx, Itype=2: ABx = lambda x, Itype=3: BAx = lambda x | matrix | Yes |
| Itype | see descrition of "RHS", default: 1 | integer | Yes |

### Result
- **Description:** {eigenvalues:array of real or a list of 2 arrays of real, eigenvectors (or right eigenvectors and left eigenvectors if Vtype=2): matrix or a list of 2 matrices}
- **Types:** record
<a name="ludecomposition"></a>
```yaml
---
type: command
name: LUdecomposition
suite: Linear algebra
---
```

## Command: LUdecomposition

**Description:** returns the A=PLU decomposition or the Cholesky decomposition (A=U**TU) of a matrix A. P is a permutation matrix, L a lower triangular matrix and U an upper triangular matrix

### Direct Parameter
- **Description:** you can provide a list of two matrices to define a complex matrix
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| positive | false: general matrix, compute LU decomposition. True: compute Chowlesky decomposition; in this case the matrix A has to be positive symmetric or Hermitian. Default: false | boolean | Yes |

### Result
- **Description:** {uppermatrix:matrix, lowermatrix:matrix, permutation vector:array of real, determinant:real}. lowermatrix and  permutation vector are not provided in case of Chowlesky decomposition. If you have provided a complex matrix, the results are lists of two matrices {real, imaginary}
- **Types:** Lapack result
<a name="pivot"></a>
```yaml
---
type: command
name: pivot
suite: Linear algebra
---
```

## Command: pivot

**Description:** Apply the permutation defined by the permutation vector of the result of LUdecomposition

### Direct Parameter
- **Description:** the permutation vector as returned by LUdecomposition
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | matrix or array of real | anything | Yes |

### Result
- **Types:** anything
<a name="compute_determinant"></a>
```yaml
---
type: command
name: compute determinant
suite: Linear algebra
---
```

## Command: compute determinant

**Description:** determinant of a matrix

### Direct Parameter
- **Description:** a square matrix. You can provide a list of two matrices to define a complex matrix
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| positive | false: general matrix, true: positive symmetric or Hermitian matrix. default: false | boolean | Yes |

### Result
- **Description:** or a list of 2 reals {re(det), im(det)}
- **Types:** real
<a name="anything"></a>
```yaml
---
type: class
name: anything
suite: Linear algebra
---
```

## Class: anything

**Description:** any class or reference

<a name="array_of_real"></a>
```yaml
---
type: class
name: array of real
suite: Linear algebra
---
```

## Class: array of real

<a name="matrix"></a>
```yaml
---
type: class
name: matrix
suite: Linear algebra
---
```

## Class: matrix

<a name="dimensions"></a>
```yaml
---
type: class
name: dimensions
suite: Linear algebra
---
```

## Class: dimensions

<a name="scale"></a>
```yaml
---
type: class
name: scale
suite: Linear algebra
---
```

## Class: scale

<a name="number_of_field"></a>
```yaml
---
type: class
name: number of field
suite: Linear algebra
---
```

## Class: number of field

<a name="alias"></a>
```yaml
---
type: class
name: alias
suite: Linear algebra
---
```

## Class: alias

<a name="file_specification"></a>
```yaml
---
type: class
name: file specification
suite: Linear algebra
---
```

## Class: file specification

<a name="bounding_rectangle"></a>
```yaml
---
type: class
name: bounding rectangle
suite: Linear algebra
---
```

## Class: bounding rectangle

<a name="xmlref"></a>
```yaml
---
type: class
name: XMLRef
suite: Linear algebra
---
```

## Class: XMLRef

<a name="lapack_result"></a>
```yaml
---
type: record-type
name: Lapack result
suite: Linear algebra
---
```

## Record Type: Lapack result

**Description:** for complex data, each term list of two terms {real,imag}

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| eigenvalues | Eigenvalues E | array of real | read/write |
| eigenvectors | Eigenvectors | matrix | read/write |
| right eigenvectors | Right Eigenvectors | matrix | read/write |
| left eigenvectors | Left Eigenvectors | matrix | read/write |
| uppermatrix | upper matrix from LU decomposition | matrix | read/write |
| lowermatrix | lower matrix from LU decomposition | matrix | read/write |
| permutation vector | Permutation vector | matrix | read/write |
| determinant | determinant | real | read/write |

## FFT and convolution

**Description:** 

<a name="fft1d"></a>
```yaml
---
type: command
name: fft1d
suite: FFT and convolution
---
```

## Command: fft1d

**Description:** normalized, general fast Fourier transform. This is a general interface allowing grouped and n-dimensional fft. Time is of order Nlog(N) but is better when the size of vectors is a product of powers of small prime numbers

### Direct Parameter
- **Description:** or a list {real part, imaginary part} of 2 arrays of real
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| inverse | default false, if true the inverse fft | boolean | Yes |
| lot | the number of vectors to transform | integer | Yes |
| vector size | the number of elements of each vector | integer | Yes |
| vector step | the distance between elements in a vector | integer | Yes |
| vector offset | the distance between vectors | integer | Yes |

### Result
- **Description:** {real part, imaginary part} of the resulting fft
- **Types:** array of real
<a name="fft2d"></a>
```yaml
---
type: command
name: fft2d
suite: FFT and convolution
---
```

## Command: fft2d

**Description:** 2d fast Fourier transform

### Direct Parameter
- **Description:** or a list {real part, imaginary part} of 2 matrices
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| inverse | default false, if true the inverse fft | boolean | Yes |

### Result
- **Description:** {real part, imaginary part} of the resulting fft
- **Types:** matrix
<a name="filterarray"></a>
```yaml
---
type: command
name: filterarray
suite: FFT and convolution
---
```

## Command: filterarray

**Description:** performs convolution. result is r(i)=sum over j of (s(i-j)f(j))

### Direct Parameter
- **Description:** the signal s (size ns)
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | the filter f (size nf) | array of real | No |
| correlation | calculate correlation instead of convolution | boolean | No |

### Result
- **Description:** the result r. its size is nr=ns-nf+1
- **Types:** array of real
<a name="convolve"></a>
```yaml
---
type: command
name: convolve
suite: FFT and convolution
---
```

## Command: convolve

**Description:** a function f by a function g. Returns the sum over j of f(i-j)*g(j). If not circular f is padded with n 0's outside its definition set

### Direct Parameter
- **Description:** the function f: an array of real of size n
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | the function g: an array of real of size m. If m≠n, either f or g is padded with 0's | array of real | No |
| circular | the functions f and g are periodized with period max(n,m). Default: true | boolean | Yes |

### Result
- **Description:** if circular size of the result is max(n,m), else 2*max(n,m)-1
- **Types:** array of real
<a name="correlate"></a>
```yaml
---
type: command
name: correlate
suite: FFT and convolution
---
```

## Command: correlate

**Description:** returns the sum over j of (f(i+j)-<f>)*(g(j)-<g>)

### Direct Parameter
- **Description:** the signal (size n)
- **Types:** array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | another signal of size n | array of real | No |
| circular | the signals are periodized with period n. Default: true | boolean | Yes |
| normalized | if normalized the result of "correlate x to x" is smaller than 1 and takes the value 1 at index 1 if circular, and at index n if not circular. Default: true | boolean | Yes |

### Result
- **Description:** if circular size of the result is n, else 2*n-1 and the origin (i=0) is at index n
- **Types:** array of real
<a name="interpolate"></a>
```yaml
---
type: command
name: interpolate
suite: FFT and convolution
---
```

## Command: interpolate

### Direct Parameter
- **Description:** {xs,ys}
- **Types:** list of array of real
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the new xs | array of real | No |
| period |  | real | Yes |
| linear | linear interpolation vs. spline. Default false. | boolean | Yes |
| boundary conditions | {dy1,dyn} | list of real | Yes |

### Result
- **Description:** the new ys
- **Types:** array of real
## Image files

**Description:** utilities for image processing.

<a name="imagefile_bounds"></a>
```yaml
---
type: command
name: imagefile bounds
suite: Image files
---
```

## Command: imagefile bounds

**Description:** return the bounds of a bitmap image (JPEG, TIFF etc.)

### Direct Parameter
- **Types:** alias
### Result
- **Types:** bounding rectangle
<a name="convert_imagefile"></a>
```yaml
---
type: command
name: convert imagefile
suite: Image files
---
```

## Command: convert imagefile

**Description:** return the array of the gray levels of a bitmap image (JPEG, TIFF etc.)

### Direct Parameter
- **Types:** alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| selected rectangle |  | bounding rectangle | Yes |
| vertical flip | default:false, the origin of the matrix corresponds to the top-left corner. | boolean | Yes |

### Result
- **Types:** matrix
<a name="create_grayimagefile"></a>
```yaml
---
type: command
name: create grayimagefile
suite: Image files
---
```

## Command: create grayimagefile

**Description:** convert matrix values into 256 levels then save it as a gray bitmap image (PNG, JPEG, TIFF etc.)

### Direct Parameter
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | destination file. Its extension specifies the image format | file specification | No |
| inverted | inverse image levels. Default false | boolean | Yes |
| minimum | matrix values equal or greater than this value are set to 255. Default: maximum of the matrix values | real | Yes |
| maximum | matrix values equal or lower than this value are set to 0. Default: minimum of the matrix values | real | Yes |
| resolution | image resolution. Default: 72dpi | integer | Yes |

### Result
- **Types:** alias
<a name="particles"></a>
```yaml
---
type: command
name: particles
suite: Image files
---
```

## Command: particles

**Description:** find particles in an image

### Direct Parameter
- **Description:** the image as a matrix containing the grey levels
- **Types:** matrix
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| threshold |  | real | No |
| data | get xdata and ydata info in the result record | boolean | Yes |
| minimum | minimum area | real | Yes |
| maximum | maximum area | real | Yes |

### Result
- **Description:** info on particles
- **Types:** record
## 3D array handling

**Description:** commands to handle 3D arrays. "open3D" loads a 3D array in memory and returns an ID number. You refer to a 3D array either with its ID or its name

<a name="open3d"></a>
```yaml
---
type: command
name: open3D
suite: 3D array handling
---
```

## Command: open3D

**Description:** Loads a 3D array and returns an ID for it. The memory must be released with "close3D"

### Direct Parameter
- **Description:** the name of the 3D array
- **Types:** string
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| dimensions | the 3 dimensions {nx, ny, nz} of the array. nx, ny and, nz are either an integer or an array of real altogether defining the size and the scale. If a dimension is an integer the scale is assumed to be {0, 1, 2, ...} | list of integer | No |
| field | an array of real (or a list of 3 arrays of real defining a vector field) with nz as leading dimension. The value for {ix, iy, iz} must be at offset ix+nx*iy+nx*ny*iz | array of real | No |

### Result
- **Description:** ID to the 3D array
- **Types:** Array3DRef
<a name="close3d"></a>
```yaml
---
type: command
name: close3D
suite: 3D array handling
---
```

## Command: close3D

**Description:** release the memory associated to a opened 3D array

### Direct Parameter
- **Description:** a reference to an opened 3D array (or its name)
- **Types:** Array3DRef
<a name="info3d"></a>
```yaml
---
type: command
name: info3D
suite: 3D array handling
---
```

## Command: info3D

### Direct Parameter
- **Description:** a reference to an opened 3D array (or its name)
- **Types:** Array3DRef
### Result
- **Description:** the dimensions and scales
- **Types:** record
<a name="contents3d"></a>
```yaml
---
type: command
name: contents3D
suite: 3D array handling
---
```

## Command: contents3D

### Direct Parameter
- **Description:** a reference to an opened 3D array (or its name)
- **Types:** Array3DRef
### Result
- **Description:** the data
- **Types:** array of real
<a name="list3d"></a>
```yaml
---
type: command
name: list3D
suite: 3D array handling
---
```

## Command: list3D

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | list3D as string returns the names of the opened 3D arrays instead of their references | anything | Yes |

### Result
- **Description:** the references of the opened 3D arrays
- **Types:** list of Array3DRef
<a name="rename3d"></a>
```yaml
---
type: command
name: rename3D
suite: 3D array handling
---
```

## Command: rename3D

**Description:** rename an opened 3D array.

### Direct Parameter
- **Description:** a reference to an opened 3D array (or its name)
- **Types:** Array3DRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| into | the new name | string | No |

<a name="extract3d"></a>
```yaml
---
type: command
name: extract3D
suite: 3D array handling
---
```

## Command: extract3D

**Description:** Extract a subset from a 3D array

### Direct Parameter
- **Description:** a reference to an opened 3D array (or its name)
- **Types:** Array3DRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| start | the 3 1-based offsets | list of integer | No |
| length | the 3 lengths | list of integer | No |
| field index | if the 3D array is a vector field, a number between 1 and 3. Default 1 | integer | Yes |

### Result
- **Types:** array of real
<a name="isosurface"></a>
```yaml
---
type: command
name: isosurface
suite: 3D array handling
---
```

## Command: isosurface

**Description:** computes an isosurface for a 3D field

### Direct Parameter
- **Description:** a reference to an opened 3D array (or its name)
- **Types:** Array3DRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the isosurface value | real | No |
| field index | if the 3D array is a vector field, a number between 1 and 3. Default 1 | integer | Yes |

### Result
- **Description:** the triangle list as an array of real that defines the isosurface
- **Types:** array of real
<a name="streamline"></a>
```yaml
---
type: command
name: streamline
suite: 3D array handling
---
```

## Command: streamline

**Description:** Computes a streamline for an opened vector field

### Direct Parameter
- **Description:** a reference to an opened 3D array (or its name)
- **Types:** Array3DRef
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| starting at | a point {x, y, z} | list of real | No |
| resolution | Default 1. Smaller value increases the number of points in the streamline | real | Yes |
| direction | Default 1. Set to -1 to compute the streamline along opposite direction | integer | Yes |

### Result
- **Description:** the coordinates of the streamline's points {x1,y1,z1,...,xn,yn,zn}
- **Types:** array of real
<a name="array3dref"></a>
```yaml
---
type: value-type
name: Array3DRef
suite: 3D array handling
---
```

## Value Type: Array3DRef

**Description:** a reference to an opened 3D array

## FITS

**Description:** FITS.osax provides commands to read FITS data files. Uses the FITSIO project. mailto:support@satimage-software.com

<a name="fitsopen"></a>
```yaml
---
type: command
name: FITSOpen
suite: FITS
---
```

## Command: FITSOpen

**Description:** open a FITS file

### Direct Parameter
- **Description:** path to the FITS file
- **Types:** alias
### Result
- **Description:** a reference number to the opened file
- **Types:** integer
<a name="fitsclose"></a>
```yaml
---
type: command
name: FITSClose
suite: FITS
---
```

## Command: FITSClose

**Description:** close a FITS file

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
<a name="fitscount"></a>
```yaml
---
type: command
name: FITSCount
suite: FITS
---
```

## Command: FITSCount

**Description:** count data units in a FITS file

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Result
- **Description:** the number of units
- **Types:** integer
<a name="fitsmovein"></a>
```yaml
---
type: command
name: FITSMovein
suite: FITS
---
```

## Command: FITSMovein

**Description:** select a data unit in a FITS file

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the unit index or the unit name | integer | No |

### Result
- **Description:** the type of the selected unit
- **Types:** string
<a name="fitsinfo"></a>
```yaml
---
type: command
name: FITSInfo
suite: FITS
---
```

## Command: FITSInfo

**Description:** get info from the current unit of the opened FITS file

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| verbose | default: false. If verbose is true, FITSInfo returns the full header of the current unit. Otherwise, returns the type of the unit and the list of its dimensions. | boolean | Yes |

### Result
- **Description:** or string if verbose
- **Types:** record
<a name="fitsplist"></a>
```yaml
---
type: command
name: FITSPlist
suite: FITS
---
```

## Command: FITSPlist

**Description:** get info from the current unit of the opened FITS file as xml data

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | string or CFRef. Default: CFRef | type | Yes |

### Result
- **Types:** string, CFRef
<a name="fitsreadimage"></a>
```yaml
---
type: command
name: FITSReadImage
suite: FITS
---
```

## Command: FITSReadImage

**Description:**  read an image unit in  a FITS file

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| along | axis to slice for image dimension equal to 3  | integer | Yes |
| at |  index to read for image dimension equal to 3  | integer | Yes |

### Result
- **Description:** or matrix if result is 2D.
- **Types:** array of real
<a name="fitstableinfo"></a>
```yaml
---
type: command
name: FITSTableInfo
suite: FITS
---
```

## Command: FITSTableInfo

**Description:**  Get basic info about the column of a table unit in  a FITS file

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| column | index (or name) of column | integer, string | No |

### Result
- **Description:** column name, number of rows and data type of the column
- **Types:** record
<a name="fitsreadtable"></a>
```yaml
---
type: command
name: FITSReadTable
suite: FITS
---
```

## Command: FITSReadTable

**Description:**  Read a column of a table unit in  a FITS file

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| column | index (or name) of column | integer, string | No |

### Result
- **Description:** the table column as array of real or string if the column type is string
- **Types:** array of real, string
<a name="fitsextractimage"></a>
```yaml
---
type: command
name: FITSExtractimage
suite: FITS
---
```

## Command: FITSExtractimage

### Direct Parameter
- **Description:** a reference to an opened FITS file
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| start | for each dimension of the image, the first element to read. 1-based | integer | No |
| length | for each dimension of the image, number of elements to read | integer | No |

### Result
- **Types:** array of real, record
<a name="kind"></a>
```yaml
---
type: class
name: kind
suite: FITS
---
```

## Class: kind

<a name="alias"></a>
```yaml
---
type: class
name: alias
suite: FITS
---
```

## Class: alias

<a name="array_of_real"></a>
```yaml
---
type: class
name: array of real
suite: FITS
---
```

## Class: array of real

**Description:** a packed list of small real. Can be coerced to an AppleScript list with 'as list of real'. Conversely, a list of real may be translated using 'as array of real' for fast computation.

<a name="dimensions"></a>
```yaml
---
type: class
name: dimensions
suite: FITS
---
```

## Class: dimensions

<a name="matrix"></a>
```yaml
---
type: class
name: matrix
suite: FITS
---
```

## Class: matrix

**Description:** An AppleScript representation of a 2D array of real numbers as a record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| ncols | the number of columns | integer | read/write |
| nrows | the number of rows | integer | read/write |
| array of real | the data, as an array of real or as a standard AppleScript list of real numbers. Ordering: the first numbers are the data for the first row. | array of real | read/write |

## Files and folders suite

**Description:** None

### Sample Code
<a name="filenew"></a>
```yaml
---
type: command
name: filenew
suite: Files and folders suite
---
```

## Command: filenew

**Description:** create a new empty file, fail if already exists.

### Direct Parameter
- **Description:** the destination folder, or a file path.
- **Types:** alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the file name. If the name parameter is not provided, the direct parameter is considered as the destination file path. | string | No |
| recursively | create intermediate directories as required. Default false. | boolean | Yes |

### Result
- **Description:** the new file
- **Types:** alias
<a name="mkdir"></a>
```yaml
---
type: command
name: mkdir
suite: Files and folders suite
---
```

## Command: mkdir

**Description:** create a new directory.

### Direct Parameter
- **Description:** a  directory path
- **Types:** alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the name of the new directory (if not provided in the direct parameter) | string | Yes |
| recursively | create intermediate directories as required. Default true. | boolean | Yes |

### Result
- **Description:** the new directory
- **Types:** alias
<a name="filecopy"></a>
```yaml
---
type: command
name: filecopy
suite: Files and folders suite
---
```

## Command: filecopy

**Description:** copy a file synchronously

### Direct Parameter
- **Description:** the file(s) to copy
- **Types:** alias, alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the base url. Relevant if direct parameter is a string or a list of strings. | alias | Yes |
| to | the destination folder. Required unless the "filepath" parameter is specified | alias | Yes |
| name | the new file name (when using the "to" parameter). Not allowed if the direct parameter is a list. Default: the original file name | string | Yes |
| filepath | an alternative to the use of the "to" and "name" parameters: the destination file path. Not allowed if the direct parameter is a list | file specification | Yes |
| into | for backward compatibility. Same as as filepath. | file specification | Yes |
| replacing | allow to replace an existing item. Default: false | boolean | Yes |
| full copy | copy all attributes of the file. Default: false | boolean | Yes |

### Result
- **Description:** the copied file(s)
- **Types:** alias, alias
<a name="filemove"></a>
```yaml
---
type: command
name: filemove
suite: Files and folders suite
---
```

## Command: filemove

**Description:** move a file synchronously

### Direct Parameter
- **Description:** the file(s) to move
- **Types:** alias, alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the base url. Relevant if direct parameter is a string or a list of strings. | alias | Yes |
| to | the destination folder. Required unless the "filepath" parameter is specified | alias | Yes |
| name | the new file name (when using the "to" parameter). Not allowed if the direct parameter is a list. Default: the old file name | string | Yes |
| filepath | an alternative to the use of the "to" and "name" parameters: the destination file path. Not allowed if the direct parameter is a list | file specification | Yes |
| into | for backward compatibility. Same as as filepath. | file specification | Yes |
| replacing | allow to replace an existing item. Default: false | boolean | Yes |
| full copy | copy all attributes of the file. Default: false | boolean | Yes |

### Result
- **Description:** the moved file(s)
- **Types:** alias, alias
<a name="fileremove"></a>
```yaml
---
type: command
name: fileremove
suite: Files and folders suite
---
```

## Command: fileremove

**Description:** remove a file synchronously

### Direct Parameter
- **Description:** the file(s) or folder(s) to remove
- **Types:** alias, alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the base url. Relevant if direct parameter is a string or a list of strings. | alias | Yes |
| filesonly | False : delete the item(s) of direct parameter. True : delete only files and handle a folder in the direct parameters as the list of its files. Default: false | boolean | Yes |
| after | allowed only with filesonly true | date | Yes |
| before | allowed only with filesonly true | date | Yes |
| locked files | if true, remove also locked files. Default true | boolean | Yes |
| busy files | if true, unlink busy files. Default true | boolean | Yes |

<a name="filegetname"></a>
```yaml
---
type: command
name: filegetname
suite: Files and folders suite
---
```

## Command: filegetname

**Description:** returns the name of a file

### Direct Parameter
- **Types:** alias, alias
### Result
- **Description:** the file name
- **Types:** string, string
<a name="filerename"></a>
```yaml
---
type: command
name: filerename
suite: Files and folders suite
---
```

## Command: filerename

**Description:** rename a file

### Direct Parameter
- **Types:** alias
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the new file name. | string | No |

### Result
- **Description:** the renamed file
- **Types:** alias
<a name="mkstemp"></a>
```yaml
---
type: command
name: mkstemp
suite: Files and folders suite
---
```

## Command: mkstemp

**Description:** create a new empty file using mkstemp.

### Direct Parameter
- **Description:** the destination folder, or a file path.
- **Types:** alias, posix path
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the template of the file name. mkstemp will create a new file named prefixXXXXXXsuffix where name is prefixsuffix. If missing, the direct parameter must be a file path | string | Yes |
| suffix | the length of the suffix in name (typically the length of the extension+1). Default 0 | integer | Yes |
| wildcards | number of wildcards. Default 6 | integer | Yes |
| mode | the permissions, an integer provided as an octal string. Default: "666" | string | Yes |

### Result
- **Description:** the new file
- **Types:** alias
<a name="mkdtemp"></a>
```yaml
---
type: command
name: mkdtemp
suite: Files and folders suite
---
```

## Command: mkdtemp

**Description:** create a new folder using mkdtemp.

### Direct Parameter
- **Description:** the destination folder, or the full folder path.
- **Types:** alias, posix path
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | the prefix of the folder name. mkdtemp will create a new folder named prefixXXXXXX | string | Yes |
| wildcards | number of wildcards. Default 6 | integer | Yes |
| mode | the permissions, an integer provided as an octal string. Default: "777" | string | Yes |

### Result
- **Description:** the new folder
- **Types:** alias
<a name="chmod"></a>
```yaml
---
type: command
name: chmod
suite: Files and folders suite
---
```

## Command: chmod

**Description:** set and get the access permissions. If the "to" parameter is missing "chmod" simply returns the current permissions

### Direct Parameter
- **Description:** the file or the folder
- **Types:** alias, posix path
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the new permissions, an integer provided as an octal string (1:excecute +2:write+4:read for user, group and others) | string | Yes |

### Result
- **Description:** the previous permissions as an octal string.
- **Types:** string
<a name="alias"></a>
```yaml
---
type: class
name: alias
suite: Files and folders suite
---
```

## Class: alias

<a name="file_specification"></a>
```yaml
---
type: class
name: file specification
suite: Files and folders suite
---
```

## Class: file specification

## Symlink suite

**Description:** None

<a name="create_symlink"></a>
```yaml
---
type: command
name: create symlink
suite: Symlink suite
---
```

## Command: create symlink

**Description:** create a symlink

### Direct Parameter
- **Description:** the target of the new symlink. Can be an alias or a string (an absolute or relative posix path)
- **Types:** alias, posix path
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the folder where to create the symlink | alias | No |
| name | the new file name. Default: the name of the symlink's target | string | Yes |
| replacing | allow to replace an existing symlink. Default: true | boolean | Yes |

<a name="testsymlink"></a>
```yaml
---
type: command
name: testsymlink
suite: Symlink suite
---
```

## Command: testsymlink

**Description:** return true if the direct parameter is a symlink, false otherwise

### Sample Code
### Direct Parameter
- **Description:** don't provide an alias; the symlink will be automatically resolved
- **Types:** url, posix path
### Result
- **Types:** boolean
<a name="readlink"></a>
```yaml
---
type: command
name: readlink
suite: Symlink suite
---
```

## Command: readlink

**Description:** return the contents of a symlink

### Direct Parameter
- **Description:** don't provide an alias; the symlink will be automatically resolved
- **Types:** url, posix path
### Result
- **Types:** string
