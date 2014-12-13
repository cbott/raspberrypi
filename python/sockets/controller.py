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
background = (255,255,255)

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
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_program(conn)

    keys = pygame.key.get_pressed()

    drive = 0#forward:1 #back:2 #left:3 #right:4

#move a ball with the arrow keys
    move = [0,0]
    if keys[K_UP]:
        move[1] = -1
        drive = 1
    elif keys[K_DOWN]:
        move[1] = 1
        drive = 2
    elif keys[K_LEFT]:
        move[0] = -1
        drive = 3
    elif keys[K_RIGHT]:
        move[0] = 1
        drive = 4

    pointrect = pointrect.move(move)
    screen.blit(point, pointrect)

    pygame.display.flip()

##    data = pickle.loads(conn.recv(1024))
##    if not data:
##        break

    commands = [drive]#values for the drivetrain

    d_to_send = commands
    conn.send(pickle.dumps(d_to_send, protocol=2))
    print("sent ",commands)
