import rclpy
import time
import geometry_msgs.msg
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
e : speed up (+1)
d : speed down (-1)
-----------
"""

class KeyboardControl(Node):

    MAX_SPEED = 10

    def __init__(self):
        super().__init__("keyboard_control")
        self.logger = self.get_logger()
        self.logger.info("keyboard_control initialized!")

        self.speed = 0.5
        self.direction_control = {
            'i': 0,
            'k': 0,
            'l': 0, 
            's': 0
        }

        # Publisher for Twist messages
        self.publisher = self.create_publisher(geometry_msgs.msg.Twist, 'keyboard_control', 10)

    def start(self):
        self.logger.info("Starting keyboard listener...")
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char.lower() in self.direction_control:
                k = key.char.lower()
                self.direction_control[k] = 1

                if self.direction_control['i'] == 1 and self.direction_control['s'] == 1:
                    self.direction_control['i'] = 0
                    self.direction_control['k'] = 0
                    self.logger.warn("Do not press 'i' and `k` at the same time!!")
                    self.logger.info(msg)
                    
                elif self.direction_control['j'] == 1 and self.direction_control['d'] == 1:
                    self.direction_control['j'] = 0
                    self.direction_control['l'] = 0
                    self.logger.warn("Do not press `j' and `l` at the same time!!")
                    self.logger.info(msg)

                self.publish_twist()
                self.logger.info(f"Direction control: {self.direction_control}\n")
            else:
                self.logger.info(f"Invalid key pressed: {key}")
        except AttributeError:
            self.logger.info('Special key {0} pressed'.format(key))
            
    def on_release(self, key):
        if hasattr(key, 'char') and key.char.lower() in self.direction_control:
            k = key.char.lower()
            self.direction_control[k] = 0
            self.publish_twist()
            self.logger.info(f"Direction control: {self.direction_control}\n")
        if key == keyboard.Key.esc:
            return False

    def publish_twist(self):
        msg = geometry_msgs.msg.Twist()
        # Set linear and angular velocities based on direction control and speed
        msg.linear.x = self.speed * (self.direction_control['w'] - self.direction_control['s'])
        msg.angular.z = self.speed * (self.direction_control['d'] - self.direction_control['a'])
        self.publisher.publish(msg)
        self.logger.info(f"Twist message published: { msg}")

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    node.start()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
