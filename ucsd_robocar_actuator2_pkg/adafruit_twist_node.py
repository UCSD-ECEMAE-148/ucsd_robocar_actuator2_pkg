import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from adafruit_servokit import ServoKit
import board
import busio

NODE_NAME = 'adafruit_twist_node'
TOPIC_NAME = '/cmd_vel'

class AdafruitTwist(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        self.rpm_subscriber = self.create_subscription(Twist, TOPIC_NAME, self.callback, 10)
        
        # Default board values
        self.default_bus_num = int(1)
        self.default_steering_channel = int(1)
        self.default_throttle_channel = int(2)
        self.default_steering_polarity = int(1) # if polarity is flipped, switch from 1 --> -1
        self.default_throttle_polarity = int(1) # if polarity is flipped, switch from 1 --> -1

        # declaring ROS parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bus_num', self.default_bus_num),
                ('steering_channel', self.default_steering_channel),
                ('throttle_channel', self.default_throttle_channel),
                ('steering_polarity', self.default_steering_polarity),
                ('throttle_polarity', self.default_throttle_polarity)
            ])
        
        # Get ROS parameters from config
        self.bus_num = int(self.get_parameter('bus_num').value)
        self.steering_channel = int(self.get_parameter('steering_channel').value)
        self.throttle_channel = int(self.get_parameter('throttle_channel').value)
        self.steering_polarity = int(self.get_parameter('steering_polarity').value)
        self.throttle_polarity = int(self.get_parameter('throttle_polarity').value)
        
        # Set BUS ID
        if self.bus_num == 0:
            i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
            self.kit = ServoKit(channels=16, i2c=i2c_bus0)
        else:
            self.kit = ServoKit(channels=16)


    def callback(self, msg):
        data_min_limit = -1
        data_max_limit = 1
        adafruit_min_limit = -1 # These will be rosparams eventually... : max_left
        adafruit_max_limit = 1  # These will be rosparams eventually... : max_right
        steering_angle = float(-0.1 + ((msg.angular.z-data_min_limit)*(adafruit_max_limit - adafruit_min_limit))/(data_max_limit-data_min_limit))

        # Send values to adafruit board 
        self.kit.servo[self.steering_channel].angle = float(90 * (1 + self.steering_polarity * msg.angular.z))
        self.kit.continuous_servo[self.throttle_channel].throttle = self.throttle_polarity * msg.linear.x


def main(args=None):
    rclpy.init(args=args)
    try:
        adafruit_twist = AdafruitTwist()
        rclpy.spin(adafruit_twist)
        adafruit_twist.destroy_node()
        rclpy.shutdown()
    except:
        adafruit_twist.get_logger().info(f'Could not connect to Adafruit, Shutting down {NODE_NAME}...')
        adafruit_twist.destroy_node()
        rclpy.shutdown()
        adafruit_twist.get_logger().info(f'{NODE_NAME} shut down successfully.')


if __name__ == '__main__':
    main()
