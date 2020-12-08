#!/bin/python

#Dieses Programm lässt das Auto selbstständig fahren mit einem Radarsensor.

from jetbot import Robot
import time
import Radar_Python

robot = Robot()

while true:
    if abstand<=Radar_Python.getabstand:
        robot.left(0.3)
        time.sleep(1)
        robot.stop()
    else:
        robot.set_motors(0.6, 0.6)
        robot.stop()