"""
Name: Mopeli Moka
Student Number: MPLMOK001
WP: 3-Programming task
Date:25/09/2020
"""

#import libraries
import RPi.GPIO as GPIO
import time
#setmodes
GPIO.setmode(GPIO.BOARD)
#Enable GPIO pin for output.
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#Set LED to be initially low.
GPIO.output(7,GPIO.LOW)

#Function to turn LED on.
def turnOn(channel):
	print("LED IS ON")
	time.sleep(1)
	GPIO.output(7,GPIO.HIGH)
	



