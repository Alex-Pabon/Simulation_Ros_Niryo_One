#!/usr/bin/env python
import time
import rospy
import actionlib 
import roslib;
from control_msgs.msg import *
from trajectory_msgs.msg import *

from sensor_msgs.msg import JointState
from funciones import *
import math

# Joint names
joint_names=["joint_1","joint_2","joint_3","joint_4","joint_5","joint_6"]    #Joint name

#Pick and place

if __name__ == "__main__":
	rospy.init_node("sendJointsNode")

    	robot_client = actionlib.SimpleActionClient('niryo_one_follow_joint_trajectory_controller/follow_joint_trajectory',FollowJointTrajectoryAction) #Connect to server

    	print "Waiting for server..."
   	robot_client.wait_for_server()
	print "Connected to server"

	Q0 = [0, 0.2, 0, 1, 0, 1] #Initial position

   	g = FollowJointTrajectoryGoal()
    	g.trajectory = JointTrajectory()
   	g.trajectory.joint_names = joint_names

	#Simulate pick and place
    	# Send Initial position
    	g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(2.0))]
    	robot_client.send_goal(g)		#Send goal
    	robot_client.wait_for_result()
    	rospy.sleep(1)
    	rate = rospy.Rate(100)
        rate.sleep()

	print('Esperando')
	rospy.sleep(5)				#Wait 5 seconds in the starting position
	Q0 = [1.35, -1.07, 0, 0, 0, 0]		#Objecto position
       	g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(0.008))]
        robot_client.send_goal(g)
        robot_client.wait_for_result()

	rospy.sleep(3)

	print(Q0)
	Q0 = [0, 0, 0, 0, 0, 0]			#Return position
       	g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(0.008))]
        robot_client.send_goal(g)
        robot_client.wait_for_result()

	rospy.sleep(3)

	Q0 = [-1.30, -1.07, 0, 0, 0, 0]		#Place Object
       	g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(0.008))]
        robot_client.send_goal(g)
        robot_client.wait_for_result()


