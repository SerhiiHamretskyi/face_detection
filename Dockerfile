FROM python:3.9-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    libxcb-cursor0 \
    pulseaudio \
    alsa-utils \
    libportaudio2 libportaudiocpp0 portaudio19-dev \
    python3-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    cmake \
    build-essential \
    espeak \
    libxcb-xinerama0 \
    libxcb1 \
    libx11-dev \
    libxrender-dev \
    libfreetype6 \
    libfontconfig1 \
    libxext6 \
    qt5-qmake \
    qtbase5-dev \
    qtchooser \
    qtbase5-dev-tools \
    flac \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Explicitly set the QT plugin path
ENV QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins
ENV QT_X11_NO_MITSHM=1
ENV PULSE_SERVER=unix:/run/user/1000/pulse/native
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the entrypoint to run your application
ENTRYPOINT ["python", "start.py"]

