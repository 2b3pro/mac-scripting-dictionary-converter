# Keynote Terminology: AppleScript/JSX

## Table of Contents

### Keynote Suite
#### Commands
- [export](#export)
- [duplicate](#duplicate)
- [get](#get)
#### Classs
- [slide layout](#slide_layout)
- [slide](#slide)
- [theme](#theme)
#### Enumerations
- [saveable file format](#saveable_file_format)
- [export format](#export_format)
- [image export formats](#image_export_formats)
- [movie export formats](#movie_export_formats)
- [movie codecs](#movie_codecs)
- [movie framerates](#movie_framerates)
- [print what](#print_what)
- [PDF image quality](#pdf_image_quality)
- [transition effects](#transition_effects)
#### Record Types
- [export options](#export_options)
- [transition settings](#transition_settings)
#### Class Extensions
- [application](#application)
- [document](#document)
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
### Compatibility Suite
#### Commands
- [add chart](#add_chart)
- [start](#start)
- [make image slides](#make_image_slides)
- [stop](#stop)
- [show next](#show_next)
- [show previous](#show_previous)
- [show slide switcher](#show_slide_switcher)
- [hide slide switcher](#hide_slide_switcher)
- [move slide switcher forward](#move_slide_switcher_forward)
- [move slide switcher backward](#move_slide_switcher_backward)
- [cancel slide switcher](#cancel_slide_switcher)
- [accept slide switcher](#accept_slide_switcher)
- [start slideshow](#start_slideshow)
- [start from](#start_from)
- [stop slideshow](#stop_slideshow)
- [show](#show)
#### Enumerations
- [legacy chart type](#legacy_chart_type)
- [legacy chart grouping](#legacy_chart_grouping)
#### Class Extensions
- [application](#application)
- [document](#document)
- [slide](#slide)


## Keynote Suite

**Description:** Classes and commands for Keynote.

<a name="export"></a>
```yaml
---
type: command
name: export
suite: Keynote Suite
---
```

## Command: export

**Description:** Export a slideshow to another file

### Sample Code
### Direct Parameter
- **Description:** The slideshow to export
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the destination file | file | No |
| as | The format to use. | export format | No |
| with properties | Optional export settings. | export options | Yes |

<a name="duplicate"></a>
```yaml
---
type: command
name: duplicate
suite: Keynote Suite
---
```

## Command: duplicate

**Description:** Copy an object.

### Direct Parameter
- **Description:** The object(s) to copy.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The location for the new copy or copies. | location specifier | Yes |
| with properties | Properties to set in the new copy or copies right away. | record | Yes |

<a name="get"></a>
```yaml
---
type: command
name: get
suite: Keynote Suite
---
```

## Command: get

**Description:** Returns the value of the specified object(s).

### Direct Parameter
- **Types:** specifier
### Result
- **Types:** any
<a name="slide_layout"></a>
```yaml
---
type: class
name: slide layout
suite: Keynote Suite
---
```

## Class: slide layout

**Description:** A slide layout in a theme or slideshow document

**Inherits:** slide

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the slide layout | text | r |

<a name="slide"></a>
```yaml
---
type: class
name: slide
suite: Keynote Suite
---
```

## Class: slide

**Description:** A slide in a slideshow document

**Inherits:** iWork container

### Sample Code
### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| base layout | The slide layout this slide is based upon | slide layout | rw |
| body showing | Is the default body text displayed? | boolean | rw |
| skipped | Is the slide skipped? | boolean | rw |
| slide number | index of the slide in the document | integer | r |
| title showing | Is the default slide title displayed? | boolean | rw |
| default body item | The default body container of the slide | shape | r |
| default title item | The default title container of the slide | shape | r |
| presenter notes | The presenter notes for the slide | rich text | rw |
| transition properties | The transition settings to apply to the slide. | transition settings | read/write |

<a name="theme"></a>
```yaml
---
type: class
name: theme
suite: Keynote Suite
---
```

## Class: theme

**Description:** A collection of slide layouts, with shared design intents and elements.

### Sample Code
### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier used by the application. | text | r |
| name |  | text | r |

<a name="saveable_file_format"></a>
```yaml
---
type: enumeration
name: saveable file format
suite: Keynote Suite
---
```

## Enumeration: saveable file format

### Enumerators
| Name | Description |
|---|---|
| Keynote | The Keynote native file format |

<a name="export_format"></a>
```yaml
---
type: enumeration
name: export format
suite: Keynote Suite
---
```

## Enumeration: export format

### Enumerators
| Name | Description |
|---|---|
| HTML | HTML |
| QuickTime movie | QuickTime movie |
| PDF | PDF |
| slide images | image |
| Microsoft PowerPoint | Microsoft PowerPoint |
| Keynote 09 | Keynote 09 |

<a name="image_export_formats"></a>
```yaml
---
type: enumeration
name: image export formats
suite: Keynote Suite
---
```

## Enumeration: image export formats

### Enumerators
| Name | Description |
|---|---|
| JPEG | JPEG |
| PNG | PNG |
| TIFF | TIFF |

<a name="movie_export_formats"></a>
```yaml
---
type: enumeration
name: movie export formats
suite: Keynote Suite
---
```

## Enumeration: movie export formats

### Enumerators
| Name | Description |
|---|---|
| format360p | 360p |
| format540p | 540p |
| format720p | 720p |
| format1080p | 1080p |
| format2160p | DCI 4K (4096x2160) |
| native size | Exported movie will have the same dimensions as the document, up to 4096x2160 |

<a name="movie_codecs"></a>
```yaml
---
type: enumeration
name: movie codecs
suite: Keynote Suite
---
```

## Enumeration: movie codecs

### Enumerators
| Name | Description |
|---|---|
| h264 | H.264 |
| AppleProRes422 | Apple ProRes 422 |
| AppleProRes4444 | Apple ProRes 4444 |
| AppleProRes422LT | Apple ProRes 422LT |
| AppleProRes422HQ | Apple ProRes 422HQ |
| AppleProRes422Proxy | Apple ProRes 422Proxy |
| HEVC | HEVC |

<a name="movie_framerates"></a>
```yaml
---
type: enumeration
name: movie framerates
suite: Keynote Suite
---
```

## Enumeration: movie framerates

### Enumerators
| Name | Description |
|---|---|
| FPS12 | 12 FPS |
| FPS2398 | 23.98 FPS |
| FPS24 | 24 FPS |
| FPS25 | 25 FPS |
| FPS2997 | 29.97 FPS |
| FPS30 | 30 FPS |
| FPS50 | 50 FPS |
| FPS5994 | 59.94 FPS |
| FPS60 | 60 FPS |

<a name="print_what"></a>
```yaml
---
type: enumeration
name: print what
suite: Keynote Suite
---
```

## Enumeration: print what

### Enumerators
| Name | Description |
|---|---|
| IndividualSlides | individual slides |
| SlideWithNotes | slides with notes |
| Handouts | handouts |

<a name="pdf_image_quality"></a>
```yaml
---
type: enumeration
name: PDF image quality
suite: Keynote Suite
---
```

## Enumeration: PDF image quality

### Enumerators
| Name | Description |
|---|---|
| Good | good quality |
| Better | better quality |
| Best | best quality |

<a name="transition_effects"></a>
```yaml
---
type: enumeration
name: transition effects
suite: Keynote Suite
---
```

## Enumeration: transition effects

### Enumerators
| Name | Description |
|---|---|
| no transition effect |  |
| magic move |  |
| shimmer |  |
| sparkle |  |
| swing |  |
| object cube |  |
| object flip |  |
| object pop |  |
| object push |  |
| object revolve |  |
| object zoom |  |
| perspective |  |
| clothesline |  |
| confetti |  |
| dissolve |  |
| drop |  |
| droplet |  |
| fade through color |  |
| grid |  |
| iris |  |
| move in |  |
| push |  |
| reveal |  |
| switch |  |
| wipe |  |
| blinds |  |
| color planes |  |
| cube |  |
| doorway |  |
| fall |  |
| flip |  |
| flop |  |
| mosaic |  |
| page flip |  |
| pivot |  |
| reflection |  |
| revolving door |  |
| scale |  |
| swap |  |
| swoosh |  |
| twirl |  |
| twist |  |
| fade and move |  |

<a name="export_options"></a>
```yaml
---
type: record-type
name: export options
suite: Keynote Suite
---
```

## Record Type: export options

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| compression factor | compressed image quality, ranging from 0.0 (maximum compression, lowest quality) to 1.0 (lossless compression, highest quality).  This option only pertains to JPEG format images. | real | read/write |
| image format | format for resulting images. | image export formats | read/write |
| movie format | format for exported movie. | movie export formats | read/write |
| movie codec | codec for movie exported at native size. | movie codecs | read/write |
| movie framerate | frame rate for movie exported at native size. | movie framerates | read/write |
| export style | choose whether to include notes, etc. | print what | read/write |
| all stages | print each stage of builds | boolean | read/write |
| skipped slides | include skipped slides | boolean | read/write |
| borders | add borders around slides | boolean | read/write |
| slide numbers | include slide numbers | boolean | read/write |
| date | include date | boolean | read/write |
| rawKPF | export in raw KPF | boolean | read/write |
| password | password | text | read/write |
| password hint | password hint | text | read/write |
| include comments | include comments description | boolean | read/write |
| PDF image quality | quality of images in PDF document | PDF image quality | read/write |

<a name="transition_settings"></a>
```yaml
---
type: record-type
name: transition settings
suite: Keynote Suite
---
```

## Record Type: transition settings

**Description:** Properties common to all transitions

### Sample Code
### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| automatic transition | Should the transition begin automatically? A value of false indicates to transition on click. | boolean | read/write |
| transition delay | The number of seconds to wait until beginning the transition. | real | read/write |
| transition duration | The number of seconds allocated for the transition to occur. | real | read/write |
| transition effect | The transition effect to apply between the current and following slides. | transition effects | read/write |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Keynote Suite
---
```

## Class Extension: application

**Description:** The Keynote application.

### Elements
- **Type:** theme
<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: Keynote Suite
---
```

## Class Extension: document

**Description:** The Keynote document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | Document ID. | text | r |
| slide numbers showing | Are the slide numbers displayed? | boolean | read/write |
| document theme | The theme assigned to the document. | theme | rw |
| auto loop | Make the slideshow play repeatedly. | boolean | rw |
| auto play | Automatically play the presentation when opening the file. | boolean | rw |
| auto restart | Restart the slideshow if it's inactive for the specified time | boolean | rw |
| maximum idle duration | Restart the slideshow if it's inactive for the specified time | integer | rw |
| current slide | The currently selected slide, or the slide that would display if the presentation was started. | slide | read/write |
| height | The height of the document (in points). Standard slide height = 768. Wide slide height = 1080. | integer | rw |
| width | The width of the document (in points). Standard slide width = 1024. Wide slide width = 1920. | integer | rw |

### Elements
- **Type:** slide
- **Type:** slide layout
### Responds To
- **Command:** export
- **Command:** start
- **Command:** stop
- **Command:** show next
- **Command:** show previous
- **Command:** show slide switcher
- **Command:** cancel slide switcher
- **Command:** accept slide switcher
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
## Compatibility Suite

**Description:** A set of basic classes for compatibility with prior releases.

<a name="add_chart"></a>
```yaml
---
type: command
name: add chart
suite: Compatibility Suite
---
```

## Command: add chart

**Description:** Add a chart to a slide

### Direct Parameter
- **Description:** the slide to add the chart to
- **Types:** slide
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| row names |  | text | Yes |
| column names |  | text | Yes |
| data |  | any | Yes |
| type |  | legacy chart type | Yes |
| group by |  | legacy chart grouping | Yes |

<a name="start"></a>
```yaml
---
type: command
name: start
suite: Compatibility Suite
---
```

## Command: start

**Description:** Start playing the presentation.

### Direct Parameter
- **Description:** The presentation to play
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | slide at which to start playing | slide | Yes |

<a name="make_image_slides"></a>
```yaml
---
type: command
name: make image slides
suite: Compatibility Suite
---
```

## Command: make image slides

**Description:** Make a series of slides from a list of files.

### Direct Parameter
- **Description:** the document to add the slides to
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| files | a list of image files to add | file | No |
| set titles |  | boolean | Yes |
| slide layout |  | slide layout | Yes |

<a name="stop"></a>
```yaml
---
type: command
name: stop
suite: Compatibility Suite
---
```

## Command: stop

**Description:** Stop the presentation.

### Direct Parameter
- **Types:** document
<a name="show_next"></a>
```yaml
---
type: command
name: show next
suite: Compatibility Suite
---
```

## Command: show next

**Description:** Advance one build or slide.

<a name="show_previous"></a>
```yaml
---
type: command
name: show previous
suite: Compatibility Suite
---
```

## Command: show previous

**Description:** Go to the previous slide.

<a name="show_slide_switcher"></a>
```yaml
---
type: command
name: show slide switcher
suite: Compatibility Suite
---
```

## Command: show slide switcher

**Description:** Show the slide switcher in play mode

### Direct Parameter
- **Types:** document
<a name="hide_slide_switcher"></a>
```yaml
---
type: command
name: hide slide switcher
suite: Compatibility Suite
---
```

## Command: hide slide switcher

**Description:** Hide the slide switcher in play mode

### Direct Parameter
- **Types:** document
<a name="move_slide_switcher_forward"></a>
```yaml
---
type: command
name: move slide switcher forward
suite: Compatibility Suite
---
```

## Command: move slide switcher forward

**Description:** Move the slide switcher forward one slide

### Direct Parameter
- **Types:** document
<a name="move_slide_switcher_backward"></a>
```yaml
---
type: command
name: move slide switcher backward
suite: Compatibility Suite
---
```

## Command: move slide switcher backward

**Description:** Move the slide switcher backward one slide

### Direct Parameter
- **Types:** document
<a name="cancel_slide_switcher"></a>
```yaml
---
type: command
name: cancel slide switcher
suite: Compatibility Suite
---
```

## Command: cancel slide switcher

**Description:** Hide the slide switcher without changing slides

### Direct Parameter
- **Types:** document
<a name="accept_slide_switcher"></a>
```yaml
---
type: command
name: accept slide switcher
suite: Compatibility Suite
---
```

## Command: accept slide switcher

**Description:** Hide the slide switcher, going to the slide it has selected

### Direct Parameter
- **Types:** document
<a name="start_slideshow"></a>
```yaml
---
type: command
name: start slideshow
suite: Compatibility Suite
---
```

## Command: start slideshow

<a name="start_from"></a>
```yaml
---
type: command
name: start from
suite: Compatibility Suite
---
```

## Command: start from

### Direct Parameter
- **Description:** the object for the command
- **Types:** slide
<a name="stop_slideshow"></a>
```yaml
---
type: command
name: stop slideshow
suite: Compatibility Suite
---
```

## Command: stop slideshow

<a name="show"></a>
```yaml
---
type: command
name: show
suite: Compatibility Suite
---
```

## Command: show

### Direct Parameter
- **Description:** the object for the command
- **Types:** slide
<a name="legacy_chart_type"></a>
```yaml
---
type: enumeration
name: legacy chart type
suite: Compatibility Suite
---
```

## Enumeration: legacy chart type

**Description:** Visual style of chart

### Enumerators
| Name | Description |
|---|---|
| pie_2d | two-dimensional pie chart |
| vertical_bar_2d | two-dimensional vertical bar chart |
| stacked_vertical_bar_2d | two-dimensional stacked vertical bar chart |
| horizontal_bar_2d | two-dimensional horizontal bar chart |
| stacked_horizontal_bar_2d | two-dimensional stacked horizontal bar chart |
| pie_3d | three-dimensional pie chart. |
| vertical_bar_3d | three-dimensional vertical bar chart |
| stacked_vertical_bar_3d | three-dimensional stacked bar chart |
| horizontal_bar_3d | three-dimensional horizontal bar chart |
| stacked_horizontal_bar_3d | three-dimensional stacked horizontal bar chart |
| area_2d | two-dimensional area chart. |
| stacked_area_2d | two-dimensional stacked area chart |
| line_2d |  two-dimensional line chart. |
| line_3d | three-dimensional line chart |
| area_3d | three-dimensional area chart |
| stacked_area_3d | three-dimensional stacked area chart |
| scatterplot_2d | two-dimensional scatterplot chart |

<a name="legacy_chart_grouping"></a>
```yaml
---
type: enumeration
name: legacy chart grouping
suite: Compatibility Suite
---
```

## Enumeration: legacy chart grouping

**Description:** Grouping for chart data

### Enumerators
| Name | Description |
|---|---|
| chart row | group by row |
| chart column | group by column |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Compatibility Suite
---
```

## Class Extension: application

**Description:** Deprecated Keynote application properties and verbs.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| playing | Are any slideshows playing | boolean | r |
| slide switcher visible | Is the slide selector visible? | boolean | r |
| frozen |  | boolean | rw |

### Responds To
- **Command:** start slideshow
- **Command:** stop slideshow
- **Command:** show next
- **Command:** show previous
- **Command:** show slide switcher
- **Command:** cancel slide switcher
- **Command:** move slide switcher forward
- **Command:** move slide switcher backward
- **Command:** accept slide switcher
<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: Compatibility Suite
---
```

## Class Extension: document

### Responds To
- **Command:** make image slides
<a name="slide"></a>
```yaml
---
type: class-extension
name: slide
suite: Compatibility Suite
---
```

## Class Extension: slide

### Responds To
- **Command:** show
- **Command:** start from
- **Command:** add chart
