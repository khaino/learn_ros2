# This is an auto generated Dockerfile for ros:ros-core
# generated from docker_images/create_ros_core_image.Dockerfile.em
FROM ubuntu:focal

# setup timezone
RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends tzdata && \
    rm -rf /var/lib/apt/lists/*

# install packages
RUN apt-get update && apt-get install -q -y --no-install-recommends \
    dirmngr \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

##### NOETIC #####
# setup keys
RUN set -eux; \
       key='C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654'; \
       export GNUPGHOME="$(mktemp -d)"; \
       gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"; \
       mkdir -p /usr/share/keyrings; \
       gpg --batch --export "$key" > /usr/share/keyrings/ros1-latest-archive-keyring.gpg; \
       gpgconf --kill all; \
       rm -rf "$GNUPGHOME"

# setup sources.list
RUN echo "deb [ signed-by=/usr/share/keyrings/ros1-latest-archive-keyring.gpg ] http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros1-latest.list

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-core=1.5.0-1* \
    ros-noetic-tf2* \
    && rm -rf /var/lib/apt/lists/*

##########

##### FOXY #####
# setup keys
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 4B63CF8FDE49746E98FA01DDAD19BAB3CBF125EA

# setup sources.list
RUN echo "deb http://snapshots.ros.org/foxy/final/ubuntu focal main" > /etc/apt/sources.list.d/ros2-snapshots.list

# install ros2 packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-foxy-ros-core=0.9.2-1* \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -q -y --no-install-recommends python3-colcon-common-extensions 
##########

# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# install git
RUN apt-get update && apt-get install -q -y --no-install-recommends git

RUN apt-get update && apt-get install -q -y --no-install-recommends linux-generic 
RUN cp -r /lib/modules/5.4.0-192-generic /lib/modules/5.10.104-tegra

##### setup scout mobile robot wrapper #####
RUN apt-get update && apt-get install -q -y --no-install-recommends \
    build-essential \
    libasio-dev \
    ros-noetic-teleop-twist-keyboard

RUN apt-get update && apt-get install -q -y --no-install-recommends \
    kmod \
    iproute2

RUN mkdir -p /catkin_ws/src
RUN cd /catkin_ws/src && git clone https://github.com/agilexrobotics/ugv_sdk.git 
RUN cd /catkin_ws/src && git clone https://github.com/agilexrobotics/scout_ros.git
RUN /bin/bash -c "cd /catkin_ws && source /opt/ros/noetic/setup.bash && catkin_make && env"
##########
# ENV ROS_DISTRO noetic

RUN mkdir -p /scripts
# setup entrypoint
COPY ./ros_entrypoint.sh /scripts/
COPY ./init.sh /scripts/

ENTRYPOINT ["/scripts/init.sh"]
CMD ["bash"]