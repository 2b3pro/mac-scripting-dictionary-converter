# Filemaker Pro 18: AppleScript/JSX

## Table of Contents

### URL Suite
#### Commands
- [getURL](#geturl)
### Subset of the Core, Table, and Database suites
#### Commands
- [class info](#class_info)
- [close](#close)
- [copy](#copy)
- [count](#count)
- [create](#create)
- [cut](#cut)
- [data size](#data_size)
- [delete](#delete)
- [do menu](#do_menu)
- [do script](#do_script)
- [duplicate](#duplicate)
- [event info](#event_info)
- [exists](#exists)
- [get data](#get_data)
- [open](#open)
- [paste](#paste)
- [print](#print)
- [quit](#quit)
- [redo](#redo)
- [save](#save)
- [set data](#set_data)
- [show](#show)
- [sort](#sort)
- [undo](#undo)
#### Classs
- [application](#application)
- [window](#window)
- [document](#document)
- [database](#database)
- [table](#table)
- [FileMaker script](#filemaker_script)
- [layout](#layout)
- [field](#field)
- [record](#record)
- [cell](#cell)
- [repetition](#repetition)
#### Enumerations
- [tblt](#tblt)
- [prtn](#prtn)
- [accs](#accs)
- [sort](#sort)
- [grup](#grup)
- [lock](#lock)
- [shar](#shar)
- [erpt](#erpt)
- [gust](#gust)
#### Value Types
- [list](#list)
- [type class info](#type_class_info)
- [type event info](#type_event_info)
### FileMaker Suite
#### Commands
- [go to](#go_to)
- [find](#find)
- [get remote URL](#get_remote_url)
#### Classs
- [request](#request)
- [menu item](#menu_item)
- [menu](#menu)
#### Enumerations
- [posi](#posi)
- [kfrm](#kfrm)


## URL Suite

**Description:** Standard Suite for Uniform Resource Locators

<a name="geturl"></a>
```yaml
---
type: command
name: getURL
suite: URL Suite
---
```

## Command: getURL

**Description:** Open a FileMaker Pro Advanced database using a URL specification

### Direct Parameter
- **Description:** The URL specification for the FileMaker Pro Advanced database in the form "[<][URL:]fmp://[[username[:password]@]host]/filename[>]"
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for accounts | opens the file for specific privileges | gust | Yes |

## Subset of the Core, Table, and Database suites

**Description:** Subset of Events supported by other Applications

<a name="class_info"></a>
```yaml
---
type: command
name: class info
suite: Subset of the Core, Table, and Database suites
---
```

## Command: class info

**Description:** Get information about an object class

### Direct Parameter
- **Description:** The object class about which information is requested
- **Types:** type
### Result
- **Description:** A record containing the object’s properties and elements
- **Types:** type class info
<a name="close"></a>
```yaml
---
type: command
name: close
suite: Subset of the Core, Table, and Database suites
---
```

## Command: close

**Description:** Close an object

### Direct Parameter
- **Description:** The object to close
- **Types:** specifier
<a name="copy"></a>
```yaml
---
type: command
name: copy
suite: Subset of the Core, Table, and Database suites
---
```

## Command: copy

**Description:** Copy an object to the clipboard

<a name="count"></a>
```yaml
---
type: command
name: count
suite: Subset of the Core, Table, and Database suites
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
| class | The class of the elements to be counted | type | No |

### Result
- **Description:** The number of elements
- **Types:** integer
<a name="create"></a>
```yaml
---
type: command
name: create
suite: Subset of the Core, Table, and Database suites
---
```

## Command: create

**Description:** Create a new element

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new element | type | No |
| at | The location at which to insert the element | location specifier | Yes |
| with data | The initial data for the element | any | Yes |
| with properties | The initial data for the properties of the element | record | Yes |

### Result
- **Description:** To the new object(s)
- **Types:** specifier
<a name="cut"></a>
```yaml
---
type: command
name: cut
suite: Subset of the Core, Table, and Database suites
---
```

## Command: cut

**Description:** Cut an object to the clipboard

<a name="data_size"></a>
```yaml
---
type: command
name: data size
suite: Subset of the Core, Table, and Database suites
---
```

## Command: data size

**Description:** Return the size in bytes of an object

### Direct Parameter
- **Description:** The object whose data size is to be returned
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | The data type for which the size is calculated | type | Yes |

### Result
- **Description:** The size of the object in bytes
- **Types:** integer
<a name="delete"></a>
```yaml
---
type: command
name: delete
suite: Subset of the Core, Table, and Database suites
---
```

## Command: delete

**Description:** Delete an element from an object

### Direct Parameter
- **Description:** The element to delete
- **Types:** specifier
<a name="do_menu"></a>
```yaml
---
type: command
name: do menu
suite: Subset of the Core, Table, and Database suites
---
```

## Command: do menu

**Description:** Execute a menu command

### Direct Parameter
- **Description:** This denotes both the menu ID and the menu item
- **Types:** any
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| menu named | The name of the menu item | text | Yes |

### Result
- **Description:** Result of menu selection
- **Types:** any
<a name="do_script"></a>
```yaml
---
type: command
name: do script
suite: Subset of the Core, Table, and Database suites
---
```

## Command: do script

**Description:** Execute a script

### Direct Parameter
- **Description:** The name or specifier of the FileMaker script to be executed
- **Types:** text
### Result
- **Description:** The result of the Script
- **Types:** any
<a name="duplicate"></a>
```yaml
---
type: command
name: duplicate
suite: Subset of the Core, Table, and Database suites
---
```

## Command: duplicate

**Description:** Duplicate an object

### Direct Parameter
- **Description:** The object to copy
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new location for the object | location specifier | Yes |

### Result
- **Description:** To the duplicated object(s)
- **Types:** specifier
<a name="event_info"></a>
```yaml
---
type: command
name: event info
suite: Subset of the Core, Table, and Database suites
---
```

## Command: event info

**Description:** Get information about the Apple events in a suite

### Direct Parameter
- **Description:** The event class of the Apple events for which to return information
- **Types:** type
### Result
- **Description:** A record containing the events and their parameters
- **Types:** type event info
<a name="exists"></a>
```yaml
---
type: command
name: exists
suite: Subset of the Core, Table, and Database suites
---
```

## Command: exists

**Description:** Tell if an object exists

### Direct Parameter
- **Description:** The object in question
- **Types:** specifier
### Result
- **Description:** True if it exists, false if not
- **Types:** boolean
<a name="get_data"></a>
```yaml
---
type: command
name: get data
suite: Subset of the Core, Table, and Database suites
---
```

## Command: get data

**Description:** Get the data for an object

### Direct Parameter
- **Description:** The object whose data is to be returned
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | The desired types for the data, in order of preference | type | Yes |

### Result
- **Types:** any
<a name="open"></a>
```yaml
---
type: command
name: open
suite: Subset of the Core, Table, and Database suites
---
```

## Command: open

**Description:** Open an object

### Direct Parameter
- **Description:** The object to open
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with passwords | The password to use | text | Yes |
| for Accounts | The account name | text | Yes |

<a name="paste"></a>
```yaml
---
type: command
name: paste
suite: Subset of the Core, Table, and Database suites
---
```

## Command: paste

**Description:** Paste an object from the clipboard

<a name="print"></a>
```yaml
---
type: command
name: print
suite: Subset of the Core, Table, and Database suites
---
```

## Command: print

**Description:** Print an object

### Direct Parameter
- **Description:** The object to print
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with password | The password to use | text | Yes |
| for Accounts | The account name | text | Yes |
| from page | start page | integer | Yes |
| to page | end page | integer | Yes |
| with copies | number of copies | integer | Yes |

<a name="quit"></a>
```yaml
---
type: command
name: quit
suite: Subset of the Core, Table, and Database suites
---
```

## Command: quit

**Description:** Perform tasks before termination, then terminate

<a name="redo"></a>
```yaml
---
type: command
name: redo
suite: Subset of the Core, Table, and Database suites
---
```

## Command: redo

**Description:** Reverse the action of the immediately preceding undo

<a name="save"></a>
```yaml
---
type: command
name: save
suite: Subset of the Core, Table, and Database suites
---
```

## Command: save

**Description:** Save an object

### Direct Parameter
- **Description:** The object to save
- **Types:** specifier
<a name="set_data"></a>
```yaml
---
type: command
name: set data
suite: Subset of the Core, Table, and Database suites
---
```

## Command: set data

**Description:** Set an object's data

### Direct Parameter
- **Description:** The object to change
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new value | any | No |

<a name="show"></a>
```yaml
---
type: command
name: show
suite: Subset of the Core, Table, and Database suites
---
```

## Command: show

**Description:** Bring an object into view

### Direct Parameter
- **Description:** The object to be made visible
- **Types:** specifier
<a name="sort"></a>
```yaml
---
type: command
name: sort
suite: Subset of the Core, Table, and Database suites
---
```

## Command: sort

**Description:** Sort the records in a layout

### Direct Parameter
- **Description:** The layout to sort
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | The fields to sort by | specifier | Yes |
| in order | The sort type | sort | Yes |

<a name="undo"></a>
```yaml
---
type: command
name: undo
suite: Subset of the Core, Table, and Database suites
---
```

## Command: undo

**Description:** Undo the action of the previous event or user interaction

<a name="application"></a>
```yaml
---
type: class
name: application
suite: Subset of the Core, Table, and Database suites
---
```

## Class: application

**Description:** The application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| frontmost | Is this the frontmost application? | boolean | r |
| name | The name of the application | text | r |
| version | The version of the application | text | r |

### Elements
- **Type:** document
- **Type:** window
- **Type:** database
- **Type:** menu
<a name="window"></a>
```yaml
---
type: class
name: window
suite: Subset of the Core, Table, and Database suites
---
```

## Class: window

**Description:** A FileMaker Pro Advanced document window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the window | text | r |
| bounds | The bounding rectangle of the window | rectangle | read/write |
| visible | Is the window visible? | boolean | read/write |
| index | The number of the window | integer | r |
| floating | Does the window float? | boolean | r |
| zoomable | Is the window zoomable? | boolean | r |
| zoomed | Is the window zoomed? | boolean | read/write |
| modal | Is the window modal? | boolean | r |
| resizable | Is the window resizable? | boolean | r |
| has close box | Does the window have a close box? | boolean | r |
| has title bar | Does the window have a title bar? | boolean | r |
| current layout | The current layout | layout | read/write |
| current record | The current record | record | read/write |
| current table | The current table | table | read/write |
| current cell | The current cell | cell | read/write |

### Elements
- **Type:** layout
<a name="document"></a>
```yaml
---
type: class
name: document
suite: Subset of the Core, Table, and Database suites
---
```

## Class: document

**Description:** A FileMaker Pro Advanced document

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the document | text | r |
| modified | True if the document has been modified | boolean | r |

### Elements
- **Type:** window
- **Type:** FileMaker script
- **Type:** layout
- **Type:** table
<a name="database"></a>
```yaml
---
type: class
name: database
suite: Subset of the Core, Table, and Database suites
---
```

## Class: database

**Description:** A FileMaker Pro Advanced database

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the database | text | r |
| multiuser | If true, users have access to the database over the network | shar | read/write |

### Elements
- **Type:** table
- **Type:** layout
- **Type:** FileMaker script
<a name="table"></a>
```yaml
---
type: class
name: table
suite: Subset of the Core, Table, and Database suites
---
```

## Class: table

**Description:** A FileMaker Pro Advanced table

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the database | text | r |
| lock | The current session's lock on the database | lock | r |
| access | The access privileges | accs | r |

### Elements
- **Type:** field
- **Type:** record
- **Type:** cell
<a name="filemaker_script"></a>
```yaml
---
type: class
name: FileMaker script
suite: Subset of the Core, Table, and Database suites
---
```

## Class: FileMaker script

**Description:** A FileMaker script

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the FileMaker Script | text | r |
| ID | The unique ID of the FileMaker Script | real | r |

<a name="layout"></a>
```yaml
---
type: class
name: layout
suite: Subset of the Core, Table, and Database suites
---
```

## Class: layout

**Description:** A FileMaker Pro Advanced layout

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the layout | text | r |
| ID | The unique ID of the layout | real | r |
| access | The access privileges of the layout | accs | r |
| protection | Indicates whether the formulas of the cells in the layout can be changed | prtn | r |
| lock | The lock on the layout | lock | r |
| kind | The kind of layout (View = FileMaker Pro Advanced layout, table = all fields for table) | tblt | r |
| visible | Is the layout visible in the layouts menu? | boolean | r |

### Elements
- **Type:** field
- **Type:** record
- **Type:** cell
- **Type:** request
<a name="field"></a>
```yaml
---
type: class
name: field
suite: Subset of the Core, Table, and Database suites
---
```

## Class: field

**Description:** A FileMaker Pro Advanced field

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| choices | The value list for the field | list | r |
| access | The access privileges for the field | accs | r |
| formula | The field's calculation formula | text | r |
| ID | The unique ID of the field | real | r |
| lock | The lock status of the field | lock | r |
| name | The name of the field | text | r |
| nulls OK | Is this field allowed to be empty? | boolean | r |
| protection | The protection of this field | prtn | r |
| repeats | Is this a repeating field? | erpt | r |
| repeat size | Maximum number of repetitions of the field | integer | r |
| unique value | Must this field contain unique values? | boolean | r |
| globalValue | Is this field a global field? | boolean | r |

### Elements
- **Type:** cell
- **Type:** repetition
<a name="record"></a>
```yaml
---
type: class
name: record
suite: Subset of the Core, Table, and Database suites
---
```

## Class: record

**Description:** A FileMaker Pro Advanced record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the record | text | r |
| ID | The unique ID of the record | real | r |
| lock | The lock for the record | lock | r |
| protection | Indicates whether the formulas of the cells in the record can be changed | prtn | r |
| access | Indicates the access privileges for the record | accs | r |

### Elements
- **Type:** cell
<a name="cell"></a>
```yaml
---
type: class
name: cell
suite: Subset of the Core, Table, and Database suites
---
```

## Class: cell

**Description:** A field value in a record or request

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| choices | The value list for the cell | list | r |
| formula | The cell's calculation formula | text | r |
| lock | The lock status of the cell | lock | r |
| name | The cell's name | text | r |
| protection | The protection of this cell | prtn | r |
| cellValue | The cell value | text | read/write |
| ID | The unique ID of the cell (the first element is the record ID, the second element is the cell ID) | list | r |
| repeat size | Number of repetitions of the cell | integer | r |
| globalValue | Is this cell a global cell? | boolean | r |
| access | The access privileges | accs | r |

### Elements
- **Type:** repetition
<a name="repetition"></a>
```yaml
---
type: class
name: repetition
suite: Subset of the Core, Table, and Database suites
---
```

## Class: repetition

**Description:** A repetition value from a cell

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| choices | The value list for the cell | list | r |
| formula | The cell's calculation formula | text | r |
| lock | The lock status of the cell | lock | r |
| name | The cell's name | text | r |
| protection | The protection of this cell | prtn | r |
| cellValue | The cell value | text | read/write |
| ID | The unique ID of the cell (the first element is the record ID, the second element is the cell ID) | list | r |
| globalValue | Is this cell a global cell? | boolean | r |

<a name="tblt"></a>
```yaml
---
type: enumeration
name: tblt
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: tblt

### Enumerators
| Name | Description |
|---|---|
| table | A table |
| view | A layout or view |

<a name="prtn"></a>
```yaml
---
type: enumeration
name: prtn
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: prtn

### Enumerators
| Name | Description |
|---|---|
| read only | Can't change values or formulas |
| formulas protected | Can changes values but not formulas |
| read/write | Can change values and formulas |

<a name="accs"></a>
```yaml
---
type: enumeration
name: accs
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: accs

### Enumerators
| Name | Description |
|---|---|
| no access | No access |
| read | Read only access |
| write | Write only access |
| update | Update access |
| create | Create access |
| delete | Delete access |
| read/write | Read/Write access |
| read/update | Read/Update access |
| read/create | Read/Create access |
| read/delete | Read/Delete access |
| write/update | Write/Update access |
| write/create | Write/Create access |
| write/delete | Write/Delete access |
| update/create | Update/Create access |
| update/delete | Update/Delete access |
| create/delete | Create/Delete access |
| read/write/update | Read/Write/Update access |
| read/write/create | Read/Write/Create access |
| read/write/delete | Read/Write/Delete access |
| write/update/create | Write/Update/Create access |
| write/update/delete | Write/Update/Delete access |
| update/create/delete | Update/Create/Delete access |
| read/create/delete | Read/Create/Delete access |
| read/update/delete | Read/Update/Delete access |
| write/create/delete | Write/Create/Delete access |
| read/update/create | Read/Update/Create access |
| no delete | No delete access |
| no create | no create access |
| no update | No update access |
| no read | No read access |
| no write | No write access |
| full | Full access |

<a name="sort"></a>
```yaml
---
type: enumeration
name: sort
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: sort

### Enumerators
| Name | Description |
|---|---|
| ascending | Ascending sort order |
| descending | Descending sort order |
| custom | Custom sort order |

<a name="grup"></a>
```yaml
---
type: enumeration
name: grup
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: grup

### Enumerators
| Name | Description |
|---|---|
| sum | Summarize sum of elements |
| count | Summarize count of elements |
| mean | Summarize mean of elements |
| standard deviation | Summarize standard deviation of elements |
| average | Summarize average of elements |
| minimum | Summarize the minimum of the elements |
| maximum | Summarize the maximum of the elements |

<a name="lock"></a>
```yaml
---
type: enumeration
name: lock
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: lock

### Enumerators
| Name | Description |
|---|---|
| unlocked | Not currently locked |
| shared lock | A multiple reader lock |
| exclusive lock | A read/write lock |

<a name="shar"></a>
```yaml
---
type: enumeration
name: shar
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: shar

### Enumerators
| Name | Description |
|---|---|
| false | single user |
| sharing hidden | To share this file, but suppress its display in the Hosts dialog |
| true | To share this file, and display it in the Hosts dialog |

<a name="erpt"></a>
```yaml
---
type: enumeration
name: erpt
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: erpt

### Enumerators
| Name | Description |
|---|---|
| single | single repetition field |
| repeated | multiple repeatition field |

<a name="gust"></a>
```yaml
---
type: enumeration
name: gust
suite: Subset of the Core, Table, and Database suites
---
```

## Enumeration: gust

### Enumerators
| Name | Description |
|---|---|
| guest | guest account |

<a name="list"></a>
```yaml
---
type: value-type
name: list
suite: Subset of the Core, Table, and Database suites
---
```

## Value Type: list

<a name="type_class_info"></a>
```yaml
---
type: value-type
name: type class info
suite: Subset of the Core, Table, and Database suites
---
```

## Value Type: type class info

<a name="type_event_info"></a>
```yaml
---
type: value-type
name: type event info
suite: Subset of the Core, Table, and Database suites
---
```

## Value Type: type event info

## FileMaker Suite

**Description:** FileMaker Pro Advanced-specific events and objects

<a name="go_to"></a>
```yaml
---
type: command
name: go to
suite: FileMaker Suite
---
```

## Command: go to

**Description:** Go to an object

### Direct Parameter
- **Description:** The object to which to go
- **Types:** specifier
<a name="find"></a>
```yaml
---
type: command
name: find
suite: FileMaker Suite
---
```

## Command: find

**Description:** Perform a FileMaker Pro Advanced Find given current requests

### Direct Parameter
- **Description:** The window in which to find
- **Types:** specifier
<a name="get_remote_url"></a>
```yaml
---
type: command
name: get remote URL
suite: FileMaker Suite
---
```

## Command: get remote URL

**Description:** Opens a hosted FileMaker Pro Advanced database

### Result
- **Description:** The URL specification for the opened database in the form "fmp://host/filename"
- **Types:** text
<a name="request"></a>
```yaml
---
type: class
name: request
suite: FileMaker Suite
---
```

## Class: request

**Description:** A FileMaker Pro Advanced find request

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the find request | text | r |
| ID | The unique ID of the find request | real | r |
| omitted | True if the request is to be omitted | boolean | read/write |

### Elements
- **Type:** cell
<a name="menu_item"></a>
```yaml
---
type: class
name: menu item
suite: FileMaker Suite
---
```

## Class: menu item

**Description:** A menu item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the menu item | text | read/write |
| enabled | Is the menu item enabled? | boolean | read/write |
| item number | The menu item number | integer | r |
| checked | Is the menu item checked? | boolean | read/write |

<a name="menu"></a>
```yaml
---
type: class
name: menu
suite: FileMaker Suite
---
```

## Class: menu

**Description:** A menu

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| best type | The best descriptor type | type | r |
| class | The class | type | r |
| default type | The default descriptor type | type | r |
| name | The name of the menu | text | read/write |
| ID | The resource ID of the menu | integer | r |
| enabled | Is the menu enabled? | boolean | read/write |

### Elements
- **Type:** menu item
- **Type:** menu
<a name="posi"></a>
```yaml
---
type: enumeration
name: posi
suite: FileMaker Suite
---
```

## Enumeration: posi

### Enumerators
| Name | Description |
|---|---|
| before | Before specified object |
| after | After specified object |
| beginning | At the beginning of the specified container |
| end | At the end of the specified container |
| replace | Replacing the specified object |

<a name="kfrm"></a>
```yaml
---
type: enumeration
name: kfrm
suite: FileMaker Suite
---
```

## Enumeration: kfrm

### Enumerators
| Name | Description |
|---|---|
| index | Keyform designating indexed access |
| named | Keyform designating named access |
| ID | Keyform designating identifier access |

