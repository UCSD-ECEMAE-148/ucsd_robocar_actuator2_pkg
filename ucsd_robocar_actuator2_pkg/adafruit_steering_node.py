#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from adafruit_servokit import ServoKit

NODE_NAME = 'adafruit_steering_node'
STEERING_TOPIC_NAME = 'adafruit_steering'


class AdafruitSteering(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        self.steering_subscriber = self.create_subscription(Float32, STEERING_TOPIC_NAME, self.callback, 10)


    def callback(self, data):
        normalized_steering = data.data
        angle_delta = normalized_steering * 90  # difference in degrees from the center 90 degrees
        kit.servo[1].angle = 90 + angle_delta



def main(args=None):
    rclpy.init(args=args)
    adafruit_steering = AdafruitSteering()
    rclpy.spin(adafruit_steering)
    adafruit_steering.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
