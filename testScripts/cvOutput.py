import picamera
import datetime as dt

camera = picamera.PiCamera(resolution=(1280, 720), framerate=60)
camera.start_preview()

camera.annotate_background = picamera.Color('black')
camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

camera.start_recording('timeStampTestMin2.h264')
start = dt.datetime.now()


while (dt.datetime.now() - start).seconds < 60:
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.wait_recording(.5)

camera.stop_recording()
