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


#funcion de trayectoria
def trayectoria(Q0, Qfinal):
	flag = False
	epsilon = 0.02
	while flag == False:
		for i in range(6):
			#if (Q0[i]>0):
			if (Q0[i]>Qfinal[i]+epsilon):	
				Q0[i]=round(Q0[i] - 0.04,2)
			elif (Q0[i]<Qfinal[i]-epsilon):
				Q0[i] = round(Q0[i] + 0.04,2)
			#else:
			#	if(Q0[i]<Qfinal[i]
		#print(Q0)
		g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*7, time_from_start=rospy.Duration(0.008))]
	        robot_client.send_goal(g)
        	robot_client.wait_for_result()	
		if (Q0[0]< Qfinal[0]+epsilon and Q0[0]>Qfinal[0]-epsilon):
			#print('Listo1')
			if (Q0[1]< Qfinal[1]+epsilon and Q0[1]>Qfinal[1]-epsilon):
				#print('Listo2')
				if (Q0[2]< Qfinal[2]+epsilon and Q0[2]>Qfinal[2]-epsilon):
					#print('Listo3')
					if (Q0[3]< Qfinal[3]+epsilon and Q0[3]>Qfinal[3]-epsilon):
						flag = True
						#print('Listo0') 
	return Q0
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
    	g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*9, time_from_start=rospy.Duration(0.008))]
    	robot_client.send_goal(g)		#Send goal
    	robot_client.wait_for_result()
    	rospy.sleep(1)
    	rate = rospy.Rate(100)
        rate.sleep()

	print('Esperando')
	rospy.sleep(1)				#Wait 5 seconds in the starting position
	Q1 = [1.35, -1.07, 0, 0, 0, 0]		#Objecto position
	Q0 = trayectoria(Q0,Q1)
	
       	#g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(0.008))]
        #robot_client.send_goal(g)
        #robot_client.wait_for_result()

	rospy.sleep(1)


	print(Q0)
	Q1 = [0, 0, 0, 0, 0, 0]			#Return position
       	#g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(0.008))]
        #robot_client.send_goal(g)
        #robot_client.wait_for_result()
	Q0 = trayectoria(Q0,Q1)

	rospy.sleep(3)

	print(Q0)
	Q1 = [-1.35, -1.08, 0, 0, 0, 0]		#Place Object
	Q0 = trayectoria(Q0,Q1)
       	#g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*6, time_from_start=rospy.Duration(0.008))]
        #robot_client.send_goal(g)
        #robot_client.wait_for_result()
	print(Q0)


