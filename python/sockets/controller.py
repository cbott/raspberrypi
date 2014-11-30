#program to read controlling computer input which will be sent to the Pi

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("Pi Communications")

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("left")
    if keys[pygame.K_RIGHT]:
        print("right")
