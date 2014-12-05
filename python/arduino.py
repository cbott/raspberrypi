import smbus
import time

class I2C(object):
	"""An I squared C (I2C) device to communicate with using the RPi"""
	def __init__(self, address=0x04):
		self.address = address
		self.bus = smbus.SMBus(1)
	def writeNumber(self, value):
		self.bus.write_byte(self.address, value)
		return -1
	def readNumber(self):
                rec = 0
                while not rec:
                        try:
                                number = self.bus.read_byte(self.address)
                                rec = 1
                        except IOError:
                                rec = 0
		return number

arduino = I2C()
while True:
	identifier = input("Id (1-15): ")
	data = input("Data (1-15): ")
	
##	if not var:
##		continue
	val = identifier<<4 | (data & 0b1111)#make id the 1st 4 bits
                                            #and data last 4 bits and limit to 4 bits
	arduino.writeNumber(val)
	print "[RPi] Sent:", val
	time.sleep(0.01)
	number = arduino.readNumber()
	print"[Arduino] Received:", number
	print
