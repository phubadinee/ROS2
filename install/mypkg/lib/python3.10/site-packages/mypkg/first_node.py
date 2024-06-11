#!/usr/bin/env python3



import rclpy                        # rcl -> ros client library 
from rclpy.node import Node
from std_msgs.msg import Int64      # Import Message
import random
from rclpy import qos               # Import qos

class NumberNode(Node):
    def __init__(self):
        super().__init__("number_publisher_node")

        # self.num_pub = self.create_publisher(Type, TopicName, [Qos_profile, Dept])
        self.num_pub = self.create_publisher(Int64, "number_topic", qos_profile=qos.qos_profile_sensor_data)

        # Frequency of Send msgs and call "self.num_timer_callback" function
        self.num_timer = self.create_timer(0.5, self.num_timer_callback)

    def num_timer_callback(self):
        random1 = random.randint(0,100)
        msg = Int64()
        msg.data = random1
        print(f"Send message : {msg.data}")
        self.num_pub.publish(msg)      # Calling Publisher


def main():
    rclpy.init()
    node = NumberNode()

    rclpy.spin(node)        # for running loop
    rclpy.shutdown()

if __name__=="__main__":
    main()