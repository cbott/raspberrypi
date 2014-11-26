import RPi.GPIO as gpio
import time

def pulse_len(angle):
	#in seconds
    return (-0.000011111111111111*angle + 0.0021)

pin = 12

gpio.setmode(gpio.BOARD)
gpio.setup(pin , gpio.OUT)

servo = gpio.PWM(pin, 100)
servo.start(0)


def set(angle):
	pulse = -0.0527777777*angle+10.083333333333333
	servo.ChangeDutyCycle(pulse)

while True:
	dc = input("duty cycle:")
	servo.ChangeDutyCycle(dc)

print ("done")
