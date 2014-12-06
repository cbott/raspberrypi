import time
from i2c import *

arduino = I2C()
DATA_BITS = 4#bits used as data. must match value on arduino
while True:
	identifier = input("Id (1-15): ")
	data = input("Data (1-15): ")
	
	val = combine_bits(DATA_BITS, identifier, data)#make id the 1st 4 bits
                                            #and data last 4 bits and limit to 4 bits
	arduino.writeNumber(val)
	print "[RPi] Sent:", val
	time.sleep(0.01)
	number = arduino.readNumber()
	print"[Arduino] Received:", number
	print
