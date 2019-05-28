# This example moves a servo its full range (180 degrees by default) and then back.
 
from board import SCL, SDA
import busio
import time
from tkinter import *
import sys

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685
 
# This example also relies on the Adafruit motor library available here:
# https://github.com/adafruit/Adafruit_CircuitPython_Motor
from adafruit_motor import servo
 
i2c = busio.I2C(SCL, SDA)
 
# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 50
 
# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# This is an example for the Sub-micro servo: https://www.adafruit.com/product/2201
# servo7 = servo.Servo(pca.channels[7], min_pulse=580, max_pulse=2480)
# This is an example for the Micro Servo - High Powered, High Torque Metal Gear:
#   https://www.adafruit.com/product/2307
# servo7 = servo.Servo(pca.channels[7], min_pulse=600, max_pulse=2400)
# This is an example for the Standard servo - TowerPro SG-5010 - 5010:
#   https://www.adafruit.com/product/155
# servo7 = servo.Servo(pca.channels[7], min_pulse=600, max_pulse=2500)
# This is an example for the Analog Feedback Servo: https://www.adafruit.com/product/1404
# servo7 = servo.Servo(pca.channels[7], min_pulse=600, max_pulse=2600)
 
# The pulse range is 1000 - 2000 by default.
abs_min = 580 #580
abs_max = 2480 #2480

servo = servo.Servo(pca.channels[0])

current_val = 1530
servo.angle = 0


def show_values(self):
    current_val = w1.get()
    servo.set_pulse_width_range(current_val, abs_max)
    servo.angle = 0

master = Tk()
w1 = Scale(master, from_=abs_min, to=abs_max,command=show_values)     #slider 1
w1.pack()
print (w1.get())
Button(master, text='Show', command=show_values).pack()  #call function
                                                             #to get slider
mainloop()   


pca.deinit()