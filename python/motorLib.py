#library to ease use of L298N motor controller with Raspberry Pi
import time
import RPi.GPIO as gpio

class Motor(object):
    def __init__(self, ena1 = 7, ena2 = 11, in1 = 13, in2 = 15):
        self.ena_pin1 = ena1
        self.ena_pin2 = ena2
        self.in1 = in1
        self.in2 = in2

        #allow use of gpio pins
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.ena_pin1, gpio.OUT)
        gpio.setup(self.ena_pin2, gpio.OUT)
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)

        #set enable pins on
        gpio.output(self.ena_pin1, True)
        gpio.output(self.ena_pin2, True)

    #movement functions, optional execution time
    def fwd(self, t=0):
        """Runs motor in one direction until stopped"""
        gpio.output(self.in1, True)
        gpio.output(self.in2, False)
        time.sleep(t)
        
    def rev(self, t=0):
        """Runs motor in opposite direction until stopped"""
        gpio.output(self.in1, False)
        gpio.output(self.in2, True)
        time.sleep(t)
        
    def stop(self, t=0):
        """Stops signals going to motor controller"""
        gpio.output(self.in1, False)
        gpio.output(self.in2, False)
        time.sleep(t)
