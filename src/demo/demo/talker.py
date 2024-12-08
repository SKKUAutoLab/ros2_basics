import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Talker node has started.')

    def timer_callback(self):
        msg = String()
        msg.data = "I am a proud Korean."
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published message: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
