# Apple Shortcuts: AppleScript/JSX

## Table of Contents

### Shortcuts Suite
#### Commands
- [run](#run)
#### Classs
- [shortcut](#shortcut)
- [folder](#folder)
#### Value Types
- [RGB color](#rgb_color)
- [TIFF image](#tiff_image)
#### Class Extensions
- [application](#application)


## Shortcuts Suite

**Description:** Classes and Commands for working with Shortcuts

<a name="run"></a>
```yaml
---
type: command
name: run
suite: Shortcuts Suite
---
```

## Command: run

**Description:** Run a shortcut. To run a shortcut in the background, without opening the Shortcuts app, tell 'Shortcuts Events' instead of 'Shortcuts'.

### Direct Parameter
- **Description:** the shortcut to run
- **Types:** shortcut
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with input | the input to provide to the shortcut | any | Yes |

### Result
- **Description:** the result of the shortcut
- **Types:** any
<a name="shortcut"></a>
```yaml
---
type: class
name: shortcut
suite: Shortcuts Suite
---
```

## Class: shortcut

**Description:** a shortcut in the Shortcuts application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the name of the shortcut | text | r |
| subtitle | the shortcut's subtitle | text | r |
| id | the unique identifier of the shortcut | text | r |
| folder | the folder containing this shortcut | folder | rw |
| color | the shortcut's color | RGB color | r |
| icon | the shortcut's icon | TIFF image | r |
| accepts input | indicates whether or not the shortcut accepts input data | boolean | r |
| action count | the number of actions in the shortcut | integer | r |

### Responds To
- **Command:** run
<a name="folder"></a>
```yaml
---
type: class
name: folder
suite: Shortcuts Suite
---
```

## Class: folder

**Description:** a folder containing shortcuts

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the name of the folder | text | rw |
| id | the unique identifier of the folder | text | r |

### Elements
- **Type:** shortcut
<a name="rgb_color"></a>
```yaml
---
type: value-type
name: RGB color
suite: Shortcuts Suite
---
```

## Value Type: RGB color

<a name="tiff_image"></a>
```yaml
---
type: value-type
name: TIFF image
suite: Shortcuts Suite
---
```

## Value Type: TIFF image

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Shortcuts Suite
---
```

## Class Extension: application

### Elements
- **Type:** shortcut
- **Type:** folder
