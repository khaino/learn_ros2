#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.get_logger().info("AddTwoIntsClientNode started")
        self.call_add_two_ints_server(7, 9)
        self.call_add_two_ints_server(13, 5)


    def call_add_two_ints_server(self, a, b):
        print("call_add_two_ints_server")
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1):
            self.get_logger().warn("Waiting for server add_two_ints")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        print("callback_call_add_two_ints")
        try:   
            response = future.result()
            self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed: %r", (e,))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__mian__":
    main()