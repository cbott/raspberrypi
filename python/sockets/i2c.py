import smbus

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

def combine_bits(databits, num1, num2):
        #take 2 numbers and combine into 1 byte
        #num1 = 10 = 0b00001010 and num2 = 5 = 0b00000101 and databits = 4
        #returns 0b10100101 = 165
        return num1<<databits | (num2 & (2**databits - 1))#limits data to specified # of bits
