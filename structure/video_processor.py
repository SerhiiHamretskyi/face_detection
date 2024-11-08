
import cv2 as cv
import os

from structure.helpers import get_path_to_cur_dir
from structure.helpers import ensure_directory_exists


frame_count = 0
#output_dir = "./photos"
output_dir = None

#os.makedirs(output_dir , exist_ok=True)
haarcascades = "./haarcascade_frontalface_default.xml"



class VideoProcessor:
    def __init__(self):
        self.cam = cv.VideoCapture(0)
        self.codec = cv.VideoWriter_fourcc(*"XVID")
        if not self.cam.isOpened():
            print("error opening camera")
            exit()

class VoiceProcessor:
    def __init__(self   ):
        self.question_name = input("Provide your name: ")

    def set_output_dir(self):
        global output_dir
        output_dir=  self.question_name






voice = VoiceProcessor()
voice.set_output_dir()
path_with_name = get_path_to_cur_dir(output_dir)
ensure_directory_exists(path_with_name)
vp =VideoProcessor()



while True:
    # Capture frame-by-frame
    ret, frame = vp.cam.read()

    # if frame is read correctly ret is True
    if not ret:
        print("error in retrieving frame")
        break



    facecascade = cv.CascadeClassifier(haarcascades)
    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img_gray_mask = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face = facecascade.detectMultiScale(img_gray_mask , 1.1 , 4)
   # for(x , y,w ,h) in face:
    #    face_rectangle = img[y:y+h , x:x+w] #slicing face from the image

    #    cv.rectangle(img , (x , y) , (x+w, y+h) ,(0,255,0),2)
    cv.imshow('frame', img)

    if cv.waitKey(1) == ord("s"):
        photo_path = os.path.join(path_with_name, f"photo_{frame_count}.jpg")
        if cv.imwrite(photo_path, img):
            print(f"Saved {photo_path}")
        else:
            print("Failed to save image")
        frame_count += 1
    if cv.waitKey(1) == ord('q'):
        break
vp.cam.release()
# file.release()
cv.destroyAllWindows()
