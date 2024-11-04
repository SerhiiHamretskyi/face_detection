
import cv2 as cv
import os
import csv

names = ["Serhii"]
frame_count = 0
output_dir = "./photos"
os.makedirs(output_dir , exist_ok=True)
haarcascades = "./haarcascade_frontalface_default.xml"

while True:
    name = input("Who are you , stranger?")
    if name not in names:
        input("Sorry I couldn't hear you,  proivde your name  one more time, please ")
        names.append(f"{name}")
        print(names)
        break
    else:
        print(f"Hello ,{name} , we missed you!")
        break
with open('guest_names.txt', 'w') as f:
    csv.writer(f, delimiter=' ').writerows(names)

class VideoProcessor:
    def __init__(self):
        self.cam = cv.VideoCapture(0)
        self.codec = cv.VideoWriter_fourcc(*"XVID")
        if not self.cam.isOpened():
            print("error opening camera")
            exit()



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
    for(x , y,w ,h) in face:
        face_rectangle = img[y:y+h , x:x+w] #slicing face from the image

        cv.rectangle(img , (x , y) , (x+w, y+h) ,(0,255,0),2)
    cv.imshow('frame', img)

    if cv.waitKey(1) == ord("s"):
        photo_path = os.path.join(output_dir, f"photo_{frame_count}.jpg")
        if cv.imwrite(photo_path, face_rectangle):
            print(f"Saved {photo_path}")
        else:
            print("Failed to save image")
        frame_count += 1
    if cv.waitKey(1) == ord('q'):
        break
vp.cam.release()
# file.release()
cv.destroyAllWindows()