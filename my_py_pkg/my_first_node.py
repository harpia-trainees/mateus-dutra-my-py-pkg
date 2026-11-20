#!/usr/bin/env python3
import rclpy #vai precisar em todos seus nodulos de python
from rclpy.node import Node

#O nodulo nao e o arquivo em si, e sim o que esta dentro dele

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0 
        self.get_logger().info("Hello World")
        self.create_timer(1.0,self.timer_callback)


    def timer_callback(self):
        self.get_logger().info("Hello"+ " " + str(self.counter_))
        self.counter_+=1



def main(args=None):
    rclpy.init(args=args)#tem que ter
    node = MyNode()
    rclpy.spin(node) #keep the node alive,until cntrl+c

    rclpy.shutdown()#tem que ter


if __name__ == "__main__":
    main()  
