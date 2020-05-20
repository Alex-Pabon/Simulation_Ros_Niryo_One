cmake_minimum_required(VERSION 2.8.3)
project(niryo_one_gazebo)
find_package(catkin REQUIRED 
  actionlib
  actionlib_msgs
  control_msgs
  rospy
  trajectory_msgs)

catkin_package()
