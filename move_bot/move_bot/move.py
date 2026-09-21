import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


class Move(Node):
    #Constructor for class Move
    def __init__(self):
        super().__init__('move')
        
        #Subscribing to the controller topic to receive move data
        self.con_sub = self.create_subscription(
            Joy,'/ros_robot_controller/joy',self.con_callback,10)

        #Instanciating a publisher to upload controller data to the bot
        self.publisher = self.create_publisher(
                Twist,'/cmd_vel',10)

    def con_callback(self, joy_msg):
        
        #Getting all off the controller input data
        msg = Twist()

        #Grabbing the 2 data points we care about, forward and rotation
        msg.linear.x = joy_msg.axes[1]
        msg.angular.z = joy_msg.axes[0]

        #Uploading the move data to the bot
        self.publisher.publish(msg)


def main():

    #Standard main stuff cuz Nave said so
    rclpy.init()
    move = Move()
    rclpy.spin(move)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
