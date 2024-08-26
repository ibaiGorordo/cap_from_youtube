from datetime import timedelta
import cv2

from cap_from_youtube import cap_from_youtube


youtube_url = 'https://youtu.be/LXb3EKWsInQ'

start_time = timedelta(seconds=5)
cap = cap_from_youtube(youtube_url, 'best', start=start_time)

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

