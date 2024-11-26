import os
import face_recognition
import cv2 as cv
import time
import pyttsx3

from structure.helpers import get_path_to_cur_dir, ensure_directory_exists
from structure.video_processor import load_reference_face, VideoProcessor
from structure.voice_processor import VoiceProcessor

engine = pyttsx3.init()
voice = VoiceProcessor()
voice.set_output_dir()
path_with_name = get_path_to_cur_dir(voice.output_dir)
ensure_directory_exists(path_with_name)

reference_encoding = load_reference_face(path_with_name)
vp = VideoProcessor()
reference_photo_taken = reference_encoding is not None

# Initialize a timer for 30-second intervals
last_comparison_time = time.time()

# Set default label and color
last_message_time = 0
message_interval = 120

label_text = "No Face Detected"
color = (0, 255, 255)  # Yellow for "no face detected"
engine.say("Analyzing your face")
engine.runAndWait()

# Flags to track if message was spoken
recognized_spoken = False
unrecognized_spoken = False

while True:
    current_time2 = time.time()

    ret, frame = vp.cam.read()
    if not ret:
        print("Error in retrieving frame")
        break

    if not reference_photo_taken:
        cv.imshow("Capture Reference Photo", frame)

        # Save reference photo when 's' is pressed
        if cv.waitKey(1) == ord("s"):
            reference_photo_path = os.path.join(path_with_name, "reference_photo.jpg")
            if cv.imwrite(reference_photo_path, frame):
                print(f"Reference photo saved at {reference_photo_path}")
                reference_encoding = load_reference_face(path_with_name)
                reference_photo_taken = True
            else:
                print("Failed to save reference photo")

        if cv.waitKey(1) == ord("q"):
            print("Exiting without saving a reference photo.")
            vp.cam.release()
            cv.destroyAllWindows()
            exit()

    else:
        img_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img_rgb)

        # Draw rectangles continuously around detected faces
        for top, right, bottom, left in face_locations:
            cv.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv.putText(
                frame,
                label_text,
                (left, top - 10),
                cv.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2,
            )

        # Perform face comparison every 5 seconds
        current_time = time.time()
        if current_time - last_comparison_time >= 10:
            last_comparison_time = current_time  # Update last comparison time

            # Run face encoding and comparison
            for top, right, bottom, left in face_locations:
                face_frame = img_rgb[top:bottom, left:right]
                current_encodings = face_recognition.face_encodings(
                    img_rgb, [(top, right, bottom, left)]
                )

                if current_encodings:
                    current_encoding = current_encodings[0]
                    match = face_recognition.compare_faces(
                        [reference_encoding], current_encoding
                    )[0]
                    distance = face_recognition.face_distance(
                        [reference_encoding], current_encoding
                    )[0]

                    # Update label and color based on match result
                    label_text = (
                        f"Match: {voice.output_dir} (Dist: {round(distance, 2)})"
                        if match
                        else "No Match"
                    )

                    # If match and message not spoken, play recognized message once
                    if match and not recognized_spoken:
                        color = (0, 255, 0)
                        engine.say(f"Hello {voice.output_dir}")
                        engine.runAndWait()
                        recognized_spoken = True
                        unrecognized_spoken = False  # Reset unrecognized message flag

                    # If no match and message not spoken, play unrecognized message once
                    elif not match and not unrecognized_spoken:
                        color = (0, 0, 255)
                        engine.say("Hello, but I don't recognize your face")
                        engine.runAndWait()
                        unrecognized_spoken = True
                        recognized_spoken = False  # Reset recognized message flag

        # Reset flags when no face is detected
        if not face_locations:
            recognized_spoken = False
            unrecognized_spoken = False

        # Display the frame
        cv.imshow("Face Recognition", frame)

    if cv.waitKey(1) == ord("q"):
        break

vp.cam.release()
cv.destroyAllWindows()
