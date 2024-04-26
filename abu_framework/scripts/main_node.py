#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MainNode(Node):
    def __init__(self):
        super().__init__("main_node")
        self.arrays = [[0, 0, 0] for _ in range(64)]
        self.declare_parameters(
            namespace='',
            parameters=[
                ('team','red'), # value can have 'red' and 'blue'
                ('start','start') # value can have 'start' and 'retry'
            ])
        self.sub_frame = self.create_subscription(
            String,
            'frame',
            self.frame_callback,
            10
        )

    def frame_callback(self, msg):
        # Process the received message here
        elements = msg.data[:-1].split(',')
        rows = [row.strip('[').strip(']') for row in elements]
        result = [[int(num) for num in row.split()] for row in rows]
        self.arrays = result
        self.get_logger().info("Received message: %s" % str(self.arrays))

def main(args=None):
    rclpy.init(args=args)
    main_node = MainNode()

    try:
        while rclpy.ok():
            # Your main loop logic
            team = main_node.get_parameter('team').get_parameter_value().string_value
            start = main_node.get_parameter('start').get_parameter_value().string_value
            #main_node.get_logger().info(f"{team} {start}")
            rclpy.spin_once(main_node, timeout_sec=0.1)  # Process ROS events
    except KeyboardInterrupt:
        pass

    main_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
