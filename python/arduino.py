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
		number = self.bus.read_byte(self.address)
		return number

arduino = I2C()
while True:
	var = input("Number 1-9:")
	if not var:
		continue
	arduino.writeNumber(var)
	print("[RPi] Sent:", var)
	time.sleep(1)
	number = arduino.readNumber()
	print("[Arduino] Received:", number)
	print
