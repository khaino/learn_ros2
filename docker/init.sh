#!/bin/bash

sudo modprobe gs_usb

source /opt/ros/noetic/setup.bash
source catkin_ws/devel/setup.bash

rosrun scout_bringup setup_can2usb.bash
roslaunch scout_bringup scout_mini_robot_base.launch