#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MainNode(Node):
	def __init__(self):
		super().__init__("main_node")
		self.declare_parameters(
		namespace='',
		parameters=[
			('team','red'), # value can have 'red' and 'blue'
			('start','start') # value can have 'start' and 'retry'
		])
def main(args=None):
	rclpy.init(args=args)
	mainnode = MainNode()
	while(1):
		try :
			team = mainnode.get_parameter('team').get_parameter_value().string_value
			start = mainnode.get_parameter('start').get_parameter_value().string_value
			mainnode.get_logger().info(f"{team} {start}")
		except KeyboardInterrupt:
			break
	mainnode.destroy_node()
if __name__ == "__main__":
	main()
