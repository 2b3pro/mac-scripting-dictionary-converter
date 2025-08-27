# Sound Studio Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [open](#open)
- [save](#save)
- [close](#close)
- [quit](#quit)
- [count](#count)
- [delete](#delete)
- [duplicate](#duplicate)
- [exists](#exists)
- [make](#make)
- [move](#move)
#### Classs
- [application](#application)
- [document](#document)
- [window](#window)
#### Enumerations
- [save options](#save_options)
### Sound Studio Suite
#### Commands
- [play](#play)
- [record](#record)
- [pause](#pause)
- [unpause](#unpause)
- [stop](#stop)
- [resample](#resample)
- [mixdown](#mixdown)
- [cut](#cut)
- [copy](#copy)
- [paste](#paste)
- [clear](#clear)
- [silence](#silence)
- [crop](#crop)
- [split](#split)
- [insert silence at](#insert_silence_at)
- [insert noise at](#insert_noise_at)
- [insert tone at](#insert_tone_at)
- [insert fm at](#insert_fm_at)
- [amplify](#amplify)
- [fade](#fade)
- [normalize](#normalize)
- [compress dynamics of](#compress_dynamics_of)
- [expand dynamics of](#expand_dynamics_of)
- [noise gate](#noise_gate)
- [add noise to](#add_noise_to)
- [add more cowbell to](#add_more_cowbell_to)
- [dc offset](#dc_offset)
- [interpolate](#interpolate)
- [invert](#invert)
- [swap channels of](#swap_channels_of)
- [reverse](#reverse)
- [add chorus to](#add_chorus_to)
- [add delay to](#add_delay_to)
- [flange](#flange)
- [change pitch of](#change_pitch_of)
- [add reverb to](#add_reverb_to)
- [equalize](#equalize)
- [high pass](#high_pass)
- [low pass](#low_pass)
- [expand tilde](#expand_tilde)
#### Classs
- [metadata](#metadata)
- [marker](#marker)
- [track](#track)
- [sound selection](#sound_selection)
#### Enumerations
- [track configurations](#track_configurations)
- [wave shapes](#wave_shapes)
- [fade directions](#fade_directions)


## Standard Suite

**Description:** Common classes and commands for all applications.

<a name="open"></a>
```yaml
---
type: command
name: open
suite: Standard Suite
---
```

## Command: open

**Description:** Open a document.

### Direct Parameter
- **Description:** The file(s) to be opened, as a file Alias or String
- **Types:** file
<a name="save"></a>
```yaml
---
type: command
name: save
suite: Standard Suite
---
```

## Command: save

**Description:** Save a document.

### Direct Parameter
- **Description:** the document(s) or window(s) to save.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | the file in which to save the document. | file | Yes |
| as | the file format. Accepted values include: AIFF (or AIF), AIFF-C (or AIFC), ADTS (or ADTC AAC), CAF, FLAC, AAC (or M4A), Apple Lossless (or ALAC or Lossless), NeXT (or au or Sun or ulaw), MP3 (or MPEG3), Ogg Vorbis (or Ogg or Vorbis), Text (or TXT), and WAV (or WAVE or BWF). Also accepts file type names from the Save panel's File Format pop-up. | text | Yes |

<a name="close"></a>
```yaml
---
type: command
name: close
suite: Standard Suite
---
```

## Command: close

**Description:** Close a document.

### Direct Parameter
- **Description:** the document(s) or window(s) to close.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Whether or not changes should be saved before closing. | save options | Yes |
| saving in | the file in which to save the document. | file | Yes |

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
| saving | Whether or not changed documents should be saved before closing. | save options | Yes |

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
- **Description:** the object whose elements are to be counted
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| each | the class of objects to be counted. | type | Yes |

### Result
- **Description:** the number of elements
- **Types:** integer
<a name="delete"></a>
```yaml
---
type: command
name: delete
suite: Standard Suite
---
```

## Command: delete

**Description:** Delete an object.

### Direct Parameter
- **Description:** the object to delete
- **Types:** specifier
<a name="duplicate"></a>
```yaml
---
type: command
name: duplicate
suite: Standard Suite
---
```

## Command: duplicate

**Description:** Copy object(s) and put the copies at a new location.

### Direct Parameter
- **Description:** the object(s) to duplicate
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the location for the new object(s). | location specifier | No |
| with properties | Properties to be set in the new duplicated object(s). | record | Yes |

<a name="exists"></a>
```yaml
---
type: command
name: exists
suite: Standard Suite
---
```

## Command: exists

**Description:** Verify if an object exists.

### Direct Parameter
- **Description:** the object in question
- **Types:** any
### Result
- **Description:** true if it exists, false if not
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

**Description:** Make a new object.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | the class of the new object. | type | No |
| at | the location at which to insert the object. | location specifier | Yes |
| with data | the initial contents of the object. | any | Yes |
| with properties | the initial values for properties of the object. | record | Yes |

### Result
- **Description:** to the new object
- **Types:** specifier
<a name="move"></a>
```yaml
---
type: command
name: move
suite: Standard Suite
---
```

## Command: move

**Description:** Move object(s) to a new location.

### Direct Parameter
- **Description:** the object(s) to move
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the new location for the object(s). | location specifier | No |

<a name="application"></a>
```yaml
---
type: class
name: application
suite: Standard Suite
---
```

## Class: application

**Description:** the application's top-level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the name of the application. | text | r |
| frontmost | Is this the frontmost (active) application? | boolean | r |
| version | the version of the application. | text | r |
| playback volume | the playback volume in decibels. | real | read/write |
| is recording | Is Sound Studio recording in any document? | boolean | r |
| selection | the current selection in the frontmost window. | sound selection | r |

### Elements
- **Type:** document
- **Type:** window
### Responds To
- **Command:** None
- **Command:** None
<a name="document"></a>
```yaml
---
type: class
name: document
suite: Standard Suite
---
```

## Class: document

**Description:** A Sound Studio document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the document's name. | text | r |
| modified | Has the document been modified since the last save? | boolean | r |
| file | the document's location on disk. | file | r |
| sample rate | the sample rate in hertz. | real | read/write |
| bit rate | the bit rate in bits per second. | real | read/write |
| sample size | the sample size in bits per sample (for AIFF, WAVE, NeXT/Sun, and CAF file formats, if applicable). | integer | read/write |
| data format | the data format (as an integer code converted from OSType) of the audio in the file, if applicable to the document's file type. | integer | read/write |
| sample count | the total number of sample frames. | integer | r |
| total time | the total duration in seconds. | real | r |
| loops | if set to yes, playback repeats. | boolean | read/write |
| options window shown on save | (Obsolete) | boolean | read/write |
| extensionless name | the display name without filename extension. | text | r |
| metadata | audio file metadata. | metadata | read/write |

### Elements
- **Type:** marker
- **Type:** track
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
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

**Description:** A window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the full title of the window. | text | r |
| id | the unique identifier of the window. | integer | r |
| index | the index of the window, ordered front to back. | integer | read/write |
| bounds | the bounding rectangle of the window. | rectangle | read/write |
| closeable | Whether the window has a close box. | boolean | r |
| miniaturizable | Whether the window can be minimized. | boolean | r |
| miniaturized | Whether the window is currently minimized. | boolean | read/write |
| resizable | Whether the window can be resized. | boolean | r |
| visible | Whether the window is currently visible. | boolean | read/write |
| zoomable | Whether the window frame can be zoomed (maximized). | boolean | r |
| zoomed | Whether the window frame is currently zoomed (maximized). | boolean | read/write |
| document | the document whose contents are being displayed in the window. | document | r |
| selection | the current selection in this window. | sound selection | read/write |

### Responds To
- **Command:** None
- **Command:** None
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

## Sound Studio Suite

**Description:** Sound Studio-specific classes and commands.

<a name="play"></a>
```yaml
---
type: command
name: play
suite: Sound Studio Suite
---
```

## Command: play

**Description:** Play back audio.

### Direct Parameter
- **Description:** the item(s) to play
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the starting time in seconds. | real | Yes |
| to | the ending time in seconds. | real | Yes |

<a name="record"></a>
```yaml
---
type: command
name: record
suite: Sound Studio Suite
---
```

## Command: record

**Description:** Record audio at end of file.

### Direct Parameter
- **Description:** the document(s) for recording
- **Types:** specifier
<a name="pause"></a>
```yaml
---
type: command
name: pause
suite: Sound Studio Suite
---
```

## Command: pause

**Description:** Pause playback or recording.

### Direct Parameter
- **Description:** the item(s) to pause
- **Types:** specifier
<a name="unpause"></a>
```yaml
---
type: command
name: unpause
suite: Sound Studio Suite
---
```

## Command: unpause

**Description:** Unpause playback or recording.

### Direct Parameter
- **Description:** the item(s) to unpause
- **Types:** specifier
<a name="stop"></a>
```yaml
---
type: command
name: stop
suite: Sound Studio Suite
---
```

## Command: stop

**Description:** Stop playback or recording.

### Direct Parameter
- **Description:** the item(s) to stop
- **Types:** specifier
<a name="resample"></a>
```yaml
---
type: command
name: resample
suite: Sound Studio Suite
---
```

## Command: resample

**Description:** Resample audio sample data.

### Direct Parameter
- **Description:** the document(s) to resample
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the new sample rate in hertz. | real | No |

<a name="mixdown"></a>
```yaml
---
type: command
name: mixdown
suite: Sound Studio Suite
---
```

## Command: mixdown

**Description:** Mixdown audio tracks.

### Direct Parameter
- **Description:** the document(s) to mixdown
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the desired number of tracks to mix down to. | track configurations | No |

<a name="cut"></a>
```yaml
---
type: command
name: cut
suite: Sound Studio Suite
---
```

## Command: cut

**Description:** Cut

### Direct Parameter
- **Description:** selection
- **Types:** specifier
<a name="copy"></a>
```yaml
---
type: command
name: copy
suite: Sound Studio Suite
---
```

## Command: copy

**Description:** Copy

### Direct Parameter
- **Description:** selection
- **Types:** specifier
<a name="paste"></a>
```yaml
---
type: command
name: paste
suite: Sound Studio Suite
---
```

## Command: paste

**Description:** Paste

### Direct Parameter
- **Description:** selection
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| existing | setting for level for existing, selected audio | real | Yes |
| pasteboard | setting for level for copied pasteboard audio | real | Yes |
| inside | if true, paste inside selection only | boolean | Yes |

<a name="clear"></a>
```yaml
---
type: command
name: clear
suite: Sound Studio Suite
---
```

## Command: clear

**Description:** Delete audio

### Direct Parameter
- **Description:** selection
- **Types:** specifier
<a name="silence"></a>
```yaml
---
type: command
name: silence
suite: Sound Studio Suite
---
```

## Command: silence

**Description:** Silence

### Direct Parameter
- **Description:** selection
- **Types:** specifier
<a name="crop"></a>
```yaml
---
type: command
name: crop
suite: Sound Studio Suite
---
```

## Command: crop

**Description:** Crop by deleting audio before and after the specified times.

### Direct Parameter
- **Description:** the item(s) to crop
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| start | the start time for the crop | real | No |
| end | the end time for the crop | real | No |

<a name="split"></a>
```yaml
---
type: command
name: split
suite: Sound Studio Suite
---
```

## Command: split

**Description:** Split by markers and save to files.

### Direct Parameter
- **Description:** the document to split
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| into | the folder into which to save, as a POSIX path (/Users/name/Desktop for example). | file | Yes |
| prefix | if set, prefix file names with a number (01, 02, 03, etc.) | boolean | Yes |
| start | the number from which to start counting | integer | Yes |
| format | file format. Accepted values include: AIFF (or AIF), AIFF-C (or AIFC), ADTS (or ADTC AAC), CAF, FLAC, AAC (or M4A), Apple Lossless (or ALAC or Lossless), NeXT (or au or Sun or ulaw), MP3 (or MPEG3), Ogg Vorbis (or Ogg or Vorbis), Text (or TXT), and WAV (or WAVE or BWF). Also accepts file type names from the Save panel's File Format pop-up. | text | Yes |
| bit rate | target bit rate for MP3 and AAC formats (8000 to 320000) | integer | Yes |
| sample size | sample size for AIFF, WAVE and other PCM formats | integer | Yes |

### Result
- **Description:** files created
- **Types:** list of file
<a name="insert_silence_at"></a>
```yaml
---
type: command
name: insert silence at
suite: Sound Studio Suite
---
```

## Command: insert silence at

**Description:** Insert silence at selection.

### Direct Parameter
- **Description:** the selection
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| duration | the duration, in seconds, of the silence to be inserted | real | No |
| replacing selection | if set, replace the selection with specified duration of silence, otherwise insert silence after selection. Default is yes. | boolean | Yes |

<a name="insert_noise_at"></a>
```yaml
---
type: command
name: insert noise at
suite: Sound Studio Suite
---
```

## Command: insert noise at

**Description:** Insert noise at selection.

### Direct Parameter
- **Description:** the selection
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| duration | the duration, in seconds, of the noise to be inserted | real | No |
| amplitude | the amplitude, in decibels, of the noise to be inserted. This is typically a negative value. Defaults to 0 dB. | real | Yes |
| replacing selection | if set, replace the selection with specified duration of silence, otherwise insert silence after selection. Default is yes. | boolean | Yes |

<a name="insert_tone_at"></a>
```yaml
---
type: command
name: insert tone at
suite: Sound Studio Suite
---
```

## Command: insert tone at

**Description:** Insert tone at selection.

### Direct Parameter
- **Description:** the selection
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| duration | the duration, in seconds, of the tone to be inserted. | real | No |
| amplitude | the amplitude, in decibels, of the tone to be inserted. This is typically a negative value. Defaults to 0 dB. | real | Yes |
| frequency | the frequency, in hertz, of the tone to be inserted. | real | No |
| wave shape | the wave shape of the tone to be inserted. Defaults to sine wave. | wave shapes | Yes |
| replacing selection | if set, replace the selection, otherwise insert after selection. Default is yes. | boolean | Yes |

<a name="insert_fm_at"></a>
```yaml
---
type: command
name: insert fm at
suite: Sound Studio Suite
---
```

## Command: insert fm at

**Description:** Insert FM Synthesis at selection.

### Direct Parameter
- **Description:** the selection
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| duration | the duration, in seconds, of the tone to be inserted | real | No |
| amplitude | the amplitude, in decibels, of the tone to be inserted. This is typically a negative value. Defaults to 0 dB. | real | Yes |
| carrier | the carrier frequency, in hertz, of the tone to be inserted. | real | No |
| modulation | the modulation frequency, in hertz, of the tone to be inserted. | real | No |
| deviation | the deviation frequency, in hertz, of the tone to be inserted. | real | No |
| replacing selection | if set, replace the selection, otherwise insert after selection. Default is yes. | boolean | Yes |

<a name="amplify"></a>
```yaml
---
type: command
name: amplify
suite: Sound Studio Suite
---
```

## Command: amplify

**Description:** Apply the Amplify/Volume filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | the gain, in decibels; amplification or volume change. | real | No |

<a name="fade"></a>
```yaml
---
type: command
name: fade
suite: Sound Studio Suite
---
```

## Command: fade

**Description:** Apply the Fade In/Out filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| start | the start time for the fade. If not set, then fade the entire selection or document. | real | Yes |
| end | the end time for the fade. If not set, then fade the entire selection or document. | real | Yes |
| direction | if set, applies a linear fade in if coming and a linear fade out if going; the fade is coming in from silence or going out to silence. | fade directions | Yes |
| data points | a set of data points in the form of x-y coordinate pairs, such as {0.0, 1.0, 1.0, 1.0}. If set, this overrides the direction parameter. | list of real | Yes |

<a name="normalize"></a>
```yaml
---
type: command
name: normalize
suite: Sound Studio Suite
---
```

## Command: normalize

**Description:** Apply the Normalize filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the level which to set the peak, in decibels. | real | No |
| independently | if set, adjust the levels in each track separately from each other, otherwise determine a single amplification factor for all tracks and apply the same change to all tracks. | boolean | Yes |
| RMS | if set, measure levels using root-mean-square, which is the average power of the signal, otherwise use the peaks, which are the tallest parts of the waveform. | boolean | Yes |

<a name="compress_dynamics_of"></a>
```yaml
---
type: command
name: compress dynamics of
suite: Sound Studio Suite
---
```

## Command: compress dynamics of

**Description:** Apply the Dynamics Compressor filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| rms | If set to true, use RMS to measure the signal. If set to false, use peaks to measure the signal. | boolean | No |
| threshold | the level above which to compress the waveform, in decibels. | real | No |
| ratio | the compression ratio. | real | No |
| attack | how fast the compressor reacts to the level going above the threshold, in seconds. | real | No |
| release | how fast the compressor reacts to the level going above the threshold, in seconds. | real | No |
| post | the post gain, in decibels. If omitted, post gain is automatic. | real | Yes |

<a name="expand_dynamics_of"></a>
```yaml
---
type: command
name: expand dynamics of
suite: Sound Studio Suite
---
```

## Command: expand dynamics of

**Description:** Apply the Dynamics Expander filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| rms | If set to true, use RMS to measure the signal. If set to false, use peaks to measure the signal. | boolean | No |
| threshold | the level above which to compress the waveform, in decibels. | real | No |
| ratio | the compression ratio. | real | No |
| attack | how fast the compressor reacts to the level going above the threshold, in seconds. | real | No |
| release | how fast the compressor reacts to the level going above the threshold, in seconds. | real | No |

<a name="noise_gate"></a>
```yaml
---
type: command
name: noise gate
suite: Sound Studio Suite
---
```

## Command: noise gate

**Description:** Apply the Dynamics Noise Gate Expander filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| rms | If set to true, use RMS to measure the signal. If set to false, use peaks to measure the signal. | boolean | No |
| threshold | the level above which to compress the waveform, in decibels. | real | No |
| attack | how fast the compressor reacts to the level going above the threshold, in seconds. | real | No |
| release | how fast the compressor reacts to the level going above the threshold, in seconds. | real | No |

<a name="add_noise_to"></a>
```yaml
---
type: command
name: add noise to
suite: Sound Studio Suite
---
```

## Command: add noise to

**Description:** Apply the Add Noise filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| amplitude | the noise amplitude, in decibels, of the noise to be inserted. This is typically a negative value. | real | No |

<a name="add_more_cowbell_to"></a>
```yaml
---
type: command
name: add more cowbell to
suite: Sound Studio Suite
---
```

## Command: add more cowbell to

**Description:** More Cowbell. Really explore the studio space this time.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| amplitude | how much cowbell? | real | No |

<a name="dc_offset"></a>
```yaml
---
type: command
name: dc offset
suite: Sound Studio Suite
---
```

## Command: dc offset

**Description:** Apply the DC Offset filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | the percent to offset, typically from -100 to 100. If omitted, this command will remove any DC offset. | real | Yes |

<a name="interpolate"></a>
```yaml
---
type: command
name: interpolate
suite: Sound Studio Suite
---
```

## Command: interpolate

**Description:** Apply the Interpolate filter to the audio; replaces audio with a straight line between the first and last samples.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
<a name="invert"></a>
```yaml
---
type: command
name: invert
suite: Sound Studio Suite
---
```

## Command: invert

**Description:** Apply the Invert Signal Polarity filter to the audio; flips audio vertically.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
<a name="swap_channels_of"></a>
```yaml
---
type: command
name: swap channels of
suite: Sound Studio Suite
---
```

## Command: swap channels of

**Description:** Apply the Swap Left and Right Channels filter to the audio; swaps audio data between even and odd numbered tracks.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
<a name="reverse"></a>
```yaml
---
type: command
name: reverse
suite: Sound Studio Suite
---
```

## Command: reverse

**Description:** Apply the Backwards/Reverse Audio filter to the audio; makes audio sound like it is played backwards.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
<a name="add_chorus_to"></a>
```yaml
---
type: command
name: add chorus to
suite: Sound Studio Suite
---
```

## Command: add chorus to

**Description:** Apply the Chorus filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| dry | the dry mix level, in decibels. Defaults to 0 dB. | real | Yes |
| wet | the wet mix level, in decibels. Defaults to 0 dB. | real | Yes |
| speed | the speed at which the chorus cycles, in seconds. Defaults to 2 seconds. | real | Yes |
| delay | the minimum delay, in milliseconds. Defaults to 10 milliseconds. | real | Yes |
| depth | the sweep depth, in milliseconds. Defaults to 15 milliseconds. | real | Yes |

<a name="add_delay_to"></a>
```yaml
---
type: command
name: add delay to
suite: Sound Studio Suite
---
```

## Command: add delay to

**Description:** Apply the Delay and Echo filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| dry | the dry mix level, in decibels. Defaults to 0 dB. | real | Yes |
| wet | the wet mix level, in decibels. Defaults to 0 dB. | real | Yes |
| delay | the delay, in seconds. Defaults to 0.1 seconds. | real | Yes |
| feedback | if set to true, feed the delayed audio back into the feedback loop. Defaults to false. | boolean | Yes |

<a name="flange"></a>
```yaml
---
type: command
name: flange
suite: Sound Studio Suite
---
```

## Command: flange

**Description:** Apply the Flanger filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| dry | the dry mix level, in decibels. Defaults to 0 dB. | real | Yes |
| wet | the wet mix level, in decibels. Defaults to 0 dB. | real | Yes |
| speed | the speed at which the flanger cycles, in seconds. Defaults to 2 seconds. | real | Yes |
| delay | the minimum delay, in milliseconds. Defaults to 10 milliseconds. | real | Yes |
| depth | the sweep depth, in milliseconds. Defaults to 15 milliseconds. | real | Yes |

<a name="change_pitch_of"></a>
```yaml
---
type: command
name: change pitch of
suite: Sound Studio Suite
---
```

## Command: change pitch of

**Description:** Apply the Pitch and Tempo filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | the number of cents to change pitch (negative values lower the pitch, positive values raise the pitch). | real | No |
| tempo | the tempo as a percent. | real | Yes |

<a name="add_reverb_to"></a>
```yaml
---
type: command
name: add reverb to
suite: Sound Studio Suite
---
```

## Command: add reverb to

**Description:** Apply the Reverb filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| room size | the approximate width and length of the room to simulate, in meters. Defaults to 10 meters. | real | Yes |
| decay | the decay, in seconds. Defaults to 2 seconds. | real | Yes |
| color | the cut-off for the low-pass filter, in hertz. Defaults to 12,800 Hz. | real | Yes |
| wet | the wet mix level, in decibels. Defaults to -20 dB. | real | Yes |

<a name="equalize"></a>
```yaml
---
type: command
name: equalize
suite: Sound Studio Suite
---
```

## Command: equalize

**Description:** Apply the Graphic Equalizer filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| data points | the cut-off frequency, in hertz. | list of real | No |

<a name="high_pass"></a>
```yaml
---
type: command
name: high pass
suite: Sound Studio Suite
---
```

## Command: high pass

**Description:** Apply the High Pass filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| frequency | the cut-off frequency, in hertz. | real | No |
| steepness | the steepness or window width, in number of samples. A higher number results in a steeper drop-off. Defaults to 63 samples. | integer | Yes |

<a name="low_pass"></a>
```yaml
---
type: command
name: low pass
suite: Sound Studio Suite
---
```

## Command: low pass

**Description:** Apply the Low Pass filter to the audio.

### Direct Parameter
- **Description:** the item(s) to filter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| frequency | the cut-off frequency, in hertz. | real | No |
| steepness | the steepness or window width, in number of samples. A higher number results in a steeper drop-off. Defaults to 63 samples. | integer | Yes |

<a name="expand_tilde"></a>
```yaml
---
type: command
name: expand tilde
suite: Sound Studio Suite
---
```

## Command: expand tilde

**Description:** Expand tilde in POSIX path to full absolute path. (Example: expand tilde document from "~/Desktop/".) Granted, the syntax of this command isn't elegant, but I'm working with the default Cocoa AppleScript implementation's limitations.

### Direct Parameter
- **Description:** document to use for conversion
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | the tilde path. | text | No |

### Result
- **Description:** the absolute path
- **Types:** text
<a name="metadata"></a>
```yaml
---
type: class
name: metadata
suite: Sound Studio Suite
---
```

## Class: metadata

**Description:** Audio file metadata.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| title | song name/title | text | read/write |
| artist | artist | text | read/write |
| album artist | album artist | text | read/write |
| album | album | text | read/write |
| track number | track number | integer | read/write |
| track total | total number of tracks | integer | read/write |
| disc number | disc number | integer | read/write |
| disc total | total number of discs | integer | read/write |
| grouping | grouping | text | read/write |
| composer | composer | text | read/write |
| comments | comments | text | read/write |
| year | year | text | read/write |
| tempo | tempo | integer | read/write |
| genre | genre | text | read/write |
| compilation | compilation | boolean | read/write |
| gapless | gapless | boolean | read/write |
| podcast | podcast | boolean | read/write |
| advisory | advisory | integer | read/write |
| copyright | copyright | text | read/write |
| director | director | text | read/write |
| format | format | text | read/write |
| purchase date | purchase date | text | read/write |
| category | category | text | read/write |
| egid | egid | text | read/write |
| short description | normal description | text | read/write |
| long description | extended description | text | read/write |
| keywords | keywords | text | read/write |
| podcast url | feed url | text | read/write |
| lyrics | lyrics | text | read/write |

<a name="marker"></a>
```yaml
---
type: class
name: marker
suite: Sound Studio Suite
---
```

## Class: marker

**Description:** An audio marker. This class represents an individual marker cue point in the document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| ident | the numeric identifier (ID). | integer | read/write |
| position | the position of the marker in the file, as a sample offset. | integer | read/write |
| name | the marker's name. | text | read/write |

<a name="track"></a>
```yaml
---
type: class
name: track
suite: Sound Studio Suite
---
```

## Class: track

**Description:** An audio track. This class represents an individual audio track in the document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| volume | the track volume in decibels. | real | read/write |
| pan | the track pan, where -1 is hard left, 0 is center, and 1 is hard right. | real | read/write |

<a name="sound_selection"></a>
```yaml
---
type: class
name: sound selection
suite: Sound Studio Suite
---
```

## Class: sound selection

**Description:** A selection. For macro-type scripting, almost all the commands use a sound selection as the direct parameter. Get the selection from the application or window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| start time | the beginning of the selection, in seconds. | real | read/write |
| stop time | the end of the selection, in seconds. | real | read/write |
| first track | the index of the first track of the selection. | integer | read/write |
| track count | the number of tracks in the selection. | integer | read/write |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="track_configurations"></a>
```yaml
---
type: enumeration
name: track configurations
suite: Sound Studio Suite
---
```

## Enumeration: track configurations

### Enumerators
| Name | Description |
|---|---|
| mono | Monophonic audio. |
| stereo | Stereophonic audio. |

<a name="wave_shapes"></a>
```yaml
---
type: enumeration
name: wave shapes
suite: Sound Studio Suite
---
```

## Enumeration: wave shapes

### Enumerators
| Name | Description |
|---|---|
| sine | a pure sine wave. |
| square | a square wave. |
| triangle | a triangular wave. |

<a name="fade_directions"></a>
```yaml
---
type: enumeration
name: fade directions
suite: Sound Studio Suite
---
```

## Enumeration: fade directions

### Enumerators
| Name | Description |
|---|---|
| coming | Fade In |
| going | Fade Out |

