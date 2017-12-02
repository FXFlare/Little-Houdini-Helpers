# Little-Houdini-Helpers

A collection of scripts that make your life easier in day-to-day work with Houdini.

## Install

Set the Houdini script location to the *src* folder.   
For more informations about Python script locations in Houdini: http://www.sidefx.com/docs/houdini/hom/locations.html)

(Re)Start Houdini to source the scripts in the *src* folder. 

## Modules

### Quickbook

#### exec_quickbook(framerate, resolution, images_output_dir, video_output_dir, file_name)
Write an jpg image sequence from flipbook to disk and converte this sequence to a mov file via ffmpeg.

```python
import Quickbook  
Quickbook.exec_quickbook("25", "1920x1080", "C:/Some/Folder/You/Choose/", "C:/Some/Folder/You/Choose/", "Sequ1_Shot01_someName")
```
