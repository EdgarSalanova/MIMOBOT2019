from adafruit_servokit import ServoKit
from time import sleep
import random
kit = ServoKit(channels = 16)

minAngle = 580
maxAngle = 2480
migAngle = 1530
migAngleL = 1350

def initMimobot():
    kit.servo[1].set_pulse_width_range(migAngle, maxAngle)
    kit.servo[1].angle = 0
    kit.servo[0].set_pulse_width_range(migAngle, maxAngle)
    kit.servo[0].angle = 0
    kit.servo[2].set_pulse_width_range(minAngle, maxAngle)
    kit.servo[2].angle = 0
    kit.servo[3].set_pulse_width_range(minAngle, maxAngle)
    kit.servo[3].angle = 0
    kit.servo[4].set_pulse_width_range(minAngle, maxAngle)
    kit.servo[4].angle = 0
    kit.servo[5].set_pulse_width_range(maxAngle, maxAngle)
    kit.servo[5].angle = 0
    sleep(1)
    
def colocarAngles(mimoB):
    c = mimoB[4]
    #cas elevat
    if c == 0:  
        #kit.servo[4].set_pulse_width_range(maxAngle, maxAngle)
        #kit.servo[4].angle = 0
        #kit.servo[5].angle = 0
        s6 = (mimoB[0]*10) + (minAngle+50)
        s4 = (mimoB[1]*10) + minAngle + 50
        if s4 > 1530:
            s4 = maxAngle - s4
            s4 = 1530 + s4
        else:
            s4 = 2480
        s5 = (mimoB[2]*10) + (minAngle+50)
        s3 = (mimoB[3]*10) + minAngle + 50
        if s3 > 1530:
            s3 = maxAngle - s3
            s3 = 1530 + s3
        else:
            s3 = 2480
        
            
        kit.servo[0].set_pulse_width_range(s3, maxAngle)  #re
        kit.servo[0].angle = 0
        #s4 = (mimoB[1]*10) + (950)
        kit.servo[1].set_pulse_width_range(s4, maxAngle)  #le
        kit.servo[1].angle = 0
        kit.servo[2].set_pulse_width_range(s5, maxAngle)  #rs
        kit.servo[2].angle = 0
        kit.servo[3].set_pulse_width_range(s6, maxAngle)  #ls
        kit.servo[3].angle = 0
        
    if c == 1: #croissant
        s6 = (mimoB[0]*10) + (minAngle+50)
        s4 = (mimoB[1]*10) + minAngle + 50
        if s4 > 1530:
            s4 = maxAngle - s4
            s4 = 1530 - s4
        else:
            s4 = 630
            
        s5 = (mimoB[2]*10) + (minAngle+50)
        s3 = (mimoB[3]*10) + minAngle + 50
        if s3 > 1530:
            s3 = maxAngle - s3
            s3 = 1530 - s3
        else:
            s3 = 630
        #kit.servo[4].angle = 0
        #kit.servo[5].angle = 180
        kit.servo[0].set_pulse_width_range(s3, maxAngle)  #re
        kit.servo[0].angle = 0
        kit.servo[1].set_pulse_width_range(s4, maxAngle)  #le
        kit.servo[1].angle = 0
        kit.servo[2].set_pulse_width_range(s5, maxAngle)  #rs
        kit.servo[2].angle = 0
        kit.servo[3].set_pulse_width_range(s6, maxAngle)  #ls
        kit.servo[3].angle = 0
       
    if c == 2: #l down & r up
        #banda dreta amunt
        s5 = (mimoB[2]*10) + (minAngle+50)
        s3 = (mimoB[3]*10) + minAngle + 50
        if s3 > 1530:
            s3 = maxAngle - s3
            s3 = 1530 + s3
        else:
            s3 = 2480
            
        #banda esquerra avall
        s6 = (mimoB[0]*10) + (minAngle+50)
        s4 = (mimoB[1]*10) + minAngle + 50
        if s4 > 1530:
            s4 = maxAngle - s4
            s4 = 1530 - s4
        else:
            s4 = 630 
        kit.servo[0].set_pulse_width_range(s3, maxAngle)  #re
        kit.servo[0].angle = 0
        kit.servo[1].set_pulse_width_range(s4, maxAngle)  #le
        kit.servo[1].angle = 0
        kit.servo[2].set_pulse_width_range(s5, maxAngle)  #rs
        kit.servo[2].angle = 0
        kit.servo[3].set_pulse_width_range(s6, maxAngle)  #ls
        kit.servo[3].angle = 0   
    if c == 3: #r down & l up
        #banda esquerra amunt
        s6 = (mimoB[0]*10) + (minAngle+50)
        s4 = (mimoB[1]*10) + minAngle + 50
        if s4 > 1530:
            s4 = maxAngle - s4
            s4 = 1530 + s4
        else:
            s4 = 2480
            
        #banda dreta avall
        s5 = (mimoB[2]*10) + (minAngle+50)
        s3 = (mimoB[3]*10) + minAngle + 50
        if s3 > 1530:
            s3 = maxAngle - s3
            s3 = 1530 - s3
        else:
            s3 = 630
        kit.servo[0].set_pulse_width_range(s3, maxAngle)  #re
        kit.servo[0].angle = 0
        kit.servo[1].set_pulse_width_range(s4, maxAngle)  #le
        kit.servo[1].angle = 0
        kit.servo[2].set_pulse_width_range(s5, maxAngle)  #rs
        kit.servo[2].angle = 0
        kit.servo[3].set_pulse_width_range(s6, maxAngle)  #ls
        kit.servo[3].angle = 0
