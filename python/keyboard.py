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
LED_PIN = 22
gpio.setup(LED_PIN, gpio.OUT)
#Term = TermIO()
win = curses.initscr()
win.nodelay(1)
curses.noecho()

####main code
key=" "
break_key = 'a'#keypress to end the loop

while key!=ord(break_key):
    key = win.getch()#get keyboard input
    if key!=-1:
	gpio.output(LED_PIN, True)
    else:#no keys pressed
	gpio.output(LED_PIN, False)    
    time.sleep(0.01)
print(key)

#cleanup procedures
curses.endwin()
gpio.output(LED_PIN, False)
gpio.cleanup()
