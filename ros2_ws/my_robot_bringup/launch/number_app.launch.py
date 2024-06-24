from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot_news_station_node = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        # to rename
        name="hello_sender",
        # remap topic
        remappings=[
            ("robot_news", "hello_news")
        ]
    )

    smartphone_node = Node(
        package="my_py_pkg",
        executable="smartphone",
        name="hello_receiver",
        remappings=[
            ("robot_news", "hello_news")
        ]
    )

    ld.add_action(robot_news_station_node)
    ld.add_action(smartphone_node)
    return ld