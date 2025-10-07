import cv2
import threading

class VideoCamera:
    def __init__(self, video_source=0):
        self.video = cv2.VideoCapture(video_source)
        self.lock = threading.Lock()

    def get_frame(self):
        with self.lock:
            ret, frame = self.video.read()
            if not ret:
                return None
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

    def release(self):
        self.video.release()
