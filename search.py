import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
from pymavlink import mavutil

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

precaution = 20
counter = 0
detector = HandDetector(maxHands=1)

telemetry = mavutil.mavlink_connection(com, baud=57600) 

while True:
    msg = telemetry.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    
    latitude = msg.lat / 1.0e7
    longitude = msg.lon / 1.0e7
    altitude = msg.alt / 1.0e3

    print(f'Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}')

    capture = cv.VideoCapture(0)
    check, img = capture.read()
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    hands, img2 = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        img_crop = img[y - precaution:y + h + precaution, x - precaution:x + w + precaution]
        cv.imshow('hand', img_crop)
        aspect_ratio = h / w

        if aspect_ratio > 1:
            k = 400 / h
            new_w = math.ceil(k * w)
            dimension = (new_w, 400)
            imgResize = cv.resize(img_crop, dimension, interpolation=cv.INTER_CUBIC)
            w_gap = math.ceil((400 - new_w) / 2)
            blank = np.ones((400, 400, 3), dtype='uint8') * 255
            blank[:, w_gap:imgResize.shape[1] + w_gap] = imgResize
            cv.imshow('blank', blank)
        else:
            k = 400 / w
            new_h = math.ceil(k * h)
            dimension = (400, new_h)
            imgResize = cv.resize(img_crop, dimension, interpolation=cv.INTER_CUBIC)
            h_gap = math.ceil((400 - new_h) / 2)
            blank = np.ones((400, 400, 3), dtype='uint8') * 255
            blank[h_gap:imgResize.shape[0] + h_gap, :] = imgResize
            cv.imshow('blank', blank)

        x, y = hand['lmList'][4]  
        print(f'Face detected at X: {x}, Y: {y}')

    if check:
        cv.imshow('image', img)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

    if cv.waitKey(20) & 0xFF == ord('s'):
        counter += 1-
        cv.imwrite(f'data/STOP/Image_{time.time()}.jpg', blank)
        print(counter)

capture.release()
cv.destroyAllWindows()
