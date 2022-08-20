import time
from dataclasses import dataclass
import yt_dlp
import numpy as np
import cv2


@dataclass
class VideoStream:
    url: str = None
    resolution: str = None
    height: int = 0
    width: int = 0

    def __init__(self, video_format):
        self.url = video_format['url']
        self.resolution = video_format['format_note']
        self.height = video_format['height']
        self.width = video_format['width']

    def __str__(self):
        return f'{self.resolution} ({self.height}x{self.width}): {self.url}'


def list_video_streams(url):
    cap = None

    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        streams = [VideoStream(format)
                   for format in info['formats'][::-1]
                   if format['vcodec'] != 'none']
        _, unique_indices = np.unique(np.array([stream.resolution
                                                for stream in streams]), return_index=True)
        streams = [streams[index] for index in np.sort(unique_indices)]
        resolutions = np.array([stream.resolution for stream in streams])
        return streams[::-1], resolutions[::-1]


def cap_from_youtube(url, resolution=None):
    cap = None

    streams, resolutions = list_video_streams(url)

    if not resolution or resolution == 'best':
        return cv2.VideoCapture(streams[-1].url)

    if resolution not in resolutions:
        raise ValueError(f'Resolution {resolution} not available')
    res_index = np.where(resolutions == resolution)[0][0]
    return cv2.VideoCapture(streams[res_index].url)


if __name__ == '__main__':

    def test_video(cap, vid_res):
        num_frames = 100
        for i in range(num_frames):
            start_time = time.perf_counter()
            ret, frame = cap.read()
            # print(f'Frame process time: {time.perf_counter() - start_time}s')
            if not ret:
                break
            cv2.imshow(f'{vid_res}', frame)
            cv2.waitKey(1)
        cap.release()


    youtube_url = 'https://youtu.be/XqZsoesa55w'

    _, resolutions = list_video_streams(youtube_url)
    resolutions = np.append(resolutions, 'best')
    for vid_res in resolutions:
        cap = cap_from_youtube(youtube_url, vid_res)
        test_video(cap, vid_res)
