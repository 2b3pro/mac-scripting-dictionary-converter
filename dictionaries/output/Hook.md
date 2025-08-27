# Hookmark Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [exists](#exists)
- [make](#make)
- [count](#count)
#### Classs
- [application](#application)
### Hookmark Suite
#### Commands
- [percent encode](#percent_encode)
- [percent decode](#percent_decode)
- [hook](#hook)
- [unhook](#unhook)
- [invoke on](#invoke_on)
- [bookmark by request handle](#bookmark_by_request_handle)
- [bookmark from active window](#bookmark_from_active_window)
#### Classs
- [application](#application)
- [bookmark](#bookmark)


## Standard Suite

**Description:** Subset of the Standard Suite.

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
| with properties | The initial values for properties of the object. | record | Yes |

### Result
- **Description:** The new object.
- **Types:** specifier
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
## Hookmark Suite

**Description:** Hook-specific classes.

<a name="percent_encode"></a>
```yaml
---
type: command
name: percent encode
suite: Hookmark Suite
---
```

## Command: percent encode

**Description:** percent encode a given string

### Direct Parameter
- **Description:** string
- **Types:** text
### Result
- **Description:** encoded string
- **Types:** text
<a name="percent_decode"></a>
```yaml
---
type: command
name: percent decode
suite: Hookmark Suite
---
```

## Command: percent decode

**Description:** remove percent encoding from a string

### Direct Parameter
- **Description:** string
- **Types:** text
### Result
- **Description:** decoded string
- **Types:** text
<a name="hook"></a>
```yaml
---
type: command
name: hook
suite: Hookmark Suite
---
```

## Command: hook

**Description:** Hook two bookmark together

### Direct Parameter
- **Description:** bookmark
- **Types:** bookmark
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| and | another bookmark | bookmark | No |

<a name="unhook"></a>
```yaml
---
type: command
name: unhook
suite: Hookmark Suite
---
```

## Command: unhook

**Description:** Remove link between two bookmarks.

### Direct Parameter
- **Description:** bookmark
- **Types:** bookmark
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| and | another bookmark | bookmark | No |

<a name="invoke_on"></a>
```yaml
---
type: command
name: invoke on
suite: Hookmark Suite
---
```

## Command: invoke on

**Description:** Open a bookmark in Hookmark.

### Direct Parameter
- **Description:** bookmark
- **Types:** bookmark
<a name="bookmark_by_request_handle"></a>
```yaml
---
type: command
name: bookmark by request handle
suite: Hookmark Suite
---
```

## Command: bookmark by request handle

**Description:** Get a bookmark for the specified asynchronous request handle (ID) that was previously returned by Hookmark's  "bookmark from active window" command. This is typically useful for apps controlled by x-callback-url.

### Direct Parameter
- **Description:** an asynchronous request handle (an ID)
- **Types:** text
### Result
- **Description:** a bookmark
- **Types:** bookmark
<a name="bookmark_from_active_window"></a>
```yaml
---
type: command
name: bookmark from active window
suite: Hookmark Suite
---
```

## Command: bookmark from active window

**Description:** Get a bookmark for the currently selected or currently open item of the active window of the active app. However, if Hookmark cannot immediately return such a bookmark for the item (e.g., in case of apps with which Hookmark uses x-callback-url), then you'll receive an asynchronous request handle (ID) for this item. In the latter case, you can subsequently apply the request handle (ID) to Hookmark's "bookmark by request handle" command to get the bookmark you need. 

### Result
- **Description:** a bookmark or a request handle
- **Types:** bookmark, text
<a name="application"></a>
```yaml
---
type: class
name: application
suite: Hookmark Suite
---
```

## Class: application

**Description:** Hookmark's top level scripting object.

**Inherits:** application

### Elements
- **Type:** bookmark
<a name="bookmark"></a>
```yaml
---
type: class
name: bookmark
suite: Hookmark Suite
---
```

## Class: bookmark

**Description:** A hookable reference to a file or document.

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the bookmark. | text | rw |
| address | The URL of the bookmarked item. | text | r |
| path | The POSIX path of the bookmarked item, or "" if bookmarked item is not an available file. | text | r |
| hooked bookmarks | List of bookmarks which are hooked together with the bookmarked item. | bookmark | r |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
