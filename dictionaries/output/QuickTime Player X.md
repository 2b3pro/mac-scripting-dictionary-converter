# Quicktime Player X: AppleScript/JSX

## Table of Contents

### Internet Suite
#### Commands
- [open URL](#open_url)
#### Class Extensions
- [application](#application)
### QuickTime Player Suite
#### Commands
- [play](#play)
- [start](#start)
- [pause](#pause)
- [resume](#resume)
- [stop](#stop)
- [step backward](#step_backward)
- [step forward](#step_forward)
- [trim](#trim)
- [present](#present)
- [new movie recording](#new_movie_recording)
- [new audio recording](#new_audio_recording)
- [new screen recording](#new_screen_recording)
- [export](#export)
- [show remote hud](#show_remote_hud)
#### Classs
- [video recording device](#video_recording_device)
- [audio recording device](#audio_recording_device)
- [audio compression preset](#audio_compression_preset)
- [movie compression preset](#movie_compression_preset)
- [screen compression preset](#screen_compression_preset)
#### Class Extensions
- [application](#application)
- [document](#document)


## Internet Suite

**Description:** Common URL related functionality

<a name="open_url"></a>
```yaml
---
type: command
name: open URL
suite: Internet Suite
---
```

## Command: open URL

**Description:** Open a URL.

### Direct Parameter
- **Description:** the URL
- **Types:** text
<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Internet Suite
---
```

## Class Extension: application

### Responds To
- **Command:** open URL
## QuickTime Player Suite

**Description:** Classes and Commands for working with QuickTime Player

<a name="play"></a>
```yaml
---
type: command
name: play
suite: QuickTime Player Suite
---
```

## Command: play

**Description:** Play the movie.

### Direct Parameter
- **Description:** the movie to play
- **Types:** document
<a name="start"></a>
```yaml
---
type: command
name: start
suite: QuickTime Player Suite
---
```

## Command: start

**Description:** Start the movie recording.

### Direct Parameter
- **Description:** the recording to start
- **Types:** document
<a name="pause"></a>
```yaml
---
type: command
name: pause
suite: QuickTime Player Suite
---
```

## Command: pause

**Description:** Pause the recording.

### Direct Parameter
- **Description:** the recording to pause
- **Types:** document
<a name="resume"></a>
```yaml
---
type: command
name: resume
suite: QuickTime Player Suite
---
```

## Command: resume

**Description:** Resume the recording.

### Direct Parameter
- **Description:** the recording to resume
- **Types:** document
<a name="stop"></a>
```yaml
---
type: command
name: stop
suite: QuickTime Player Suite
---
```

## Command: stop

**Description:** Stop the movie or recording.

### Direct Parameter
- **Description:** the movie or recording to stop
- **Types:** document
<a name="step_backward"></a>
```yaml
---
type: command
name: step backward
suite: QuickTime Player Suite
---
```

## Command: step backward

**Description:** Step the movie backward the specified number of steps (default is 1).

### Direct Parameter
- **Description:** the movie to step
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | number of steps | integer | Yes |

<a name="step_forward"></a>
```yaml
---
type: command
name: step forward
suite: QuickTime Player Suite
---
```

## Command: step forward

**Description:** Step the movie forward the specified number of steps (default is 1).

### Direct Parameter
- **Description:** the movie to step
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | number of steps | integer | Yes |

<a name="trim"></a>
```yaml
---
type: command
name: trim
suite: QuickTime Player Suite
---
```

## Command: trim

**Description:** Trim the movie.

### Direct Parameter
- **Description:** the movie to trim
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | start time in seconds | real | No |
| to | end time in seconds | real | No |

<a name="present"></a>
```yaml
---
type: command
name: present
suite: QuickTime Player Suite
---
```

## Command: present

**Description:** Present the document full screen.

### Direct Parameter
- **Description:** the document to present
- **Types:** document
<a name="new_movie_recording"></a>
```yaml
---
type: command
name: new movie recording
suite: QuickTime Player Suite
---
```

## Command: new movie recording

**Description:** Create a new movie recording document.

### Result
- **Description:** The new movie recording document.
- **Types:** document
<a name="new_audio_recording"></a>
```yaml
---
type: command
name: new audio recording
suite: QuickTime Player Suite
---
```

## Command: new audio recording

**Description:** Create a new audio recording document.

### Result
- **Description:** The new audio recording document.
- **Types:** document
<a name="new_screen_recording"></a>
```yaml
---
type: command
name: new screen recording
suite: QuickTime Player Suite
---
```

## Command: new screen recording

**Description:** Create a new screen recording document.

<a name="export"></a>
```yaml
---
type: command
name: export
suite: QuickTime Player Suite
---
```

## Command: export

**Description:** Export a movie to another file

### Direct Parameter
- **Description:** the movie to export
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the destination file | file | No |
| using settings preset | the name of the export settings preset to use | text | No |

<a name="show_remote_hud"></a>
```yaml
---
type: command
name: show remote hud
suite: QuickTime Player Suite
---
```

## Command: show remote hud

**Description:** Show the document's Remote HUD

### Direct Parameter
- **Types:** document
<a name="video_recording_device"></a>
```yaml
---
type: class
name: video recording device
suite: QuickTime Player Suite
---
```

## Class: video recording device

**Description:** A video recording device

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the device. | text | r |
| id | The unique identifier of the device. | text | r |

<a name="audio_recording_device"></a>
```yaml
---
type: class
name: audio recording device
suite: QuickTime Player Suite
---
```

## Class: audio recording device

**Description:** An audio recording device

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the device. | text | r |
| id | The unique identifier of the device. | text | r |

<a name="audio_compression_preset"></a>
```yaml
---
type: class
name: audio compression preset
suite: QuickTime Player Suite
---
```

## Class: audio compression preset

**Description:** An audio recording compression preset

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the preset. | text | r |
| id | The unique identifier of the preset. | text | r |

<a name="movie_compression_preset"></a>
```yaml
---
type: class
name: movie compression preset
suite: QuickTime Player Suite
---
```

## Class: movie compression preset

**Description:** A movie recording compression preset

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the preset. | text | r |
| id | The unique identifier of the preset. | text | r |

<a name="screen_compression_preset"></a>
```yaml
---
type: class
name: screen compression preset
suite: QuickTime Player Suite
---
```

## Class: screen compression preset

**Description:** A screen recording compression preset

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the preset. | text | r |
| id | The unique identifier of the preset. | text | r |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: QuickTime Player Suite
---
```

## Class Extension: application

### Elements
- **Type:** video recording device
- **Type:** audio recording device
- **Type:** audio compression preset
- **Type:** movie compression preset
- **Type:** screen compression preset
### Responds To
- **Command:** new movie recording
- **Command:** new audio recording
- **Command:** new screen recording
<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: QuickTime Player Suite
---
```

## Class Extension: document

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| audio volume | The volume of the movie from 0 to 1, where 1 is 100%. | real | rw |
| current time | The current time of the movie in seconds. | real | rw |
| data rate | The data rate of the movie in bytes per second. | integer | r |
| data size | The data size of the movie in bytes. | integer | r |
| duration | The duration of the movie in seconds. | real | r |
| looping | Is the movie playing in a loop? | boolean | rw |
| muted | Is the movie muted? | boolean | rw |
| natural dimensions | The natural dimensions of the movie. | point | r |
| playing | Is the movie playing? | boolean | r |
| rate | The current rate of the movie. | real | rw |
| presenting | Is the movie presented in full screen? | boolean | rw |
| current microphone | The currently previewing audio device. | audio recording device | rw |
| current camera | The currently previewing video device. | video recording device | rw |
| current audio compression | The current audio compression preset. | audio compression preset | rw |
| current movie compression | The current movie compression preset. | movie compression preset | rw |
| current screen compression | The current screen compression preset. | screen compression preset | rw |

### Responds To
- **Command:** play
- **Command:** start
- **Command:** pause
- **Command:** resume
- **Command:** stop
- **Command:** step backward
- **Command:** step forward
- **Command:** trim
- **Command:** present
- **Command:** export
