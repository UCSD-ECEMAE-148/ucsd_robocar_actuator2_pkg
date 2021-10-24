# ucsd_robocar_actuator2_pkg 

<div>

## Table of Contents
  - [**Dependencies**](#dependencies)
    - [adafruit_servokit](#adafruit_servokit)
    - [pyVesc](#pyVesc)
  - [**Nodes**](#nodes)
    - [adafruit_steering_node](#adafruit_steering_node)
    - [adafruit_throttle_node](#adafruit_throttle_node)
    - [vesc_steering_node](#vesc_steering_node)
    - [vesc_rpm_node](#vesc_rpm_node)
  - [**Topics**](#topics)
    - [steering](#steering)
    - [throttle](#throttle)
  - [**Launch**](#launch)
    - [adafruit](#adafruit)
    - [vesc](#vesc)

<div align="center">

## Nodes

</div>

### **adafruit_steering_node**

Associated file: **adafruit_steering_node.py**


Associated Topics:
- Subscribes to the [**steering**](#steering)

This node subscribes to the [**steering**](#Topics) topic. Then use the [**adafruit_servokit**](#adafruit_servokit)
module on **channel 1** for sending signals to the hardware.

Plenty of information on how to use the adafruit_servokit libraries can be found <a href="https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython" >here</a> and <a href="https://github.com/adafruit/Adafruit_CircuitPython_ServoKit" >here</a> 


### **adafruit_throttle_node**

Associated file: **adafruit_throttle_node.py**

Associated Topics:
- Subscribes to the [**throttle**](#throttle)

This node subscribes to the [**throttle**](#Topics) topic. Then use the [**adafruit_servokit**](#adafruit_servokit)
module on **channel 2** for sending signals to the hardware.

This node is also responsible for reading and setting the throttle calibration values.

### **vesc_steering_node**

Associated file: **vesc_steering_node.py**

Associated Topics:
- Subscribes to the [**steering**](#steering)

This node subscribes to the [**steering**](#Topics) topic. Then use the [pyVesc](#pyVesc)
module through usb serial communication to send steering commands.

Plenty of information on how to use the vesc python libraries can be found <a href="https://pyvesc.readthedocs.io/en/latest/" >here</a> and <a href="https://github.com/LiamBindle/PyVESC" >here</a> 


### **vesc_rpm_node**

Associated file: **vesc_rpm_node.py**

Associated Topics:
- Subscribes to the [**throttle**](#throttle)

This node subscribes to the [**throttle**](#Topics) topic. It then converts the data to an integer value thats scaled by its maximum RPM. Then use the [pyVesc](#pyVesc) module through usb serial communication to send rpm commands.

<div align="center">

## Topics

</div>

| Nodes |  Msg Type | Subscribed Topics |
| ------ | ------ | ------ |
| adafruit_steering_node | std_msgs.msg.Float32 | /steering |
| adafruit_throttle_node | std_msgs.msg.Float32 | /throttle |
| vesc_steering_node     | std_msgs.msg.Float32 | /steering |
| vesc_rpm_node          | std_msgs.msg.Float32 | /throttle |


`ros2 topic pub /stering std_msgs/msg/Float32 "{angle: 0.0, throttle: 0.0}"`

<div align="center">

## Launch

</div>



#### **adafruit**

Associated file: **adafruit.launch.py**

This file launches both [adafruit_steering_node](#adafruit_steering_node) and [adafruit_throttle_node](#adafruit_throttle_node) nodes.

`ros2 launch ucsd_robocar_actuator2_pkg adafruit.launch.py`

#### **vesc**

Associated file: **vesc.launch.py**

This file launches both [vesc_steering_node](#vesc_steering_node) and [vesc_rpm_node](#vesc_rpm_node) nodes.

`ros2 launch ucsd_robocar_actuator2_pkg adafruit.launch.py`
