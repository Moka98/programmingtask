import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import threading
import time
import math
import RPi.GPIO as GPIO


# spi bus
spi = busio.SPI(clock =board.SCK,MISO=board.MISO,MOSI=board.MOSI)

# chip select
cs = digitalio.DigitalInOut(board.D5)

# mcp object
mcp = MCP.MCP3008(spi,cs)

#set up gpio switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#set variables
Tc = 0.01 # temperature coefficient =10.0 mV/degrees C
V0 = 0.5 # voltage at 0 degrees C
sample_rate=10

# analog input channels on pin 0 and pin 1
chan = AnalogIn(mcp,MCP.P0)
chanLDR = AnalogIn(mcp,MCP.P1)

print('Runtime      Luminosity       Temp Reading        Temp')
t0=time.time()
def print_sensors_thread():
	global sample_rate
	thread = threading.Timer(sample_rate,print_sensors_thread)
	thread.daemon = True
	thread.start()
	Vout=chan.voltage
	Vdiff=Vout-V0
	TA =Vdiff/Tc
	t1 = time.time()
	tt =math.floor(t1-t0)
	print(str(tt)+'s      '+str("{:.1f}".format(chanLDR.voltage*1333)+'       '), chan.value,str(TA) + '      C')

if __name__ == "__main__":
	print_sensors_thread()
	while True:
		input_state=GPIO.input(4)
		if input_state==False:
			if sample_rate==10:
				sample_rate=5
			elif sample_rate==5:
				sample_rate=1
			else:
				sample_rate=10
		pass


