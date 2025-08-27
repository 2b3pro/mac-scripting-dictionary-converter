# DEVONthink v4.0 Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [close](#close)
- [save](#save)
- [print](#print)
- [quit](#quit)
- [count](#count)
- [exists](#exists)
- [make](#make)
#### Classs
- [application](#application)
- [window](#window)
#### Enumerations
- [save options](#save_options)
- [printing error handling](#printing_error_handling)
#### Record Types
- [print settings](#print_settings)
#### Value Types
- [dictionary](#dictionary)
- [raw data](#raw_data)
- [RGB color](#rgb_color)
- [array](#array)
### Text Suite
#### Classs
- [attachment](#attachment)
- [rich text](#rich_text)
- [attribute run](#attribute_run)
- [character](#character)
- [paragraph](#paragraph)
- [word](#word)
### Extended Text Suite
#### Commands
- [bold](#bold)
- [italicize](#italicize)
- [plain](#plain)
- [reformat](#reformat)
- [scroll to visible](#scroll_to_visible)
- [strike](#strike)
- [unbold](#unbold)
- [underline](#underline)
- [unitalicize](#unitalicize)
- [unstrike](#unstrike)
- [ununderline](#ununderline)
#### Enumerations
- [text alignment](#text_alignment)
#### Class Extensions
- [attachment](#attachment)
- [rich text](#rich_text)
- [attribute run](#attribute_run)
- [character](#character)
- [paragraph](#paragraph)
- [word](#word)
### DEVONthink Suite
#### Commands
- [add custom meta data](#add_custom_meta_data)
- [add download](#add_download)
- [add reading list](#add_reading_list)
- [add reminder](#add_reminder)
- [add row](#add_row)
- [check file integrity of](#check_file_integrity_of)
- [classify](#classify)
- [compare](#compare)
- [compress](#compress)
- [convert](#convert)
- [convert feed to HTML](#convert_feed_to_html)
- [create database](#create_database)
- [create formatted note from](#create_formatted_note_from)
- [create location](#create_location)
- [create Markdown from](#create_markdown_from)
- [create PDF document from](#create_pdf_document_from)
- [create record with](#create_record_with)
- [create thumbnail](#create_thumbnail)
- [create web document from](#create_web_document_from)
- [delete](#delete)
- [delete row at](#delete_row_at)
- [delete thumbnail](#delete_thumbnail)
- [delete workspace](#delete_workspace)
- [do JavaScript](#do_javascript)
- [download image for prompt](#download_image_for_prompt)
- [download JSON from](#download_json_from)
- [download markup from](#download_markup_from)
- [download URL](#download_url)
- [display authentication dialog](#display_authentication_dialog)
- [display chat dialog](#display_chat_dialog)
- [display date editor](#display_date_editor)
- [display group selector](#display_group_selector)
- [display name editor](#display_name_editor)
- [duplicate](#duplicate)
- [exists record at](#exists_record_at)
- [exists record with comment](#exists_record_with_comment)
- [exists record with content hash](#exists_record_with_content_hash)
- [exists record with file](#exists_record_with_file)
- [exists record with path](#exists_record_with_path)
- [exists record with URL](#exists_record_with_url)
- [export](#export)
- [export tags of](#export_tags_of)
- [export website](#export_website)
- [extract keywords from](#extract_keywords_from)
- [get cached data for URL](#get_cached_data_for_url)
- [get cell at](#get_cell_at)
- [get chat models for engine](#get_chat_models_for_engine)
- [get chat response for message](#get_chat_response_for_message)
- [get concordance of](#get_concordance_of)
- [get custom meta data](#get_custom_meta_data)
- [get database with id](#get_database_with_id)
- [get database with uuid](#get_database_with_uuid)
- [get embedded images of](#get_embedded_images_of)
- [get embedded objects of](#get_embedded_objects_of)
- [get embedded sheets and scripts of](#get_embedded_sheets_and_scripts_of)
- [get favicon of](#get_favicon_of)
- [get feed items of](#get_feed_items_of)
- [get frames of](#get_frames_of)
- [get items of feed](#get_items_of_feed)
- [get links of](#get_links_of)
- [get metadata of](#get_metadata_of)
- [get record at](#get_record_at)
- [get record with id](#get_record_with_id)
- [get record with uuid](#get_record_with_uuid)
- [get rich text of](#get_rich_text_of)
- [get text of](#get_text_of)
- [get title of](#get_title_of)
- [get versions of](#get_versions_of)
- [hide progress indicator](#hide_progress_indicator)
- [import attachments of](#import_attachments_of)
- [import path](#import_path)
- [import template](#import_template)
- [index path](#index_path)
- [load workspace](#load_workspace)
- [log message](#log_message)
- [lookup records with comment](#lookup_records_with_comment)
- [lookup records with content hash](#lookup_records_with_content_hash)
- [lookup records with file](#lookup_records_with_file)
- [lookup records with path](#lookup_records_with_path)
- [lookup records with tags](#lookup_records_with_tags)
- [lookup records with URL](#lookup_records_with_url)
- [merge](#merge)
- [move](#move)
- [move into database](#move_into_database)
- [move to external folder](#move_to_external_folder)
- [open database](#open_database)
- [open tab for](#open_tab_for)
- [open window for](#open_window_for)
- [optimize](#optimize)
- [paste clipboard](#paste_clipboard)
- [perform smart rule](#perform_smart_rule)
- [refresh](#refresh)
- [replicate](#replicate)
- [restore record with](#restore_record_with)
- [save version of](#save_version_of)
- [save workspace](#save_workspace)
- [search](#search)
- [set cell at](#set_cell_at)
- [show progress indicator](#show_progress_indicator)
- [show search](#show_search)
- [start downloads](#start_downloads)
- [step progress indicator](#step_progress_indicator)
- [stop downloads](#stop_downloads)
- [summarize annotations of](#summarize_annotations_of)
- [summarize contents of](#summarize_contents_of)
- [summarize mentions of](#summarize_mentions_of)
- [summarize text](#summarize_text)
- [synchronize](#synchronize)
- [transcribe](#transcribe)
- [update](#update)
- [update thumbnail](#update_thumbnail)
- [verify](#verify)
#### Classs
- [document window](#document_window)
- [main window](#main_window)
- [application](#application)
- [child](#child)
- [content](#content)
- [database](#database)
- [incoming reference](#incoming_reference)
- [incoming Wiki reference](#incoming_wiki_reference)
- [outgoing reference](#outgoing_reference)
- [outgoing Wiki reference](#outgoing_wiki_reference)
- [parent](#parent)
- [record](#record)
- [reminder](#reminder)
- [selected record](#selected_record)
- [smart parent](#smart_parent)
- [tag group](#tag_group)
- [tab](#tab)
- [think window](#think_window)
#### Enumerations
- [comparison type](#comparison_type)
- [convert type](#convert_type)
- [data type](#data_type)
- [reminder alarm](#reminder_alarm)
- [reminder day](#reminder_day)
- [reminder schedule](#reminder_schedule)
- [reminder week](#reminder_week)
- [rule event](#rule_event)
- [search comparison](#search_comparison)
- [summary style](#summary_style)
- [summary type](#summary_type)
- [tag type](#tag_type)
- [update mode](#update_mode)
- [concordance sorting](#concordance_sorting)
- [chat engine](#chat_engine)
- [image engine](#image_engine)
#### Record Types
- [reading list item](#reading_list_item)
- [group selector result](#group_selector_result)
- [authentication result](#authentication_result)
- [HTTP response](#http_response)
- [feed item](#feed_item)
### OCR Commands Suite
#### Commands
- [convert image](#convert_image)
- [ocr](#ocr)
#### Enumerations
- [OCR convert type](#ocr_convert_type)
#### Record Types
- [PDF properties](#pdf_properties)
### Imprint Commands Suite
#### Commands
- [imprinter configuration names](#imprinter_configuration_names)
- [imprint configuration](#imprint_configuration)
- [imprint](#imprint)
#### Enumerations
- [border style type](#border_style_type)
- [imprint position](#imprint_position)
- [occurrence type](#occurrence_type)


## Standard Suite

**Description:** Common classes and commands for all applications.

<a name="close"></a>
```yaml
---
type: command
name: close
suite: Standard Suite
---
```

## Command: close

**Description:** Close a window, tab or database.

### Direct Parameter
- **Description:** The window(s), tab(s) or database(s) to close.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Should changes be saved before closing? | save options | Yes |

<a name="save"></a>
```yaml
---
type: command
name: save
suite: Standard Suite
---
```

## Command: save

**Description:** Save a window or tab.

### Direct Parameter
- **Description:** The window(s) or tab(s) to save.
- **Types:** specifier
<a name="print"></a>
```yaml
---
type: command
name: print
suite: Standard Suite
---
```

## Command: print

**Description:** Print a window or tab.

### Direct Parameter
- **Description:** The window(s) or tab(s) to be printed.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with properties | The print settings to use. | print settings | Yes |
| print dialog | Should the application show the print dialog? | boolean | Yes |

<a name="quit"></a>
```yaml
---
type: command
name: quit
suite: Standard Suite
---
```

## Command: quit

**Description:** Quit the application.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Should changes be saved before quitting? | save options | Yes |

<a name="count"></a>
```yaml
---
type: command
name: count
suite: Standard Suite
---
```

## Command: count

**Description:** Return the number of elements of a particular class within an object.

### Direct Parameter
- **Description:** The objects to be counted.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| each | The class of objects to be counted. | type | Yes |

### Result
- **Description:** The count.
- **Types:** integer
<a name="exists"></a>
```yaml
---
type: command
name: exists
suite: Standard Suite
---
```

## Command: exists

**Description:** Verify that an object exists.

### Direct Parameter
- **Description:** The object(s) to check.
- **Types:** any
### Result
- **Description:** Did the object(s) exist?
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

**Description:** Create a new object.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new object. | type | No |
| at | The location at which to insert the object. | location specifier | Yes |
| with data | The initial contents of the object. | any | Yes |
| with properties | The initial values for properties of the object. | dictionary | Yes |

### Result
- **Description:** The new object.
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

**Description:** The application's top-level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the application. | text | r |
| frontmost | Is this the active application? | boolean | r |
| version | The version number of the application. | text | r |

### Elements
- **Type:** window
### Responds To
- **Command:** open
- **Command:** print
- **Command:** quit
<a name="window"></a>
```yaml
---
type: class
name: window
suite: Standard Suite
---
```

## Class: window

**Description:** A window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The title of the window. | text | r |
| id | The unique identifier of the window. | integer | r |
| index | The index of the window, ordered front to back. | integer | read/write |
| bounds | The bounding rectangle of the window. | rectangle | read/write |
| closeable | Does the window have a close button? | boolean | r |
| miniaturizable | Does the window have a minimize button? | boolean | r |
| miniaturized | Is the window minimized right now? | boolean | read/write |
| resizable | Can the window be resized? | boolean | r |
| visible | Is the window visible right now? | boolean | read/write |
| zoomable | Does the window have a zoom button? | boolean | r |
| zoomed | Is the window zoomed right now? | boolean | read/write |

### Responds To
- **Command:** close
- **Command:** print
- **Command:** save
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

<a name="printing_error_handling"></a>
```yaml
---
type: enumeration
name: printing error handling
suite: Standard Suite
---
```

## Enumeration: printing error handling

### Enumerators
| Name | Description |
|---|---|
| standard | Standard PostScript error handling |
| detailed | print a detailed report of PostScript errors |

<a name="print_settings"></a>
```yaml
---
type: record-type
name: print settings
suite: Standard Suite
---
```

## Record Type: print settings

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| copies | the number of copies of a document to be printed | integer | read/write |
| collating | Should printed copies be collated? | boolean | read/write |
| starting page | the first page of the document to be printed | integer | read/write |
| ending page | the last page of the document to be printed | integer | read/write |
| pages across | number of logical pages laid across a physical page | integer | read/write |
| pages down | number of logical pages laid out down a physical page | integer | read/write |
| requested print time | the time at which the desktop printer should print the document | date | read/write |
| error handling | how errors are handled | printing error handling | read/write |
| fax number | for fax number | text | read/write |
| target printer | for target printer | text | read/write |

<a name="dictionary"></a>
```yaml
---
type: value-type
name: dictionary
suite: Standard Suite
---
```

## Value Type: dictionary

**Description:** Dictionary containing key-value pairs.

<a name="raw_data"></a>
```yaml
---
type: value-type
name: raw data
suite: Standard Suite
---
```

## Value Type: raw data

**Description:** Raw data.

<a name="rgb_color"></a>
```yaml
---
type: value-type
name: RGB color
suite: Standard Suite
---
```

## Value Type: RGB color

**Description:** An RGB color.

<a name="array"></a>
```yaml
---
type: value-type
name: array
suite: Standard Suite
---
```

## Value Type: array

**Description:** Array of items.

## Text Suite

**Description:** Classes and commands for Text Suite

<a name="attachment"></a>
```yaml
---
type: class
name: attachment
suite: Text Suite
---
```

## Class: attachment

**Description:** Represents an inline text attachment.  This class is used mainly for make commands.

**Inherits:** rich text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file name | The path to the file for the attachment | file, missing value | read/write |

<a name="rich_text"></a>
```yaml
---
type: class
name: rich text
suite: Text Suite
---
```

## Class: rich text

**Description:** Rich (styled) text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The color of the first character. | RGB color, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
<a name="attribute_run"></a>
```yaml
---
type: class
name: attribute run
suite: Text Suite
---
```

## Class: attribute run

**Description:** This subdivides the text into chunks that all have the same attributes.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The color of the first character. | RGB color, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
<a name="character"></a>
```yaml
---
type: class
name: character
suite: Text Suite
---
```

## Class: character

**Description:** This subdivides the text into characters.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The color of the first character. | RGB color, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
<a name="paragraph"></a>
```yaml
---
type: class
name: paragraph
suite: Text Suite
---
```

## Class: paragraph

**Description:** This subdivides the text into paragraphs.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The color of the first character. | RGB color, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
<a name="word"></a>
```yaml
---
type: class
name: word
suite: Text Suite
---
```

## Class: word

**Description:** This subdivides the text into words.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The color of the first character. | RGB color, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
## Extended Text Suite

**Description:** Classes and commands for Extended Text Suite

<a name="bold"></a>
```yaml
---
type: command
name: bold
suite: Extended Text Suite
---
```

## Command: bold

**Description:** Bold some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="italicize"></a>
```yaml
---
type: command
name: italicize
suite: Extended Text Suite
---
```

## Command: italicize

**Description:** Italicize some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="plain"></a>
```yaml
---
type: command
name: plain
suite: Extended Text Suite
---
```

## Command: plain

**Description:** Make some text plain

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="reformat"></a>
```yaml
---
type: command
name: reformat
suite: Extended Text Suite
---
```

## Command: reformat

**Description:** Reformat some text. Similar to WordService's Reformat service.

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="scroll_to_visible"></a>
```yaml
---
type: command
name: scroll to visible
suite: Extended Text Suite
---
```

## Command: scroll to visible

**Description:** Scroll to and animate some text.

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="strike"></a>
```yaml
---
type: command
name: strike
suite: Extended Text Suite
---
```

## Command: strike

**Description:** Strike some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="unbold"></a>
```yaml
---
type: command
name: unbold
suite: Extended Text Suite
---
```

## Command: unbold

**Description:** Unbold some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="underline"></a>
```yaml
---
type: command
name: underline
suite: Extended Text Suite
---
```

## Command: underline

**Description:** Underline some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="unitalicize"></a>
```yaml
---
type: command
name: unitalicize
suite: Extended Text Suite
---
```

## Command: unitalicize

**Description:** Unitalicize some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="unstrike"></a>
```yaml
---
type: command
name: unstrike
suite: Extended Text Suite
---
```

## Command: unstrike

**Description:** Unstrike some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="ununderline"></a>
```yaml
---
type: command
name: ununderline
suite: Extended Text Suite
---
```

## Command: ununderline

**Description:** Ununderline some text

### Direct Parameter
- **Description:** The text.
- **Types:** specifier
<a name="text_alignment"></a>
```yaml
---
type: enumeration
name: text alignment
suite: Extended Text Suite
---
```

## Enumeration: text alignment

### Enumerators
| Name | Description |
|---|---|
| left |  |
| center |  |
| right |  |
| justified |  |
| natural |  |

<a name="attachment"></a>
```yaml
---
type: class-extension
name: attachment
suite: Extended Text Suite
---
```

## Class Extension: attachment

**Description:** Represents an inline text attachment.  This class is used mainly for make commands.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file name | The path to the file for the attachment | file, missing value | read/write |

<a name="rich_text"></a>
```yaml
---
type: class-extension
name: rich text
suite: Extended Text Suite
---
```

## Class Extension: rich text

**Description:** Rich (styled) text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| baseline offset | Number of points shifted above or below the normal baseline. | real | read/write |
| background | The background color of the first character. | RGB color, missing value | read/write |
| first line head indent | Paragraph first line head indent of the text (always 0 or positive) | real | read/write |
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The foreground color of the first character. | RGB color, missing value | read/write |
| head indent | Paragraph head indent of the text (always 0 or positive). | real | read/write |
| underlined | Is the first character underlined? | boolean | read/write |
| line spacing | Line spacing of the text. | real | read/write |
| multiple line height | Multiple line height of the text. | real | read/write |
| maximum line height | Maximum line height of the text. | real | read/write |
| minimum line height | Minimum line height of the text. | real | read/write |
| paragraph spacing | Paragraph spacing of the text. | real | read/write |
| superscript | The superscript level of the text. | integer | read/write |
| tail indent | Paragraph tail indent of the text. If positive, it's the absolute line width. If 0 or negative, it's added to the line width. | real | read/write |
| text content | The actual text content. | text, missing value | read/write |
| alignment | Alignment of the text. | text alignment | read/write |
| URL | Link of the text. | text, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
### Responds To
- **Command:** bold
- **Command:** italicize
- **Command:** plain
- **Command:** reformat
- **Command:** scroll to visible
- **Command:** strike
- **Command:** unbold
- **Command:** underline
- **Command:** unitalicize
- **Command:** unstrike
- **Command:** ununderline
<a name="attribute_run"></a>
```yaml
---
type: class-extension
name: attribute run
suite: Extended Text Suite
---
```

## Class Extension: attribute run

**Description:** This subdivides the text into chunks that all have the same attributes.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| baseline offset | Number of points shifted above or below the normal baseline. | real | read/write |
| background | The background color of the first character. | RGB color, missing value | read/write |
| first line head indent | Paragraph first line head indent of the text (always 0 or positive) | real | read/write |
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The foreground color of the first character. | RGB color, missing value | read/write |
| head indent | Paragraph head indent of the text (always 0 or positive). | real | read/write |
| underlined | Is the first character underlined? | boolean | read/write |
| line spacing | Line spacing of the text. | real | read/write |
| multiple line height | Multiple line height of the text. | real | read/write |
| maximum line height | Maximum line height of the text. | real | read/write |
| minimum line height | Minimum line height of the text. | real | read/write |
| paragraph spacing | Paragraph spacing of the text. | real | read/write |
| superscript | The superscript level of the text. | integer | read/write |
| tail indent | Paragraph tail indent of the text. If positive, it's the absolute line width. If 0 or negative, it's added to the line width. | real | read/write |
| text content | The actual text content. | text, missing value | read/write |
| alignment | Alignment of the text. | text alignment | read/write |
| URL | Link of the text. | text, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
### Responds To
- **Command:** bold
- **Command:** italicize
- **Command:** plain
- **Command:** reformat
- **Command:** scroll to visible
- **Command:** strike
- **Command:** unbold
- **Command:** underline
- **Command:** unitalicize
- **Command:** unstrike
- **Command:** ununderline
<a name="character"></a>
```yaml
---
type: class-extension
name: character
suite: Extended Text Suite
---
```

## Class Extension: character

**Description:** This subdivides the text into characters.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| baseline offset | Number of points shifted above or below the normal baseline. | real | read/write |
| background | The background color of the first character. | RGB color, missing value | read/write |
| first line head indent | Paragraph first line head indent of the text (always 0 or positive) | real | read/write |
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The foreground color of the first character. | RGB color, missing value | read/write |
| head indent | Paragraph head indent of the text (always 0 or positive). | real | read/write |
| underlined | Is the first character underlined? | boolean | read/write |
| line spacing | Line spacing of the text. | real | read/write |
| multiple line height | Multiple line height of the text. | real | read/write |
| maximum line height | Maximum line height of the text. | real | read/write |
| minimum line height | Minimum line height of the text. | real | read/write |
| paragraph spacing | Paragraph spacing of the text. | real | read/write |
| superscript | The superscript level of the text. | integer | read/write |
| tail indent | Paragraph tail indent of the text. If positive, it's the absolute line width. If 0 or negative, it's added to the line width. | real | read/write |
| text content | The actual text content. | text, missing value | read/write |
| alignment | Alignment of the text. | text alignment | read/write |
| URL | Link of the text. | text, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
### Responds To
- **Command:** bold
- **Command:** italicize
- **Command:** plain
- **Command:** reformat
- **Command:** scroll to visible
- **Command:** strike
- **Command:** unbold
- **Command:** underline
- **Command:** unitalicize
- **Command:** unstrike
- **Command:** ununderline
<a name="paragraph"></a>
```yaml
---
type: class-extension
name: paragraph
suite: Extended Text Suite
---
```

## Class Extension: paragraph

**Description:** This subdivides the text into paragraphs.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| baseline offset | Number of points shifted above or below the normal baseline. | real | read/write |
| background | The background color of the first character. | RGB color, missing value | read/write |
| first line head indent | Paragraph first line head indent of the text (always 0 or positive) | real | read/write |
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The foreground color of the first character. | RGB color, missing value | read/write |
| head indent | Paragraph head indent of the text (always 0 or positive). | real | read/write |
| underlined | Is the first character underlined? | boolean | read/write |
| line spacing | Line spacing of the text. | real | read/write |
| multiple line height | Multiple line height of the text. | real | read/write |
| maximum line height | Maximum line height of the text. | real | read/write |
| minimum line height | Minimum line height of the text. | real | read/write |
| paragraph spacing | Paragraph spacing of the text. | real | read/write |
| superscript | The superscript level of the text. | integer | read/write |
| tail indent | Paragraph tail indent of the text. If positive, it's the absolute line width. If 0 or negative, it's added to the line width. | real | read/write |
| text content | The actual text content. | text, missing value | read/write |
| alignment | Alignment of the text. | text alignment | read/write |
| URL | Link of the text. | text, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
### Responds To
- **Command:** bold
- **Command:** italicize
- **Command:** plain
- **Command:** reformat
- **Command:** scroll to visible
- **Command:** strike
- **Command:** unbold
- **Command:** underline
- **Command:** unitalicize
- **Command:** unstrike
- **Command:** ununderline
<a name="word"></a>
```yaml
---
type: class-extension
name: word
suite: Extended Text Suite
---
```

## Class Extension: word

**Description:** This subdivides the text into words.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| baseline offset | Number of points shifted above or below the normal baseline. | real | read/write |
| background | The background color of the first character. | RGB color, missing value | read/write |
| first line head indent | Paragraph first line head indent of the text (always 0 or positive) | real | read/write |
| font | The name of the font of the first character. | text, missing value | read/write |
| size | The size in points of the first character. | number | read/write |
| color | The foreground color of the first character. | RGB color, missing value | read/write |
| head indent | Paragraph head indent of the text (always 0 or positive). | real | read/write |
| underlined | Is the first character underlined? | boolean | read/write |
| line spacing | Line spacing of the text. | real | read/write |
| multiple line height | Multiple line height of the text. | real | read/write |
| maximum line height | Maximum line height of the text. | real | read/write |
| minimum line height | Minimum line height of the text. | real | read/write |
| paragraph spacing | Paragraph spacing of the text. | real | read/write |
| superscript | The superscript level of the text. | integer | read/write |
| tail indent | Paragraph tail indent of the text. If positive, it's the absolute line width. If 0 or negative, it's added to the line width. | real | read/write |
| text content | The actual text content. | text, missing value | read/write |
| alignment | Alignment of the text. | text alignment | read/write |
| URL | Link of the text. | text, missing value | read/write |

### Elements
- **Type:** attachment
- **Type:** attribute run
- **Type:** character
- **Type:** paragraph
- **Type:** word
### Responds To
- **Command:** bold
- **Command:** italicize
- **Command:** plain
- **Command:** reformat
- **Command:** scroll to visible
- **Command:** strike
- **Command:** unbold
- **Command:** underline
- **Command:** unitalicize
- **Command:** unstrike
- **Command:** ununderline
## DEVONthink Suite

**Description:** Classes and commands for the DEVONthink application

### Sample Code
```applescript
-- It's recommended to use the id instead of the application's name or bundle identifier to make the script compatible to future versions.
tell application id "DNtp"
	-- Process selection
	repeat with theRecord in selected records
	end repeat

	-- Process Markdown documents of current database
	repeat with theRecord in (contents of current database whose record type is markdown)
	end repeat

	-- Execute JavaScript in AppleScript
	set theJavaScript to "var app = Application.currentApplication();
		app.includeStandardAdditions = true;
		app.displayDialog(\"JavaScript Code\");"
	run script theJavaScript in "JavaScript"
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	theApp.includeStandardAdditions = true;

	// Process selection
	let theSelection = theApp.selectedRecords();
	theSelection.forEach (r => {
	})

	// Process Markdown documents of current database
	let theDocs = theApp.currentDatabase.contents.whose({ _match: [ObjectSpecifier().recordType, "markdown"] })();
	theDocs.forEach (r => {
	})

	// Execute AppleScript in JavaScript
	const theAppleScript = 'display dialog "AppleScript Code"';
	var app = Application.currentApplication();
	app.includeStandardAdditions = true;
	app.runScript(theAppleScript, { 'in': "AppleScript" });
})();
```

<a name="add_custom_meta_data"></a>
```yaml
---
type: command
name: add custom meta data
suite: DEVONthink Suite
---
```

## Command: add custom meta data

**Description:** Add user-defined metadata to a record or updates already existing metadata of a record. Setting a value for an unknown key automatically adds a definition to Settings > Data.

### Sample Code
```applescript
tell application id "DNtp"
	set theDate to current date
	repeat with theRecord in selected records
		add custom meta data "Me" for "author" to theRecord
		add custom meta data theDate for "date" to theRecord
		add custom meta data 3.14 for "price" to theRecord
	end repeat
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const theRecords = theApp.selectedRecords();
	const theDate = new Date();
	theRecords.forEach (r => {
		theApp.addCustomMetaData("Me",{for: 'author', to:r});
		theApp.addCustomMetaData(theDate,{for: 'date', to:r});
		theApp.addCustomMetaData(3.14,{for: 'price', to:r});
	})
})();
```

### Direct Parameter
- **Description:** The value to add.
- **Types:** rich text, text, number, integer, real, boolean, date
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for | The key for the user-defined value. | text | No |
| to | The record. | record | No |
| as | The desired format. Either 'text' (default), 'richtext', 'string', 'uuid', 'url', 'crosslink', 'date', 'real', 'int', 'bool', 'set', 'countries' or 'languages'. | text, missing value | Yes |

### Result
- **Description:** True if adding was successful, false if not.
- **Types:** boolean
### See Also
- [get custom meta data](#get_custom_meta_data)
<a name="add_download"></a>
```yaml
---
type: command
name: add download
suite: DEVONthink Suite
---
```

## Command: add download

**Description:** Add a URL to the download manager.

### Direct Parameter
- **Description:** The URL to add.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| automatic | Automatic or user (default) download. | boolean | Yes |
| password | The password for protected websites. | text, missing value | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |
| user | The user name for protected websites. | text, missing value | Yes |

### Result
- **Description:** True if adding was successful, false if not.
- **Types:** boolean
<a name="add_reading_list"></a>
```yaml
---
type: command
name: add reading list
suite: DEVONthink Suite
---
```

## Command: add reading list

**Description:** Add record or URL to reading list.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record. Only documents are supported. | record, missing value | Yes |
| URL | The URL of the webpage. | text, missing value | Yes |
| title | The title of the webpage. | text, missing value | Yes |

### Result
- **Description:** True if adding was successful, false if not.
- **Types:** boolean
<a name="add_reminder"></a>
```yaml
---
type: command
name: add reminder
suite: DEVONthink Suite
---
```

## Command: add reminder

**Description:** Add a new reminder to a record.

### Sample Code
```applescript
tell application id "DNtp"
	set due_date to current date
	set due_date to due_date + 3600 * 24
	repeat with theRecord in selected records
		add reminder {schedule:once, alarm:alert, alarm string:"Test", due date:due_date} to theRecord
	end repeat
end tell
```

```javascript
(() => {
	const theApp = Application('DEVONthink');
	const theRecords = theApp.selectedRecords();
	const due_date = new Date(new Date().getTime() + 3600 * 24 * 1000);
	theRecords.forEach (r => {
		let reminder = theApp.addReminder({schedule: 'once', alarm: 'alert', 'alarm string': 'Test', 'due date': due_date},{to:r});
	})
})();
```

### Direct Parameter
- **Description:** The properties of the reminder. At least 'schedule' and 'due date' are required.
- **Types:** dictionary
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The record. | record | No |

### Result
- **Description:** The added reminder.
- **Types:** reminder, missing value
<a name="add_row"></a>
```yaml
---
type: command
name: add row
suite: DEVONthink Suite
---
```

## Command: add row

**Description:** Add new row to current sheet.

### Sample Code
```applescript
tell application id "DNtp"
	tell think window 1
		add row cells {"Dummy"}
	end tell
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const theWindow = theApp.thinkWindows()[0];
	theApp.addRow(theWindow,{cells:"Dummy"});
})();
```

### Direct Parameter
- **Description:** The tab or window.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| cells | Cells of new row. | text | No |

### Result
- **Description:** True if adding was successful, false if not.
- **Types:** boolean
### See Also
- [delete row at](#delete_row_at)
<a name="check_file_integrity_of"></a>
```yaml
---
type: command
name: check file integrity of
suite: DEVONthink Suite
---
```

## Command: check file integrity of

**Description:** Check file integrity of database.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| database | The database to check. | database | No |

### Result
- **Description:** Number of files having an invalid content hash.
- **Types:** integer
### See Also
- [optimize](#optimize)
- [verify](#verify)
<a name="classify"></a>
```yaml
---
type: command
name: classify
suite: DEVONthink Suite
---
```

## Command: classify

**Description:** Get a list of classification proposals.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to classify. | record | No |
| in | The database. Uses all databases if not specified. | database, missing value | Yes |
| comparison | The comparison to use (default is data comparison). | comparison type | Yes |
| tags | Propose ordinary tags instead of groups (off by default). | boolean | Yes |

### Result
- **Description:** The proposed groups or tags.
- **Types:** parent, missing value
### See Also
- [compare](#compare)
<a name="compare"></a>
```yaml
---
type: command
name: compare
suite: DEVONthink Suite
---
```

## Command: compare

**Description:** Get a list of similar records, either by specifying a record or a content.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to compare. | content, missing value | Yes |
| content | The content to compare. | text, missing value | Yes |
| to | The database. Uses all databases if not specified. | database, missing value | Yes |
| comparison | The comparison to use (default is data comparison). | comparison type | Yes |

### Result
- **Description:** The similar records.
- **Types:** content, missing value
### See Also
- [classify](#classify)
<a name="compress"></a>
```yaml
---
type: command
name: compress
suite: DEVONthink Suite
---
```

## Command: compress

**Description:** Compress a database into a Zip archive.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| database | The database to compress. | database | No |
| password | The required password for encrypted or audit-proof databases. | text, missing value | Yes |
| to | POSIX path or file URL of Zip archive. The path extension '.zip' is required. | text | No |

### Result
- **Description:** True if compressing was successful, false if not.
- **Types:** boolean
<a name="convert"></a>
```yaml
---
type: command
name: convert
suite: DEVONthink Suite
---
```

## Command: convert

**Description:** Convert a record to plain or rich text, formatted note or HTML and create a new record afterwards.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record(s) to convert. | content, content | No |
| to | The desired format (default simple). | convert type | Yes |
| in | The destination group for the converted record. Parents of the record to convert are used if not specified. | parent, missing value | Yes |

### Result
- **Description:** The converted records.
- **Types:** content, content, missing value
<a name="convert_feed_to_html"></a>
```yaml
---
type: command
name: convert feed to HTML
suite: DEVONthink Suite
---
```

## Command: convert feed to HTML

**Description:** Convert a RSS, RDF, JSON or Atom feed to HTML.

### Direct Parameter
- **Description:** The source code of the feed.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the feed. | text, missing value | Yes |

### Result
- **Description:** The converted HTML.
- **Types:** text, missing value
<a name="create_database"></a>
```yaml
---
type: command
name: create database
suite: DEVONthink Suite
---
```

## Command: create database

**Description:** Create a new database.

### Direct Parameter
- **Description:** POSIX file path of database. Suffix has to be either .dtBase2, .dtSparse (encrypted) or .dtArchive (encrypted & audit-proof).
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| encryption key | The encryption key. | text, missing value | Yes |
| size | The maximal size of encrypted databases in MB. | integer | Yes |

### Result
- **Description:** The created database.
- **Types:** database, missing value
<a name="create_formatted_note_from"></a>
```yaml
---
type: command
name: create formatted note from
suite: DEVONthink Suite
---
```

## Command: create formatted note from

**Description:** Create a new formatted note from a web page.

### Direct Parameter
- **Description:** The URL to download.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| agent | The user agent. | text, missing value | Yes |
| in | The destination group for the new record. Uses incoming group or group selector if not specified. | parent, missing value | Yes |
| name | The name for the new record. | text, missing value | Yes |
| readability | Declutter page layout. | boolean | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |
| source | The HTML source. | text, missing value | Yes |

### Result
- **Description:** The created record.
- **Types:** content, missing value
<a name="create_location"></a>
```yaml
---
type: command
name: create location
suite: DEVONthink Suite
---
```

## Command: create location

**Description:** Create a hierarchy of groups if necessary.

### Direct Parameter
- **Description:** The hierarchy as a POSIX path (/ in names has to be replaced with \/, see location property).
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The destination database or group. Uses current database if not specified. | database, parent, missing value | Yes |

### Result
- **Description:** The existing or created group.
- **Types:** parent, missing value
### See Also
- [exists record at](#exists_record_at)
- [get record at](#get_record_at)
<a name="create_markdown_from"></a>
```yaml
---
type: command
name: create Markdown from
suite: DEVONthink Suite
---
```

## Command: create Markdown from

**Description:** Create a Markdown document from a web resource.

### Direct Parameter
- **Description:** The URL to download.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| agent | The user agent. | text, missing value | Yes |
| in | The destination group for the new record. Uses incoming group or group selector if not specified. | parent, missing value | Yes |
| name | The name for the new record. | text, missing value | Yes |
| readability | Declutter page layout. | boolean | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |

### Result
- **Description:** The created record.
- **Types:** content, missing value
<a name="create_pdf_document_from"></a>
```yaml
---
type: command
name: create PDF document from
suite: DEVONthink Suite
---
```

## Command: create PDF document from

**Description:** Create a new PDF document with or without pagination from a web resource.

### Direct Parameter
- **Description:** The URL to download.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| agent | The user agent. | text, missing value | Yes |
| in | The destination group for the new record. Uses incoming group or group selector if not specified. | parent, missing value | Yes |
| name | The name for the new record. | text, missing value | Yes |
| pagination | Paginate PDF document or not. | boolean | Yes |
| readability | Declutter page layout. | boolean | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |
| width | The preferred width for the PDF document in points. | number | Yes |

### Result
- **Description:** The clipped record.
- **Types:** content, missing value
<a name="create_record_with"></a>
```yaml
---
type: command
name: create record with
suite: DEVONthink Suite
---
```

## Command: create record with

**Description:** Create a new record.

### Sample Code
```applescript
tell application id "DNtp"
	set theGroup to current group
	set theBookmark to create record with {name:"DEVONtechnologies", type:bookmark, URL:"https://www.devon-technologies.com", comment:"Our website.", tags:"DEVONtechnologies,DEVONthink,DEVONagent"} in theGroup
	set theNote to create record with {name:"Note", |type|:"markdown", content:"# Headline" & return & return & "Type your notes here."} in theGroup
	set theDocument to create record with {name:"Demo", aliases:"Demos", record type:txt, plain text:"Dummy", date:(current date), tags:"A,B,C"} in theGroup
	set theSmartGroup to create record with {name:"All documents", record type:smart group, search predicates:"kind:any"} in theGroup
	set theSheet to create record with {name:"Sheet", record type:sheet, columns:{"Name#text", "ID#uuid", "Num#int"}, cells:{{"First", "1", "1.23"}, {"Second", "2", "4.56"}}} in theGroup
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const theGroup = theApp.currentGroup();
	let theBookmark  = theApp.createRecordWith({name:"DEVONtechnologies", 'record type':"bookmark", URL:"https://www.devon-technologies.com", comment:"Our website.", tags:"DEVONtechnologies,DEVONthink,DEVONagent"},{in:theGroup});
	let theNote  = theApp.createRecordWith({'name':"Note", type:"markdown", content:"# Headline\n\nType your notes here."},{in:theGroup});
	let theSheet = theApp.createRecordWith({'name': "Sheet", type: "sheet", columns:['Name#text','ID#uuid','Num#int'],cells:[['First','1','1.23'],['Second','2','4.56']]},{in:theGroup});
})();
```

### Direct Parameter
- **Description:** The properties of the record. At least 'type' or 'record type' is required, its value can be also specified as a string.
- **Types:** dictionary
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The destination group for the new record. Uses incoming group or group selector if not specified. | parent, missing value | Yes |

### Result
- **Description:** The created record.
- **Types:** record, missing value
### See Also
- [delete](#delete)
<a name="create_thumbnail"></a>
```yaml
---
type: command
name: create thumbnail
suite: DEVONthink Suite
---
```

## Command: create thumbnail

**Description:** Create or update existing thumbnail of a record. Thumbnailing is performed asynchronously in the background.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for | The record. | record | No |

### Result
- **Description:** True if thumbnailing was successful, false if not.
- **Types:** boolean
### See Also
- [update thumbnail](#update_thumbnail)
- [delete thumbnail](#delete_thumbnail)
<a name="create_web_document_from"></a>
```yaml
---
type: command
name: create web document from
suite: DEVONthink Suite
---
```

## Command: create web document from

**Description:** Create a new record (picture, PDF or web archive) from a web resource.

### Direct Parameter
- **Description:** The URL to download.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| agent | The user agent. | text, missing value | Yes |
| in | The destination group for the new record. Uses incoming group or group selector if not specified. | parent, missing value | Yes |
| name | The name for the new record. | text, missing value | Yes |
| readability | Declutter page layout. | boolean | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |

### Result
- **Description:** The clipped record.
- **Types:** content, missing value
<a name="delete"></a>
```yaml
---
type: command
name: delete
suite: DEVONthink Suite
---
```

## Command: delete

**Description:** Delete all instances of a record from the database or one instance from the specified group.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record(s) to delete. | record, record | No |
| in | The parent group of this instance. | parent, missing value | Yes |

### Result
- **Description:** True if deleting was successful, false if not.
- **Types:** boolean
### See Also
- [create record with](#create_record_with)
<a name="delete_row_at"></a>
```yaml
---
type: command
name: delete row at
suite: DEVONthink Suite
---
```

## Command: delete row at

**Description:** Remove row at specified position from current sheet.

### Sample Code
```applescript
tell application id "DNtp"
	tell current tab of think window 1
		delete row at position 1
	end tell
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const theWindow = theApp.thinkWindows()[0];
	theApp.deleteRowAt(theWindow,{position:1});
})();
```

### Direct Parameter
- **Description:** The tab or window.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| position | Position of row (1...n). | integer | No |

### Result
- **Description:** True if deleting was successful, false if not.
- **Types:** boolean
### See Also
- [add row](#add_row)
<a name="delete_thumbnail"></a>
```yaml
---
type: command
name: delete thumbnail
suite: DEVONthink Suite
---
```

## Command: delete thumbnail

**Description:** Delete existing thumbnail of a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| of | The record. | record | No |

### Result
- **Description:** True if deleting was successful, false if not.
- **Types:** boolean
### See Also
- [create thumbnail](#create_thumbnail)
- [update thumbnail](#update_thumbnail)
<a name="delete_workspace"></a>
```yaml
---
type: command
name: delete workspace
suite: DEVONthink Suite
---
```

## Command: delete workspace

**Description:** Delete a workspace.

### Direct Parameter
- **Description:** The name of the workspace.
- **Types:** text
### Result
- **Description:** True if deleting was successful, false if not.
- **Types:** boolean
### See Also
- [save workspace](#save_workspace)
- [load workspace](#load_workspace)
<a name="do_javascript"></a>
```yaml
---
type: command
name: do JavaScript
suite: DEVONthink Suite
---
```

## Command: do JavaScript

**Description:** Executes a string of JavaScript code (optionally in the web view of a think window).

### Direct Parameter
- **Description:** The code.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The think window that the JavaScript should be executed in. | think window, missing value | Yes |

### Result
- **Description:** The result returned by the JavaScript code.
- **Types:** text, missing value
<a name="download_image_for_prompt"></a>
```yaml
---
type: command
name: download image for prompt
suite: DEVONthink Suite
---
```

## Command: download image for prompt

**Description:** Download image for a prompt.

### Sample Code
```applescript
tell application id "DNtp"
	set thePrompt to "A 1934 canary-yellow Ford sitting at a stop light next to a red Ford Fusion. High noon on a small town main street."
	set theImageData to download image for prompt thePrompt engine FluxPro size "1344x768"
	set theRecord to create record with {name:"Fords", type:picture, data:theImageData} in current group
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const thePrompt = "A 1934 canary-yellow Ford sitting at a stop light next to a red Ford Fusion. High noon on a small town main street.";
	let theImageData = theApp.downloadImageForPrompt(thePrompt,{'engine':"FluxPro",'size':"1344x768"});
	let theRecord = theApp.createRecordWith({name:"Fords", 'type':"picture", 'data':theImageData},{in:theApp.currentGroup()});
})();
```

### Direct Parameter
- **Description:** The prompt to send.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| prompt strength | Prompt strength (0.0-1.0) when using 'image' parameter. 1.0 uses only the text prompt, 0.0 only the image, default is 0.15. Only supported by Flux Pro Ultra and Stable Diffusion. | real | Yes |
| image | Optional image data or image URL to send. Only supported by Flux Pro/Pro Ultra, GPT-Image-1 and Stable Diffusion Large/Turbo. | raw data, text, missing value | Yes |
| engine | The desired engine, default depends on settings. | image engine | Yes |
| quality | The quality of the image. Either 'standard' (default) or 'hd'. Only supported by Dall-E 3, GPT-Image-1, Flux Schnell/Pro & Stable Diffusion. Default quality depends on settings. | text | Yes |
| size | The size of the image. Size is automatically choosen in case of image data if not specified, otherwise default size depends on settings. | text | Yes |
| style | The style of the image. Default style depends on settings. | text | Yes |
| seed | Set for reproducible generation, otherwise random seed. Only supported by Flux and Stable Diffusion. | integer | Yes |

### Result
- **Description:** The received image data.
- **Types:** raw data, missing value
### See Also
- [get chat response for message](#get_chat_response_for_message)
- [display chat dialog](#display_chat_dialog)
<a name="download_json_from"></a>
```yaml
---
type: command
name: download JSON from
suite: DEVONthink Suite
---
```

## Command: download JSON from

**Description:** Download a JSON object.

### Direct Parameter
- **Description:** The URL of the JSON object to download.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| agent | The user agent. | text, missing value | Yes |
| method | The HTTP method ('GET' by default) | text, missing value | Yes |
| password | The password for protected websites. | text, missing value | Yes |
| post | A dictionary containing key-value pairs for HTTP POST actions. | dictionary, missing value | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |
| user | The user name for protected websites. | text, missing value | Yes |

### Result
- **Description:** The downloaded JSON object.
- **Types:** dictionary, missing value
<a name="download_markup_from"></a>
```yaml
---
type: command
name: download markup from
suite: DEVONthink Suite
---
```

## Command: download markup from

**Description:** Download an HTML or XML page (including RSS, RDF or Atom feeds).

### Direct Parameter
- **Description:** The URL of the HTML or XML page to download.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| agent | The user agent. | text, missing value | Yes |
| encoding | The encoding of the page (default UTF-8). | text, missing value | Yes |
| method | The HTTP method ('GET' by default) | text, missing value | Yes |
| password | The password for protected websites. | text, missing value | Yes |
| post | A dictionary containing key-value pairs for HTTP POST actions. | dictionary, missing value | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |
| user | The user name for protected websites. | text, missing value | Yes |

### Result
- **Description:** The downloaded XML/HTML.
- **Types:** text, missing value
<a name="download_url"></a>
```yaml
---
type: command
name: download URL
suite: DEVONthink Suite
---
```

## Command: download URL

**Description:** Download a URL.

### Sample Code
```applescript
tell application "DEVONthink"
	set theURL to "https://www.devontechnologies.com/assets/images/appicons/300900000.png"
	set theData to download URL theURL
	set theRecord to create record with {name:"Test", URL:theURL, type:picture, content:theData} in current group
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	theApp.includeStandardAdditions = true;

	let theURL = "https://www.devontechnologies.com/assets/images/appicons/300900000.png";
	let theData = theApp.downloadURL(theURL);
	let theRecord = theApp.createRecordWith({"name":"Test", "URL":theURL, "type":"picture", "data":theData},{in:theApp.currentGroup});
})();
```

### Direct Parameter
- **Description:** The URL to download.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| agent | The user agent. | text, missing value | Yes |
| method | The HTTP method ('GET' by default) | text, missing value | Yes |
| password | The password for protected websites. | text, missing value | Yes |
| post | A dictionary containing key-value pairs for HTTP POST actions. | dictionary, missing value | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |
| user | The user name for protected websites. | text, missing value | Yes |

### Result
- **Description:** The downloaded data.
- **Types:** raw data, missing value
<a name="display_authentication_dialog"></a>
```yaml
---
type: command
name: display authentication dialog
suite: DEVONthink Suite
---
```

## Command: display authentication dialog

**Description:** Display a dialog to enter a username and its password.

### Direct Parameter
- **Description:** The info for the dialog.
- **Types:** text, missing value
### Result
- **Description:** The authentication result.
- **Types:** authentication result, missing value
<a name="display_chat_dialog"></a>
```yaml
---
type: command
name: display chat dialog
suite: DEVONthink Suite
---
```

## Command: display chat dialog

**Description:** Display a dialog to show the response for a chat prompt for the current document. Either the selected text or the complete document is used.

### Direct Parameter
- **Description:** The tab or window.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | The title of the dialog. | text, missing value | Yes |
| role | The desired role for the chat. | text, missing value | Yes |
| prompt | The desired prompt. | text, missing value | No |
| model | The desired model. | text, missing value | Yes |
| engine | The desired engine. | chat engine | Yes |
| temperature | The desired temperature (0-2). Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. | real | Yes |

### Result
- **Description:** The text content of the response.
- **Types:** text, missing value
### See Also
- [get chat models for engine](#get_chat_models_for_engine)
- [get chat response for message](#get_chat_response_for_message)
<a name="display_date_editor"></a>
```yaml
---
type: command
name: display date editor
suite: DEVONthink Suite
---
```

## Command: display date editor

**Description:** Display a dialog to enter a date.

### Direct Parameter
- **Description:** The title of the dialog. By default the application name.
- **Types:** text, missing value
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| default date | The default date. | date, missing value | Yes |
| info | The info for the dialog. | text, missing value | Yes |

### Result
- **Description:** The entered date.
- **Types:** date, missing value
<a name="display_group_selector"></a>
```yaml
---
type: command
name: display group selector
suite: DEVONthink Suite
---
```

## Command: display group selector

**Description:** Display a dialog to select a (destination) group.

### Direct Parameter
- **Description:** The title of the dialog.
- **Types:** text, missing value
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| buttons | The labels for the cancel and select buttons. | text, missing value | Yes |
| for | The database. All open databases are used if not specified. | database, missing value | Yes |
| name | Show field to enter a name (off by default) | boolean | Yes |
| tags | Show field to enter tags (off by default) | boolean | Yes |

### Result
- **Description:** The selected group (without 'name' and 'tags' parameters) due to compatibility to older versions or a group selector result (with 'name' and/or 'tags' parameters).
- **Types:** parent, group selector result, missing value
<a name="display_name_editor"></a>
```yaml
---
type: command
name: display name editor
suite: DEVONthink Suite
---
```

## Command: display name editor

**Description:** Display a dialog to enter a name.

### Direct Parameter
- **Description:** The title of the dialog. By default the application name.
- **Types:** text, missing value
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| default answer | The default editable name. | text, missing value | Yes |
| info | The info for the dialog. | text, missing value | Yes |

### Result
- **Description:** The entered name.
- **Types:** text, missing value
<a name="duplicate"></a>
```yaml
---
type: command
name: duplicate
suite: DEVONthink Suite
---
```

## Command: duplicate

**Description:** Duplicate a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record(s) to duplicate. Indexed items are not supported by audit-proof databases. | record, record | No |
| to | The destination group which doesn't have to be in the same database. | parent | No |

### Result
- **Description:** The duplicated record(s).
- **Types:** record, record, missing value
### See Also
- [replicate](#replicate)
- [move](#move)
<a name="exists_record_at"></a>
```yaml
---
type: command
name: exists record at
suite: DEVONthink Suite
---
```

## Command: exists record at

**Description:** Check if at least one record exists at the specified location.

### Direct Parameter
- **Description:** The location of the record as a POSIX path (/ in names has to be replaced with \/, see location property).
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The base database or group. Uses current database if not specified. | database, parent, missing value | Yes |

### Result
- **Description:** True if records exists, false if not.
- **Types:** boolean
### See Also
- [create location](#create_location)
- [get record at](#get_record_at)
<a name="exists_record_with_comment"></a>
```yaml
---
type: command
name: exists record with comment
suite: DEVONthink Suite
---
```

## Command: exists record with comment

**Description:** Check if at least one record with the specified comment exists.

### Direct Parameter
- **Description:** The comment.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified | database, missing value | Yes |

### Result
- **Description:** True if records exists, false if not.
- **Types:** boolean
### See Also
- [lookup records with comment](#lookup_records_with_comment)
<a name="exists_record_with_content_hash"></a>
```yaml
---
type: command
name: exists record with content hash
suite: DEVONthink Suite
---
```

## Command: exists record with content hash

**Description:** Check if at least one record with the specified content hash exists.

### Direct Parameter
- **Description:** The content hash.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified | database, missing value | Yes |

### Result
- **Description:** True if records exists, false if not.
- **Types:** boolean
### See Also
- [lookup records with content hash](#lookup_records_with_content_hash)
<a name="exists_record_with_file"></a>
```yaml
---
type: command
name: exists record with file
suite: DEVONthink Suite
---
```

## Command: exists record with file

**Description:** Check if at least one record with the specified last path component exists.

### Direct Parameter
- **Description:** The filename.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified | database, missing value | Yes |

### Result
- **Description:** True if records exists, false if not.
- **Types:** boolean
### See Also
- [lookup records with file](#lookup_records_with_file)
<a name="exists_record_with_path"></a>
```yaml
---
type: command
name: exists record with path
suite: DEVONthink Suite
---
```

## Command: exists record with path

**Description:** Check if at least one record with the specified path exists.

### Direct Parameter
- **Description:** The path.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified. | database, missing value | Yes |

### Result
- **Description:** True if records exists, false if not.
- **Types:** boolean
### See Also
- [lookup records with path](#lookup_records_with_path)
<a name="exists_record_with_url"></a>
```yaml
---
type: command
name: exists record with URL
suite: DEVONthink Suite
---
```

## Command: exists record with URL

**Description:** Check if at least one record with the specified URL exists.

### Direct Parameter
- **Description:** The URL (or path).
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified. | database, missing value | Yes |

### Result
- **Description:** True if records exists, false if not.
- **Types:** boolean
### See Also
- [lookup records with URL](#lookup_records_with_url)
<a name="export"></a>
```yaml
---
type: command
name: export
suite: DEVONthink Suite
---
```

## Command: export

**Description:** Export a record (and its children).

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to export. | record | No |
| to | The destination directory as a POSIX path or file URL. DEVONthink creates the destination if necessary. | text | No |
| DEVONtech_Storage | Export 'DEVONtech_Storage' files which include all metadata (e.g. flag, label, locking, aliases, comments, exclusions, custom metadata etc.) for importing. On by default. | boolean | Yes |

### Result
- **Description:** The path of the exported record.
- **Types:** text, missing value
<a name="export_tags_of"></a>
```yaml
---
type: command
name: export tags of
suite: DEVONthink Suite
---
```

## Command: export tags of

**Description:** Export Finder tags of a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record. | record | No |

### Result
- **Description:** True if exporting was successful, false if not.
- **Types:** boolean
<a name="export_website"></a>
```yaml
---
type: command
name: export website
suite: DEVONthink Suite
---
```

## Command: export website

**Description:** Export a record (and its children) as a website.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to export. | record | No |
| to | The destination directory as a POSIX path or file URL. DEVONthink creates the destination if necessary. | text | No |
| template | Name of built-in template or full POSIX path of template. Uses Default template if not specified. | text, missing value | Yes |
| index pages | Create index pages. Off by default. | boolean | Yes |
| encoding | The encoding of the exported HTML pages (default UTF-8). | text, missing value | Yes |
| entities | Use HTML entities. Off by default. | boolean | Yes |

### Result
- **Description:** The path of the exported record.
- **Types:** text, missing value
<a name="extract_keywords_from"></a>
```yaml
---
type: command
name: extract keywords from
suite: DEVONthink Suite
---
```

## Command: extract keywords from

**Description:** Extract list of keywords from a record. The list is sorted by number of occurrences.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record. | record | No |
| barcodes | Include scanned barcodes. | boolean | Yes |
| existing tags | Include existing tags (and their aliases) found in the title, comment or text of the record. | boolean | Yes |
| hash tags | Include hash tags found in the title or text of the record. | boolean | Yes |
| image tags | Include suggested image tags. | boolean | Yes |

### Result
- **Description:** The extracted keywords.
- **Types:** text, missing value
<a name="get_cached_data_for_url"></a>
```yaml
---
type: command
name: get cached data for URL
suite: DEVONthink Suite
---
```

## Command: get cached data for URL

**Description:** Get cached data for URL of a resource which is part of a loaded webpage and its DOM tree, rendered in a think tab/window.

### Direct Parameter
- **Description:** The URL.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | The source think tab. Uses current tab of frontmost think window otherwise. | tab, missing value | Yes |

### Result
- **Description:** The cached data.
- **Types:** raw data, missing value
<a name="get_cell_at"></a>
```yaml
---
type: command
name: get cell at
suite: DEVONthink Suite
---
```

## Command: get cell at

**Description:** Get content of cell at specified position of current sheet.

### Sample Code
```applescript
tell application id "DNtp"
	tell think window 1
		set theValue to get cell at column 1 row 1
	end tell
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const theWindow = theApp.thinkWindows()[0];
	let theValue = theApp.getCellAt(theWindow,{column:1,row:1});
})();
```

### Direct Parameter
- **Description:** The tab or window.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| column | Either the index (1...n) or the name of the column of the cell. | integer, text | No |
| row | The row (1...n) of the cell. | integer | No |

### Result
- **Description:** The value of the cell.
- **Types:** text, missing value
### See Also
- [set cell at](#set_cell_at)
<a name="get_chat_models_for_engine"></a>
```yaml
---
type: command
name: get chat models for engine
suite: DEVONthink Suite
---
```

## Command: get chat models for engine

**Description:** Retrieve list of supported models of a chat engine.

### Direct Parameter
- **Description:** The engine.
- **Types:** chat engine
### Result
- **Description:** The retrieved list of models.
- **Types:** text
### See Also
- [get chat response for message](#get_chat_response_for_message)
- [display chat dialog](#display_chat_dialog)
<a name="get_chat_response_for_message"></a>
```yaml
---
type: command
name: get chat response for message
suite: DEVONthink Suite
---
```

## Command: get chat response for message

**Description:** Retrieve the response for a chat message. The chat might perform a web, Wikipedia or PubMed search if necessary depending on the parameters and the settings.

### Sample Code
```applescript
tell application id "DNtp"
	-- Process the selection at once. Alternatively use a loop and process each record on its own. This is slower but each record benefits of the complete context window.
	set theSelectionPrompt to "Create one detailed summary table combining data comprehensively from all selected documents. The Markdown table should have entries for brief narrative summary of each chapter, 3-bullet point summary of each chapter, pages, document name, and reference links as working hyperlinks."
	set theSelectionResponse to get chat response for message theSelectionPrompt record (selected records) temperature 0

	-- Process online images & web pages
	set theImageResponse to get chat response for message "Summarize this image" URL "https://www.devontechnologies.com/assets/images/appicons/300900000.png"
	set theWebResponse to get chat response for message "Summarize this web page" URL "https://www.devontechnologies.com/blog"
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	
	// Process the selection at once. Alternatively use a loop and process each record on its own. This is slower but each record benefits of the complete context window.
	let theSelectionPrompt = "Create one detailed summary table combining data comprehensively from all selected documents. The Markdown table should have entries for brief narrative summary of each chapter, 3-bullet point summary of each chapter, pages, document name, and reference links as working hyperlinks.";
	let theSelectionResponse = theApp.getChatResponseForMessage(theSelectionPrompt,{'record':theApp.selectedRecords(),'temperature':0});

	let theImageResponse = theApp.getChatResponseForMessage("Describe this image",{'url':"https://www.devontechnologies.com/assets/images/appicons/300900000.png"});
	let theWebResponse = theApp.getChatResponseForMessage("Summarize this web page",{'url':"https://www.devontechnologies.com/blog"});
})();
```

### Direct Parameter
- **Description:** The prompt or message(s) to send.
- **Types:** text, dictionary, dictionary
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | Optional text- or image-based document(s) or bookmark(s), a text prompt is required. NOTE: 'image' & 'URL' parameters are ignored. | record, record, missing value | Yes |
| mode | The record's contents to use. Either 'auto' (default), 'text' or 'vision'. | text, missing value | Yes |
| image | Optional image data to send, a text prompt is required. NOTE: Web, Wikipedia and PubMed search isn't available. | raw data, missing value | Yes |
| URL | Optional path or URL of a web page, a PDF document or an image to send, a text prompt is required. NOTE: Web, Wikipedia and PubMed search isn't available. | text, missing value | Yes |
| model | The desired model. | text, missing value | Yes |
| role | The desired role for the chat. | text, missing value | Yes |
| engine | The desired engine. | chat engine | Yes |
| temperature | The desired temperature (0-2). Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. Not used in case of tool usage. | real | Yes |
| thinking | Allow (default) or disallow optional thinking ("reasoning"). Without thinking the response might be faster and require less tokens. Only fully supported by Claude 3.7 Sonnet, Claude 4 Sonnet/Opus and Gemini 2.5 Flash/Pro. In case of O1, O3 and O4 the minimum effort is used if disallowed. | boolean | Yes |
| tool calls | Allow (default) or disallow usage of tool calls (depending on the used engine and model). Without tool calls the response might be faster and require less tokens but advanced features like searching aren't possible. Useful e.g. for JSON response format. | boolean | Yes |
| as | The response format to use. Either 'text' (default), 'JSON', 'HTML', 'message' or 'raw'. | text, missing value | Yes |

### Result
- **Description:** The received text, JSON object or raw message.
- **Types:** text, array, dictionary, missing value
### See Also
- [download image for prompt](#download_image_for_prompt)
- [get chat models for engine](#get_chat_models_for_engine)
- [display chat dialog](#display_chat_dialog)
<a name="get_concordance_of"></a>
```yaml
---
type: command
name: get concordance of
suite: DEVONthink Suite
---
```

## Command: get concordance of

**Description:** Get list of words of a record. Supports both documents and groups/feeds.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record. | content | No |
| sorted by | Sorting of words (default is weight). | concordance sorting | Yes |

### Result
- **Description:** The words.
- **Types:** text, missing value
<a name="get_custom_meta_data"></a>
```yaml
---
type: command
name: get custom meta data
suite: DEVONthink Suite
---
```

## Command: get custom meta data

**Description:** Get user-defined metadata from a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| default value | Default value if user-defined metadata does not yet exist, otherwise a missing value is returned. | rich text, text, number, integer, real, boolean, date, missing value | Yes |
| for | The key of the user-defined value. | text | No |
| from | The record. | record | No |

### Result
- **Description:** The custom metadata value.
- **Types:** date, rich text, text, number, integer, real, boolean, missing value
### See Also
- [add custom meta data](#add_custom_meta_data)
<a name="get_database_with_id"></a>
```yaml
---
type: command
name: get database with id
suite: DEVONthink Suite
---
```

## Command: get database with id

**Description:** Get database with the specified id.

### Direct Parameter
- **Description:** The scripting identifier.
- **Types:** integer
### Result
- **Description:** The database with the specified id.
- **Types:** database, missing value
<a name="get_database_with_uuid"></a>
```yaml
---
type: command
name: get database with uuid
suite: DEVONthink Suite
---
```

## Command: get database with uuid

**Description:** Get database with the specified uuid.

### Direct Parameter
- **Description:** The unique identifier.
- **Types:** text
### Result
- **Description:** The database with the specified UUID.
- **Types:** database, missing value
<a name="get_embedded_images_of"></a>
```yaml
---
type: command
name: get embedded images of
suite: DEVONthink Suite
---
```

## Command: get embedded images of

**Description:** Get the URLs of all embedded images of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the images. | text, missing value | Yes |
| file type | The desired type of the images (e.g. JPG, GIF, PNG, ...). | text, missing value | Yes |

### Result
- **Description:** The URLs of the images.
- **Types:** text, missing value
<a name="get_embedded_objects_of"></a>
```yaml
---
type: command
name: get embedded objects of
suite: DEVONthink Suite
---
```

## Command: get embedded objects of

**Description:** Get the URLs of all embedded objects of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the embedded objects | text, missing value | Yes |
| file type | The desired type of the objects (e.g. MOV). | text, missing value | Yes |

### Result
- **Description:** The URLs of the objects.
- **Types:** text, missing value
<a name="get_embedded_sheets_and_scripts_of"></a>
```yaml
---
type: command
name: get embedded sheets and scripts of
suite: DEVONthink Suite
---
```

## Command: get embedded sheets and scripts of

**Description:** Get the URLs of all embedded style sheets and scripts of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the style sheets and scripts. | text, missing value | Yes |
| file type | The desired type of the sheets/scripts (e.g. CSS). | text, missing value | Yes |

### Result
- **Description:** The URLs of the sheets and scripts.
- **Types:** text, missing value
<a name="get_favicon_of"></a>
```yaml
---
type: command
name: get favicon of
suite: DEVONthink Suite
---
```

## Command: get favicon of

**Description:** Get the favicon of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the favicon. | text, missing value | Yes |

### Result
- **Description:** The URL of the favicon.
- **Types:** text, missing value
<a name="get_feed_items_of"></a>
```yaml
---
type: command
name: get feed items of
suite: DEVONthink Suite
---
```

## Command: get feed items of

**Description:** Get the feed items of a RSS, RDF, JSON or Atom feed.

### Direct Parameter
- **Description:** The source code of the feed.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the feed. | text, missing value | Yes |

### Result
- **Description:** The items of the feed.
- **Types:** feed item, missing value
<a name="get_frames_of"></a>
```yaml
---
type: command
name: get frames of
suite: DEVONthink Suite
---
```

## Command: get frames of

**Description:** Get the URLs of all frames of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the frames. | text, missing value | Yes |

### Result
- **Description:** The URLs of the frames.
- **Types:** text, missing value
<a name="get_items_of_feed"></a>
```yaml
---
type: command
name: get items of feed
suite: DEVONthink Suite
---
```

## Command: get items of feed

**Description:** Get the items of a RSS, RDF, JSON or Atom feed as dictionaries. 'get feed items of' is recommended for new scripts.

### Direct Parameter
- **Description:** The source code of the feed.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the feed. | text, missing value | Yes |

### Result
- **Description:** The items of the feed.
- **Types:** dictionary, missing value
### See Also
- [get feed items of](#get_feed_items_of)
<a name="get_links_of"></a>
```yaml
---
type: command
name: get links of
suite: DEVONthink Suite
---
```

## Command: get links of

**Description:** Get the URLs of all links of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the links. | text, missing value | Yes |
| containing | The case sensitive string matched against the description of links. | text, missing value | Yes |
| file type | The desired type of the links (e.g. HTML, PHP, JPG, ...). | text, missing value | Yes |

### Result
- **Description:** The URLs of the links.
- **Types:** text, missing value
<a name="get_metadata_of"></a>
```yaml
---
type: command
name: get metadata of
suite: DEVONthink Suite
---
```

## Command: get metadata of

**Description:** Get the metadata of an HTML page or of a Markdown document.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page. | text, missing value | Yes |
| markdown | The source of the Markdown document. | text, missing value | Yes |

### Result
- **Description:** The metadata.
- **Types:** dictionary, missing value
<a name="get_record_at"></a>
```yaml
---
type: command
name: get record at
suite: DEVONthink Suite
---
```

## Command: get record at

**Description:** Search for record at the specified location.

### Direct Parameter
- **Description:** The location of the record as a POSIX path (/ in names has to be replaced with \/, see location property).
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The base database or group. Uses current database if not specified. | database, parent, missing value | Yes |

### Result
- **Description:** The record at the specified location.
- **Types:** record, missing value
### See Also
- [create location](#create_location)
- [exists record at](#exists_record_at)
<a name="get_record_with_id"></a>
```yaml
---
type: command
name: get record with id
suite: DEVONthink Suite
---
```

## Command: get record with id

**Description:** Get record with the specified id.

### Direct Parameter
- **Description:** The scripting identifier.
- **Types:** integer
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified. | database, missing value | Yes |

### Result
- **Description:** The record with the specified id.
- **Types:** record, missing value
<a name="get_record_with_uuid"></a>
```yaml
---
type: command
name: get record with uuid
suite: DEVONthink Suite
---
```

## Command: get record with uuid

**Description:** Get record with the specified uuid or item link.

### Direct Parameter
- **Description:** The unique identifier or item link.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses all databases if not specified. | database, missing value | Yes |

### Result
- **Description:** The record with the specified UUID.
- **Types:** record, missing value
<a name="get_rich_text_of"></a>
```yaml
---
type: command
name: get rich text of
suite: DEVONthink Suite
---
```

## Command: get rich text of

**Description:** Get the rich text of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page | text, missing value | Yes |

### Result
- **Description:** The HTML page converted to rich text.
- **Types:** rich text, missing value
<a name="get_text_of"></a>
```yaml
---
type: command
name: get text of
suite: DEVONthink Suite
---
```

## Command: get text of

**Description:** Get the text of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Result
- **Description:** The plain text of the HTML page.
- **Types:** text, missing value
<a name="get_title_of"></a>
```yaml
---
type: command
name: get title of
suite: DEVONthink Suite
---
```

## Command: get title of

**Description:** Get the title of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
### Result
- **Description:** The title of the HTML page.
- **Types:** text, missing value
<a name="get_versions_of"></a>
```yaml
---
type: command
name: get versions of
suite: DEVONthink Suite
---
```

## Command: get versions of

**Description:** Get saved versions of a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record. | record | No |

### Result
- **Description:** The list of saved versions sorted by date (oldest one at beginning).
- **Types:** record, missing value
### See Also
- [save version of](#save_version_of)
- [restore record with](#restore_record_with)
<a name="hide_progress_indicator"></a>
```yaml
---
type: command
name: hide progress indicator
suite: DEVONthink Suite
---
```

## Command: hide progress indicator

**Description:** Hide a visible progress indicator.

### Result
- **Description:** True if hiding was successful, false if not.
- **Types:** boolean
### See Also
- [show progress indicator](#show_progress_indicator)
- [step progress indicator](#step_progress_indicator)
<a name="import_attachments_of"></a>
```yaml
---
type: command
name: import attachments of
suite: DEVONthink Suite
---
```

## Command: import attachments of

**Description:** Import attachments of an email.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record of an email. | record | No |
| to | The destination group. Uses incoming group or group selector if not specified. | parent, missing value | Yes |

### Result
- **Description:** The imported attachment records. The creation and modification date of the email is retained.
- **Types:** record, missing value
### See Also
- [import path](#import_path)
- [import template](#import_template)
<a name="import_path"></a>
```yaml
---
type: command
name: import path
suite: DEVONthink Suite
---
```

## Command: import path

**Description:** Import a file or folder (including its subfolders).

### Direct Parameter
- **Description:** The POSIX path or file URL of the file or folder.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | The name of the source application. | text, missing value | Yes |
| name | The name for the imported record. | text, missing value | Yes |
| placeholders | Optional placeholders as key-value-pairs for text, RTF/RTFD & HTML/XML templates and filenames. NOTE: The standard placeholders of .dtTemplate packages are also supported if this parameter is specified. | dictionary, missing value | Yes |
| to | The destination group. Uses incoming group or group selector if not specified. | parent, missing value | Yes |

### Result
- **Description:** The imported record.
- **Types:** record, missing value
### See Also
- [import attachments of](#import_attachments_of)
- [import template](#import_template)
- [index path](#index_path)
<a name="import_template"></a>
```yaml
---
type: command
name: import template
suite: DEVONthink Suite
---
```

## Command: import template

**Description:** Import a template. Template scripts are not supported and audit-proof databases do not support any templates at all.

### Direct Parameter
- **Description:** The POSIX path or file URL of the template.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The destination group. Uses incoming group or group selector if not specified. | parent, missing value | Yes |

### Result
- **Description:** The imported record.
- **Types:** record, missing value
### See Also
- [import attachments of](#import_attachments_of)
- [import path](#import_path)
<a name="index_path"></a>
```yaml
---
type: command
name: index path
suite: DEVONthink Suite
---
```

## Command: index path

**Description:** Index a file or folder (including its subfolders). Not supported by audit-proof databases.

### Direct Parameter
- **Description:** The POSIX path or file URL of the file or folder.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The destination group. Uses incoming group or group selector if not specified. | parent, missing value | Yes |

### Result
- **Description:** The indexed record.
- **Types:** record, missing value
### See Also
- [import path](#import_path)
<a name="load_workspace"></a>
```yaml
---
type: command
name: load workspace
suite: DEVONthink Suite
---
```

## Command: load workspace

**Description:** Load a workspace.

### Direct Parameter
- **Description:** The name of the workspace.
- **Types:** text
### Result
- **Description:** True if loading was successful, false if not.
- **Types:** boolean
### See Also
- [save workspace](#save_workspace)
- [delete workspace](#delete_workspace)
<a name="log_message"></a>
```yaml
---
type: command
name: log message
suite: DEVONthink Suite
---
```

## Command: log message

**Description:** Log info for a record, file or action to the Window > Log panel

### Direct Parameter
- **Description:** The optional POSIX path or action.
- **Types:** text, missing value
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record. Requires either the direct or the 'info' parameter. | record, missing value | Yes |
| info | Additional information. | text, missing value | Yes |

### Result
- **Description:** True if logging was successful, false if not.
- **Types:** boolean
<a name="lookup_records_with_comment"></a>
```yaml
---
type: command
name: lookup records with comment
suite: DEVONthink Suite
---
```

## Command: lookup records with comment

**Description:** Lookup records with specified comment.

### Direct Parameter
- **Description:** The comment.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified | database, missing value | Yes |

### Result
- **Description:** The records with the specified comment.
- **Types:** record, missing value
### See Also
- [exists record with comment](#exists_record_with_comment)
<a name="lookup_records_with_content_hash"></a>
```yaml
---
type: command
name: lookup records with content hash
suite: DEVONthink Suite
---
```

## Command: lookup records with content hash

**Description:** Lookup records with specified content hash.

### Direct Parameter
- **Description:** The content hash.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified | database, missing value | Yes |

### Result
- **Description:** The records with the specified content hash.
- **Types:** record, missing value
### See Also
- [exists record with content hash](#exists_record_with_content_hash)
<a name="lookup_records_with_file"></a>
```yaml
---
type: command
name: lookup records with file
suite: DEVONthink Suite
---
```

## Command: lookup records with file

**Description:** Lookup records whose last path component is the specified file.

### Direct Parameter
- **Description:** The filename.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified | database, missing value | Yes |

### Result
- **Description:** The records with the specified file.
- **Types:** content, missing value
### See Also
- [exists record with file](#exists_record_with_file)
<a name="lookup_records_with_path"></a>
```yaml
---
type: command
name: lookup records with path
suite: DEVONthink Suite
---
```

## Command: lookup records with path

**Description:** Lookup records with specified path.

### Direct Parameter
- **Description:** The path.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified. | database, missing value | Yes |

### Result
- **Description:** The records with the specified path.
- **Types:** record, missing value
### See Also
- [exists record with path](#exists_record_with_path)
<a name="lookup_records_with_tags"></a>
```yaml
---
type: command
name: lookup records with tags
suite: DEVONthink Suite
---
```

## Command: lookup records with tags

**Description:** Lookup records with all or any of the specified tags.

### Direct Parameter
- **Description:** The tags.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| any | Lookup any or all (default) tags. | boolean | Yes |
| in | The database. Uses current database if not specified. | database, missing value | Yes |

### Result
- **Description:** The found records.
- **Types:** record, missing value
<a name="lookup_records_with_url"></a>
```yaml
---
type: command
name: lookup records with URL
suite: DEVONthink Suite
---
```

## Command: lookup records with URL

**Description:** Lookup records with specified URL.

### Direct Parameter
- **Description:** The URL (or path).
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The database. Uses current database if not specified. | database, missing value | Yes |

### Result
- **Description:** The records with the specified URL.
- **Types:** record, missing value
### See Also
- [exists record with URL](#exists_record_with_url)
<a name="merge"></a>
```yaml
---
type: command
name: merge
suite: DEVONthink Suite
---
```

## Command: merge

**Description:** Merge either a list of records as an RTF(D)/a PDF document or merge a list of not indexed groups/tags.

### Sample Code
```applescript
tell application id "DNtp"
	merge records selected records in current group
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	theApp.merge({records:theApp.selectedRecords(),group:theApp.currentGroup()});
})();
```

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The destination group for the merged record. The root of the database is used if not specified. | parent, missing value | Yes |
| records | The records to merge. | record | No |

### Result
- **Description:** The merged record.
- **Types:** record, missing value
<a name="move"></a>
```yaml
---
type: command
name: move
suite: DEVONthink Suite
---
```

## Command: move

**Description:** Move all instances of a record to a different group.  Specify the 'from' group to move a single instance to a different group.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record(s) to move. Indexed items are not supported by audit-proof databases. | record, record | No |
| from | The source group. Only applicable if record and destination group are in the same database | parent, missing value | Yes |
| to | The destination group which doesn't have to be in the same database. | parent | No |

### Result
- **Description:** The moved record(s).
- **Types:** record, record, missing value
### See Also
- [duplicate](#duplicate)
- [replicate](#replicate)
<a name="move_into_database"></a>
```yaml
---
type: command
name: move into database
suite: DEVONthink Suite
---
```

## Command: move into database

**Description:** Move an external/indexed record (and its children) into the database. Not supported by audit-proof databases.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to move. | record | No |

### Result
- **Description:** True if moving was successful, false if not.
- **Types:** boolean
### See Also
- [move to external folder](#move_to_external_folder)
<a name="move_to_external_folder"></a>
```yaml
---
type: command
name: move to external folder
suite: DEVONthink Suite
---
```

## Command: move to external folder

**Description:** Move an internal/imported record (and its children) to the enclosing external folder in the filesystem. Creation/Modification dates, Spotlight comments and OpenMeta tags are immediately updated. Not supported by audit-proof databases.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to move. | record | No |
| to | The POSIX path or file URL of the destination folder. Only supported by documents. | text, missing value | Yes |

### Result
- **Description:** True if moving was successful, false if not.
- **Types:** boolean
### See Also
- [move into database](#move_into_database)
<a name="open_database"></a>
```yaml
---
type: command
name: open database
suite: DEVONthink Suite
---
```

## Command: open database

**Description:** Open an existing database.

### Direct Parameter
- **Description:** POSIX file path of database.
- **Types:** text
### Result
- **Description:** The opened database.
- **Types:** database, missing value
### See Also
- [close](#close)
<a name="open_tab_for"></a>
```yaml
---
type: command
name: open tab for
suite: DEVONthink Suite
---
```

## Command: open tab for

**Description:** Open a new tab for the specified URL or record in a think window.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to open. | record, missing value | Yes |
| URL | The URL to open. | text, missing value | Yes |
| referrer | The HTTP referrer. | text, missing value | Yes |
| in | The optional think window that should open a new tab. A new window is used otherwise. | think window, missing value | Yes |

### Result
- **Description:** The opened tab.
- **Types:** tab, missing value
### See Also
- [close](#close)
- [open window for](#open_window_for)
<a name="open_window_for"></a>
```yaml
---
type: command
name: open window for
suite: DEVONthink Suite
---
```

## Command: open window for

**Description:** Open a (new) viewer or document window for the specified record. Only recommended for main windows, use 'open tab for' for document windows.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to open. | record | No |
| enforcement | Enforce DEVONthink to always open a new window, even if the record is already opened in one. Off by default. | boolean | Yes |

### Result
- **Description:** The opened window.
- **Types:** think window, missing value
### See Also
- [open tab for](#open_tab_for)
- [close](#close)
<a name="optimize"></a>
```yaml
---
type: command
name: optimize
suite: DEVONthink Suite
---
```

## Command: optimize

**Description:** Backup & optimize a database.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| database | The database to optimize. | database | No |

### Result
- **Description:** True if optimizing was successful, false if not.
- **Types:** boolean
### See Also
- [check file integrity of](#check_file_integrity_of)
- [verify](#verify)
<a name="paste_clipboard"></a>
```yaml
---
type: command
name: paste clipboard
suite: DEVONthink Suite
---
```

## Command: paste clipboard

**Description:** Create a new record with the contents of the clipboard.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The destination group for the new record. Uses incoming group or group selector if not specified. | parent, missing value | Yes |

### Result
- **Description:** The pasted record.
- **Types:** record, missing value
<a name="perform_smart_rule"></a>
```yaml
---
type: command
name: perform smart rule
suite: DEVONthink Suite
---
```

## Command: perform smart rule

**Description:** Perform one or all smart rules.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | The name of the smart rule. All smart rules are used if not specified. | text, missing value | Yes |
| record | The record. All records matching the smart rule(s) conditions are used if no record is specified. | record, missing value | Yes |
| trigger | The optional event to trigger smart rules. | rule event | Yes |

### Result
- **Description:** True if performing was successful, false if not.
- **Types:** boolean
<a name="refresh"></a>
```yaml
---
type: command
name: refresh
suite: DEVONthink Suite
---
```

## Command: refresh

**Description:** Refresh a record. Currently only supported by feeds but not by audit-proof databases.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to refresh. | record | No |

### Result
- **Description:** True if refreshing was successful, false if not.
- **Types:** boolean
<a name="replicate"></a>
```yaml
---
type: command
name: replicate
suite: DEVONthink Suite
---
```

## Command: replicate

**Description:** Replicate a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record(s) to replicate. | record, record | No |
| to | The destination group which must be in the same database. | parent | No |

### Result
- **Description:** The replicated record(s).
- **Types:** record, record, missing value
### See Also
- [duplicate](#duplicate)
- [move](#move)
<a name="restore_record_with"></a>
```yaml
---
type: command
name: restore record with
suite: DEVONthink Suite
---
```

## Command: restore record with

**Description:** Restore saved version of a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| version | The saved version. The record of the version is automatically retrieved. | record | No |

### Result
- **Description:** True if restoring was successful, false otherwise.
- **Types:** boolean
### See Also
- [get versions of](#get_versions_of)
- [save version of](#save_version_of)
<a name="save_version_of"></a>
```yaml
---
type: command
name: save version of
suite: DEVONthink Suite
---
```

## Command: save version of

**Description:** Save version of current record. NOTE: Use this command right before editing the contents, not afterwards, as duplicates are automatically removed.

### Sample Code
```applescript
tell application id "DNtp"
	set theRecord to create record with {name:"Test", type:txt, content:"Content"} in (current group)
	save version of record theRecord
	set plain text of theRecord to "Modified"
	return get versions of record theRecord
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	let theRecord = theApp.createRecordWith({name:"Test", 'type':"txt", 'content':"Content"},{in:theApp.currentGroup()});
	theApp.saveVersionOf({'record':theRecord});
	theRecord.plainText = "Modified";
	return theApp.getVersionsOf({'record':theRecord});
})();
```

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record. | record | No |

### Result
- **Description:** The saved version.
- **Types:** record, missing value
### See Also
- [delete](#delete)
- [get versions of](#get_versions_of)
- [restore record with](#restore_record_with)
<a name="save_workspace"></a>
```yaml
---
type: command
name: save workspace
suite: DEVONthink Suite
---
```

## Command: save workspace

**Description:** Save a workspace.

### Direct Parameter
- **Description:** The name of the workspace.
- **Types:** text
### Result
- **Description:** True if saving was successful, false if not.
- **Types:** boolean
### See Also
- [load workspace](#load_workspace)
- [delete workspace](#delete_workspace)
<a name="search"></a>
```yaml
---
type: command
name: search
suite: DEVONthink Suite
---
```

## Command: search

**Description:** Search for records in specified group or all databases.

### Direct Parameter
- **Description:** The search string. Supports keys, operators and wildcards.
- **Types:** text, missing value
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| comparison | The comparison to use (default no case). | search comparison | Yes |
| exclude subgroups | Don't search in subgroups of the specified group. Off by default. | boolean | Yes |
| in | The group to search in. Searches in all databases if not specified. | parent, missing value | Yes |

### Result
- **Description:** The found records.
- **Types:** record, missing value
### See Also
- [show search](#show_search)
<a name="set_cell_at"></a>
```yaml
---
type: command
name: set cell at
suite: DEVONthink Suite
---
```

## Command: set cell at

**Description:** Set cell at specified position of current sheet.

### Sample Code
```applescript
tell application id "DNtp"
	tell current tab of think window 1
		set cell at column 1 row 1 to "1"
	end tell
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const theWindow = theApp.thinkWindows()[0];
	let theValue = theApp.setCellAt(theWindow,{column:1,row:1,to:"1"});
})();
```

### Direct Parameter
- **Description:** The tab or window.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| column | Either the index (1...n) or the name of the column of the cell. | integer, text | No |
| row | The row (1...n) of the cell. | integer | No |
| to | The content of the cell. | text | No |

### Result
- **Description:** True if setting was successful, false if not.
- **Types:** boolean
### See Also
- [get cell at](#get_cell_at)
<a name="show_progress_indicator"></a>
```yaml
---
type: command
name: show progress indicator
suite: DEVONthink Suite
---
```

## Command: show progress indicator

**Description:** Show a progress indicator or update an already visible indicator. You have to ensure that the indicator is hidden again via 'hide progress indicator' when the script ends or if an error occurs.

### Direct Parameter
- **Description:** The title of the progress.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| cancel button | Display a button to cancel the process. | boolean | Yes |
| steps | The number of steps of the progress or a negative value for an indeterminate number. | number | Yes |

### Result
- **Description:** True if showing was successful, false if not.
- **Types:** boolean
### See Also
- [step progress indicator](#step_progress_indicator)
- [hide progress indicator](#hide_progress_indicator)
<a name="show_search"></a>
```yaml
---
type: command
name: show search
suite: DEVONthink Suite
---
```

## Command: show search

**Description:** Perform search in frontmost main window. Opens a new main window if there's none.

### Direct Parameter
- **Description:** The search string. Supports keys, operators and wildcards.
- **Types:** text, missing value
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| comparison | The comparison to use (default no case). | search comparison | Yes |
| exclude subgroups | Don't search in subgroups of the specified group. Off by default. | boolean | Yes |

### Result
- **Description:** True if the search was performed, false if not.
- **Types:** boolean
### See Also
- [search](#search)
<a name="start_downloads"></a>
```yaml
---
type: command
name: start downloads
suite: DEVONthink Suite
---
```

## Command: start downloads

**Description:** Start queue of download manager.

### Result
- **Description:** True if starting was successful, false if not.
- **Types:** boolean
<a name="step_progress_indicator"></a>
```yaml
---
type: command
name: step progress indicator
suite: DEVONthink Suite
---
```

## Command: step progress indicator

**Description:** Go to next step of a progress.

### Direct Parameter
- **Description:** The info for the current step.
- **Types:** text, missing value
### Result
- **Description:** True if stepping was successful, false if not.
- **Types:** boolean
### See Also
- [show progress indicator](#show_progress_indicator)
- [hide progress indicator](#hide_progress_indicator)
<a name="stop_downloads"></a>
```yaml
---
type: command
name: stop downloads
suite: DEVONthink Suite
---
```

## Command: stop downloads

**Description:** Stop queue of download manager.

### Result
- **Description:** True if stopping was successful, false if not.
- **Types:** boolean
<a name="summarize_annotations_of"></a>
```yaml
---
type: command
name: summarize annotations of
suite: DEVONthink Suite
---
```

## Command: summarize annotations of

**Description:** Summarize highlights & annotations of records. PDF, RTF(D), Markdown and web documents are currently supported.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The destination group for the summary. The current group of the database is used if not specified. | parent, missing value | Yes |
| records | The records to summarize. | content | No |
| to | The desired format. Only 'markdown', 'rich' and 'sheet' are currently supported. | summary type | No |

### Result
- **Description:** The created record.
- **Types:** content, missing value
### See Also
- [summarize contents of](#summarize_contents_of)
- [summarize mentions of](#summarize_mentions_of)
- [summarize text](#summarize_text)
<a name="summarize_contents_of"></a>
```yaml
---
type: command
name: summarize contents of
suite: DEVONthink Suite
---
```

## Command: summarize contents of

**Description:** Summarize content of records.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The destination group for the summary. The current group of the database is used if not specified. | parent, missing value | Yes |
| records | The records to summarize. | content | No |
| to | The desired format. Only 'markdown', 'simple' and 'rich' are currently supported. | summary type | No |
| as | The desired summary style. If no value is specified the settings default is used. | summary style | Yes |

### Result
- **Description:** The created record.
- **Types:** content, missing value
### See Also
- [summarize annotations of](#summarize_annotations_of)
- [summarize mentions of](#summarize_mentions_of)
- [summarize text](#summarize_text)
<a name="summarize_mentions_of"></a>
```yaml
---
type: command
name: summarize mentions of
suite: DEVONthink Suite
---
```

## Command: summarize mentions of

**Description:** Summarize mentions of records.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The destination group for the summary. The current group of the database is used if not specified. | parent, missing value | Yes |
| records | The records to summarize. | content | No |
| to | The desired format. Only 'markdown' and 'rich' are currently supported. | summary type | No |

### Result
- **Description:** The created record.
- **Types:** content, missing value
### See Also
- [summarize annotations of](#summarize_annotations_of)
- [summarize contents of](#summarize_contents_of)
- [summarize text](#summarize_text)
<a name="summarize_text"></a>
```yaml
---
type: command
name: summarize text
suite: DEVONthink Suite
---
```

## Command: summarize text

**Description:** Summarizes text.

### Direct Parameter
- **Description:** The text to summarize.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | The desired summary style. If no value is specified the settings default is used. | summary style | Yes |

### Result
- **Description:** The summarized text.
- **Types:** text, missing value
### See Also
- [summarize annotations of](#summarize_annotations_of)
- [summarize contents of](#summarize_contents_of)
- [summarize mentions of](#summarize_mentions_of)
<a name="synchronize"></a>
```yaml
---
type: command
name: synchronize
suite: DEVONthink Suite
---
```

## Command: synchronize

**Description:** Synchronizes records with the filesystem or databases with their sync locations. Only one of both operations is supported.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The (external) record to update. New items are added, updated ones indexed and obsolete ones removed. NOTE: This is rarely necessary as databases are usually automatically updated by filesystem events. In addition, audit-proof databases do not support this. | record, missing value | Yes |
| database | The database to synchronize via its sync locations. | database, missing value | Yes |

### Result
- **Description:** True if synchronizing was successful, false if not.
- **Types:** boolean
<a name="transcribe"></a>
```yaml
---
type: command
name: transcribe
suite: DEVONthink Suite
---
```

## Command: transcribe

**Description:** Transcribes speech, text or notes of a record.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | An audio record, a video record containing an audio track, a PDF document or an image. | content | No |
| language | ISO language code, e.g. 'en' or 'de'. If no value is specified the settings default is used. | text | Yes |
| timestamps | Transcription should include timestamps or not. If no value is specified the settings default is used. | boolean | Yes |

### Result
- **Description:** The transcribed text if successful.
- **Types:** text, missing value
<a name="update"></a>
```yaml
---
type: command
name: update
suite: DEVONthink Suite
---
```

## Command: update

**Description:** Update text of a plain/rich text, Markdown document, formatted note or HTML page. Not supported by audit-proof databases.

### Sample Code
```applescript
tell application id "DNtp"
	set theMergedNote to missing value
	repeat with theRecord in selected records
		if theMergedNote is missing value then
			set theMergedNote to convert record theRecord to note
		else if (record type of theRecord is in {RTF, RTFD}) then
			update record theMergedNote with text (rich text of theRecord) mode appending
		else
			update record theMergedNote with text (source of theRecord) mode appending
		end if
	end repeat
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	let theRecords = theApp.selectedRecords(), theMergedNote = null;
	theRecords.forEach (r => {
		if (theMergedNote==null)
			theMergedNote = theApp.convert({record:r,to:"note"});
		else
			theApp.update({record:theMergedNote, withText:r.source(), mode:"appending"});
	})
})();
```

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The record to update. | record | No |
| with text | The text which should be updated/set, inserted or appended. | text, rich text | No |
| mode | The desired mode. | update mode | No |
| URL | The URL of the text. | text, missing value | Yes |

### Result
- **Description:** True if updating was successful, false if not.
- **Types:** boolean
<a name="update_thumbnail"></a>
```yaml
---
type: command
name: update thumbnail
suite: DEVONthink Suite
---
```

## Command: update thumbnail

**Description:** Update existing thumbnail of a record. Thumbnailing is performed asynchronously in the background.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| of | The record. | record | No |

### Result
- **Description:** True if updating was successful, false if not.
- **Types:** boolean
### See Also
- [create thumbnail](#create_thumbnail)
- [delete thumbnail](#delete_thumbnail)
<a name="verify"></a>
```yaml
---
type: command
name: verify
suite: DEVONthink Suite
---
```

## Command: verify

**Description:** Verify a database.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| database | The database to verify. | database | No |

### Result
- **Description:** Total number of errors, invalid filenames and missing files.
- **Types:** integer
### See Also
- [optimize](#optimize)
- [check file integrity of](#check_file_integrity_of)
<a name="document_window"></a>
```yaml
---
type: class
name: document window
suite: DEVONthink Suite
---
```

## Class: document window

**Description:** A document window.

**Inherits:** think window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| content record | The record of the visible document. | content, missing value | read/write |

<a name="main_window"></a>
```yaml
---
type: class
name: main window
suite: DEVONthink Suite
---
```

## Class: main window

**Description:** A main window.

**Inherits:** think window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| search results | The search results. | record, missing value | read/write |
| root | The top level group of the viewer. | parent, missing value | read/write |
| search query | The search query. Setting the query performs a search. | text, missing value | read/write |
| selection | The current selection. 'selected records' element is recommended instead. | record, missing value | read/write |

### Elements
- **Type:** selected record
<a name="application"></a>
```yaml
---
type: class
name: application
suite: DEVONthink Suite
---
```

## Class: application

**Description:** DEVONthink's top level scripting object.

**Inherits:** application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| bates number | Current bates number. | integer | read/write |
| cancelled progress | Specifies if a process with a visible progress indicator should be cancelled. | boolean | r |
| current chat engine | The default chat engine. | chat engine, missing value | r |
| current group | The (selected) group of the frontmost window of the current database. Returns root of current database if no current group exists. | parent, missing value | r |
| current workspace | The name of the currently used workspace. | text, missing value | r |
| current database | The currently used database. | database, missing value | r |
| content record | The record of the visible document in the frontmost think window. | content, missing value | r |
| inbox | The global inbox. | database, missing value | r |
| incoming group | The default group for new notes. Either global inbox or incoming group of current database if global inbox isn't available. | parent, missing value | r |
| label names | List of all 7 label names. | text, missing value | r |
| last downloaded response | The last downloaded HTTP(S) response. | HTTP response, missing value | r |
| last downloaded URL | The actual URL of the last download. | text, missing value | r |
| preferred import destination | The default destination for data from external sources. See Settings > Import > Destination. | parent, missing value | r |
| reading list | The items of the reading list. | reading list item, missing value | r |
| selection | The current selection of the frontmost main window or the record of the frontmost document window. 'selected records' element is recommended instead especially for bulk retrieval of properties like UUID. | record, missing value | r |
| strict duplicate recognition | Specifies if recognition of duplicates is strict (exact) or not (fuzzy). | boolean | read/write |
| workspaces | The names of all available workspaces. | text, missing value | r |

### Elements
- **Type:** database
- **Type:** think window
- **Type:** main window
- **Type:** document window
- **Type:** selected record
### Responds To
- **Command:** add download
- **Command:** add reading list
- **Command:** classify
- **Command:** compress
- **Command:** move into database
- **Command:** convert
- **Command:** convert feed to HTML
- **Command:** create record with
- **Command:** add reminder
- **Command:** create database
- **Command:** create formatted note from
- **Command:** create location
- **Command:** create Markdown from
- **Command:** create PDF document from
- **Command:** create thumbnail
- **Command:** create web document from
- **Command:** move to external folder
- **Command:** delete
- **Command:** delete thumbnail
- **Command:** delete workspace
- **Command:** do JavaScript
- **Command:** download URL
- **Command:** download markup from
- **Command:** download JSON from
- **Command:** duplicate
- **Command:** display authentication dialog
- **Command:** display date editor
- **Command:** display name editor
- **Command:** display group selector
- **Command:** exists record with comment
- **Command:** exists record with content hash
- **Command:** exists record with file
- **Command:** exists record at
- **Command:** exists record with path
- **Command:** exists record with URL
- **Command:** export
- **Command:** export tags of
- **Command:** export website
- **Command:** get cached data for URL
- **Command:** get database with id
- **Command:** get database with uuid
- **Command:** get favicon of
- **Command:** get items of feed
- **Command:** get feed items of
- **Command:** get frames of
- **Command:** get embedded images of
- **Command:** extract keywords from
- **Command:** get links of
- **Command:** get metadata of
- **Command:** get custom meta data
- **Command:** get embedded objects of
- **Command:** get record at
- **Command:** get record with id
- **Command:** get record with uuid
- **Command:** get rich text of
- **Command:** get embedded sheets and scripts of
- **Command:** get text of
- **Command:** get title of
- **Command:** get concordance of
- **Command:** hide progress indicator
- **Command:** import attachments of
- **Command:** import path
- **Command:** import template
- **Command:** index path
- **Command:** load workspace
- **Command:** log message
- **Command:** lookup records with comment
- **Command:** lookup records with content hash
- **Command:** lookup records with file
- **Command:** lookup records with path
- **Command:** lookup records with tags
- **Command:** lookup records with URL
- **Command:** merge
- **Command:** move
- **Command:** open database
- **Command:** open tab for
- **Command:** open window for
- **Command:** optimize
- **Command:** paste clipboard
- **Command:** perform smart rule
- **Command:** refresh
- **Command:** replicate
- **Command:** save workspace
- **Command:** search
- **Command:** show search
- **Command:** get chat models for engine
- **Command:** get chat response for message
- **Command:** download image for prompt
- **Command:** save version of
- **Command:** get versions of
- **Command:** restore record with
- **Command:** show progress indicator
- **Command:** compare
- **Command:** start downloads
- **Command:** step progress indicator
- **Command:** stop downloads
- **Command:** summarize annotations of
- **Command:** summarize mentions of
- **Command:** summarize contents of
- **Command:** summarize text
- **Command:** synchronize
- **Command:** transcribe
- **Command:** update
- **Command:** update thumbnail
- **Command:** check file integrity of
- **Command:** verify
<a name="child"></a>
```yaml
---
type: class
name: child
suite: DEVONthink Suite
---
```

## Class: child

**Description:** A child record of a group.

**Inherits:** record

<a name="content"></a>
```yaml
---
type: class
name: content
suite: DEVONthink Suite
---
```

## Class: content

**Description:** A content record of a database.

**Inherits:** record

<a name="database"></a>
```yaml
---
type: class
name: database
suite: DEVONthink Suite
---
```

## Class: database

**Description:** A database.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The scripting identifier of a database. | integer | r |
| uuid | The unique and persistent identifier of a database for external referencing. | text, missing value | r |
| annotations group | The group for annotations, will be created if necessary. | parent, missing value | r |
| comment | The comment of the database. | text, missing value | read/write |
| current group | The (selected) group of the frontmost window. Returns root if no current group exists. | parent, missing value | r |
| incoming group | The default group for new notes. Might be identical to root. | parent, missing value | r |
| encrypted | Specifies if a database is encrypted or not. | boolean | r |
| audit proof | Specifies if a database is audit-proof or not. | boolean | r |
| read only | Specifies if a database is read-only and can't be modified. | boolean | r |
| Spotlight indexing | Specifies if Spotlight indexing of a database is en- or disabled. | boolean | read/write |
| versioning | Specifies whether versioning of documents is en- or disabled. | boolean | read/write |
| name | The name of the database. | text | read/write |
| filename | The filename of the database. | text, missing value | r |
| path | The POSIX path of the database. | text, missing value | r |
| root | The top level group of the database. | parent, missing value | r |
| tags group | The group for tags. | parent, missing value | r |
| trash group | The trash's group. | parent, missing value | r |
| versions group | The group for versioning. | parent, missing value | r |

### Elements
- **Type:** content
- **Type:** parent
- **Type:** record
- **Type:** smart parent
- **Type:** tag group
### Responds To
- **Command:** close
### See Also
- [close](#close)
<a name="incoming_reference"></a>
```yaml
---
type: class
name: incoming reference
suite: DEVONthink Suite
---
```

## Class: incoming reference

**Description:** A reference from another record.

**Inherits:** record

<a name="incoming_wiki_reference"></a>
```yaml
---
type: class
name: incoming Wiki reference
suite: DEVONthink Suite
---
```

## Class: incoming Wiki reference

**Description:** An automatic Wiki reference from another record. This depends on the current Wiki linking settings.

**Inherits:** record

<a name="outgoing_reference"></a>
```yaml
---
type: class
name: outgoing reference
suite: DEVONthink Suite
---
```

## Class: outgoing reference

**Description:** A reference to another record.

**Inherits:** record

<a name="outgoing_wiki_reference"></a>
```yaml
---
type: class
name: outgoing Wiki reference
suite: DEVONthink Suite
---
```

## Class: outgoing Wiki reference

**Description:** An automatic Wiki reference to another record. This depends on the current Wiki linking settings.

**Inherits:** record

<a name="parent"></a>
```yaml
---
type: class
name: parent
suite: DEVONthink Suite
---
```

## Class: parent

**Description:** A parent (either group, feed or tag) of a record.

**Inherits:** record

<a name="record"></a>
```yaml
---
type: class
name: record
suite: DEVONthink Suite
---
```

## Class: record

**Description:** A database record.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The scripting identifier of a record. Optimizing or closing a database might modify this identifier. | integer | r |
| MIME type | The (proposed) MIME type of a record. | text, missing value | r |
| uuid | The unique and persistent identifier of a record. | text, missing value | r |
| addition date | Date when the record was added to the database. | date, missing value | r |
| aliases | Wiki aliases (separated by commas or semicolons) of a record. | text, missing value | read/write |
| altitude | The altitude in metres of a record. | real | read/write |
| annotation | Annotation of a record. Only plain & rich text and Markdown documents are supported. Read-only in case of audit-proof databases. | content, missing value | read/write |
| annotation count | The number of annotations. Supported by HTML pages, formatted notes, web archives, PDF, rich text & Markdown documents. | integer | r |
| web archive | The web archive of a record if available or the record converted to web archive if possible. | raw data, missing value | r |
| attached script | POSIX path of script attached to a record. | text, missing value | read/write |
| attachment count | The number of attachments. Currently only supported for RTFD documents and emails. | integer | r |
| attributes change date | The change date of the record's attributes. | date, missing value | read/write |
| bates number | Bates number. | integer | read/write |
| cells | The cells of a sheet. This is a list of rows, each row contains a list of string values for the various colums. Read-only in case of audit-proof databases. | array | read/write |
| character count | The character count of a record. | integer | r |
| color | The color of a record. Currently only supported by tags & groups. | RGB color, missing value | read/write |
| columns | The column names of a sheet. | text, missing value | r |
| comment | The comment of a record. | text, missing value | read/write |
| content hash | Stored SHA1 hash of files and document packages. | text, missing value | r |
| creation date | The creation date of a record. Read-only in case of audit-proof databases. | date, missing value | read/write |
| custom meta data | User-defined metadata of a record as a dictionary containing key-value pairs. Setting a value for an unknown key automatically adds a definition to Settings > Data. | dictionary, missing value | read/write |
| data | The file data of a record. Currently only supported by PDF documents, images, rich text documents and web archives. Read-only in case of audit-proof databases. | raw data, missing value | read/write |
| database | The database of the record. | database, missing value | r |
| date | The (creation/modification) date of a record. Read-only in case of audit-proof databases. | date, missing value | read/write |
| digital object identifier | Digital object identifier (DOI) extracted from text of document, e.g. a scanned receipt, or from the title. | text, missing value | r |
| dimensions | The width and height of an image or PDF document in pixels or points. | integer | r |
| document amount | Amount extracted from text of document, e.g. a scanned receipt. | text, missing value | r |
| document date | First date extracted from text of document, e.g. a scan. | date, missing value | r |
| all document dates | All dates extracted from text of document, e.g. a scan. | date, missing value | r |
| document name | Name based on text or properties of document | text, missing value | r |
| dpi | The resultion of an image in dpi. | number | r |
| duplicates | The duplicates of a record (only other instances, not including the record). | record, missing value | r |
| duration | The duration of audio and video files. | real | r |
| exclude from chat | Exclude group or record from chat. | boolean | read/write |
| exclude from classification | Exclude group or record from classifying. | boolean | read/write |
| exclude from search | Exclude group or record from searching. | boolean | read/write |
| exclude from see also | Exclude record from see also. | boolean | read/write |
| exclude from tagging | Exclude group from tagging. | boolean | read/write |
| exclude from Wiki linking | Exclude record from automatic Wiki linking. | boolean | read/write |
| filename | The current filename of a record. | text, missing value | r |
| geolocation | The human readable geogr. location of a record. | text, missing value | read/write |
| height | The height of an image or PDF document in pixels or points. | number | r |
| image | The image or PDF document of a record. Setting supports both raw data and strings containing paths or URLs. Read-only in case of audit-proof databases. | any, missing value | read/write |
| indexed | Indexed or imported record. | boolean | r |
| international standard book number | International standard book number (ISBN) extracted from text of document, e.g. a scanned receipt, or from the title. | text, missing value | r |
| interval | Refresh interval of a feed. Currently overriden by settings. | real | read/write |
| encrypted | Specifies if a document is encrypted or not. Currently only supported by PDF documents. | boolean | r |
| pending | Flag whether the (latest) contents of a record haven't been downloaded from a sync location yet. | boolean | r |
| kind | The human readable and localized kind of a record. WARNING: Don't use this to check the type of a record, otherwise your script might fail depending on the version and the localization. | text, missing value | r |
| label | Index of label (0-7) of a record. | integer | read/write |
| latitude | The latitude in degrees of a record. | real | read/write |
| location | The primary location of the record in the database as a POSIX path (/ in names is replaced with \/). | text, missing value | r |
| location group | The group of the record's primary location. This is identical to the first parent group. | parent, missing value | r |
| location with name | The full primary location of the record including its name (/ in names is replaced with \/). | text, missing value | r |
| locking | The locking of a record. Read-only in case of audit-proof databases. | boolean | read/write |
| longitude | The longitude in degrees of a record. | real | read/write |
| meta data | Document metadata (e.g. of PDF & RTF documents, web pages or emails) of a record as a dictionary containing key-value pairs. | dictionary, missing value | r |
| modification date | The modification date of a record. Read-only in case of audit-proof databases. | date, missing value | read/write |
| name | The name of a record. | text | read/write |
| name without date | The name of a record without any dates. | text, missing value | r |
| name without extension | The name of a record without a file extension (independent of settings). | text, missing value | r |
| newest document date | Newest date extracted from text of document, e.g. a scan. | date, missing value | r |
| number of duplicates | The number of duplicates of a record. | integer | r |
| number of hits | The number of hits of a record. | integer | read/write |
| number of replicants | The number of replicants of a record. | integer | r |
| oldest document date | Oldest date extracted from text of document, e.g. a scan. | date, missing value | r |
| original name | The original name of a record. | text | r |
| opening date | Date when a content was opened the last time or when a feed was refreshed the last time. | date, missing value | r |
| page count | The page count of a record. Currently only supported by PDF documents. | integer | r |
| paginated PDF | A printed/converted PDF of the record. | raw data, missing value | r |
| path | The POSIX file path of a record. Only the path of external records can be changed. Not accessible at all in case of audit-proof databases. | text, missing value | read/write |
| plain text | The plain text of a record. Read-only in case of audit-proof databases. | text, missing value | read/write |
| proposed filename | The proposed filename for a record. | text, missing value | r |
| rating | Rating (0-5) of a record. | integer | read/write |
| record type | The type of a record. WARNING: Don't use string conversions of this type for comparisons, this might fail due to known scripting issues of macOS. | data type | r |
| reference URL | The URL (x-devonthink-item://...) to reference/link back to a record. | text, missing value | r |
| reminder | Reminder of a record. | reminder, missing value | read/write |
| rich text | The rich text of the record (see extended text suite). Changes are only supported in case of RTF/RTFD documents and not by audit-proof databases. | rich text, missing value | read/write |
| score | The score of the last comparison, classification or search (value between 0.0 and 1.0) or undefined otherwise. | real | r |
| size | The size of a record in bytes. | integer | r |
| source | The HTML/XML source of a record if available or the record converted to HTML if possible. Read-only in case of audit-proof databases. | text, missing value | read/write |
| flag | The flag of a record. | boolean | read/write |
| tag type | The tag type of a record. | tag type | r |
| tags | The tags of a record. Setting accepts both strings and parents. | array, missing value | read/write |
| thumbnail | The thumbnail of a record. Setting supports both raw data and strings containing paths or URLs. | any, missing value | read/write |
| unread | The unread flag of a record. | boolean | read/write |
| URL | The URL of a record. Read-only in case of bookmarks in audit-proof databases. | text, missing value | read/write |
| width | The width of an image or PDF document in pixels or points. | number | r |
| word count | The word count of a record. | integer | r |

### Elements
- **Type:** child
- **Type:** incoming reference
- **Type:** incoming Wiki reference
- **Type:** outgoing reference
- **Type:** outgoing Wiki reference
- **Type:** parent
<a name="reminder"></a>
```yaml
---
type: class
name: reminder
suite: DEVONthink Suite
---
```

## Class: reminder

**Description:** A reminder of a record.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| alarm | Alarm of reminder. | reminder alarm | read/write |
| alarm string | Name of sound, text to speak, text of alert/notification, source/path of script or recipient of email. Text can also contain placeholders. | text, missing value | read/write |
| day of week | Scheduled day of week. | reminder day | read/write |
| due date | Due date. | date, missing value | read/write |
| interval | Interval of schedule (every n hours, days, weeks, months or years) | integer | read/write |
| masc | Bitmap specifying scheduled days of week/month or scheduled months of year. | integer | read/write |
| schedule | Schedule of reminder. | reminder schedule | read/write |
| week of month | Scheduled week of month. | reminder week | read/write |

### See Also
- [add reminder](#add_reminder)
<a name="selected_record"></a>
```yaml
---
type: class
name: selected record
suite: DEVONthink Suite
---
```

## Class: selected record

**Description:** A selected record.

**Inherits:** record

<a name="smart_parent"></a>
```yaml
---
type: class
name: smart parent
suite: DEVONthink Suite
---
```

## Class: smart parent

**Description:** A smart group.

**Inherits:** record

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| exclude subgroups | Exclude subgroups of the search group from searching. | boolean | read/write |
| highlight occurrences | Highlight found occurrences in documents. | boolean | read/write |
| search group | Group of the smart group to search in. | parent, missing value | read/write |
| search predicates | A string representation of the conditions of the smart group. | text, missing value | read/write |

<a name="tag_group"></a>
```yaml
---
type: class
name: tag group
suite: DEVONthink Suite
---
```

## Class: tag group

**Description:** A tag of a database.

**Inherits:** parent

<a name="tab"></a>
```yaml
---
type: class
name: tab
suite: DEVONthink Suite
---
```

## Class: tab

**Description:** A tab of a think window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier of the tab. | integer | r |
| PDF | A PDF without pagination of the visible document retaining the screen layout. | raw data, missing value | r |
| web archive | Web archive of the current web page. | raw data, missing value | r |
| current line | Zero-based index of current line. | integer | r |
| current movie frame | Image of current movie frame. | raw data, missing value | r |
| current time | Time of current audio/video file. | real | read/write |
| current page | Zero-based index of current PDF page. | integer | read/write |
| database | The database of the tab. | database, missing value | r |
| content record | The record of the visible document. | content, missing value | r |
| loading | Specifies if the current web page is still loading. | boolean | r |
| number of columns | Number of columns of the current sheet. | integer | r |
| number of rows | Number of rows of the current sheet. | integer | r |
| paginated PDF | A printed PDF with pagination of the visible document. | raw data, missing value | r |
| reference URL | The URL (x-devonthink-item://...) to reference/link back to the current content record and its selection, page, frame etc. | text, missing value | r |
| selected column | Index (1...n) of selected column of the current sheet. | integer | read/write |
| selected columns | Indices (1...n) of selected columns of the current sheet. | integer | r |
| selected row | Index (1...n) of selected row of the current sheet. | integer | read/write |
| selected rows | Indices (1...n) of selected rows of the current sheet. | integer | r |
| source | The HTML source of the current web page. | text, missing value | r |
| think window | The think window of the tab. | think window, missing value | r |
| URL | The URL of the current web page. In addition, setting the URL can be used to load a web page. | text, missing value | read/write |
| selected text | The rich text for the selection of the tab. Setting supports both text- and web-based documents, e.g. plain/rich text, Markdown documents or formatted notes. In addition, Markdown & HTML formatted input is supported too. | text, rich text, missing value | read/write |
| plain text | The plain text of the tab. | text, missing value | r |
| rich text | The rich text of the tab. Changes are only supported in case of RTF/RTFD documents. In addition, Markdown & HTML formatted input is supported too. | text, rich text, missing value | read/write |

### Responds To
- **Command:** close
- **Command:** print
- **Command:** save
- **Command:** display chat dialog
- **Command:** add row
- **Command:** delete row at
- **Command:** get cell at
- **Command:** set cell at
<a name="think_window"></a>
```yaml
---
type: class
name: think window
suite: DEVONthink Suite
---
```

## Class: think window

**Description:** A document window or main window.

**Inherits:** window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| PDF | A PDF without pagination of the visible document retaining the screen layout. | raw data, missing value | r |
| web archive | Web archive of the current web page. | raw data, missing value | r |
| current line | Zero-based index of current line. | integer | r |
| current movie frame | Image of current movie frame. | raw data, missing value | r |
| current time | Time of current audio/video file. | real | read/write |
| current page | Zero-based index of current PDF page. | integer | read/write |
| current tab | The selected tab of the think window. | tab, missing value | read/write |
| database | The database of the window. | database, missing value | r |
| content record | The record of the visible document. | content, missing value | r |
| loading | Specifies if the current web page is still loading. | boolean | r |
| number of columns | Number of columns of the current sheet. | integer | r |
| number of rows | Number of rows of the current sheet. | integer | r |
| paginated PDF | A printed PDF with pagination of the visible document. | raw data, missing value | r |
| reference URL | The URL (x-devonthink-item://...) to reference/link back to the current content record and its selection, page, frame etc. | text, missing value | r |
| selected column | Index (1...n) of selected column of the current sheet. | integer | read/write |
| selected columns | Indices (1...n) of selected columns of the current sheet. | integer | r |
| selected row | Index (1...n) of selected row of the current sheet. | integer | read/write |
| selected rows | Indices (1...n) of selected rows of the current sheet. | integer | r |
| source | The HTML source of the current web page. | text, missing value | r |
| URL | The URL of the current web page. In addition, setting the URL can be used to load a web page. | text, missing value | read/write |
| selected text | The rich text for the selection of the window. Setting supports both text- and web-based documents, e.g. plain/rich text, Markdown documents or formatted notes. In addition, Markdown & HTML formatted input is supported too. | text, rich text, missing value | read/write |
| plain text | The plain text of the window. | text, missing value | r |
| rich text | The rich text of the window. Changes are only supported in case of RTF/RTFD documents. In addition, Markdown & HTML formatted input is supported too. | text, rich text, missing value | read/write |

### Elements
- **Type:** tab
### Responds To
- **Command:** close
- **Command:** print
- **Command:** save
- **Command:** display chat dialog
- **Command:** add row
- **Command:** delete row at
- **Command:** get cell at
- **Command:** set cell at
<a name="comparison_type"></a>
```yaml
---
type: enumeration
name: comparison type
suite: DEVONthink Suite
---
```

## Enumeration: comparison type

### Enumerators
| Name | Description |
|---|---|
| data comparison | Uses text & metadata |
| tags comparison | Uses tags |

<a name="convert_type"></a>
```yaml
---
type: enumeration
name: convert type
suite: DEVONthink Suite
---
```

## Enumeration: convert type

### Enumerators
| Name | Description |
|---|---|
| bookmark | Bookmark |
| simple | Plain text |
| rich | Rich text |
| note | Formatted Note |
| markdown | Markdown document |
| HTML | HTML document |
| webarchive | Web Archive |
| PDF document | PDF document (Paginated) |
| single page PDF document | PDF document (One Page) |
| PDF without annotations | PDF document without annotations |
| PDF with annotations burnt in | PDF/A document with annotations burnt in |

<a name="data_type"></a>
```yaml
---
type: enumeration
name: data type
suite: DEVONthink Suite
---
```

## Enumeration: data type

### Enumerators
| Name | Description |
|---|---|
| group | Group |
| smart group | Smart group |
| feed | RSS, RDF or Atom feed |
| bookmark | Internet or filesystem location |
| formatted note | None |
| HTML | HTML document |
| webarchive | Web Archive |
| markdown | Markdown document |
| txt | Text document |
| RTF | RTF document |
| RTFD | RTFD document |
| picture | Picture |
| multimedia | Audio or video file |
| PDF document | PDF document |
| sheet | Sheet |
| XML | XML document |
| property list | Property list |
| AppleScript file | AppleScript file |
| email | Email |
| unknown | Unknown file |

<a name="reminder_alarm"></a>
```yaml
---
type: enumeration
name: reminder alarm
suite: DEVONthink Suite
---
```

## Enumeration: reminder alarm

### Enumerators
| Name | Description |
|---|---|
| no alarm | No alarm. |
| dock | Bounce Dock icon. |
| sound | Play sound. |
| speak | Speak text. |
| notification | Display notification. |
| alert | Display alert. |
| open internally | Open in DEVONthink. |
| open externally | Open in default application. |
| launch | Launch URL. |
| mail with item link | Send mail with item link. |
| mail with attachment | Send mail with attachment. |
| add to reading list | Add to reading list. |
| embedded script | Execute embedded script (AppleScript). |
| embedded JXA script | Execute embedded script (JavaScript). |
| external script | Execute external script. |

<a name="reminder_day"></a>
```yaml
---
type: enumeration
name: reminder day
suite: DEVONthink Suite
---
```

## Enumeration: reminder day

### Enumerators
| Name | Description |
|---|---|
| no day | No day. |
| sunday | Sunday. |
| monday | Monday. |
| tuesday | Tuesday. |
| wednesday | Wednesday. |
| thursday | Thursday. |
| friday | Friday. |
| saturday | Saturday. |
| any day | Any day. |
| workdays | Workdays. |
| weekend | Weekend. |

<a name="reminder_schedule"></a>
```yaml
---
type: enumeration
name: reminder schedule
suite: DEVONthink Suite
---
```

## Enumeration: reminder schedule

### Enumerators
| Name | Description |
|---|---|
| never | No schedule. |
| once | One shot schedule. |
| hourly | Hourly schedule. |
| daily | Daily schedule. |
| weekly | Weekly schedule. |
| monthly | Monthly schedule. |
| yearly | Yearly schedule. |

<a name="reminder_week"></a>
```yaml
---
type: enumeration
name: reminder week
suite: DEVONthink Suite
---
```

## Enumeration: reminder week

### Enumerators
| Name | Description |
|---|---|
| no week | No week. |
| last week | Last week of month. |
| first week | First week of month. |
| second week | Second week of month. |
| third week | Third week of month. |
| fourth week | Fourth week of month. |

<a name="rule_event"></a>
```yaml
---
type: enumeration
name: rule event
suite: DEVONthink Suite
---
```

## Enumeration: rule event

### Enumerators
| Name | Description |
|---|---|
| no event | No event. |
| open event | Event after opening items. |
| open externally event | Event after opening items externally. |
| edit externally event | Event after editing items externally. |
| launch event | Event after launching the URL of items. |
| creation event | Event after creating items. |
| import event | Event after importing items. |
| clipping event | Event after clipping websites. |
| download event | Event after downloading items. |
| rename event | Event after renaming items. |
| move event | Event after moving items. |
| classify event | Event after classifying items. |
| replicate event | Event after replicating items. |
| duplicate event | Event after duplicating items. |
| tagging event | Event after tagging items. |
| flagging event | Event after flagging items. |
| labelling event | Event after labelling items. |
| rating event | Event after rating items. |
| move into database event | Event after consolidating items. |
| move to external folder event | Event after deconsolidating items. |
| commenting event | Event after commenting items. |
| convert event | Event after converting items. |
| OCR event | Event after performing OCR. |
| imprint event | Event after imprinting items. |
| trashing event | Event before trashing items. |

<a name="search_comparison"></a>
```yaml
---
type: enumeration
name: search comparison
suite: DEVONthink Suite
---
```

## Enumeration: search comparison

### Enumerators
| Name | Description |
|---|---|
| no case | Case insensitive search. |
| no umlauts | Diacritics insensitive search. |
| fuzzy | Fuzzy search. |
| related | Related search. |

<a name="summary_style"></a>
```yaml
---
type: enumeration
name: summary style
suite: DEVONthink Suite
---
```

## Enumeration: summary style

### Enumerators
| Name | Description |
|---|---|
| list summary | Bullet list summary. |
| key points summary | Key points summary. |
| table summary | Table summary. |
| text summary | Text summary. |
| custom summary | Custom summary. |

<a name="summary_type"></a>
```yaml
---
type: enumeration
name: summary type
suite: DEVONthink Suite
---
```

## Enumeration: summary type

### Enumerators
| Name | Description |
|---|---|
| markdown | Markdown document |
| simple | Plain text |
| rich | Rich text |
| sheet | Sheet |

<a name="tag_type"></a>
```yaml
---
type: enumeration
name: tag type
suite: DEVONthink Suite
---
```

## Enumeration: tag type

### Enumerators
| Name | Description |
|---|---|
| no tag | No tag (not a group or excluded from tagging). |
| ordinary tag | An 'ordinary' tag located inside of the tags group. |
| group tag | A 'group' tag located outside of the tags group. |

<a name="update_mode"></a>
```yaml
---
type: enumeration
name: update mode
suite: DEVONthink Suite
---
```

## Enumeration: update mode

### Enumerators
| Name | Description |
|---|---|
| replacing | Replace text. |
| appending | Append text. |
| inserting | Insert text |

<a name="concordance_sorting"></a>
```yaml
---
type: enumeration
name: concordance sorting
suite: DEVONthink Suite
---
```

## Enumeration: concordance sorting

### Enumerators
| Name | Description |
|---|---|
| weight | Sorted by weight |
| frequency | Sorted by frequency |

<a name="chat_engine"></a>
```yaml
---
type: enumeration
name: chat engine
suite: DEVONthink Suite
---
```

## Enumeration: chat engine

### Enumerators
| Name | Description |
|---|---|
| Apple AI | Apple's Intelligence |
| ChatGPT | OpenAI's ChatGPT |
| Claude | Anthropic's Claude |
| Gemini | Google's Gemini |
| Mistral AI | Mistral's AI |
| Perplexity | Perplexity's AI |
| GPT4All | Nomic's GPT4All |
| LM Studio | Element Lab's LM Studio |
| Ollama | Ollama |

<a name="image_engine"></a>
```yaml
---
type: enumeration
name: image engine
suite: DEVONthink Suite
---
```

## Enumeration: image engine

### Enumerators
| Name | Description |
|---|---|
| DallE2 | OpenAI's Dall-E 2 |
| DallE3 | OpenAI's Dall-E 3 |
| GPTImage1 | OpenAI's GPT-Image-1 |
| FluxSchnell | Black Forest Labs' Flux Schnell |
| FluxPro | Black Forest Labs' Flux Pro |
| FluxProUltra | Black Forest Labs' Flux Pro Ultra |
| Recraft3 | Recraft AI's Recraft 3 |
| StableDiffusion | Stability AI's Stable Diffusion 3.5 Large |
| StableDiffusionTurbo | Stability AI's Stable Diffusion 3.5 Large Turbo |
| Imagen3Fast | Google's Imagen 3 Fast |
| Imagen3 | Google's Imagen 3 |
| Imagen4 | Google's Imagen 4 |
| Imagen4Ultra | Google's Imagen 4 Ultra |

<a name="reading_list_item"></a>
```yaml
---
type: record-type
name: reading list item
suite: DEVONthink Suite
---
```

## Record Type: reading list item

**Description:** An item of the reading list.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| URL | The item's url | text | read/write |
| title | The item's title | text | read/write |
| unread | The item's unread flag | boolean | read/write |
| date | The item's date | date | read/write |

<a name="group_selector_result"></a>
```yaml
---
type: record-type
name: group selector result
suite: DEVONthink Suite
---
```

## Record Type: group selector result

**Description:** The result of the 'display group selector' command

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name | text | read/write |
| selected group | The selected (destination) group | parent | read/write |
| tags | The tags | text | read/write |

### See Also
- [display group selector](#display_group_selector)
<a name="authentication_result"></a>
```yaml
---
type: record-type
name: authentication result
suite: DEVONthink Suite
---
```

## Record Type: authentication result

**Description:** The result of the 'display authentication dialog' command

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| user | The user | text | read/write |
| password | The password | text | read/write |

### See Also
- [display authentication dialog](#display_authentication_dialog)
<a name="http_response"></a>
```yaml
---
type: record-type
name: HTTP response
suite: DEVONthink Suite
---
```

## Record Type: HTTP response

**Description:** Header fields of HTTP(s) response

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| HTTP status | The HTTP(s) status code. | integer | read/write |
| last modified | The last modification date. | date | read/write |
| content type | The content type. | text | read/write |
| content length | The (expected) content length. | integer | read/write |
| charset | The charset. | text | read/write |

<a name="feed_item"></a>
```yaml
---
type: record-type
name: feed item
suite: DEVONthink Suite
---
```

## Record Type: feed item

**Description:** An item of a RSS, RDF, JSON or Atom feed

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| title | The item's title | text | read/write |
| description | The item's description | text | read/write |
| author | The item's author | text | read/write |
| URL | The item's URL | text | read/write |
| text content | The item's content | text | read/write |
| source | The item's HTML source | text | read/write |
| guid | The item's unique identifier | text | read/write |
| last modified | The item's modification date | text | read/write |
| tags | The item's tags | array | read/write |
| enclosures | The item's enclosures | array | read/write |

## OCR Commands Suite

**Description:** Classes and commands for OCR Commands Suite

<a name="convert_image"></a>
```yaml
---
type: command
name: convert image
suite: OCR Commands Suite
---
```

## Command: convert image

**Description:** Converts a record to a new record and applies OCR.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | A record containing an image | content | No |
| to | The destination group (by default the same group as the input record) | parent, missing value | Yes |
| rotate by | Rotates the incoming image page 0, 90, 180 or 270 degrees (by default it is automatic) | integer | Yes |
| file type | Specifies what type of file to convert to. If no value is specified the settings default is used. | OCR convert type | Yes |
| waiting for reply | Wait for reply (default) or perform the command in the background. | boolean | Yes |

### Result
- **Description:** The converted record.
- **Types:** content, missing value
<a name="ocr"></a>
```yaml
---
type: command
name: ocr
suite: OCR Commands Suite
---
```

## Command: ocr

**Description:** Imports a PDF document or image with OCR.

### Sample Code
```applescript
tell application id "DNtp"
	ocr file "~/Downloads/Test.jpg" to current group
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	theApp.ocr({file:"~/Downloads/Test.jpg", to:theApp.currentGroup()});
})();
```

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| file | POSIX path or file URL of the image file. | text | No |
| attributes | The PDF properties. | PDF properties, missing value | Yes |
| rotate by | Rotates the incoming image page 0, 90, 180 or 270 degrees (by default it is automatic) | integer | Yes |
| to | The destination group. Uses incoming group or group selector if not specified. | parent, missing value | Yes |
| file type | Specifies what type of file to convert to. If no value is specified the settings default is used. | OCR convert type | Yes |
| waiting for reply | Wait for reply (default) or perform the command in the background. | boolean | Yes |

### Result
- **Description:** The OCRed record.
- **Types:** content, missing value
<a name="ocr_convert_type"></a>
```yaml
---
type: enumeration
name: OCR convert type
suite: OCR Commands Suite
---
```

## Enumeration: OCR convert type

### Enumerators
| Name | Description |
|---|---|
| Annotate document | Annotation |
| Comment document | Comment |
| PDF document | PDF document |
| RTF | RTF document |
| Word document | Microsoft Word document |
| webarchive | Web Archive |

<a name="pdf_properties"></a>
```yaml
---
type: record-type
name: PDF properties
suite: OCR Commands Suite
---
```

## Record Type: PDF properties

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| author | The document's author | text | read/write |
| title | The document's title | text | read/write |
| subject | The document's subject | text | read/write |
| keywords | The document's keywords | text | read/write |

## Imprint Commands Suite

**Description:** Classes and commands for Imprint Commands Suite

<a name="imprinter_configuration_names"></a>
```yaml
---
type: command
name: imprinter configuration names
suite: Imprint Commands Suite
---
```

## Command: imprinter configuration names

**Description:** Returns list of imprinter configuration names

### Result
- **Description:** The configuration names.
- **Types:** text, missing value
<a name="imprint_configuration"></a>
```yaml
---
type: command
name: imprint configuration
suite: Imprint Commands Suite
---
```

## Command: imprint configuration

**Description:** Imprint the record with a given imprinter configuration. Not supported by audit-proof databases.

### Direct Parameter
- **Description:** The name of the imprinter configuration
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The image or PDF record to imprint | content | No |
| waiting for reply | Wait for reply (default) or perform the command in the background. | boolean | Yes |

### Result
- **Description:** True if imprinting was successful, false if not.
- **Types:** boolean
<a name="imprint"></a>
```yaml
---
type: command
name: imprint
suite: Imprint Commands Suite
---
```

## Command: imprint

**Description:** Imprint the record with a configuration defined in the parameters. Not supported by audit-proof databases.

### Sample Code
```applescript
tell application id "DNtp"
	set theRecord to selected record 1
	set theText to "Demo""
	imprint font "Times New Roman Italic" position centered record theRecord size 15 text theText border color {65535, 0, 0} border width 5 border style rounded rectangle background color {65535, 65535, 0} rotation 45 with strikethrough
end tell
```

```javascript
(() => {
	const theApp = Application("DEVONthink");
	const theRecord = theApp.selectedRecords[0];
	const theText = "Demo";
	theApp.imprint({font:"Times New Roman Italic",position:"centered",record:theRecord,size:15,text:theText,borderWidth:5,borderStyle:"rounded rectangle",rotation:45,strikeThrough:1,borderColor:[65535, 0, 0],backgroundColor:[65535, 65535, 0]});
})();
```

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| record | The image or PDF record to imprint | content | No |
| background color | Color expressed as an RGB value consisting of a list of three color values from 0 to 65535. ex: Blue = {0, 0, 65535} (Optional). | RGB color, missing value | Yes |
| border color | Color expressed as an RGB value consisting of a list of three color values from 0 to 65535. ex: Blue = {0, 0, 65535} (Optional). | RGB color, missing value | Yes |
| border style | The type of border to be drawn (Optional). | border style type | Yes |
| border width | Width of the border for a given border style (Optional). | integer | Yes |
| font | The name of the font. Can be the PostScript name, such as: “TimesNewRomanPS-ItalicMT”, or display name: “Times New Roman Italic”.  | text | No |
| foreground color | Color expressed as an RGB value consisting of a list of three color values from 0 to 65535. ex: Blue = {0, 0, 65535} (Optional). | RGB color, missing value | Yes |
| occurence | On what pages should the imprint occur (Optional).  | occurrence type | Yes |
| outlined | The text will be drawn as an outline if true (Optional). | boolean | Yes |
| position | Specifies where the imprint will be drawn | imprint position | No |
| rotation | Rotation value in degrees (Optional) | integer | Yes |
| size | Size of the font. | integer | No |
| strike through | The text is striked through if true (Optional). | boolean | Yes |
| text | The text, including any placeholders to imprint  | text | No |
| underlined | The text is underlined if true (Optional). | boolean | Yes |
| x offset | An x offset in pixels from the position (Optional). | integer | Yes |
| y offset | An y offset in pixels from the position (Optional). | integer | Yes |
| waiting for reply | Wait for reply (default) or perform the command in the background. | boolean | Yes |

### Result
- **Description:** True if imprinting was successful, false if not.
- **Types:** boolean
<a name="border_style_type"></a>
```yaml
---
type: enumeration
name: border style type
suite: Imprint Commands Suite
---
```

## Enumeration: border style type

### Enumerators
| Name | Description |
|---|---|
| none | No border, this is the default |
| rectangle | Rectangular border |
| rounded rectangle | Rectangle with rounded corners |
| oval | Oval border |
| left arrow | Left arrow |
| right arrow | Right arrow |

<a name="imprint_position"></a>
```yaml
---
type: enumeration
name: imprint position
suite: Imprint Commands Suite
---
```

## Enumeration: imprint position

### Enumerators
| Name | Description |
|---|---|
| top left | Position imprint top left of page |
| top center | Position imprint top center of page |
| top right | Position imprint top right of page |
| center left | Position imprint center left of page |
| centered | Position imprint in the center of the page |
| center right | Position imprint center right of page |
| bottom left | Position imprint bottom left of page |
| bottom center | Position imprint bottom center of page |
| bottom right | Position imprint bottom right of page |

<a name="occurrence_type"></a>
```yaml
---
type: enumeration
name: occurrence type
suite: Imprint Commands Suite
---
```

## Enumeration: occurrence type

### Enumerators
| Name | Description |
|---|---|
| every page | Imprint every page, this is the default |
| first page only | Imprint the first page only |
| even pages | Imprint even pages only |
| odd pages | Imprint odd pages only |

