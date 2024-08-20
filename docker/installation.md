docker run -it --name master ros:noetic bash
apt-get update

sudo apt install git-all
sudo apt install ros-noetic-tf2*scripts36.2/DeveloperGuide/SD/Kernel/KernelCustomization.html#building-the-jetson-linux-kernel
tar xf public_sources.tbz2 -C install/


https://stackoverflow.com/questions/34800731/module-not-found-when-i-do-a-modprobe
sudo apt install linux-generic -y 
sudo apt install --reinstall linux-image-$(uname -r) -y;
sudo apt install --reinstall linux-modules-$(uname -r) -y;
sudo apt install --reinstall linux-modules-extra-$(uname -r) -y;

ros2 topic pub /ros2_topic_a std_msgs/msg/String "data: 'Hello, ROS 2'"
rostopic pub -r 3 /example_topic std_msgs/String "data: 'Hello, World'"

ROS2 bridge
[colcon build](https://docs.ros.org/en/humble/How-To-Guides/Using-ros1_bridge-Jammy-upstream.html)colcon build

wget https://developer.nvidia.com/downloads/embedded/l4t/r35_release_v5.0/sources/public_sources.tbz2
mkdir -p /lib/modules/5.10.104-tegra
tar xf public_sources.tbz2 -C /lib/modules/5.10.104-tegra


cp -r /lib/modules/5.4.0-190-generic/ /lib/modules/5.10.104-tegra

ip -det link show can0


rosrun scout_bringup setup_can2usb.bash
sudo modprobe gs_usb
source /opt/ros/noetic/setup.bash
cd catkin_ws/
source devel/setup.bash 


docker build -t roscb .
std_msgs/String

ros2 topic pub /bridge_msg std_msgs/String "data: 'Hello, ROS 2'"

ros2 topic pub /bridge_msg std_msgs/String "data: 'Hello, ROS 2'"
Parameter Bridge Guide
https://github.com/ros2/ros1_bridge#example-4-bridge-only-selected-topics-and-services

rosparam load config/config.yml
