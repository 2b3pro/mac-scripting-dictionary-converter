# Spotify: AppleScript/JSX

## Table of Contents

### Spotify Suite
#### Commands
- [next track](#next_track)
- [previous track](#previous_track)
- [playpause](#playpause)
- [pause](#pause)
- [play](#play)
- [play track](#play_track)
#### Classs
- [application](#application)
- [track](#track)
#### Enumerations
- [ePlS](#epls)
#### Value Types
- [image data](#image_data)
### Standard Suite
#### Classs
- [application](#application)


## Spotify Suite

**Description:** Spotify specific classes.

<a name="next_track"></a>
```yaml
---
type: command
name: next track
suite: Spotify Suite
---
```

## Command: next track

**Description:** Skip to the next track.

<a name="previous_track"></a>
```yaml
---
type: command
name: previous track
suite: Spotify Suite
---
```

## Command: previous track

**Description:** Skip to the previous track.

<a name="playpause"></a>
```yaml
---
type: command
name: playpause
suite: Spotify Suite
---
```

## Command: playpause

**Description:** Toggle play/pause.

<a name="pause"></a>
```yaml
---
type: command
name: pause
suite: Spotify Suite
---
```

## Command: pause

**Description:** Pause playback.

<a name="play"></a>
```yaml
---
type: command
name: play
suite: Spotify Suite
---
```

## Command: play

**Description:** Resume playback.

<a name="play_track"></a>
```yaml
---
type: command
name: play track
suite: Spotify Suite
---
```

## Command: play track

**Description:** Start playback of a track in the given context.

### Direct Parameter
- **Description:** the URI of the track to play
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in context | the URI of the context to play in | text | Yes |

<a name="application"></a>
```yaml
---
type: class
name: application
suite: Spotify Suite
---
```

## Class: application

**Description:** The Spotify application.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| current track | The current playing track. | track | r |
| sound volume | The sound output volume (0 = minimum, 100 = maximum) | integer | read/write |
| player state | Is Spotify stopped, paused, or playing? | ePlS | r |
| player position | The player’s position within the currently playing track in seconds. | real | read/write |
| repeating enabled | Is repeating enabled in the current playback context? | boolean | r |
| repeating | Is repeating on or off? | boolean | read/write |
| shuffling enabled | Is shuffling enabled in the current playback context? | boolean | r |
| shuffling | Is shuffling on or off? | boolean | read/write |

<a name="track"></a>
```yaml
---
type: class
name: track
suite: Spotify Suite
---
```

## Class: track

**Description:** A Spotify track.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| artist | The artist of the track. | text | r |
| album | The album of the track. | text | r |
| disc number | The disc number of the track. | integer | r |
| duration | The length of the track in seconds. | integer | r |
| played count | The number of times this track has been played. | integer | r |
| track number | The index of the track in its album. | integer | r |
| starred | Is the track starred? | boolean | r |
| popularity | How popular is this track? 0-100 | integer | r |
| id | The ID of the item. | text | r |
| name | The name of the track. | text | r |
| artwork url | The URL of the track%apos;s album cover. | text | r |
| artwork | The property is deprecated and will never be set. Use the 'artwork url' instead. | image data | r |
| album artist | That album artist of the track. | text | r |
| spotify url | The URL of the track. | text | read/write |

<a name="epls"></a>
```yaml
---
type: enumeration
name: ePlS
suite: Spotify Suite
---
```

## Enumeration: ePlS

### Enumerators
| Name | Description |
|---|---|
| stopped | None |
| playing | None |
| paused | None |

<a name="image_data"></a>
```yaml
---
type: value-type
name: image data
suite: Spotify Suite
---
```

## Value Type: image data

**Description:** Image data in TIFF format.

## Standard Suite

**Description:** Common classes and commands for most applications.

<a name="application"></a>
```yaml
---
type: class
name: application
suite: Standard Suite
---
```

## Class: application

**Description:** The application's top level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the application. | text | r |
| frontmost | Is this the frontmost (active) application? | boolean | r |
| version | The version of the application. | text | r |

### Responds To
- **Command:** quit
