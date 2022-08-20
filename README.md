# cap_from_youtube
 Get an OpenCV video capture from an YouTube video URL

[![PyPI](https://img.shields.io/pypi/v/cap-from-youtube?color=2BAF2B)](https://pypi.org/project/cap-from-youtube/)
<p align="center">
  <img src="https://raw.githubusercontent.com/ibaiGorordo/cap_from_youtube/main/doc/img/cap_from_youtube_logo.png" />
</p>

# Why
- pafy is widely used to get the video URL from a YouTube video URL, but since it uses youtube-dl which has not been updated recently, it suffers from some issues (dislike_count not found...).
- This repository is a simplified version of what pafy does, by just getting the url of the video and creating an OpenCV video capture from it.
- It uses YT-DLP (https://github.com/yt-dlp/yt-dlp), which is a fork of youtube-dl that is updated frequently.

# Requirement
* YT-DLP
* OpenCV
* NumPy
 
# Installation
- The easiest way is to install it with pip:

```bash
pip install cap_from_youtube
```
- You can also install it from GitHub:

```bash
pip install git+https://github.com/ibaiGorordo/cap_from_youtube
```

# Usage

## cap_from_youtube()
- `cap_from_youtube()` is the main function to obtain a video capture from a YouTube video URL. 
- It requires the video URL as input and returns a `cv2.VideoCapture` object.
- By default, it returns the video with the highest resolution available.
- You can specify the resolution you want to get with the `resolution` parameter.
  - Resolution examples: '144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p', 'best'
- Example:

```python
from cap_from_youtube import cap_from_youtube

youtube_url = 'https://youtu.be/XqZsoesa55w'
cap = cap_from_youtube(youtube_url, 'best')
```

## list_video_streams()
- You can also use the `list_video_streams()` function to get the list of available video streams.
- It requires the video URL as input and returns two values: 
  - streams: a list of VideoStream with the information of the available video streams.
  - resolutions: a NumPy array with the available resolutions.
- Example:
```python
from cap_from_youtube import list_video_streams

youtube_url = 'https://youtu.be/XqZsoesa55w'
streams, resolutions = list_video_streams(youtube_url)

for stream in streams:
    print(stream)
```
 
# References
- pafy: https://github.com/mps-youtube/pafy
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- imread_from_url: https://github.com/Kazuhito00/imread_from_url
