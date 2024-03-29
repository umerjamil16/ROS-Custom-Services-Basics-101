#! /usr/bin/env python

import rospy
from exercise33.srv import CustomSrvMsg, CustomSrvMsgResponse # you import the service message python classes generated from Empty.srv.
#from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist


def my_callback(request):
    rospy.loginfo("MoveCircle Callback has been called")
    rospy.loginfo("STARTED service move_bb8_in_circle_custom")

    i = 0
    while i <= request.duration:
        pub.publish(move(0.2,0,0,0,0,0.2))
        rate.sleep()
        i = i+1

    pub.publish(move(0,0,0,0,0,0))
    rospy.loginfo("Finished service move_bb8_in_circle_custom")

    response = CustomSrvMsgResponse()
    response.success = True
    return response
   # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))

def move(x1, y1, z1, x2, y2, z2):
    move = Twist()
    move.linear.x = x1
    move.linear.y = y1
    move.linear.z = z1

    move.angular.x = x2
    move.angular.y = y2
    move.angular.z = z2
    return move


rospy.init_node('bb8_custom_service_server')
my_service = rospy.Service('/move_bb8_in_circle_custom', CustomSrvMsg , my_callback) # create the Service called my_service with the defined callback

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rate = rospy.Rate(1)

rospy.spin() # maintain the service open.