import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from .vesc_submodule.vesc_client import VESC_

NODE_NAME = 'vesc_rpm_node'
TOPIC_NAME = '/throttle'

v = VESC_()

class VescRPM(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        self.rpm_subscriber = self.create_subscription(Float32, TOPIC_NAME, self.callback, 10)
        self.max_rpm = 5000

    def callback(self, data):
        throttle = data.data  #scaled from [-1:1], need to convert to RPM
        rpm = int(self.max_rpm * throttle)
        v.send_rpm(rpm)


def main(args=None):
    rclpy.init(args=args)
    vesc_rpm = VescRPM()
    rclpy.spin(vesc_rpm)
    vesc_rpm.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
