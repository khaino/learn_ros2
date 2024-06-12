# Install ROS2 humble
- follow https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
# Install Colcon
- run `sudo apt install python3-colcon-common-extensions`
- add `source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash` in `~/.bashrc`
# Create ROS package
- create `ros2_ws/src` directory and go to `ros2_ws`
- run `colcon build`
- run `source install/local_setup.bash`
- run `ros2 pkg create my_py_pkg --build-type  ament_python --dependencies rclpy`
# Run a package
- ros2 run my_py_pkg py_node