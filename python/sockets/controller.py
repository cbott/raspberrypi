#program to read controlling computer input which will be sent to the Pi

import pygame, sys, time
from pygame.locals import *

import socket, pickle
import random as rand
###
HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind((HOST, PORT))
s.listen(5)
###
size = width, height = (500, 500)
current_pos = (width/2.0,height/2.0)
background = (0,0,0)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pi Communications")
screen.fill(background)

point = pygame.image.load("point.bmp")
pointrect = point.get_rect(center = current_pos)

clock = pygame.time.Clock()

conctd = False
while not conctd:
    conctd = True
    try:
        conn, addr = s.accept()
    except BlockingIOError:
        conctd = False
#################################
def end_program(conn):
    #shutdown procedures
    conn.send(pickle.dumps("halt", protocol=2))
    time.sleep(1)#wait for data to be sent
    conn.close()
    print("Connection closed")
    pygame.quit()
    sys.exit()
#################################
while 1:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_program(conn)

    keys = pygame.key.get_pressed()
    
    r=0
    g=0
    b=0
    if keys[K_r]:
        r = 255
    if keys[K_g]:
        g = 255
    if keys[K_b]:
        b = 255
  
    background = (r,g,b)
    screen.fill(background)
    
#move a ball with the arrow keys
##    move = [0,0]
##    if keys[K_LEFT]:
##        move[0] = -1
##    if keys[K_RIGHT]:
##        move[0] = 1
##    if keys[K_UP]:
##        move[1] = -1
##    if keys[K_DOWN]:
##        move[1] = 1
##    pointrect = pointrect.move(move)
##    screen.blit(point, pointrect)

    pygame.display.flip()

##    data = pickle.loads(conn.recv(1024))
##    if not data:
##        break

    val = [r,g,b]

    d_to_send = val
    conn.send(pickle.dumps(d_to_send, protocol=2))
    print("sent ",val)
