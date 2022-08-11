import numpy as np
import cv2

video_capture_0 = cv2.VideoCapture(0)
#video_capture_1 = cv2.VideoCapture(1)
#video_capture_2 = cv2.VideoCapture(2)

#video_capture_3 = cv2.VideoCapture(3)

print(video_capture_0)
# print(video_capture_1)
# print(video_capture_2)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

camera0 = cv2.VideoWriter(
    'C:/Users/Administrator/Desktop/python video cap/c0.avi', fourcc, 30, (
        640, 480)
)
'''
camera1 = cv2.VideoWriter(
    'C:/Users/Administrator/Desktop/python video cap/c1.avi', fourcc, 30, (
        640, 480)
)
 camera2 = cv2.VideoWriter(
    'C:/Users/Administrator/Desktop/python video cap/c2.avi', fourcc, 30, (
        640, 480)
) '''

while True:
    ret0, frame0 = video_capture_0.read()
    #ret1, frame1 = video_capture_1.read()
    #ret2, frame2 = video_capture_2.read()

    # FIRST CAMERA
    if(ret0):
        cv2.imshow('Cam 0', frame0)
        camera0.write(frame0)
    if not ret0:
        print('Camera_0 Capture failed')
        break

    # SECOND CAMERA
    ''' if(ret1):
        cv2.imshow('Cam 1', frame1)
        camera1.write(frame1)
    if not ret0:
        print('Camera_1 Capture failed')
        break '''

    # THIRD CAMERA
    ''' if(ret2):
        cv2.imshow('Cam 2', frame2)
        camera2.write(frame2)
    if not ret2:
        print('Camera_2 Capture failed')
        break '''

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture_0.release()
''' video_capture_1.release()
video_capture_2.release() '''
cv2.destroyAllWindows()
