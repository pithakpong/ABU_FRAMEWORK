#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from abu_interfaces.msg import Tsl


class TslPublisher(Node):

    def __init__(self):
        super().__init__('Tsl_publisher')
        self.publisher_ = self.create_publisher(Tsl, 'Tsl', 10)
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Tsl()
        for i in range(64):
            msg.sequence[i] = i
        self.publisher_.publish(msg)
        self.get_logger().info("complete publish")


def main(args=None):
    rclpy.init(args=args)
    Tsl_publisher = TslPublisher()
    rclpy.spin(Tsl_publisher)
    Tsl_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
