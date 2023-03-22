import tkinter

import cv2
import pyrebase
import keyboard
import tkinter as tk
from tkinter import simpledialog

#firebase information
config = {
  "apiKey": "AIzaSyAExT-z0P_EvSKxNenMm_t8hQPOU4gAfuQ",
  "authDomain": "projectnet-fba8a.firebaseapp.com",
  "databaseURL": "https://projectnet-fba8a-default-rtdb.firebaseio.com",
  "projectId": "projectnet-fba8a",
  "storageBucket": "projectnet-fba8a.appspot.com",
  "messagingSenderId": "581350523955",
  "appId": "1:581350523955:web:a77cd06cc9dc5ccae00f46",
  "measurementId": "G-6FJFKX7L2D"
}
#2nd firebase information (students)
configStudents = {
  "apiKey": "AIzaSyAcln-UgEYgmH_FOIRzr1T_BPMXwdrhu7k",
  "authDomain": "names-9caa6.firebaseapp.com",
  "databaseURL": "https://names-9caa6-default-rtdb.firebaseio.com",
  "projectId": "names-9caa6",
  "storageBucket": "names-9caa6.appspot.com",
  "messagingSenderId": "787313435924",
  "appId": "1:787313435924:web:eb6826df17e16f8f87ce01",
  "measurementId": "G-KNTFHFYXNC"
}

#firebase intialization
#firebase 1
firebase = pyrebase.initialize_app(config)
database = firebase.database()
#firebase 2 (students)
firebase2 = pyrebase.initialize_app(configStudents)
database2 = firebase2.database()




face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')

def gui():
    # Release the capture once all the processing is done.
    video_capture.release()
    cv2.destroyAllWindows()
    root = tk.Tk()
    root.withdraw()
    user_inp = simpledialog.askstring(title="Students", prompt="Enter Your ID")
    stu=database2.child(user_inp).child("Presence").get().val()
    if(stu is None):
        tkinter.messagebox.showinfo('Answer',"REJECTED")
        return 0
    stu += 1
    database2.child(user_inp).update({"Presence":stu})
    return 1




def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
           cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
           #reading door from firebase
           sm = database.child("num").get()
           if(sm.val() == 0 and keyboard.is_pressed('space')):
                 x = gui()
                 if(x == 1):
                    database.update({"num": 1})
    return frame

video_capture = cv2.VideoCapture(0)
while video_capture.isOpened():
    # Captures video_capture frame by frame
    _, frame = video_capture.read()

    # To capture image in monochrome
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calls the detect() function
    canvas = detect(gray, frame)

    # Displays the result on camera feed
    cv2.imshow('Video', canvas)

    # The control breaks once q key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the capture once all the processing is done.
video_capture.release()
cv2.destroyAllWindows()
