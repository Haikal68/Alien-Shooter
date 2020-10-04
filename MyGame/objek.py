import time
from cobavar import *

def text_object(text,font,color):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg, x , y, w ,h, ic , ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    #print(mouse)

    if x+w > mouse[0] > x and y+h > mouse[1] >y:
        pygame.draw.rect(screen, ac,(x, y,w,h))

        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(screen, ic,(x, y,w,h))
    
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_object(msg, smallText , white)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf,textRect)


