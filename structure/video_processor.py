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


# voice = VoiceProcessor()
# voice.set_output_dir()
# path_with_name = get_path_to_cur_dir(output_dir)
# ensure_directory_exists(path_with_name)
#
# reference_encoding = load_reference_face(path_with_name)
# vp = VideoProcessor()
# reference_photo_taken = reference_encoding is not None
#
# while True:
#     ret, frame = vp.cam.read()
#     if not ret:
#         print("Error in retrieving frame")
#         break
#
#     if not reference_photo_taken:
#         cv.imshow("Capture Reference Photo", frame)
#
#         # Save reference photo when 's' is pressed
#         if cv.waitKey(1) == ord("s"):
#             reference_photo_path = os.path.join(path_with_name, "reference_photo.jpg")
#             if cv.imwrite(reference_photo_path, frame):
#                 print(f"Reference photo saved at {reference_photo_path}")
#                 reference_encoding = load_reference_face(path_with_name)
#                 reference_photo_taken = True
#             else:
#                 print("Failed to save reference photo")
#
#         if cv.waitKey(1) == ord("q"):
#             print("Exiting without saving a reference photo.")
#             vp.cam.release()
#             cv.destroyAllWindows()
#             exit()
#
#     else:
#         img_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(img_rgb)
#
#         for (top, right, bottom, left) in face_locations:
#             face_frame = img_rgb[top:bottom, left:right]
#
#             current_encodings = face_recognition.face_encodings(img_rgb, [(top, right, bottom, left)])
#
#             if current_encodings:
#                 current_encoding = current_encodings[0]
#                 match = face_recognition.compare_faces([reference_encoding], current_encoding)[0]
#                 distance = face_recognition.face_distance([reference_encoding], current_encoding)[0]
#
#                 label_text = f"Match: {output_dir} (Dist: {round(distance, 2)})" if match else "No Match"
#                 color = (0, 255, 0) if match else (0, 0, 255)
#
#                 cv.rectangle(frame, (left, top), (right, bottom), color, 2)
#                 cv.putText(frame, label_text, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
#
#         cv.imshow('Face Recognition', frame)
#
#     if cv.waitKey(1) == ord('q'):
#         break
#
# vp.cam.release()
# cv.destroyAllWindows()
