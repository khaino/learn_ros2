#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node

class KeyboardControl(Node):
    def __init__(self):
        super().__init__("keyboard_control")
        self.get_logger().info("keyboard_control initialized!")

    def start(self):
        while True:
            print("Hello World!")
            time.sleep(1)


def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    node.start()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()