import pygame as pg
pg.mixer.init()

motor = pg.mixer.Sound("/home/pi/Desktop/python/motor.wav")
print "playing"
pg.mixer.Sound("/home/pi/Desktop/python/motor.wav").play()
print "done"
