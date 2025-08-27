# SiteSucker Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [open](#open)
- [close](#close)
- [quit](#quit)
- [count](#count)
- [get](#get)
- [save](#save)
- [set](#set)
- [exists](#exists)
- [make](#make)
#### Classs
- [application](#application)
- [window](#window)
- [preferences](#preferences)
#### Enumerations
- [save options](#save_options)
### SiteSucker suite
#### Commands
- [download](#download)
- [stop](#stop)
- [next](#next)
- [pause](#pause)
- [resume](#resume)
- [reset](#reset)
- [load](#load)
#### Classs
- [document](#document)
- [settings](#settings)
#### Enumerations
- [LDIR](#ldir)
- [FTYP](#ftyp)
- [tLOG](#tlog)
- [tREP](#trep)
- [Phtm](#phtm)
- [DEFA](#defa)
- [TPTY](#tpty)
#### Record Types
- [url record](#url_record)
- [pattern record](#pattern_record)
- [path replacement record](#path_replacement_record)
- [media type replacement record](#media_type_replacement_record)
- [size record](#size_record)


## Standard Suite

**Description:** Common terms for most applications

<a name="open"></a>
```yaml
---
type: command
name: open
suite: Standard Suite
---
```

## Command: open

**Description:** Open a document

### Direct Parameter
- **Description:** The file(s) to open
- **Types:** file
<a name="close"></a>
```yaml
---
type: command
name: close
suite: Standard Suite
---
```

## Command: close

**Description:** Close a document

### Direct Parameter
- **Description:** The document(s) or window(s) to close
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Specifies whether changes should be saved before closing. | save options | Yes |

<a name="quit"></a>
```yaml
---
type: command
name: quit
suite: Standard Suite
---
```

## Command: quit

**Description:** Quit the application

<a name="count"></a>
```yaml
---
type: command
name: count
suite: Standard Suite
---
```

## Command: count

**Description:** Return the number of elements of a particular class within an object

### Direct Parameter
- **Description:** The object whose elements are to be counted
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| each | The class of objects to be counted | type | Yes |

### Result
- **Description:** The number of elements
- **Types:** integer
<a name="get"></a>
```yaml
---
type: command
name: get
suite: Standard Suite
---
```

## Command: get

**Description:** Get the data for an object

### Direct Parameter
- **Description:** The object whose data is to be returned
- **Types:** specifier
### Result
- **Description:** The data from the object
- **Types:** any
<a name="save"></a>
```yaml
---
type: command
name: save
suite: Standard Suite
---
```

## Command: save

**Description:** Save an object

### Direct Parameter
- **Description:** The object to save, usually a document or settings
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The file in which to save the data | file | Yes |

<a name="set"></a>
```yaml
---
type: command
name: set
suite: Standard Suite
---
```

## Command: set

**Description:** Set an object's data

### Direct Parameter
- **Description:** The object to change
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new value | any | No |

<a name="exists"></a>
```yaml
---
type: command
name: exists
suite: Standard Suite
---
```

## Command: exists

**Description:** Verify if an object exists

### Direct Parameter
- **Description:** The object in question
- **Types:** any
### Result
- **Description:** True if it exists, false if not
- **Types:** boolean
<a name="make"></a>
```yaml
---
type: command
name: make
suite: Standard Suite
---
```

## Command: make

**Description:** Make a new object

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new object | type | No |
| at | The location at which to insert the object | location specifier | Yes |
| with data | The initial contents of the object | any | Yes |
| with properties | The initial values for properties of the object | record | Yes |

### Result
- **Description:** The new object
- **Types:** specifier
<a name="application"></a>
```yaml
---
type: class
name: application
suite: Standard Suite
---
```

## Class: application

**Description:** An application's top-level scripting object

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the application | text | r |
| frontmost | Is this the frontmost (active) application? | boolean | r |
| version | The version of the application | text | r |
| prefs | The application preferences | preferences | r |

### Elements
- **Type:** document
- **Type:** window
### Responds To
- **Command:** None
- **Command:** None
<a name="window"></a>
```yaml
---
type: class
name: window
suite: Standard Suite
---
```

## Class: window

**Description:** A window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The full title of the window. | text | r |
| id | The unique identifier of the window | integer | r |
| index | The index of the window, ordered front to back | integer | read/write |
| bounds | The bounding rectangle of the window | rectangle | read/write |
| closeable | Does the window have a close box? | boolean | r |
| miniaturizable | Can the window be miniaturized? | boolean | r |
| miniaturized | Is the window currently miniaturized? | boolean | read/write |
| resizable | Can the window be resized? | boolean | r |
| visible | Is the window currently visible? | boolean | read/write |
| zoomable | Can the window be zoomed? | boolean | r |
| zoomed | Is the window currently zoomed? | boolean | read/write |
| document | The document whose contents are being displayed in the window | document | r |

### Responds To
- **Command:** None
<a name="preferences"></a>
```yaml
---
type: class
name: preferences
suite: Standard Suite
---
```

## Class: preferences

**Description:** The application preferences

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| source of bookmarks | Web browser from which bookmarks should be read | text | read/write |
| clear changes | Clear document's dirty flag when download ends? | boolean | read/write |
| delete robots | Delete robots.txt files when download ends? | boolean | read/write |
| drag triggers download | Automatically start downloading after a string or file is dragged into the URL text field? | boolean | read/write |

<a name="save_options"></a>
```yaml
---
type: enumeration
name: save options
suite: Standard Suite
---
```

## Enumeration: save options

### Enumerators
| Name | Description |
|---|---|
| yes | Save the file. |
| no | Do not save the file. |
| ask | Ask the user whether or not to save the file. |

## SiteSucker suite

**Description:** Commands and terms used by SiteSucker

<a name="download"></a>
```yaml
---
type: command
name: download
suite: SiteSucker suite
---
```

## Command: download

**Description:** Downloads a URL

### Direct Parameter
- **Description:** The URL to download; if unspecified, the URL in the document
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The document affected; if unspecified, the front document | document | Yes |
| queuing | If true, the URL is added to the queue; if false, the URL is downloaded on the second level; only relevant if currently downloading; default value is true | boolean | Yes |

<a name="stop"></a>
```yaml
---
type: command
name: stop
suite: SiteSucker suite
---
```

## Command: stop

**Description:** Stops the download

### Direct Parameter
- **Description:** The document affected; if unspecified, the front document
- **Types:** document
<a name="next"></a>
```yaml
---
type: command
name: next
suite: SiteSucker suite
---
```

## Command: next

**Description:** Stops the current download and begins downloading the next URL in the queue

### Direct Parameter
- **Description:** The document affected; if unspecified, the front document
- **Types:** document
<a name="pause"></a>
```yaml
---
type: command
name: pause
suite: SiteSucker suite
---
```

## Command: pause

**Description:** Pauses the download

### Direct Parameter
- **Description:** The document affected; if unspecified, the front document
- **Types:** document
<a name="resume"></a>
```yaml
---
type: command
name: resume
suite: SiteSucker suite
---
```

## Command: resume

**Description:** Resumes the download

### Direct Parameter
- **Description:** The document affected; if unspecified, the front document
- **Types:** document
<a name="reset"></a>
```yaml
---
type: command
name: reset
suite: SiteSucker suite
---
```

## Command: reset

**Description:** Resets a document's settings to the defaults

### Direct Parameter
- **Description:** The settings to reset
- **Types:** settings
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | Specifies whether to use user or factory defaults; if unspecified, user defaults are used | DEFA | Yes |

<a name="load"></a>
```yaml
---
type: command
name: load
suite: SiteSucker suite
---
```

## Command: load

**Description:** Loads a document's settings from a file

### Direct Parameter
- **Description:** The settings to replace
- **Types:** settings
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | The name of the settings file to load | text | No |

<a name="document"></a>
```yaml
---
type: class
name: document
suite: SiteSucker suite
---
```

## Class: document

**Description:** A SiteSucker document

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The document's name | text | r |
| modified | Has it been modified since the last save? | boolean | r |
| path | Its location on disk, if it has one, as a POSIX path string. | text | r |
| URL | The URL shown in the document | text | read/write |
| settings | The settings | settings | r |
| downloading | Is SiteSucker downloading? | boolean | r |
| paused | Is SiteSucker paused? | boolean | r |
| level | The level | integer | r |
| files downloaded | The number of files downloaded | integer | r |
| files remaining | The number of files remaining | integer | r |
| errors | The number of errors | integer | r |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="settings"></a>
```yaml
---
type: class
name: settings
suite: SiteSucker suite
---
```

## Class: settings

**Description:** The settings

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| ignore robot exclusions | Ignore the robots.txt exclusions and the Robots META tag | boolean | read/write |
| ignore rel equals nofollow | Ignore rel="nofollow" in tags | boolean | read/write |
| include supporting files | Include supporting files in the download | boolean | read/write |
| always download html and css | Always download HTML and CSS despite File Replacement setting | boolean | read/write |
| download error pages | Download error pages | boolean | read/write |
| ask for destination | Ask for the destination before downloading | boolean | read/write |
| connections | Number of simultaneous connections | integer | read/write |
| login dialog | When to display the login dialog for basic HTTP authentication | tLOG | read/write |
| file replacement | When to replace existing files | tREP | read/write |
| file modification | How to modify downloaded files | Phtm | read/write |
| destination | The local folder where downloaded files are saved | file | read/write |
| log errors | Write errors to a log file | boolean | read/write |
| log warnings | Write warnings to a log file | boolean | read/write |
| log final status | Write final status information to a log file | boolean | read/write |
| log media types | Write media types to a log file | boolean | read/write |
| log history | Write download history to a log file | boolean | read/write |
| limit levels | Limit the maximum number of levels to download | boolean | read/write |
| max levels | The maximum number of levels to download | integer | read/write |
| limit files | Limit the maximum number of files to download | boolean | read/write |
| max files | The maximum number of files to download | integer | read/write |
| limit min file size | Limit the minimum file size of files to download | boolean | read/write |
| min file size | The size in kilobytes of the smallest data file to download | integer | read/write |
| limit max file size | Limit the maximum file size of files to download | boolean | read/write |
| max file size | The size in kilobytes of the largest data file to download | integer | read/write |
| limit min image size | Limit the minimum size of downloaded images | boolean | read/write |
| min image size | The minimum image size as a percentage of the main screen area | integer | read/write |
| identity | The user-agent identity | text | read/write |
| download attempts | The number of times to try to download a file | integer | read/write |
| download timeout | The number of seconds to wait for a response from the server | integer | read/write |
| download delay | The number of seconds to delay between requests | real | read/write |
| delay range | A percentage that specifies a range of randomized delay values | integer | read/write |
| check all links | Check all links in all downloaded HTML files | boolean | read/write |
| scan comments for urls | Scan comments for URLs | boolean | read/write |
| treat ambiguous URLs as folders | Treat URLs that do not end with a '/' or extension as folders | boolean | read/write |
| download links in PDFs | Download links in PDFs | boolean | read/write |
| url constraint | Limit downloaded files by URL | LDIR | read/write |
| urls to include | List of urls to include in the download | url record | read/write |
| urls to exclude | List of urls to exclude from the download | url record | read/write |
| ignore filename in headers | Ignore the filename directive in all HTTP Content-Disposition headers | boolean | read/write |
| replace special characters with underscore | Replace special characters with ‘_’ | boolean | read/write |
| paths to replace | List of paths to replace | path replacement record | read/write |
| text encoding | The text encoding to use for HTML files | text | read/write |
| download using web views | Download HTML using hidden web views | boolean | read/write |
| create PDF | Download a site as a single PDF document | boolean | read/write |
| add headers and footers | Add headers and footers to the PDF document | boolean | read/write |
| save delay | The number of seconds to delay before saving the webpage | real | read/write |
| web view size | The web view size (must match the size associated with a web view size menu item) | size record | read/write |
| custom data attributes | List of custom data attributes that SiteSucker should scan | text | read/write |
| patterns | List of patterns | pattern record | read/write |
| javascript | JavaScript to run after webpage finishes loading | text | read/write |
| file types option | Restrict the download by file type | FTYP | read/write |
| filter archives | Include or exclude archives in the download | boolean | read/write |
| filter audio files | Include or exclude audio files in the download | boolean | read/write |
| filter images | Include or exclude images in the download | boolean | read/write |
| filter custom types | Include or exclude files with the given media type in the download | boolean | read/write |
| custom types | List of media types to include or exclude | text | read/write |
| html types | List of media types that SiteSucker should treat as HTML | text | read/write |
| media type replacement | List of media types that should be assigned to URLs matching the specified pattern | media type replacement record | read/write |
| preanalysis script | Name of the script to run before analysis (use "" for none) | text | read/write |
| postanalysis script | Name of the script to run after analysis (use "" for none) | text | read/write |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
<a name="ldir"></a>
```yaml
---
type: enumeration
name: LDIR
suite: SiteSucker suite
---
```

## Enumeration: LDIR

### Enumerators
| Name | Description |
|---|---|
| no constraint | None |
| host | None |
| host plus one | None |
| subdomains | None |
| directory | None |
| url settings | None |

<a name="ftyp"></a>
```yaml
---
type: enumeration
name: FTYP
suite: SiteSucker suite
---
```

## Enumeration: FTYP

### Enumerators
| Name | Description |
|---|---|
| allow all file types | None |
| allow specified file types | None |
| disallow specified file types | None |

<a name="tlog"></a>
```yaml
---
type: enumeration
name: tLOG
suite: SiteSucker suite
---
```

## Enumeration: tLOG

### Enumerators
| Name | Description |
|---|---|
| never display | None |
| always display | None |
| display when necessary | None |

<a name="trep"></a>
```yaml
---
type: enumeration
name: tREP
suite: SiteSucker suite
---
```

## Enumeration: tREP

### Enumerators
| Name | Description |
|---|---|
| never replace | None |
| always replace | None |
| with newer | None |

<a name="phtm"></a>
```yaml
---
type: enumeration
name: Phtm
suite: SiteSucker suite
---
```

## Enumeration: Phtm

### Enumerators
| Name | Description |
|---|---|
| no modification | None |
| localize | None |
| delete after analysis | None |

<a name="defa"></a>
```yaml
---
type: enumeration
name: DEFA
suite: SiteSucker suite
---
```

## Enumeration: DEFA

### Enumerators
| Name | Description |
|---|---|
| user defaults | None |
| factory defaults | None |

<a name="tpty"></a>
```yaml
---
type: enumeration
name: TPTY
suite: SiteSucker suite
---
```

## Enumeration: TPTY

### Enumerators
| Name | Description |
|---|---|
| substitute early | None |
| substitute late | None |
| extract URL | None |
| include URL | None |
| exclude URL | None |
| retry if found | None |
| retry if missing | None |

<a name="url_record"></a>
```yaml
---
type: record-type
name: url record
suite: SiteSucker suite
---
```

## Record Type: url record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| regex | Is the path a regular expression? | boolean | read/write |
| url or pattern | Absolute URL or regular expression pattern | text | read/write |

<a name="pattern_record"></a>
```yaml
---
type: record-type
name: pattern record
suite: SiteSucker suite
---
```

## Record Type: pattern record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| search pattern | Regular expression pattern to match | text | read/write |
| template | Template specifying how to replace text or extract URLs | text | read/write |
| action | Action to be performed | TPTY | read/write |

<a name="path_replacement_record"></a>
```yaml
---
type: record-type
name: path replacement record
suite: SiteSucker suite
---
```

## Record Type: path replacement record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file path pattern | Regular expression pattern to match | text | read/write |
| template | Template specifying how to replace matching instances | text | read/write |

<a name="media_type_replacement_record"></a>
```yaml
---
type: record-type
name: media type replacement record
suite: SiteSucker suite
---
```

## Record Type: media type replacement record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| URL pattern | Regular expression pattern to match | text | read/write |
| media type | Media type to use for matching instances | text | read/write |

<a name="size_record"></a>
```yaml
---
type: record-type
name: size record
suite: SiteSucker suite
---
```

## Record Type: size record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| width | The width | integer | read/write |
| height | The height | integer | read/write |

