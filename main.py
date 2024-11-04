import cv2

# Create a video capture object and allocate camera ID 0 (your webcam)
cap = cv2.VideoCapture(0)

# Capture a photo and store it in the ‘photo’ variable
status, photo = cap.read()

# Release the camera after capturing the photo
cap.release()

# Display the captured photo in a window titled “My Photo”
cv2.imshow("My Photo", photo)

# Wait for 5 seconds before closing the window
cv2.waitKey(60000)

# Close all OpenCV windows
cv2.destroyAllWindows()