#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped


rospy.init_node('set_init_pose', anonymous=True)
pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size=1)

initpose_msg = PoseWithCovarianceStamped()
initpose_msg.header.frame_id = "map" 
initpose_msg.pose.pose.position.x = -0.03
initpose_msg.pose.pose.position.y = 0.0074
initpose_msg.pose.pose.position.z = 0.0
initpose_msg.pose.pose.orientation.x = 0.0
initpose_msg.pose.pose.orientation.y = 0.0
initpose_msg.pose.pose.orientation.z = -0.0074
initpose_msg.pose.pose.orientation.w = 1.0


rospy.sleep(1) #10Hz

rospy.loginfo("Setting initial pose")
pub.publish(initpose_msg)
rospy.loginfo("Initial pose SET")
