#! /usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal

def active_cb(extra):
        rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
        rospy.loginfo("Current location: "+str(feedback))

def done_cb(status,result):
        if status == 3:
                rospy.loginfo("Goal reached")
        if status == 2 or status == 8:
                rospy.loginfo("Goal cancelled")
        if status == 4:
                rospy.loginfo("Goal aborted")

rospy.init_node('send_goal')

navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
navclient.wait_for_server()


goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()
1,988, -1,986

goal.target_pose.pose.position.x = 1.99
goal.target_pose.pose.position.y = -1.99
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 1.0
goal.target_pose.pose.orientation.w = 0.01


navclient.send_goal(goal,done_cb,active_cb,feedback_cb)
finished = navclient.wait_for_result()

if not finished:
        rospy.logerr("Action server not avaliable")
else:
        rospy.loginfo(navclient.get_result())
i
