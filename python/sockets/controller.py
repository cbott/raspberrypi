#program to read controlling computer input which will be sent to the Pi

import pygame, sys
from pygame.locals import *

size = width, height = (500, 500)
current_pos = (width/2.0,height/2.0)
background = (255,255,255)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pi Communications")
screen.fill(background)

point = pygame.image.load("point.bmp")
pointrect = point.get_rect(center = current_pos)

clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
##        elif event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                print("left")
##            if event.key == pygame.K_RIGHT:
##                print("right")

    move = [0,0]
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        move[0] = -1
    if keys[K_RIGHT]:
        move[0] = 1
    if keys[K_UP]:
        move[1] = -1
    if keys[K_DOWN]:
        move[1] = 1

    pointrect = pointrect.move(move)

    screen.blit(point, pointrect)

    pygame.display.flip()
    
