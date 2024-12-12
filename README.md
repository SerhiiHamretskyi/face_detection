<!-- GitHub badges -->
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

# Face Recognition Camera with Voice Notifications

## Overview
A Python-based face recognition system that detects and recognizes faces in real time. It provides voice feedback to greet recognized individuals and notify about unrecognized faces, ideal for security or personalized interactions.

## Features
- **Real-Time Face Detection**: High-performance face detection using OpenCV and `face_recognition`.
- **Face Recognition**: Matches live faces against a stored reference photo.
- **Voice Feedback**: Uses `pyttsx3` for personalized voice notifications.
- **Interactive Setup**: Allows easy setup of reference photos.
- **Visual Feedback**: Displays video with annotations for detected faces.

## Technologies
- **Python 3.8+**
- **Libraries**: 
  - OpenCV (video processing and GUI)
  - face_recognition (face detection and encoding)
  - pyttsx3 (text-to-speech)

## Getting Started

### Prerequisites
Ensure you have:
- Python 3.8 or higher
- pip (Python package manager)
- A camera (webcam or compatible device)
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) (for Docker setup)

---

### Running Locally
Clone the repository, install dependencies, and run the program. Ensure that you have enough RAM on your device, as the program may consume significant memory and could cause the system to kill the process if resources are insufficient.
```bash
# Clone the repository
git clone https://github.com/SerhiiHamretskyi/face_detection.git
cd face-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the program
python start.py
```

---

### Running with Docker 
Run the program using Docker for easy deployment:

1.Pull the docker image.
To pull the image from Docker Hub, run:
```bash
docker pull serhiiham/face_analyzer
```

2.Allow GUI Access (for programs with visual components)
```bash
xhost +local:docker
```

3.Run the Docker image with this settings

Once the image is pulled and GUI access is granted, you can run the container with the following command:
```bash
docker run --rm --privileged \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=$DISPLAY \
    -e QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins \
    <your-docker-image>
```
This command mounts the X11 socket, sets the DISPLAY environment variable to allow GUI access, and specifies the path to the Qt platform plugins.

---

### Usage

1.Set up a Reference Photo:

-On the first run, the program asks for your name, creating a folder for you.

-If no reference photo exists, the program lets you capture one (you can make it with 's' button). 

2.Recognition Process:

-The program detects your face and compares it with the stored reference photo.

-If recognized, it greets you by name.

-If unrecognized, it notifies you accordingly.

3.Quit:

-You can exit the program by pressing the 'q' key, but make sure your keyboard is set to English.

## License

This project is licensed under the MIT License. See the LICENSE file for details.