# Use a lightweight Ubuntu desktop image with VNC and NoVNC built-in
FROM dorowu/ubuntu-desktop-lxde-vnc:focal

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update apt and install Python 3, pip, and tkinter
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-tk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install required Python packages for the networking projects
RUN pip3 install --no-cache-dir scapy psutil

# Set the working directory
WORKDIR /root/Networking-Projects

# Copy the entire repository into the container
COPY . /root/Networking-Projects/

# The base image automatically starts the VNC server and NoVNC web interface on port 80.
# We expose port 80 for the web interface.
EXPOSE 80
