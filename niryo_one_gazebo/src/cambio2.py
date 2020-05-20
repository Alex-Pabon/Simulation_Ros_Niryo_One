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
joint_names=["joint_1","joint_2","joint_3","joint_4","joint_5","joint_6"]


if __name__ == "__main__":
	rospy.init_node("sendJointsNode")

	#pub = rospy.Publisher("joint_states", JointState, queue_size=1000)
    	robot_client = actionlib.SimpleActionClient('niryo_one_follow_joint_trajectory_controller/follow_joint_trajectory',FollowJointTrajectoryAction) #Conectarse servidor

    	print "Waiting for server..."
   	robot_client.wait_for_server()
	print "Connected to server"

	Q0 = [0, 1, 0, 1, 0, 1]
	xd = [0.196, 0, 0.423]

   	g = FollowJointTrajectoryGoal()
    	g.trajectory = JointTrajectory()
   	g.trajectory.joint_names = joint_names

    	# Initial position
    	g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(2.0))]

	
    	robot_client.send_goal(g)
    	robot_client.wait_for_result()
    	rospy.sleep(1)
    
    	rate = rospy.Rate(100)
    	while not rospy.is_shutdown():
        	robot_client.cancel_goal()

 
        	#Q0[0] = Q0[0]+0.005

       	 	g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(0.008))]
        	robot_client.send_goal(g)
        	robot_client.wait_for_result()

		Q0 = ikine_niryo(xd, Q0)

        	rate.sleep()

    		robot_client.cancel_goal()
		
		xd = [0.196, 0.1, 0.423]
		rospy.sleep(5)

