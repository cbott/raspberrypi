import pygame, sys
from pygame.locals import *
from encoder_class import RotaryEncoder

#background = (150,143,127)
speed = 0.5
A1PIN = 11
B1PIN = 12
BUTTON1 = 13
A2PIN = 15
B2PIN = 16
BUTTON2 = 18

class EtchASketch():
    BOARD_COLOR = (150,143,127)
    LINE_COLOR = (0,0,0)
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen.fill(EtchASketch.BOARD_COLOR)
        pygame.display.set_caption("etch-A-sketch")
        self.BOARD_SIZE= self.width, self.height = self.screen.get_width(), self.screen.get_height()
        self.START_POSITION = [self.width/2, self.height/2]
        self.current_pos = self.START_POSITION
        self.last_drawn_pos = self.current_pos
        
    def clear_board(self):
        self.screen.fill(EtchASketch.BOARD_COLOR)
    def move(self, dx, dy):
        if (self.current_pos[0]>0 or dx>0) and (self.current_pos[0]<self.width or dx<0):
            self.current_pos[0]+=dx
        if (self.current_pos[1]>0 or dy>0) and (self.current_pos[1]<self.height or dy<0):
            self.current_pos[1]+=dy
    def update(self):
        pygame.draw.line(self.screen, EtchASketch.LINE_COLOR,
                         self.last_drawn_pos,
                         [int(self.current_pos[0]), int(self.current_pos[1])])
        #self.screen.set_at((int(self.current_pos[0]), int(self.current_pos[1])), EtchASketch.LINE_COLOR)
        #store the point last drawn to
        self.last_drawn_pos = [int(self.current_pos[0]), int(self.current_pos[1])]
        pygame.display.flip()

sketch = EtchASketch()

def lrevents(val):
    if val == 1:
        sketch.move(speed,0)
    elif val == 2:
        sketch.move(-speed, 0)
    elif val == 3:
        sketch.clear_board()
    else:
        pass
def udevents(val):
    if val == 1:
        sketch.move(0,speed)
    elif val == 2:
        sketch.move(0,-speed)
    elif val == 3:
        pygame.quit()
        sys.exit()
    else:
        pass
    
encoder1 = RotaryEncoder(A1PIN, B1PIN, BUTTON1, lrevents)
encoder2 = RotaryEncoder(A2PIN, B2PIN, BUTTON2, udevents)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dx = 0
    dy = 0
    if pygame.key.get_pressed()[K_RIGHT]:
        dx=1
    elif pygame.key.get_pressed()[K_LEFT]:
        dx=-1
    if pygame.key.get_pressed()[K_DOWN]:
        dy=1
    elif pygame.key.get_pressed()[K_UP]:
        dy=-1

    sketch.move(dx*speed,dy*speed)
    
    if pygame.key.get_pressed()[K_SPACE]:
        sketch.clear_board()
    sketch.update()

