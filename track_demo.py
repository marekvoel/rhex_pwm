#import
RPi.GPIO as gpio
import sys
import time

#Setup
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)

#initializing
step = float(input("Steps definieren:"))
WaitTime = float(input("WaitTime definieren:"))
StepCounter = 0

#Start main loop
while StepCounter < steps:
gpio.output(24, True)
gpio.output(24, False)
StepCounter += 1

#Wait before taking the next step, will control the rotation speed
time.sleep(WaitTime)