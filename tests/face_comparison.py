import cv2
import face_recognition
from structure.helpers import find_face_encodings




# Paths to images
image_path_1 = r"C:\Users\andro\PycharmProjects\face_detection\tests\photos\serhii\photo_11.jpg"
#image_path_2 = r"C:\Users\andro\PycharmProjects\face_detection\tests\photos\serhii\photo_23.jpg"
#image_path_1 = r"C:\Users\andro\PycharmProjects\face_detection\tests\photos\serhii\photo_0.jpg"
image_path_2 = r"C:\Users\andro\PycharmProjects\face_detection\tests\photos\serhii\photo_1.jpg"

# Find face encodings
image_1 = find_face_encodings(image_path_1)
image_2 = find_face_encodings(image_path_2)

# Check if encodings were found
if image_1 is not None and image_2 is not None:
    # Compare the two images
    is_same = face_recognition.compare_faces([image_1], image_2)[0]
    print(f"Is Same: {is_same}")

    # Calculate the distance between the encodings
    distance = face_recognition.face_distance([image_1], image_2)[0]
    # Calculate the accuracy level (lower distance means higher accuracy)
    accuracy = round((1 - distance) * 100, 2)

    print(f"Accuracy Level: {accuracy}%")

    if is_same:
        print("The images are the same")

    else:
        print("The images are not the same")
else:
    print("Face encodings could not be found in one or both images.")
