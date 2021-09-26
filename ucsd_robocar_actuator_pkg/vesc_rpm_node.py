#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from vesc_client import VESC_

NODE_NAME = 'vesc_rpm_node'
RPM_REQUEST_TOPIC_NAME = 'vesc_rpm_request'
RPM_ACTUAL_TOPIC_NAME = 'vesc_rpm_actual'

v = VESC_()

class VescRPM(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        self.centroid_subscriber = self.create_subscription(Float32, RPM_REQUEST_TOPIC_NAME, self.callback, 10)


    def callback(self, data):
        rpm = data.data
        v.send_rpm(rpm)
        # v.get_rpm()


def main(args=None):
    rclpy.init(args=args)
    vesc_rpm = VescRPM()
    rclpy.spin(vesc_rpm)
    vesc_rpm.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
