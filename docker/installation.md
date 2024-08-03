docker run -it --name master ros:noetic bash
apt-get update

sudo apt install git-all
sudo apt install ros-noetic-tf2*
sudo apt install iproute2
sudo apt-get install kmod

sudo apt-get install ros-noetic-tf
sudo apt-get install ros-noetic-tf2
sudo apt-get install ros-noetic-tf2-ros

https://docs.nvidia.com/jetson/archives/r36.2/DeveloperGuide/SD/Kernel/KernelCustomization.html#building-the-jetson-linux-kernel
tar xf public_sources.tbz2 -C install/


https://stackoverflow.com/questions/34800731/module-not-found-when-i-do-a-modprobe
sudo apt install linux-generic -y 
sudo apt install --reinstall linux-image-$(uname -r) -y;
sudo apt install --reinstall linux-modules-$(uname -r) -y;
sudo apt install --reinstall linux-modules-extra-$(uname -r) -y;

ros2 topic pub /ros2_topic std_msgs/msg/String "data: 'Hello, ROS 2'"
rostopic pub -r 3 /example_topic std_msgs/String "data: 'Hello, World'"

ROS2 bridge
[colcon build](https://docs.ros.org/en/humble/How-To-Guides/Using-ros1_bridge-Jammy-upstream.html)colcon build

wget https://developer.nvidia.com/downloads/embedded/l4t/r35_release_v5.0/sources/public_sources.tbz2
mkdir -p /lib/modules/5.10.104-tegra
tar xf public_sources.tbz2 -C /lib/modules/5.10.104-tegra


cp -r /lib/modules/5.4.0-190-generic/ /lib/modules/5.10.104-tegra