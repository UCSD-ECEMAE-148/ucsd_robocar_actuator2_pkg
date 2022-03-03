#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from adafruit_servokit import ServoKit
import board
import busio

NODE_NAME = 'adafruit_continuous_servo_node'
TOPIC_NAME = '/continuous_servo'

'''
[-1, 1] : [max reverse, max forward]
'''

class AdafruitContinuousServo(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        self.steering_subscriber = self.create_subscription(Float32, TOPIC_NAME, self.callback, 10)
        self.default_bus_num = int(1)
        self.default_continuous_servo_channel = int(4)
        self.default_max_forward_limit = 1.0
        self.default_max_reverse_limit = -1.0
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bus_num', self.default_bus_num),
                ('continuous_servo_channel', self.default_continuous_servo_channel),
                ('max_forward', self.default_max_forward_limit),
                ('max_reverse', self.default_max_reverse_limit)
            ])
        self.bus_num = int(self.get_parameter('bus_num').value)
        self.continuous_servo_channel = int(self.get_parameter('continuous_servo_channel').value)
        self.max_forward = int(self.get_parameter('max_forward').value)
        self.max_reverse = int(self.get_parameter('max_reverse').value)

        if self.bus_num == 0:
            i2c_bus0 = (busio.I2C(board.SCL_1, board.SDA_1))
            self.kit = ServoKit(channels=16, i2c=i2c_bus0)
        else:
            self.kit = ServoKit(channels=16)

    def callback(self, data):
        continuous_servo_throttle = data.data
        if continuous_servo_throttle > self.max_forward:
            continuous_servo_throttle = self.max_forward
        elif continuous_servo_throttle < self.max_reverse:
            continuous_servo_throttle = self.max_reverse
        else:
            pass
        self.kit.continuous_servo[self.continuous_servo_channel].throttle = continuous_servo_throttle


def main(args=None):
    rclpy.init(args=args)
    adafruit_continuous_servo = AdafruitContinuousServo()
    try:
        rclpy.spin(adafruit_continuous_servo)
        adafruit_continuous_servo.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        adafruit_continuous_servo.get_logger().info(f'Could not connect to Adafruit, Shutting down {NODE_NAME}...')
        adafruit_continuous_servo.destroy_node()
        rclpy.shutdown()
        adafruit_continuous_servo.get_logger().info(f'{NODE_NAME} shut down successfully.')


if __name__ == '__main__':
    main()

