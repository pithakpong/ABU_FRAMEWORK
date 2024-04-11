import rclpy
from rclpy.node import Node
from abu_interfaces.msg import Tsl
class TslSubscriber(Node):

    def __init__(self):
        super().__init__('Tsl_subscriber')
        self.subscription = self.create_subscription(
            Tsl,
            'Tsl',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        for i in range(64):
            print(f'{msg.sequence[i]} ',end='')
        print()

def main(args=None):
    rclpy.init(args=args)

    Tsl_subscriber = TslSubscriber()

    rclpy.spin(Tsl_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
