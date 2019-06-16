#!/usr/bin/env python

import rospy
from exercise33.srv import CustomSrvMsg, CustomSrvMsgRequest # you import the service message python classes generated from Empty.srv.
#from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
#from geometry_msgs.msg import Twist

rospy.init_node('call_move_bb8_in_circle_custom_srv')
rospy.wait_for_service('/move_bb8_in_circle_custom')
bb8_move_srv_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', CustomSrvMsg)
bb8_move_srv_client_obj = CustomSrvMsgRequest()

bb8_move_srv_client_obj.duration = 3

rospy.loginfo("Doing Service Call...")
result = bb8_move_srv_client(bb8_move_srv_client_obj)
rospy.loginfo(str(result)) # Print the result given by the service called
rospy.loginfo("END of Service call...")