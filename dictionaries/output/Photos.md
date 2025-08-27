# Apple Photos Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [count](#count)
- [exists](#exists)
- [open](#open)
- [quit](#quit)
#### Classs
- [application](#application)
### Photos Suite
#### Commands
- [import](#import)
- [export](#export)
- [duplicate](#duplicate)
- [make](#make)
- [delete](#delete)
- [add](#add)
- [start slideshow](#start_slideshow)
- [stop slideshow](#stop_slideshow)
- [next slide](#next_slide)
- [previous slide](#previous_slide)
- [pause slideshow](#pause_slideshow)
- [resume slideshow](#resume_slideshow)
- [spotlight](#spotlight)
- [search](#search)
#### Classs
- [media item](#media_item)
- [container](#container)
- [album](#album)
- [folder](#folder)
- [moment](#moment)
#### Class Extensions
- [application](#application)


## Standard Suite

**Description:** Common classes and commands for all applications.

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
<a name="open"></a>
```yaml
---
type: command
name: open
suite: Standard Suite
---
```

## Command: open

**Description:** Open a photo library

### Direct Parameter
- **Description:** The photo library to be opened.
- **Types:** file
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

### Responds To
- **Command:** open
- **Command:** quit
## Photos Suite

**Description:** Classes and commands for Photos

<a name="import"></a>
```yaml
---
type: command
name: import
suite: Photos Suite
---
```

## Command: import

**Description:** Import files into the library

### Direct Parameter
- **Description:** The list of files to copy.
- **Types:** file
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| into | The album to import into. | album | Yes |
| skip check duplicates | Skip duplicate checking and import everything, defaults to false. | boolean | Yes |

### Result
- **Description:** The imported media items in an array
- **Types:** media item
<a name="export"></a>
```yaml
---
type: command
name: export
suite: Photos Suite
---
```

## Command: export

**Description:** Export media items to the specified location as files

### Direct Parameter
- **Description:** The list of media items to export.
- **Types:** media item
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The destination of the export. | file | No |
| using originals | Export the original files if true, otherwise export rendered jpgs. defaults to false. | boolean | Yes |

<a name="duplicate"></a>
```yaml
---
type: command
name: duplicate
suite: Photos Suite
---
```

## Command: duplicate

**Description:** Duplicate an object.  Only media items can be duplicated

### Direct Parameter
- **Description:** The media item to duplicate
- **Types:** media item
### Result
- **Description:** The duplicated media item
- **Types:** media item
<a name="make"></a>
```yaml
---
type: command
name: make
suite: Photos Suite
---
```

## Command: make

**Description:** Create a new object.  Only new albums and folders can be created.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new object, allowed values are album or folder | type | No |
| named | The name of the new object. | text | Yes |
| at | The parent folder for the new object. | folder | Yes |

### Result
- **Description:** The new object.
- **Types:** album, folder
<a name="delete"></a>
```yaml
---
type: command
name: delete
suite: Photos Suite
---
```

## Command: delete

**Description:** Delete an object.  Only albums and folders can be deleted.

### Direct Parameter
- **Description:** The album or folder to delete.
- **Types:** album, folder
<a name="add"></a>
```yaml
---
type: command
name: add
suite: Photos Suite
---
```

## Command: add

**Description:** Add media items to an album.

### Direct Parameter
- **Description:** The list of media items to add.
- **Types:** media item
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The album to add to. | album | No |

<a name="start_slideshow"></a>
```yaml
---
type: command
name: start slideshow
suite: Photos Suite
---
```

## Command: start slideshow

**Description:** Display an ad-hoc slide show from a list of media items, an album, or a folder.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using | The media items to show. | media item | No |

<a name="stop_slideshow"></a>
```yaml
---
type: command
name: stop slideshow
suite: Photos Suite
---
```

## Command: stop slideshow

**Description:** End the currently-playing slideshow.

<a name="next_slide"></a>
```yaml
---
type: command
name: next slide
suite: Photos Suite
---
```

## Command: next slide

**Description:** Skip to next slide in currently-playing slideshow.

<a name="previous_slide"></a>
```yaml
---
type: command
name: previous slide
suite: Photos Suite
---
```

## Command: previous slide

**Description:** Skip to previous slide in currently-playing slideshow.

<a name="pause_slideshow"></a>
```yaml
---
type: command
name: pause slideshow
suite: Photos Suite
---
```

## Command: pause slideshow

**Description:** Pause the currently-playing slideshow.

<a name="resume_slideshow"></a>
```yaml
---
type: command
name: resume slideshow
suite: Photos Suite
---
```

## Command: resume slideshow

**Description:** Resume the currently-playing slideshow.

<a name="spotlight"></a>
```yaml
---
type: command
name: spotlight
suite: Photos Suite
---
```

## Command: spotlight

**Description:** Show the image at path in the application, used to show spotlight search results

### Direct Parameter
- **Description:** The full path to the image
- **Types:** text, media item, container
<a name="search"></a>
```yaml
---
type: command
name: search
suite: Photos Suite
---
```

## Command: search

**Description:** search for items matching the search string. Identical to entering search text in the Search field in Photos

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for | The text to search for | text | No |

### Result
- **Description:** reference(s) to found media item(s)
- **Types:** media item
<a name="media_item"></a>
```yaml
---
type: class
name: media item
suite: Photos Suite
---
```

## Class: media item

**Description:** A media item, such as a photo or video.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| keywords | A list of keywords to associate with a media item | text | read/write |
| name | The name (title) of the media item. | text | read/write |
| description | A description of the media item. | text | read/write |
| favorite | Whether the media item has been favorited. | boolean | read/write |
| date | The date of the media item | date | read/write |
| id | The unique ID of the media item | text | r |
| height | The height of the media item in pixels. | integer | r |
| width | The width of the media item in pixels. | integer | r |
| filename | The name of the file on disk. | text | r |
| altitude | The GPS altitude in meters. | real | r |
| size | The selected media item file size. | integer | rw |
| location | The GPS latitude and longitude, in an ordered list of 2 numbers or missing values.  Latitude in range -90.0 to 90.0, longitude in range -180.0 to 180.0. | real, missing value | read/write |

### Responds To
- **Command:** duplicate
- **Command:** spotlight
<a name="container"></a>
```yaml
---
type: class
name: container
suite: Photos Suite
---
```

## Class: container

**Description:** Base class for collections that contains other items, such as albums and folders

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique ID of this container. | text | r |
| name | The name of this container. | text | read/write |
| parent | This container's parent folder, if any. | folder | r |

### Responds To
- **Command:** spotlight
<a name="album"></a>
```yaml
---
type: class
name: album
suite: Photos Suite
---
```

## Class: album

**Description:** An album. A container that holds media items

**Inherits:** container

### Elements
- **Type:** media item
<a name="folder"></a>
```yaml
---
type: class
name: folder
suite: Photos Suite
---
```

## Class: folder

**Description:** A folder. A container that holds albums and other folders, but not media items

**Inherits:** container

### Elements
- **Type:** container
- **Type:** album
- **Type:** folder
<a name="moment"></a>
```yaml
---
type: class
name: moment
suite: Photos Suite
---
```

## Class: moment

**Description:** A set of media items that represents a Moment.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique ID of the Moment. | text | r |
| name | The name of the Moment. | text | r |

### Elements
- **Type:** media item
<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Photos Suite
---
```

## Class Extension: application

**Description:** The top level scripting object for Photos.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| selection | The currently selected media items in the application | media item | r |
| favorites album | Favorited media items album. | album | r |
| last import album | Last import album. | album | r |
| slideshow running | Returns true if a slideshow is currently running. | boolean | r |
| recently deleted album | The set of recently deleted media items | album | r |

### Elements
- **Type:** container
- **Type:** album
- **Type:** folder
- **Type:** media item
- **Type:** moment
