import pygame, sys
from pygame.locals import *
size = width, height = (500, 500)
background = (255,2,55)
pt_color = (0,0,0)
current_pos = [50,50]

speed = [1,1]

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("missile.bmp")
#ballrect = ball.get_rect()

screen.fill(background)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] *= -1
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] *= -1

    if pygame.mouse.get_pressed()[0]:
        coords = pygame.mouse.get_pos()
        m_x = coords[0]
        m_y = coords[1]
        if m_x > current_pos[0] and current_pos[0]<width:
            current_pos[0]+=1
        elif m_x < current_pos[0] and current_pos[0]>0:
            current_pos[0]-=1
        if m_y > current_pos[0] and current_pos[1]<height:
            current_pos[1]+=1
        elif m_y < current_pos[0] and current_pos[1]>0:
            current_pos[1]-=1
    
      
    if pygame.mouse.get_pressed()[1]:
        screen.fill(background)
    #screen.blit(ball, ballrect)

    if pygame.mouse.get_pressed()[0]:
        screen.set_at(current_pos, pt_color)
    pygame.display.flip()



    
    
