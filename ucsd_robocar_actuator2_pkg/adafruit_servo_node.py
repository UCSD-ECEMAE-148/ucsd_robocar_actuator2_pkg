#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from adafruit_servokit import ServoKit

NODE_NAME = 'adafruit_servo_node'
TOPIC_NAME = '/servo'

'''
[0, 180]degrees: [full right, full left]
'''

class AdafruitServo(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        self.steering_subscriber = self.create_subscription(Float32, TOPIC_NAME, self.callback, 10)
        self.kit = ServoKit(channels=16)
        self.default_bus_num = int(1)
        self.default_servo_channel = int(3)
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bus_num', self.default_bus_num),
                ('servo_channel', self.default_servo_channel)
            ])
        self.bus_num = int(self.get_parameter('bus_num').value)
        self.servo_channel = int(self.get_parameter('servo_channel').value)

        if self.bus_num == 0:
            i2c_bus0 = (busio.I2C(board.SCL_1, board.SDA_1))
            self.kit = ServoKit(channels=16, i2c=i2c_bus0)
        else:
            self.kit = ServoKit(channels=16)

    def callback(self, data):
        kit.servo[self.servo_channel].angle = data.data


def main(args=None):
    rclpy.init(args=args)
    adafruit_servo = AdafruitServo()
    try:
        rclpy.spin(adafruit_servo)
        adafruit_servo.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        adafruit_servo.get_logger().info(f'Shutting down {NODE_NAME}...')
        adafruit_servo.destroy_node()
        rclpy.shutdown()
        adafruit_servo.get_logger().info(f'{NODE_NAME} shut down successfully.')


if __name__ == '__main__':
    main()
