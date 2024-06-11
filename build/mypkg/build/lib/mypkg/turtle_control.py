
import rclpy
from rclpy.node import Node
from rclpy import *
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class turtleControl(Node):
    def __init__(self):
        super().__init__("turtle_sim")
        self.vel_pub = self.create_publisher(Twist, "cmd_vel", 10)
        self.pose_sub = self.create_subscription(Pose, "pose", self.pose_callback, 10)
        self.vel_timer = self.create_timer(1, self.vel_timer_callback)

        self.vel_cmd = Twist()
        self.i = 0.0

    def pose_callback(self, pose):
        position_x = pose.x
        position_y = pose.y

        print(f"x : {position_x}, y : {position_y}")

    def vel_timer_callback(self):
        self.pattern()
        self.vel_pub.publish(self.vel_cmd)


    def pattern(self):
        self.vel_cmd.linear.x = 0.0
        self.vel_cmd.angular.z = 1.0
        
        print("Linear x :", self.i)
        self.i += 0.05
    

def main():
    rclpy.init()

    tc = turtleControl()
    rclpy.spin(tc)
    rclpy.shutdown()

if __name__=="__main__":
    main()
