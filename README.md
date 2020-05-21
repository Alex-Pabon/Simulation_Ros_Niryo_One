# Niryo One ROS Simulation
Licensed under GPLv3 (see [LICENSE file](https://github.com/NiryoRobotics/niryo_one_ros_simulation/blob/master/LICENSE))

Works on ROS Kinetic.

ROS simulation for the robot [Niryo One](https://niryo.com/niryo-one/). This work simulates the Niryo One robot in Gazebo and Rviz, and also shows different ways to control it.



##1. Install from source

Get the code:

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/Alex-Pabon/Simulation_Ros_Niryo_One
```

Build the packages:

```bash
cd ~/catkin_ws
catkin_make
```


#### Don't forget to use those commands before you try to launch anything or terminal(you can add them in your .bashrc) : ####

```bash
source /opt/ros/kinetic/setup.bash 
source ~/catkin_ws/devel/setup.bash
```

## Display Niryo One with Rviz

To simply display the robot and get to move each joint separately, run:

```bash
roslaunch niryo_one_description display.launch
```

## Show Niryo in RVIZ and move it with the Joystick
Run: 
```bash
roslaunch niryo_one_description display2.launch
```

In another terminal, configure your Joystick you can do it bye using the following guide:
http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick

Then, in another terminal, run:
```bash
rosrun niryo_one_description joystick_ikine
```

## Niryo One in Gazebo
Developed and tested on ROS Kinetic/Gazebo 9.

1. Constant motion
El Robot tendrá una posición inicial y apartir de esta se desplazará constantemente.
First start Gazebo (empty world) and Niryo One model:

```bash
roslaunch niryo_one_gazebo niryo_one_world.launch
```

Then, start the controllers (ros_control):

```bash
roslaunch niryo_one_gazebo niryo_one_control.launch
```

Por último, en una nueva terminal ejecuta:
```bash
rosrun niryo_one_gazebo cambio.py
```

2. Pick and place

El robot se moverá hasta el lugar del objeto, y luego simulará un desplazamiento del mismo hasta un punto contrario

First start Gazebo (empty world) and Niryo One model:

```bash
roslaunch niryo_one_gazebo niryo_one_world.launch
```

Then, start the controllers (ros_control):

```bash
roslaunch niryo_one_gazebo niryo_one_control.launch
```

Por último, en una nueva terminal ejecuta:

```bash
rosrun niryo_one_gazebo cambio2.py
```bash


### Otra parte



The ROS interface to control Niryo One is the same for the [real robot](https://github.com/NiryoRobotics/niryo_one_ros) and the Gazebo simulation.

The controller used for Niryo One is a joint\_trajectory\_controller (from ros\_control). See the [joint\_trajectory\_controller documentation](http://wiki.ros.org/joint_trajectory_controller) to know how to use it.


