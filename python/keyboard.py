"""
Python Line EDiting
"""
# Python 2 compatibility
from __future__ import print_function, unicode_literals
__metaclass__ = type

#imports
import os
import sys
import RPi.GPIO as gpio
import time
import curses

#classes
class TermIO:
    def __init__(self):
        self.queue = []
        self._getch = self._getgetch()
    def _getgetch(self):
        try:
            import msvcrt
            return msvcrt.getch
        except ImportError:
            import tty, termios
            def getch():#blocking character input function
                infile = sys.stdin.fileno()
                old_settings = termios.tcgetattr(infile)
                try:
                    tty.setraw(infile)
                    return sys.stdin.read(1)
                finally:
                    termios.tcsetattr(infile, termios.TCSADRAIN, old_settings)
            return getch
    def getch(self):
        if len(self.queue):
            return self.queue.pop()
        else:
            return self._getch()
    def putch(self, ch):
        self.queue.append(ch)

####setup code
gpio.setmode(gpio.BOARD)
RED_PIN = 11
GREEN_PIN = 12
BLUE_PIN = 13
gpio.setup(RED_PIN, gpio.OUT)
gpio.setup(BLUE_PIN, gpio.OUT)
gpio.setup(GREEN_PIN, gpio.OUT)
#Term = TermIO()
win = curses.initscr()
win.nodelay(1)
curses.noecho()

gpio.output(RED_PIN, True)
gpio.output(GREEN_PIN, True)
gpio.output(BLUE_PIN, True)

####main code
key=" "
break_key = ' '#keypress to end the loop

while key!=ord(break_key):
    key = win.getch()#get keyboard input
    
    if key==ord('r'):#turn red on
	gpio.output(RED_PIN, False)
	gpio.output(GREEN_PIN, True)
        gpio.output(BLUE_PIN, True)
    elif key==ord('g'):
        gpio.output(RED_PIN, True)
	gpio.output(GREEN_PIN, False)
        gpio.output(BLUE_PIN, True)
    elif key==ord('b'):
        gpio.output(RED_PIN, True)
	gpio.output(GREEN_PIN, True)
        gpio.output(BLUE_PIN, False)
    else:#no keys pressed
	gpio.output(RED_PIN, True)
	gpio.output(GREEN_PIN, True)
        gpio.output(BLUE_PIN, True)
        
    time.sleep(0.03)
print(key)

#cleanup procedures
curses.endwin()
gpio.output(RED_PIN, True)
gpio.output(GREEN_PIN, True)
gpio.output(BLUE_PIN, True)
gpio.cleanup()
