import cv2
from base_camera_rtmp import BaseCamera


class Camera(BaseCamera):
    # video_source = 'rtmp://172.18.9.69:1935/rtmplive/live1'

    def __init__(self, num):
        self.video_source = 'rtmp://172.18.9.69:1935/rtmplive/live' + str(num)
        super(Camera, self).__init__()

    def set_video_source(self, source):
        self.video_source = source

    def frames(self):
        camera = cv2.VideoCapture(self.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
