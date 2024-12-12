import cv2 as cv
import os
import face_recognition


class VideoProcessor:
    def __init__(self):
        self.cam = cv.VideoCapture(0)
        if not self.cam.isOpened():
            print("Error opening camera")
            exit()


def load_reference_face(reference_folder):
    reference_files = os.listdir(reference_folder)
    if not reference_files:
        print("No reference photo found.")
        return None

    reference_image_path = os.path.join(reference_folder, reference_files[0])
    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encodings = face_recognition.face_encodings(reference_image)

    if reference_encodings:
        print(f"Loaded reference face from {reference_image_path}")
        return reference_encodings[0]
    else:
        print("No face detected in the reference photo.")
        return None


