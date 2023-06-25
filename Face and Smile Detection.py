import cv2
from random import randrange
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
#img = cv2.imread("me3.jpg")
webcam = cv2.VideoCapture(0)

while True:
    succ_frame_read,frame = webcam.read()
    frame_grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_grayscale)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y) ,(x+w ,y+h),(0,255,0),3)
        the_face=frame[y:y+h,x:x+w]
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.85, minNeighbors=20)
        #for(x_,y_,w_,h_) in smiles:
           #cv2.rectangle(the_face,(x_,y_) ,(x_+w_ ,y_+h_),(50,50,200),3)
        if len(smiles)>0:
            cv2.putText(frame,"Smiling ", (x,y+h+40), fontScale=2,
                        fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, color=(255,255,255))
    cv2.imshow("Clever Programmer Face Detetor" ,frame)
    key = cv2.waitKey(1)
    if key == 81 or key ==113:
        break
webcam.release()
print('Code Completed...')
