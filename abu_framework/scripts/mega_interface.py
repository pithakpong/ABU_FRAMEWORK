 #!/usr/bin/env python3
from abu_interfaces.srv import Mega
import serial
import rclpy
from rclpy.node import Node


class MegaService(Node):

    def __init__(self):
        super().__init__('mega_service')
        self.ser = serial.Serial('/dev/ttyUSB0')
        self.srv = self.create_service(Mega, 'ball_command', self.callback)

    def callback(self, request, response):
        self.ser.write(request.req.encode())
        response.res = self.ser.readline().decode().strip()
        self.get_logger().info('Incoming request %s\n' % (request.req))
        return response


def main():
    rclpy.init()
    mega_service = MegaService()

    rclpy.spin(mega_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
