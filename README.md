# ucsd_robocar_sensor_pkg 

<div>

## Table of Contents
  - [**Config**](#config)
    - [ld06](#ld06)
    - [livox_lidar_config](#livox_lidar_config)
    - [my_razor](#my_razor)
    - [rp_lidar](#rp_lidar)
    - [sick_tim_5xx](#sick_tim_5xx)
  - [**Nodes**](#nodes)
    - [webcam_node](#webcam_node)
  - [**Topics**](#topics)
    - [scan](#scan)
    - [camera](#camera)
    - [imu](#imu)
    - [gps](#gps)
  - [**Launch**](#launch)
    - [lidar_bpearl](#lidar_bpearl)
    - [lidar_ld06](#lidar_ld06)
    - [lidar_livox](#lidar_livox)
    - [lidar_rp](#lidar_rp)
    - [lidar_sicktim](#lidar_sicktim)
    - [camera_intel455](#camera-navigation-calibration-launch)
    - [imu_artemis](#imu_artemis)

<div align="center">

## Nodes

</div>


### **throttle_client**

Associated file: **throttle_client.py**

Associated Topics:
- Subscribes to the [**throttle**](#Topics)

This node subscribes to the [**throttle**](#Topics) topic. We use subscriber callback function
to validate and normalize throttle value, and then use the [**adafruit_servokit**](#adafruit_servokit)
module on **channel 2** for sending signals to the hardware.

This node is also responsible for reading and setting the throttle calibration values.

### **steering_client**

Associated file: **steering_client.py**

Similar to [**throttle_client**](#throttle_client), this node subscribes to the [**steering**](#Topics)
topic and passes the signals to the hardware. The steering servo is on **channel 1**.

Plenty of information on how to use the adafruit_servokit libraries can be found <a href="https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython" >here</a> and <a href="https://github.com/adafruit/Adafruit_CircuitPython_ServoKit" >here</a> 


<div align="center">

## Launch

</div>


#### **throttle and steering launch**

Associated file: **throttle_and_steering_launch.launch**

This file launches both [**throttle_client**](#throttle_client) and [**steering**](#Topics) seperately because these topics can take some time to initialize which can delay productivity. Launch this script once and use the other launch files listed below to get the robot moving.

`roslaunch ucsd_robo_car_simple_ros throttle_and_steering_launch.launch`
