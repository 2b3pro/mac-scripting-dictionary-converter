# Numbers Terminology: AppleScript/JSX

## Table of Contents

### iWork Text Suite
#### Classs
- [rich text](#rich_text)
- [character](#character)
- [paragraph](#paragraph)
- [word](#word)
#### Value Types
- [color](#color)
### iWork Suite
#### Commands
- [set](#set)
- [delete](#delete)
- [make](#make)
- [clear](#clear)
- [merge](#merge)
- [sort](#sort)
- [unmerge](#unmerge)
- [set password](#set_password)
- [remove password](#remove_password)
#### Classs
- [iWork container](#iwork_container)
- [iWork item](#iwork_item)
- [audio clip](#audio_clip)
- [shape](#shape)
- [chart](#chart)
- [image](#image)
- [group](#group)
- [line](#line)
- [movie](#movie)
- [table](#table)
- [text item](#text_item)
- [range](#range)
- [cell](#cell)
- [row](#row)
- [column](#column)
#### Enumerations
- [tAVT](#tavt)
- [tAHT](#taht)
- [NMSD](#nmsd)
- [NMCT](#nmct)
- [item fill options](#item_fill_options)
- [playback repetition method](#playback_repetition_method)
#### Class Extensions
- [document](#document)
### Numbers Suite
#### Commands
- [transpose](#transpose)
- [export](#export)
#### Classs
- [sheet](#sheet)
- [template](#template)
#### Enumerations
- [saveable file format](#saveable_file_format)
- [export format](#export_format)
- [image quality](#image_quality)
#### Record Types
- [export options](#export_options)
#### Class Extensions
- [application](#application)
- [document](#document)
- [table](#table)
### Compatibility Suite
#### Commands
- [add column after](#add_column_after)
- [add column before](#add_column_before)
- [add row above](#add_row_above)
- [add row below](#add_row_below)
- [remove](#remove)
#### Class Extensions
- [range](#range)
- [row](#row)
- [column](#column)


## iWork Text Suite

**Description:** Classes and commands for iWorks text objects.

<a name="rich_text"></a>
```yaml
---
type: class
name: rich text
suite: iWork Text Suite
---
```

## Class: rich text

**Description:** This provides the base rich text class for all iWork applications.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the font. Expressed as an RGB value consisting of a list of three color values from 0 to 65535. ex: Blue = {0, 0, 65535}. | color | read/write |
| font | The name of the font.  Can be the PostScript name, such as: “TimesNewRomanPS-ItalicMT”, or display name: “Times New Roman Italic”. TIP: Use the Font Book application get the information about a typeface. | text | read/write |
| size | The size of the font. | real | read/write |

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
<a name="character"></a>
```yaml
---
type: class
name: character
suite: iWork Text Suite
---
```

## Class: character

**Description:** One of some text's characters.

**Inherits:** rich text

<a name="paragraph"></a>
```yaml
---
type: class
name: paragraph
suite: iWork Text Suite
---
```

## Class: paragraph

**Description:** One of some text's paragraphs.

**Inherits:** rich text

### Elements
- **Type:** character
- **Type:** word
<a name="word"></a>
```yaml
---
type: class
name: word
suite: iWork Text Suite
---
```

## Class: word

**Description:** One of some text's words.

**Inherits:** rich text

### Elements
- **Type:** character
<a name="color"></a>
```yaml
---
type: value-type
name: color
suite: iWork Text Suite
---
```

## Value Type: color

## iWork Suite

**Description:** A set of basic classes for iWork applications.

<a name="set"></a>
```yaml
---
type: command
name: set
suite: iWork Suite
---
```

## Command: set

**Description:** Sets the value of the specified object(s).

### Direct Parameter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new value. | any | No |

<a name="delete"></a>
```yaml
---
type: command
name: delete
suite: iWork Suite
---
```

## Command: delete

**Description:** Delete an object.

### Direct Parameter
- **Types:** specifier
<a name="make"></a>
```yaml
---
type: command
name: make
suite: iWork Suite
---
```

## Command: make

**Description:** Create a new object.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new object. | type | No |
| at | The location at which to insert the object. | location specifier | Yes |
| with data | The initial contents of the object. | any | Yes |
| with properties | The initial values for properties of the object. | record | Yes |

### Result
- **Description:** The new object.
- **Types:** specifier
<a name="clear"></a>
```yaml
---
type: command
name: clear
suite: iWork Suite
---
```

## Command: clear

**Description:** Clear the contents of a specified range of cells, including formatting and style.

### Direct Parameter
- **Types:** range
<a name="merge"></a>
```yaml
---
type: command
name: merge
suite: iWork Suite
---
```

## Command: merge

**Description:** Merge a specified range of cells.

### Direct Parameter
- **Types:** range
<a name="sort"></a>
```yaml
---
type: command
name: sort
suite: iWork Suite
---
```

## Command: sort

**Description:** Sort the rows of the table.

### Direct Parameter
- **Types:** table
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | The column to sort by. | column | No |
| direction |  | NMSD | Yes |
| in rows | Limit the sort to the specified rows. | range | Yes |

<a name="unmerge"></a>
```yaml
---
type: command
name: unmerge
suite: iWork Suite
---
```

## Command: unmerge

**Description:** Unmerge all merged cells in a specified range.

### Direct Parameter
- **Types:** range
<a name="set_password"></a>
```yaml
---
type: command
name: set password
suite: iWork Suite
---
```

## Command: set password

**Description:** Set a password to an unencrypted document.

### Sample Code
### Direct Parameter
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The document to set a password to. If unspecified, the current target is assumed. | document | Yes |
| hint | A hint for the password. | text | Yes |
| saving in keychain | Whether to save the password in keychain or not. By default, the password is not saved in the keychain. | boolean | Yes |

<a name="remove_password"></a>
```yaml
---
type: command
name: remove password
suite: iWork Suite
---
```

## Command: remove password

**Description:** Remove the password from the document.

### Sample Code
### Direct Parameter
- **Description:** The current password of the document.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | The document from which to remove the password. If unspecified, the current target is assumed. | document | Yes |

<a name="iwork_container"></a>
```yaml
---
type: class
name: iWork container
suite: iWork Suite
---
```

## Class: iWork container

**Description:** A container for iWork items

### Elements
- **Type:** audio clip
- **Type:** chart
- **Type:** image
- **Type:** iWork item
- **Type:** group
- **Type:** line
- **Type:** movie
- **Type:** shape
- **Type:** table
- **Type:** text item
<a name="iwork_item"></a>
```yaml
---
type: class
name: iWork item
suite: iWork Suite
---
```

## Class: iWork item

**Description:** An item which supports formatting

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| height | The height of the iWork item. | integer | rw |
| locked | Whether the object is locked. | boolean | rw |
| parent | The iWork container containing this iWork item. | iWork container | r |
| position | The horizontal and vertical coordinates of the top left point of the iWork item. | point | rw |
| width | The width of the iWork item. | integer | rw |

<a name="audio_clip"></a>
```yaml
---
type: class
name: audio clip
suite: iWork Suite
---
```

## Class: audio clip

**Description:** An audio clip

**Inherits:** iWork item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file name | The name of the audio file. | file, text | rw |
| clip volume | The volume setting for the audio clip, from 0 (none) to 100 (full volume). | integer | rw |
| repetition method | If or how the audio clip repeats. | playback repetition method | rw |

<a name="shape"></a>
```yaml
---
type: class
name: shape
suite: iWork Suite
---
```

## Class: shape

**Description:** A shape container

**Inherits:** iWork item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| background fill type | The background, if any, for the shape. | item fill options | r |
| object text | The text contained within the shape. | rich text | rw |
| reflection showing | Is the iWork item displaying a reflection? | boolean | rw |
| reflection value | The percentage of reflection of the iWork item, from 0 (none) to 100 (full). | integer | rw |
| rotation | The rotation of the iWork item, in degrees from 0 to 359. | integer | rw |
| opacity | The opacity of the object, in percent. | integer | read/write |

<a name="chart"></a>
```yaml
---
type: class
name: chart
suite: iWork Suite
---
```

## Class: chart

**Description:** A chart

**Inherits:** iWork item

<a name="image"></a>
```yaml
---
type: class
name: image
suite: iWork Suite
---
```

## Class: image

**Description:** An image container

**Inherits:** iWork item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| description | Text associated with the image, read aloud by VoiceOver. | text | rw |
| file | The image file. | file | r |
| file name | The name of the image file. | file, text | rw |
| opacity | The opacity of the object, in percent. | integer | read/write |
| reflection showing | Is the iWork item displaying a reflection? | boolean | rw |
| reflection value | The percentage of reflection of the iWork item, from 0 (none) to 100 (full). | integer | rw |
| rotation | The rotation of the iWork item, in degrees from 0 to 359. | integer | rw |

<a name="group"></a>
```yaml
---
type: class
name: group
suite: iWork Suite
---
```

## Class: group

**Description:** A group container

**Inherits:** iWork container

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| height | The height of the iWork item. | integer | rw |
| parent | The iWork container containing this iWork item. | iWork container | r |
| position | The horizontal and vertical coordinates of the top left point of the iWork item. | point | rw |
| width | The width of the iWork item. | integer | rw |
| rotation | The rotation of the iWork item, in degrees from 0 to 359. | integer | rw |

<a name="line"></a>
```yaml
---
type: class
name: line
suite: iWork Suite
---
```

## Class: line

**Description:** A line

**Inherits:** iWork item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| end point | A list of two numbers indicating the horizontal and vertical position of the line ending point. | point | rw |
| reflection showing | Is the iWork item displaying a reflection? | boolean | rw |
| reflection value | The percentage of reflection of the iWork item, from 0 (none) to 100 (full). | integer | rw |
| rotation | The rotation of the iWork item, in degrees from 0 to 359. | integer | rw |
| start point | A list of two numbers indicating the horizontal and vertical position of the line starting point. | point | rw |

<a name="movie"></a>
```yaml
---
type: class
name: movie
suite: iWork Suite
---
```

## Class: movie

**Description:** A movie container

**Inherits:** iWork item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file name | The name of the movie file. | file, text | rw |
| movie volume | The volume setting for the movie, from 0 (none) to 100 (full volume). | integer | rw |
| opacity | The opacity of the object, in percent. | integer | read/write |
| reflection showing | Is the iWork item displaying a reflection? | boolean | rw |
| reflection value | The percentage of reflection of the iWork item, from 0 (none) to 100 (full). | integer | rw |
| repetition method | If or how the movie repeats. | playback repetition method | rw |
| rotation | The rotation of the iWork item, in degrees from 0 to 359. | integer | rw |

<a name="table"></a>
```yaml
---
type: class
name: table
suite: iWork Suite
---
```

## Class: table

**Description:** A table

**Inherits:** iWork item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The item's name. | text | read/write |
| cell range | The range describing every cell in the table. | range | r |
| selection range | The cells currently selected in the table. | range | read/write |
| row count | The number of rows in the table. | integer | read/write |
| column count | The number of columns in the table. | integer | read/write |
| header row count | The number of header rows in the table. | integer | read/write |
| header column count | The number of header columns in the table. | integer | read/write |
| footer row count | The number of footer rows in the table. | integer | read/write |

### Elements
- **Type:** cell
- **Type:** row
- **Type:** column
- **Type:** range
### Responds To
- **Command:** sort
<a name="text_item"></a>
```yaml
---
type: class
name: text item
suite: iWork Suite
---
```

## Class: text item

**Description:** A text container

**Inherits:** iWork item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| background fill type | The background, if any, for the text item. | item fill options | r |
| object text | The text contained within the text item. | rich text | rw |
| opacity | The opacity of the object, in percent. | integer | read/write |
| reflection showing | Is the iWork item displaying a reflection? | boolean | rw |
| reflection value | The percentage of reflection of the iWork item, from 0 (none) to 100 (full). | integer | rw |
| rotation | The rotation of the iWork item, in degrees from 0 to 359. | integer | rw |

<a name="range"></a>
```yaml
---
type: class
name: range
suite: iWork Suite
---
```

## Class: range

**Description:** A range of cells in a table

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| font name | The font of the range's cells. | text | read/write |
| font size | The font size of the range's cells. | real | read/write |
| format | The format of the range's cells. | NMCT, any | read/write |
| alignment | The horizontal alignment of content in the range's cells. | tAHT | read/write |
| name | The range's coordinates. | text | r |
| text color | The text color of the range's cells. | color | read/write |
| text wrap | Whether text should wrap in the range's cells. | boolean | read/write |
| background color | The background color of the range's cells. | color | read/write |
| vertical alignment | The vertical alignment of content in the range's cells. | tAVT | read/write |

### Elements
- **Type:** cell
- **Type:** column
- **Type:** row
### Responds To
- **Command:** clear
- **Command:** merge
- **Command:** unmerge
<a name="cell"></a>
```yaml
---
type: class
name: cell
suite: iWork Suite
---
```

## Class: cell

**Description:** A cell in a table

**Inherits:** range

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| column | The cell's column. | column | r |
| row | The cell's row. | row | r |
| value | The actual value in the cell, or missing value if the cell is empty. | number, date, text, boolean, missing value | read/write |
| formatted value | The formatted value in the cell, or missing value if the cell is empty. | text | r |
| formula | The formula in the cell, as text, e.g. =SUM(40+2). If the cell does not contain a formula, returns missing value. To set the value of a cell to a formula as text, use the value property. | text | r |

<a name="row"></a>
```yaml
---
type: class
name: row
suite: iWork Suite
---
```

## Class: row

**Description:** A row of cells in a table

**Inherits:** range

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| address | The row's index in the table (e.g., the second row has address 2). | integer | r |
| height | The height of the row. | real | read/write |

<a name="column"></a>
```yaml
---
type: class
name: column
suite: iWork Suite
---
```

## Class: column

**Description:** A column of cells in a table

**Inherits:** range

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| address | The column's index in the table (e.g., the second column has address 2). | integer | r |
| width | The width of the column. | real | read/write |

<a name="tavt"></a>
```yaml
---
type: enumeration
name: tAVT
suite: iWork Suite
---
```

## Enumeration: tAVT

### Enumerators
| Name | Description |
|---|---|
| bottom | Right-align content. |
| center | Center-align content. |
| top | Top-align content. |

<a name="taht"></a>
```yaml
---
type: enumeration
name: tAHT
suite: iWork Suite
---
```

## Enumeration: tAHT

### Enumerators
| Name | Description |
|---|---|
| auto align | Auto-align based on content type. |
| center | Center-align content. |
| justify | Fully justify (left and right) content. |
| left | Left-align content. |
| right | Right-align content. |

<a name="nmsd"></a>
```yaml
---
type: enumeration
name: NMSD
suite: iWork Suite
---
```

## Enumeration: NMSD

### Enumerators
| Name | Description |
|---|---|
| ascending | Sort in increasing value order |
| descending | Sort in decreasing value order |

<a name="nmct"></a>
```yaml
---
type: enumeration
name: NMCT
suite: iWork Suite
---
```

## Enumeration: NMCT

### Enumerators
| Name | Description |
|---|---|
| automatic | Automatic format |
| checkbox | Checkbox control format (Numbers only) |
| currency | Currency number format |
| date and time | Date and time format |
| fraction | Fraction number format |
| number | Decimal number format |
| percent | Percentage number format |
| pop up menu | Pop-up menu control format (Numbers only) |
| scientific | Scientific notation format |
| slider | Slider control format (Numbers only) |
| stepper | Stepper control format (Numbers only) |
| text | Text format |
| duration | Duration format |
| rating | Rating format. (Numbers only) |
| numeral system | Numeral System |

<a name="item_fill_options"></a>
```yaml
---
type: enumeration
name: item fill options
suite: iWork Suite
---
```

## Enumeration: item fill options

### Enumerators
| Name | Description |
|---|---|
| no fill |  |
| color fill |  |
| gradient fill |  |
| advanced gradient fill |  |
| image fill |  |
| advanced image fill |  |

<a name="playback_repetition_method"></a>
```yaml
---
type: enumeration
name: playback repetition method
suite: iWork Suite
---
```

## Enumeration: playback repetition method

### Enumerators
| Name | Description |
|---|---|
| none |  |
| loop |  |
| loop back and forth |  |

<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: iWork Suite
---
```

## Class Extension: document

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| selection | A list of the currently selected items. | iWork item | rw |
| password protected | Whether the document is password protected or not. | boolean | r |

### Responds To
- **Command:** set password
- **Command:** remove password
## Numbers Suite

**Description:** Classes and commands for Numbers.

<a name="transpose"></a>
```yaml
---
type: command
name: transpose
suite: Numbers Suite
---
```

## Command: transpose

**Description:** Transpose the rows and columns of the table.

### Direct Parameter
- **Types:** table
<a name="export"></a>
```yaml
---
type: command
name: export
suite: Numbers Suite
---
```

## Command: export

**Description:** Export a document to another file

### Sample Code
### Direct Parameter
- **Description:** The document to export
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the destination file | file | No |
| as | The format to use. | export format | No |
| with properties | Optional export settings. | export options | Yes |

<a name="sheet"></a>
```yaml
---
type: class
name: sheet
suite: Numbers Suite
---
```

## Class: sheet

**Description:** A sheet in a document

**Inherits:** iWork container

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The sheet's name. | text | read/write |

<a name="template"></a>
```yaml
---
type: class
name: template
suite: Numbers Suite
---
```

## Class: template

**Description:** A styled document layout.

### Sample Code
### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier used by the application. | text | r |
| name | The localized name displayed to the user. | text | r |

<a name="saveable_file_format"></a>
```yaml
---
type: enumeration
name: saveable file format
suite: Numbers Suite
---
```

## Enumeration: saveable file format

### Enumerators
| Name | Description |
|---|---|
| Numbers | The Numbers native file format |

<a name="export_format"></a>
```yaml
---
type: enumeration
name: export format
suite: Numbers Suite
---
```

## Enumeration: export format

### Enumerators
| Name | Description |
|---|---|
| PDF | PDF |
| Microsoft Excel | Microsoft Excel |
| CSV | CSV |
| Numbers 09 | Numbers 09 |

<a name="image_quality"></a>
```yaml
---
type: enumeration
name: image quality
suite: Numbers Suite
---
```

## Enumeration: image quality

### Enumerators
| Name | Description |
|---|---|
| Good | Good quality. |
| Better | Better quality. |
| Best | Best quality. |

<a name="export_options"></a>
```yaml
---
type: record-type
name: export options
suite: Numbers Suite
---
```

## Record Type: export options

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| exclude summary worksheet | Whether to exclude a summary worksheet in Excel workbook. | boolean | read/write |
| password | Password. | text | read/write |
| password hint | Password hint. | text | read/write |
| image quality | Image quality. | image quality | read/write |
| include comments | include comments description | boolean | read/write |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Numbers Suite
---
```

## Class Extension: application

**Description:** The Numbers application.

### Elements
- **Type:** template
<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: Numbers Suite
---
```

## Class Extension: document

**Description:** The Numbers document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | Document ID. | text | r |
| document template | The template assigned to the document. | template | r |
| active sheet | The active sheet. | sheet | read/write |

### Elements
- **Type:** sheet
### Responds To
- **Command:** export
<a name="table"></a>
```yaml
---
type: class-extension
name: table
suite: Numbers Suite
---
```

## Class Extension: table

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| filtered | Whether the table is currently filtered. | boolean | read/write |
| header rows frozen | Whether header rows are frozen. | boolean | read/write |
| header columns frozen | Whether header columns are frozen. | boolean | read/write |

### Responds To
- **Command:** transpose
## Compatibility Suite

**Description:** A set of basic classes for compatibility with prior releases.

<a name="add_column_after"></a>
```yaml
---
type: command
name: add column after
suite: Compatibility Suite
---
```

## Command: add column after

**Description:** Add a column to the table after a specified range of cells.

### Direct Parameter
- **Types:** range
### Result
- **Description:** A reference to the new column
- **Types:** specifier
<a name="add_column_before"></a>
```yaml
---
type: command
name: add column before
suite: Compatibility Suite
---
```

## Command: add column before

**Description:** Add a column to the table before a specified range of cells.

### Direct Parameter
- **Types:** range
### Result
- **Description:** A reference to the new column
- **Types:** specifier
<a name="add_row_above"></a>
```yaml
---
type: command
name: add row above
suite: Compatibility Suite
---
```

## Command: add row above

**Description:** Add a row to the table below a specified range of cells.

### Direct Parameter
- **Types:** range
### Result
- **Description:** A reference to the new row
- **Types:** specifier
<a name="add_row_below"></a>
```yaml
---
type: command
name: add row below
suite: Compatibility Suite
---
```

## Command: add row below

**Description:** Add a row to the table below a specified range of cells.

### Direct Parameter
- **Types:** range
### Result
- **Description:** A reference to the new row
- **Types:** specifier
<a name="remove"></a>
```yaml
---
type: command
name: remove
suite: Compatibility Suite
---
```

## Command: remove

**Description:** Remove specified rows or columns from a table.

### Direct Parameter
- **Types:** range
<a name="range"></a>
```yaml
---
type: class-extension
name: range
suite: Compatibility Suite
---
```

## Class Extension: range

### Responds To
- **Command:** add column after
- **Command:** add column before
- **Command:** add row above
- **Command:** add row below
<a name="row"></a>
```yaml
---
type: class-extension
name: row
suite: Compatibility Suite
---
```

## Class Extension: row

### Responds To
- **Command:** remove
<a name="column"></a>
```yaml
---
type: class-extension
name: column
suite: Compatibility Suite
---
```

## Class Extension: column

### Responds To
- **Command:** remove
