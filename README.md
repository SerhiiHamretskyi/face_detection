# Face Recognition Camera with Voice Notifications


## Overview
This project is a Python-based face recognition system with voice notifications. It uses real-time video input to detect and recognize faces. Recognized individuals are greeted with a voice message, while unrecognized faces trigger a different message. The system is designed for security and personalized user experiences.

## Features

- **Real-Time Face Detection**: Uses OpenCV and the ```face_recognition``` library for high-performance face detection.
- **Face Recognition**: Compares faces with a saved reference photo.
- **Voice Feedback**: Provides personalized voice messages for recognized and unrecognized faces using ```pyttsx3```.
- **Interactive Setup**: Allows users to capture and set a reference photo in real-time.
- **Simple GUI Display**: Shows the video feed with annotations for detected and recognized faces.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - OpenCV - For video processing and GUI.
  - face_recognition - For face detection and encoding.
  - pyttsx3 - For text-to-speech voice notifications.

## Getting Started
Prerequisites
Make sure you have the following installed:
  - Python 3.8 or higher
  - pip (Python package manager)
  - A webcam (or any camera device recognized by your system)

### Running the Program Locally   
You can execute the program using the following bash commands:

 Clone the repository

```bash
git clone https://github.com/SerhiiHamretskyi/face_detection.git
cd face-analyzer
```

 Install dependencies
```bash
pip install -r requirements.txt
```
 Run the program

```bash
python main.py
```

### Running the Program in Docker Compose

   1. **Ensure Docker and Docker Compose are Installed**: 
   Make sure you have Docker and Docker Compose installed on your machine. 
   2. **Prepare Your Project**: 
   Your project directory should contain the following files:
   - `docker-compose.yml`
   - `Dockerfile` for analyzing service
   - Your source code files (including `start.py`)

   3. **Build and Run the Services**:
Open your terminal, navigate to your project directory, and run the following command:
   ```bash
   # Build the Docker image
docker build -t face-analyzer 
   ```
   ```bash
   # It sets up permissions for GUI access, which is required before running the container.
xhost +local:docker
   ```
   ```bash
   # Run the container
docker run --rm -it face-analyzer
   ```
   This commands will build your face_detection image and run it in the container.
### Summary

- **Docker Compose**: Good for consistency and ease of deployment across different environments.
  
- **Local Execution**: Useful for development or testing without Docker. Ensure you have all the services running locally.

## Usage