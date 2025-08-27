# Apple Music: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [print](#print)
- [close](#close)
- [count](#count)
- [delete](#delete)
- [duplicate](#duplicate)
- [exists](#exists)
- [make](#make)
- [move](#move)
- [open](#open)
- [run](#run)
- [quit](#quit)
- [save](#save)
#### Enumerations
- [eKnd](#eknd)
- [enum](#enum)
#### Record Types
- [print settings](#print_settings)
### Music Suite
#### Commands
- [add](#add)
- [back track](#back_track)
- [convert](#convert)
- [download](#download)
- [export](#export)
- [fast forward](#fast_forward)
- [next track](#next_track)
- [pause](#pause)
- [play](#play)
- [playpause](#playpause)
- [previous track](#previous_track)
- [refresh](#refresh)
- [resume](#resume)
- [reveal](#reveal)
- [rewind](#rewind)
- [search](#search)
- [select](#select)
- [stop](#stop)
#### Classs
- [AirPlay device](#airplay_device)
- [application](#application)
- [artwork](#artwork)
- [audio CD playlist](#audio_cd_playlist)
- [audio CD track](#audio_cd_track)
- [browser window](#browser_window)
- [encoder](#encoder)
- [EQ preset](#eq_preset)
- [EQ window](#eq_window)
- [file track](#file_track)
- [folder playlist](#folder_playlist)
- [item](#item)
- [library playlist](#library_playlist)
- [miniplayer window](#miniplayer_window)
- [playlist](#playlist)
- [playlist window](#playlist_window)
- [radio tuner playlist](#radio_tuner_playlist)
- [shared track](#shared_track)
- [source](#source)
- [subscription playlist](#subscription_playlist)
- [track](#track)
- [URL track](#url_track)
- [user playlist](#user_playlist)
- [video window](#video_window)
- [visual](#visual)
- [window](#window)
#### Enumerations
- [ePlS](#epls)
- [eRpt](#erpt)
- [eShM](#eshm)
- [eSrc](#esrc)
- [eSrA](#esra)
- [eSpK](#espk)
- [eMdK](#emdk)
- [eRtK](#ertk)
- [eAPD](#eapd)
- [eClS](#ecls)
- [eExF](#eexf)
#### Value Types
- [double integer](#double_integer)
- [picture](#picture)
### Internet suite
#### Commands
- [open location](#open_location)


## Standard Suite

**Description:** Common terms for most applications

<a name="print"></a>
```yaml
---
type: command
name: print
suite: Standard Suite
---
```

## Command: print

**Description:** Print the specified object(s)

### Direct Parameter
- **Description:** list of objects to print
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| print dialog | Should the application show the print dialog | boolean | Yes |
| with properties | the print settings | print settings | Yes |
| kind | the kind of printout desired | eKnd | Yes |
| theme | name of theme to use for formatting the printout | text | Yes |

<a name="close"></a>
```yaml
---
type: command
name: close
suite: Standard Suite
---
```

## Command: close

**Description:** Close an object

### Direct Parameter
- **Description:** the object to close
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

**Description:** Return the number of elements of a particular class within an object

### Direct Parameter
- **Description:** the object whose elements are to be counted
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| each | the class of the elements to be counted. Keyword 'each' is optional in AppleScript | type | No |

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

**Description:** Delete an element from an object

### Direct Parameter
- **Description:** the element to delete
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

**Description:** Duplicate one or more object(s)

### Direct Parameter
- **Description:** the object(s) to duplicate
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the new location for the object(s) | location specifier | Yes |

### Result
- **Description:** to the duplicated object(s)
- **Types:** specifier
<a name="exists"></a>
```yaml
---
type: command
name: exists
suite: Standard Suite
---
```

## Command: exists

**Description:** Verify if an object exists

### Direct Parameter
- **Description:** the object in question
- **Types:** specifier
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

**Description:** Make a new element

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | the class of the new element. Keyword 'new' is optional in AppleScript | type | No |
| at | the location at which to insert the element | location specifier | Yes |
| with properties | the initial values for the properties of the element | record | Yes |

### Result
- **Description:** to the new object(s)
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

**Description:** Move playlist(s) to a new location

### Direct Parameter
- **Description:** the playlist(s) to move
- **Types:** playlist
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the new location for the playlist(s) | location specifier | No |

<a name="open"></a>
```yaml
---
type: command
name: open
suite: Standard Suite
---
```

## Command: open

**Description:** Open the specified object(s)

### Direct Parameter
- **Description:** list of objects to open
- **Types:** specifier
<a name="run"></a>
```yaml
---
type: command
name: run
suite: Standard Suite
---
```

## Command: run

**Description:** Run the application

<a name="quit"></a>
```yaml
---
type: command
name: quit
suite: Standard Suite
---
```

## Command: quit

**Description:** Quit the application

<a name="save"></a>
```yaml
---
type: command
name: save
suite: Standard Suite
---
```

## Command: save

**Description:** Save the specified object(s)

### Direct Parameter
- **Description:** the object(s) to save
- **Types:** specifier
<a name="eknd"></a>
```yaml
---
type: enumeration
name: eKnd
suite: Standard Suite
---
```

## Enumeration: eKnd

### Enumerators
| Name | Description |
|---|---|
| track listing | a basic listing of tracks within a playlist |
| album listing | a listing of a playlist grouped by album |
| cd insert | a printout of the playlist for jewel case inserts |

<a name="enum"></a>
```yaml
---
type: enumeration
name: enum
suite: Standard Suite
---
```

## Enumeration: enum

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
| copies | the number of copies of a document to be printed | integer | r |
| collating | Should printed copies be collated? | boolean | r |
| starting page | the first page of the document to be printed | integer | r |
| ending page | the last page of the document to be printed | integer | r |
| pages across | number of logical pages laid across a physical page | integer | r |
| pages down | number of logical pages laid out down a physical page | integer | r |
| error handling | how errors are handled | enum | r |
| requested print time | the time at which the desktop printer should print the document | date | r |
| printer features | printer specific options | text | r |
| fax number | for fax number | text | r |
| target printer | for target printer | text | r |

## Music Suite

**Description:** The event suite specific to Music

<a name="add"></a>
```yaml
---
type: command
name: add
suite: Music Suite
---
```

## Command: add

**Description:** add one or more files to a playlist

### Direct Parameter
- **Description:** the file(s) to add
- **Types:** file
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | the location of the added file(s) | location specifier | Yes |

### Result
- **Description:** reference to added track(s)
- **Types:** track
<a name="back_track"></a>
```yaml
---
type: command
name: back track
suite: Music Suite
---
```

## Command: back track

**Description:** reposition to beginning of current track or go to previous track if already at start of current track

<a name="convert"></a>
```yaml
---
type: command
name: convert
suite: Music Suite
---
```

## Command: convert

**Description:** convert one or more files or tracks

### Direct Parameter
- **Description:** the file(s)/tracks(s) to convert
- **Types:** specifier
### Result
- **Description:** reference to converted track(s)
- **Types:** track
<a name="download"></a>
```yaml
---
type: command
name: download
suite: Music Suite
---
```

## Command: download

**Description:** download a cloud track or playlist

### Direct Parameter
- **Description:** the shared track, URL track or playlist to download
- **Types:** item
<a name="export"></a>
```yaml
---
type: command
name: export
suite: Music Suite
---
```

## Command: export

**Description:** export a source or playlist

### Direct Parameter
- **Description:** the source or playlist to export
- **Types:** item
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | the format to export for a playlist | eExF | Yes |
| to | the destination of the export | file | Yes |

### Result
- **Description:** the exported data for the source or playlist, if not written to a file
- **Types:** text
<a name="fast_forward"></a>
```yaml
---
type: command
name: fast forward
suite: Music Suite
---
```

## Command: fast forward

**Description:** skip forward in a playing track

<a name="next_track"></a>
```yaml
---
type: command
name: next track
suite: Music Suite
---
```

## Command: next track

**Description:** advance to the next track in the current playlist

<a name="pause"></a>
```yaml
---
type: command
name: pause
suite: Music Suite
---
```

## Command: pause

**Description:** pause playback

<a name="play"></a>
```yaml
---
type: command
name: play
suite: Music Suite
---
```

## Command: play

**Description:** play the current track or the specified track or file.

### Direct Parameter
- **Description:** item to play
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| once | If true, play this track once and then stop. | boolean | Yes |

<a name="playpause"></a>
```yaml
---
type: command
name: playpause
suite: Music Suite
---
```

## Command: playpause

**Description:** toggle the playing/paused state of the current track

<a name="previous_track"></a>
```yaml
---
type: command
name: previous track
suite: Music Suite
---
```

## Command: previous track

**Description:** return to the previous track in the current playlist

<a name="refresh"></a>
```yaml
---
type: command
name: refresh
suite: Music Suite
---
```

## Command: refresh

**Description:** update file track information from the current information in the track’s file

### Direct Parameter
- **Description:** the file track to update
- **Types:** file track
<a name="resume"></a>
```yaml
---
type: command
name: resume
suite: Music Suite
---
```

## Command: resume

**Description:** disable fast forward/rewind and resume playback, if playing.

<a name="reveal"></a>
```yaml
---
type: command
name: reveal
suite: Music Suite
---
```

## Command: reveal

**Description:** reveal and select a track or playlist

### Direct Parameter
- **Description:** the item to reveal
- **Types:** item
<a name="rewind"></a>
```yaml
---
type: command
name: rewind
suite: Music Suite
---
```

## Command: rewind

**Description:** skip backwards in a playing track

<a name="search"></a>
```yaml
---
type: command
name: search
suite: Music Suite
---
```

## Command: search

**Description:** search a playlist for tracks matching the search string. Identical to entering search text in the Search field.

### Direct Parameter
- **Description:** the playlist to search
- **Types:** playlist
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for | the search text | text | No |
| only | area to search (default is all) | eSrA | Yes |

### Result
- **Description:** reference to found track(s)
- **Types:** track
<a name="select"></a>
```yaml
---
type: command
name: select
suite: Music Suite
---
```

## Command: select

**Description:** select the specified object(s)

### Direct Parameter
- **Description:** the object(s) to select
- **Types:** specifier
<a name="stop"></a>
```yaml
---
type: command
name: stop
suite: Music Suite
---
```

## Command: stop

**Description:** stop playback

<a name="airplay_device"></a>
```yaml
---
type: class
name: AirPlay device
suite: Music Suite
---
```

## Class: AirPlay device

**Description:** an AirPlay device

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| active | is the device currently being played to? | boolean | r |
| available | is the device currently available? | boolean | r |
| kind | the kind of the device | eAPD | r |
| network address | the network (MAC) address of the device | text | r |
| protected | is the device password- or passcode-protected? | boolean | r |
| selected | is the device currently selected? | boolean | read/write |
| supports audio | does the device support audio playback? | boolean | r |
| supports video | does the device support video playback? | boolean | r |
| sound volume | the output volume for the device (0 = minimum, 100 = maximum) | integer | read/write |

<a name="application"></a>
```yaml
---
type: class
name: application
suite: Music Suite
---
```

## Class: application

**Description:** The application program

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| AirPlay enabled | is AirPlay currently enabled? | boolean | r |
| converting | is a track currently being converted? | boolean | r |
| current AirPlay devices | the currently selected AirPlay device(s) | AirPlay device | read/write |
| current encoder | the currently selected encoder (MP3, AIFF, WAV, etc.) | encoder | read/write |
| current EQ preset | the currently selected equalizer preset | EQ preset | read/write |
| current playlist | the playlist containing the currently targeted track | playlist | r |
| current stream title | the name of the current track in the playing stream (provided by streaming server) | text | r |
| current stream URL | the URL of the playing stream or streaming web site (provided by streaming server) | text | r |
| current track | the current targeted track | track | r |
| current visual | the currently selected visual plug-in | visual | read/write |
| EQ enabled | is the equalizer enabled? | boolean | read/write |
| fixed indexing | true if all AppleScript track indices should be independent of the play order of the owning playlist. | boolean | read/write |
| frontmost | is this the active application? | boolean | read/write |
| full screen | is the application using the entire screen? | boolean | read/write |
| name | the name of the application | text | r |
| mute | has the sound output been muted? | boolean | read/write |
| player position | the player’s position within the currently playing track in seconds. | real | read/write |
| player state | is the player stopped, paused, or playing? | ePlS | r |
| selection | the selection visible to the user | specifier | r |
| shuffle enabled | are songs played in random order? | boolean | read/write |
| shuffle mode | the playback shuffle mode | eShM | read/write |
| song repeat | the playback repeat mode | eRpt | read/write |
| sound volume | the sound output volume (0 = minimum, 100 = maximum) | integer | read/write |
| version | the version of the application | text | r |
| visuals enabled | are visuals currently being displayed? | boolean | read/write |

### Elements
- **Type:** AirPlay device
- **Type:** browser window
- **Type:** encoder
- **Type:** EQ preset
- **Type:** EQ window
- **Type:** miniplayer window
- **Type:** playlist
- **Type:** playlist window
- **Type:** source
- **Type:** track
- **Type:** video window
- **Type:** visual
- **Type:** window
<a name="artwork"></a>
```yaml
---
type: class
name: artwork
suite: Music Suite
---
```

## Class: artwork

**Description:** a piece of art within a track or playlist

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| data | data for this artwork, in the form of a picture | picture | read/write |
| description | description of artwork as a string | text | read/write |
| downloaded | was this artwork downloaded by Music? | boolean | r |
| format | the data format for this piece of artwork | type | r |
| kind | kind or purpose of this piece of artwork | integer | read/write |
| raw data | data for this artwork, in original format | any | read/write |

<a name="audio_cd_playlist"></a>
```yaml
---
type: class
name: audio CD playlist
suite: Music Suite
---
```

## Class: audio CD playlist

**Description:** a playlist representing an audio CD

**Inherits:** playlist

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| artist | the artist of the CD | text | read/write |
| compilation | is this CD a compilation album? | boolean | read/write |
| composer | the composer of the CD | text | read/write |
| disc count | the total number of discs in this CD’s album | integer | read/write |
| disc number | the index of this CD disc in the source album | integer | read/write |
| genre | the genre of the CD | text | read/write |
| year | the year the album was recorded/released | integer | read/write |

### Elements
- **Type:** audio CD track
<a name="audio_cd_track"></a>
```yaml
---
type: class
name: audio CD track
suite: Music Suite
---
```

## Class: audio CD track

**Description:** a track on an audio CD

**Inherits:** track

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| location | the location of the file represented by this track | file | r |

<a name="browser_window"></a>
```yaml
---
type: class
name: browser window
suite: Music Suite
---
```

## Class: browser window

**Description:** the main window

**Inherits:** window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| selection | the selected tracks | specifier | r |
| view | the playlist currently displayed in the window | playlist | read/write |

<a name="encoder"></a>
```yaml
---
type: class
name: encoder
suite: Music Suite
---
```

## Class: encoder

**Description:** converts a track to a specific file format

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| format | the data format created by the encoder | text | r |

<a name="eq_preset"></a>
```yaml
---
type: class
name: EQ preset
suite: Music Suite
---
```

## Class: EQ preset

**Description:** equalizer preset configuration

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| band 1 | the equalizer 32 Hz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 2 | the equalizer 64 Hz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 3 | the equalizer 125 Hz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 4 | the equalizer 250 Hz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 5 | the equalizer 500 Hz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 6 | the equalizer 1 kHz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 7 | the equalizer 2 kHz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 8 | the equalizer 4 kHz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 9 | the equalizer 8 kHz band level (-12.0 dB to +12.0 dB) | real | read/write |
| band 10 | the equalizer 16 kHz band level (-12.0 dB to +12.0 dB) | real | read/write |
| modifiable | can this preset be modified? | boolean | r |
| preamp | the equalizer preamp level (-12.0 dB to +12.0 dB) | real | read/write |
| update tracks | should tracks which refer to this preset be updated when the preset is renamed or deleted? | boolean | read/write |

<a name="eq_window"></a>
```yaml
---
type: class
name: EQ window
suite: Music Suite
---
```

## Class: EQ window

**Description:** the equalizer window

**Inherits:** window

<a name="file_track"></a>
```yaml
---
type: class
name: file track
suite: Music Suite
---
```

## Class: file track

**Description:** a track representing an audio file (MP3, AIFF, etc.)

**Inherits:** track

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| location | the location of the file represented by this track | file | read/write |

<a name="folder_playlist"></a>
```yaml
---
type: class
name: folder playlist
suite: Music Suite
---
```

## Class: folder playlist

**Description:** a folder that contains other playlists

**Inherits:** user playlist

<a name="item"></a>
```yaml
---
type: class
name: item
suite: Music Suite
---
```

## Class: item

**Description:** an item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| class | the class of the item | type | r |
| container | the container of the item | specifier | r |
| id | the id of the item | integer | r |
| index | the index of the item in internal application order | integer | r |
| name | the name of the item | text | read/write |
| persistent ID | the id of the item as a hexadecimal string. This id does not change over time. | text | r |
| properties | every property of the item | record | read/write |

<a name="library_playlist"></a>
```yaml
---
type: class
name: library playlist
suite: Music Suite
---
```

## Class: library playlist

**Description:** the main library playlist

**Inherits:** playlist

### Elements
- **Type:** file track
- **Type:** URL track
- **Type:** shared track
<a name="miniplayer_window"></a>
```yaml
---
type: class
name: miniplayer window
suite: Music Suite
---
```

## Class: miniplayer window

**Description:** the miniplayer window

**Inherits:** window

<a name="playlist"></a>
```yaml
---
type: class
name: playlist
suite: Music Suite
---
```

## Class: playlist

**Description:** a list of tracks/streams

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| description | the description of the playlist | text | read/write |
| disliked | is this playlist disliked? | boolean | read/write |
| duration | the total length of all tracks (in seconds) | integer | r |
| name | the name of the playlist | text | read/write |
| favorited | is this playlist favorited? | boolean | read/write |
| parent | folder which contains this playlist (if any) | playlist | r |
| size | the total size of all tracks (in bytes) | integer | r |
| special kind | special playlist kind | eSpK | r |
| time | the length of all tracks in MM:SS format | text | r |
| visible | is this playlist visible in the Source list? | boolean | r |

### Elements
- **Type:** track
- **Type:** artwork
<a name="playlist_window"></a>
```yaml
---
type: class
name: playlist window
suite: Music Suite
---
```

## Class: playlist window

**Description:** a sub-window showing a single playlist

**Inherits:** window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| selection | the selected tracks | specifier | r |
| view | the playlist displayed in the window | playlist | r |

<a name="radio_tuner_playlist"></a>
```yaml
---
type: class
name: radio tuner playlist
suite: Music Suite
---
```

## Class: radio tuner playlist

**Description:** the radio tuner playlist

**Inherits:** playlist

### Elements
- **Type:** URL track
<a name="shared_track"></a>
```yaml
---
type: class
name: shared track
suite: Music Suite
---
```

## Class: shared track

**Description:** a track residing in a shared library

**Inherits:** track

<a name="source"></a>
```yaml
---
type: class
name: source
suite: Music Suite
---
```

## Class: source

**Description:** a media source (library, CD, device, etc.)

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| capacity | the total size of the source if it has a fixed size | double integer | r |
| free space | the free space on the source if it has a fixed size | double integer | r |
| kind |  | eSrc | r |

### Elements
- **Type:** audio CD playlist
- **Type:** library playlist
- **Type:** playlist
- **Type:** radio tuner playlist
- **Type:** subscription playlist
- **Type:** user playlist
<a name="subscription_playlist"></a>
```yaml
---
type: class
name: subscription playlist
suite: Music Suite
---
```

## Class: subscription playlist

**Description:** a subscription playlist from Apple Music

**Inherits:** playlist

### Elements
- **Type:** file track
- **Type:** URL track
<a name="track"></a>
```yaml
---
type: class
name: track
suite: Music Suite
---
```

## Class: track

**Description:** playable audio source

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| album | the album name of the track | text | read/write |
| album artist | the album artist of the track | text | read/write |
| album disliked | is the album for this track disliked? | boolean | read/write |
| album favorited | is the album for this track favorited? | boolean | read/write |
| album rating | the rating of the album for this track (0 to 100) | integer | read/write |
| album rating kind | the rating kind of the album rating for this track | eRtK | r |
| artist | the artist/source of the track | text | read/write |
| bit rate | the bit rate of the track (in kbps) | integer | r |
| bookmark | the bookmark time of the track in seconds | real | read/write |
| bookmarkable | is the playback position for this track remembered? | boolean | read/write |
| bpm | the tempo of this track in beats per minute | integer | read/write |
| category | the category of the track | text | read/write |
| cloud status | the iCloud status of the track | eClS | r |
| comment | freeform notes about the track | text | read/write |
| compilation | is this track from a compilation album? | boolean | read/write |
| composer | the composer of the track | text | read/write |
| database ID | the common, unique ID for this track. If two tracks in different playlists have the same database ID, they are sharing the same data. | integer | r |
| date added | the date the track was added to the playlist | date | r |
| description | the description of the track | text | read/write |
| disc count | the total number of discs in the source album | integer | read/write |
| disc number | the index of the disc containing this track on the source album | integer | read/write |
| disliked | is this track disliked? | boolean | read/write |
| downloader account | the account of the person who downloaded this track | text | r |
| downloader name | the name of the person who downloaded this track | text | r |
| duration | the length of the track in seconds | real | r |
| enabled | is this track checked for playback? | boolean | read/write |
| episode ID | the episode ID of the track | text | read/write |
| episode number | the episode number of the track | integer | read/write |
| EQ | the name of the EQ preset of the track | text | read/write |
| finish | the stop time of the track in seconds | real | read/write |
| gapless | is this track from a gapless album? | boolean | read/write |
| genre | the music/audio genre (category) of the track | text | read/write |
| grouping | the grouping (piece) of the track. Generally used to denote movements within a classical work. | text | read/write |
| kind | a text description of the track | text | r |
| long description | the long description of the track | text | read/write |
| favorited | is this track favorited? | boolean | read/write |
| lyrics | the lyrics of the track | text | read/write |
| media kind | the media kind of the track | eMdK | read/write |
| modification date | the modification date of the content of this track | date | r |
| movement | the movement name of the track | text | read/write |
| movement count | the total number of movements in the work | integer | read/write |
| movement number | the index of the movement in the work | integer | read/write |
| played count | number of times this track has been played | integer | read/write |
| played date | the date and time this track was last played | date | read/write |
| purchaser account | the account of the person who purchased this track | text | r |
| purchaser name | the name of the person who purchased this track | text | r |
| rating | the rating of this track (0 to 100) | integer | read/write |
| rating kind | the rating kind of this track | eRtK | r |
| release date | the release date of this track | date | r |
| sample rate | the sample rate of the track (in Hz) | integer | r |
| season number | the season number of the track | integer | read/write |
| shufflable | is this track included when shuffling? | boolean | read/write |
| skipped count | number of times this track has been skipped | integer | read/write |
| skipped date | the date and time this track was last skipped | date | read/write |
| show | the show name of the track | text | read/write |
| sort album | override string to use for the track when sorting by album | text | read/write |
| sort artist | override string to use for the track when sorting by artist | text | read/write |
| sort album artist | override string to use for the track when sorting by album artist | text | read/write |
| sort name | override string to use for the track when sorting by name | text | read/write |
| sort composer | override string to use for the track when sorting by composer | text | read/write |
| sort show | override string to use for the track when sorting by show name | text | read/write |
| size | the size of the track (in bytes) | double integer | r |
| start | the start time of the track in seconds | real | read/write |
| time | the length of the track in MM:SS format | text | r |
| track count | the total number of tracks on the source album | integer | read/write |
| track number | the index of the track on the source album | integer | read/write |
| unplayed | is this track unplayed? | boolean | read/write |
| volume adjustment | relative volume adjustment of the track (-100% to 100%) | integer | read/write |
| work | the work name of the track | text | read/write |
| year | the year the track was recorded/released | integer | read/write |

### Elements
- **Type:** artwork
<a name="url_track"></a>
```yaml
---
type: class
name: URL track
suite: Music Suite
---
```

## Class: URL track

**Description:** a track representing a network stream

**Inherits:** track

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| address | the URL for this track | text | read/write |

<a name="user_playlist"></a>
```yaml
---
type: class
name: user playlist
suite: Music Suite
---
```

## Class: user playlist

**Description:** custom playlists created by the user

**Inherits:** playlist

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| shared | is this playlist shared? | boolean | read/write |
| smart | is this a Smart Playlist? | boolean | r |
| genius | is this a Genius Playlist? | boolean | r |

### Elements
- **Type:** file track
- **Type:** URL track
- **Type:** shared track
<a name="video_window"></a>
```yaml
---
type: class
name: video window
suite: Music Suite
---
```

## Class: video window

**Description:** the video window

**Inherits:** window

<a name="visual"></a>
```yaml
---
type: class
name: visual
suite: Music Suite
---
```

## Class: visual

**Description:** a visual plug-in

**Inherits:** item

<a name="window"></a>
```yaml
---
type: class
name: window
suite: Music Suite
---
```

## Class: window

**Description:** any window

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| bounds | the boundary rectangle for the window | rectangle | read/write |
| closeable | does the window have a close button? | boolean | r |
| collapseable | does the window have a collapse button? | boolean | r |
| collapsed | is the window collapsed? | boolean | read/write |
| full screen | is the window full screen? | boolean | read/write |
| position | the upper left position of the window | point | read/write |
| resizable | is the window resizable? | boolean | r |
| visible | is the window visible? | boolean | read/write |
| zoomable | is the window zoomable? | boolean | r |
| zoomed | is the window zoomed? | boolean | read/write |

<a name="epls"></a>
```yaml
---
type: enumeration
name: ePlS
suite: Music Suite
---
```

## Enumeration: ePlS

### Enumerators
| Name | Description |
|---|---|
| stopped | None |
| playing | None |
| paused | None |
| fast forwarding | None |
| rewinding | None |

<a name="erpt"></a>
```yaml
---
type: enumeration
name: eRpt
suite: Music Suite
---
```

## Enumeration: eRpt

### Enumerators
| Name | Description |
|---|---|
| off | None |
| one | None |
| all | None |

<a name="eshm"></a>
```yaml
---
type: enumeration
name: eShM
suite: Music Suite
---
```

## Enumeration: eShM

### Enumerators
| Name | Description |
|---|---|
| songs | None |
| albums | None |
| groupings | None |

<a name="esrc"></a>
```yaml
---
type: enumeration
name: eSrc
suite: Music Suite
---
```

## Enumeration: eSrc

### Enumerators
| Name | Description |
|---|---|
| library | None |
| audio CD | None |
| MP3 CD | None |
| radio tuner | None |
| shared library | None |
| iTunes Store | None |
| unknown | None |

<a name="esra"></a>
```yaml
---
type: enumeration
name: eSrA
suite: Music Suite
---
```

## Enumeration: eSrA

### Enumerators
| Name | Description |
|---|---|
| albums | albums only |
| all | all text fields |
| artists | artists only |
| composers | composers only |
| displayed | visible text fields |
| names | track names only |

<a name="espk"></a>
```yaml
---
type: enumeration
name: eSpK
suite: Music Suite
---
```

## Enumeration: eSpK

### Enumerators
| Name | Description |
|---|---|
| none | None |
| folder | None |
| Genius | None |
| Library | None |
| Music | None |
| Purchased Music | None |

<a name="emdk"></a>
```yaml
---
type: enumeration
name: eMdK
suite: Music Suite
---
```

## Enumeration: eMdK

### Enumerators
| Name | Description |
|---|---|
| song | music track |
| music video | music video track |
| movie | movie track |
| TV show | TV show track |
| unknown | None |

<a name="ertk"></a>
```yaml
---
type: enumeration
name: eRtK
suite: Music Suite
---
```

## Enumeration: eRtK

### Enumerators
| Name | Description |
|---|---|
| user | user-specified rating |
| computed | computed rating |

<a name="eapd"></a>
```yaml
---
type: enumeration
name: eAPD
suite: Music Suite
---
```

## Enumeration: eAPD

### Enumerators
| Name | Description |
|---|---|
| computer | None |
| AirPort Express | None |
| Apple TV | None |
| AirPlay device | None |
| Bluetooth device | None |
| HomePod | None |
| TV | None |
| unknown | None |

<a name="ecls"></a>
```yaml
---
type: enumeration
name: eClS
suite: Music Suite
---
```

## Enumeration: eClS

### Enumerators
| Name | Description |
|---|---|
| unknown | None |
| purchased | None |
| matched | None |
| uploaded | None |
| ineligible | None |
| removed | None |
| error | None |
| duplicate | None |
| subscription | None |
| prerelease | None |
| no longer available | None |
| not uploaded | None |

<a name="eexf"></a>
```yaml
---
type: enumeration
name: eExF
suite: Music Suite
---
```

## Enumeration: eExF

### Enumerators
| Name | Description |
|---|---|
| plain text | None |
| Unicode text | None |
| XML | None |
| M3U | None |
| M3U8 | None |

<a name="double_integer"></a>
```yaml
---
type: value-type
name: double integer
suite: Music Suite
---
```

## Value Type: double integer

<a name="picture"></a>
```yaml
---
type: value-type
name: picture
suite: Music Suite
---
```

## Value Type: picture

## Internet suite

**Description:** Standard terms for Internet scripting

<a name="open_location"></a>
```yaml
---
type: command
name: open location
suite: Internet suite
---
```

## Command: open location

**Description:** Opens an iTunes Store or audio stream URL

### Direct Parameter
- **Description:** the URL to open
- **Types:** text
