
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy import qos


class TwistSub(Node):
    def __init__(self):
        super().__init__("twist_subscriber_node")
        self.twist_sub = self.create_subscription(Twist, "cmd_vel", self.twist_callback, qos_profile=qos.qos_profile_system_default)
        self.twist_sub

    def twist_callback(self, msg_in):
        linear_x = msg_in.linear.x
        angular_z = msg_in.angular.z

        sum_vel = linear_x + angular_z
        print("Sum vel :", sum_vel)

def main():
    rclpy.init()

    ts = TwistSub()
    
    rclpy.spin(ts)
    rclpy.shutdown()

if __name__=="__main__":
    main()