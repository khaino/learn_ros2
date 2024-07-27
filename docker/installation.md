docker run -it --name master ros:noetic bash
apt-get update

sudo apt install git-all
sudo apt install ros-noetic-tf2*
sudo apt install iproute2
sudo apt-get install kmod


https://docs.nvidia.com/jetson/archives/r36.2/DeveloperGuide/SD/Kernel/KernelCustomization.html#building-the-jetson-linux-kernel
tar xf public_sources.tbz2 -C install/