#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from pynput import keyboard

msg = """
Direction Control
-----------
     i    
j         l
     k
-----------
i : forward
k : reverse
j : left steering
l : right steering
-----------
Speed Control
-----------
w : speed up (+1)
s : speed down (-1)
-----------
"""

class KeyboardControl(Node):

    MIN_SPEED = 1
    MAX_SPEED = 2
    SPEED_STEP = 0.1
    SPEED_UP = 'w'
    SPEED_DOWN = 's'

    FORWARD = 'i'
    REVERSE = 'k'
    LEFT = 'j'
    RIGHT = 'l'

    def __init__(self):
        super().__init__("keyboard_control")
        self.logger = self.get_logger()
        self.logger.info("keyboard_control initialized!")

        self.speed = 1
        self.direction_control = {
            self.FORWARD: 0,
            self.REVERSE: 0,
            self.LEFT: 0,
            self.RIGHT: 0
        }
        self.speed_control = {self.SPEED_UP, self.SPEED_DOWN}

    def _set_speed(self, speed):
        self.speed = min(KeyboardControl.MAX_SPEED, speed)

    def start(self):
        self.get_logger().info(f"____start_____")
        running = True
        while running:
            with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
                listener.join()

    def on_press(self, key):
        try:
            if not hasattr(key, 'char'):
                self.logger.warn(f"Invalid key pressed: {key}")
                self.logger.info(msg)
                return
            
            ch = key.char.lower()
            self.logger.info(f"Key pressed: {ch}")

            if ch in self.direction_control:
                self.direction_control[ch] = 1
                if self.direction_control[self.FORWARD] == 1 and self.direction_control[self.REVERSE] == 1:
                    self.direction_control[self.FORWARD] = 0
                    self.direction_control[self.REVERSE] = 0
                    self.logger.warn(f"Do not press {self.FORWARD} and {self.REVERSE} at the same time!!")
                    self.logger.info(msg)
                    
                elif self.direction_control[self.LEFT] == 1 and self.direction_control[self.RIGHT] == 1:
                    self.direction_control[self.LEFT] = 0
                    self.direction_control[self.RIGHT] = 0
                    self.logger.warn(f"Do not press {self.LEFT} and {self.RIGHT} at the same time!!")
                    self.logger.info(msg)
            elif ch in self.speed_control:
                self.update_speed(ch)
            self.display_current_state()

        except AttributeError:
            self.logger.warn('Special key {0} pressed'.format(
                key))
            
    def on_release(self, key):
        if hasattr(key, 'char') and key.char.lower() in self.direction_control:
            k = key.char.lower()
            self.direction_control[k] = 0
            self.logger.info('{0} released'.format(key))
        if key == keyboard.Key.esc:
            return False
        
    def update_speed(self, key):
        if key == self.SPEED_UP:
            self.speed = min(self.speed + self.SPEED_STEP, self.MAX_SPEED)
        elif key == self.SPEED_DOWN:
            self.speed = max(self.speed - self.SPEED_STEP, self.MIN_SPEED)

    def display_current_state(self):
        forward = self.direction_control[self.FORWARD]
        reverse = self.direction_control[self.REVERSE]
        left = self.direction_control[self.LEFT]
        right = self.direction_control[self.RIGHT]
        speed = round(self.speed, 1)
        msg = f"speed: {speed}, forward: {forward}, reverse: {reverse}, left: {left}, right: {right}"
        self.logger.info(msg)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    node.start()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()