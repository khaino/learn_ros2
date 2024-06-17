# Install ROS2 humble
- follow https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
# Install Colcon
- run `sudo apt install python3-colcon-common-extensions`
- add `source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash` in `~/.bashrc`
# Create ROS package
- create `ros2_ws/src` directory and go to `ros2_ws`
- run `colcon build`
- run `source install/local_setup.bash`
- add `source ~/work/ros2_ws/install/setup.bash` in `~/.bashrc`
- run `ros2 pkg create my_py_pkg --build-type  ament_python --dependencies rclpy`
# Run a package
- ros2 run my_py_pkg py_node
# Tips
- `ros2 node list` to check the node currently running
- `ros2 node info nodename` to get detail information about the node
- `ros2 run my_py_pkg py_node --ros-args -r __node:=test` run node with different name
# Colcon
- colcon build --packages-select my_py_pkg --symlink-install
# ROS2 messages
- `ros2 interface show example_interfaces/msg/String` to check a message
- `ros2 topic echo /robot_news` to log messages received on a topic

# ROS2 topic debugging
- `ros2 topic list` show all the topics
- `ros2 topic info /robot_news` more information about a topic
- `ros2 topic echo /robot_news` to log messages received on a topic
- `ros2 topic hz /robot_news` frequency at which a topic receives msg
- `ros2 topic bw /robot_news` bandwidth
- `ros2 topic pub -r 5 /robot_news example_interfaces/msg/String "{data: 'Hello from terminal'}"` publish message