#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

if __name__ == "__main__":
	rospy.init_node("sendJointsNode")
	pub = rospy.Publisher("joint_states", JointState, queue_size=1000)
	# Joint names
	#jnames = ("head_pan", "right_j0", "right_j1", "right_j2", "right_j3", "right_j4", "right_j5", "right_j6")
	#jnames=("arm_link","base_link","elbow_link","forearm_link","hand_link","shoulder_link")
	jnames=("joint_1","joint_2","joint_3","joint_4","joint_5","joint_6")
	# Desired Joint Configuration (in radians)
	jvalues = [0, 1, 0, 1, 0, 1]
	# Object (message) whose type is JointState
	jstate = JointState()
	# Set values to the message
	jstate.header.stamp = rospy.Time.now()
	jstate.name = jnames
	jstate.position = jvalues
	# Loop rate (in Hz)
	rate = rospy.Rate(100)
	# Continuous execution loop
	while not rospy.is_shutdown():
		# Current time (needed as an indicator for ROS)
		jstate.header.stamp = rospy.Time.now()
		# Publish message
		pub.publish(jstate)
		# Wait for the next iteration
		rate.sleep()
