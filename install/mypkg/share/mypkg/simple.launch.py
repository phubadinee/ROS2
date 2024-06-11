# launch
# launch ros

from launch_ros.actions import Node
from launch import LaunchDescription        # อธิบาย Node

def generate_launch_description():
    node1 = Node(package="mypkg",
                 executable="first_publisher")
    node2 = Node(package="mypkg",
                 executable="first_subscription")
    
    ld = LaunchDescription()  
    ld.add_action(node1)
    ld.add_action(node2)

    return ld

 # Go to Launch file (setup.py)
    
