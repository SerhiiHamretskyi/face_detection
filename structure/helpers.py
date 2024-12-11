import os
import cv2 as cv
import face_recognition

# "C:\\Users\\andro\\PycharmProjects\\face_detection\\structure\\photos"
# "C:\\Users\\andro\\PycharmProjects\\face_detection\\Serhii"
# Specify the absolute path


def get_user_input():
    user_input = input("")
    return user_input


def ensure_directory_exists(path):
    os.makedirs(path, exist_ok=True)  # Create all intermediate directories if they do not exist


def get_path_to_cur_dir(name):
    # Check if we're inside the container
    if os.path.exists("/app/photos"):
        # If we're inside the container, use the mounted path
        cwd = "/app/photos"
    else:
        # Otherwise, use the local path
        cwd = os.path.join(os.getcwd(), "photos")

    nwd = os.path.join(cwd, name)
    print(nwd)
    return nwd


def check_if_folder_empty(path):
    if not os.listdir(path):
        print("No files found in the directory.")
        return True
    else:
        print("Some files found in the directory")
        return False


def find_face_encodings(image_path):
    # Read the image
    image = cv.imread(image_path)
    # Get face encodings from the image
    face_encodings = face_recognition.face_encodings(image)
    # Return the first face encoding if found
    return face_encodings[0] if face_encodings else None


def start_camera_if_folder_empty(path):
    check_if_folder_empty(path)

    if not os.listdir(path):
        print("Folder is empty. Start capturing the camera...")
        return True
    else:
        print("Folder is not empty. Camera will not start.")
        return False
