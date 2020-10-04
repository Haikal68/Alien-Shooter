import pygame, sys, os
import time
from objek import *
from cobavar import *

def opentopscore():
    
    if not os.path.exists("save.dat"):
        f = open("save.dat")
        f.write(str(0))
        f.close()
        v = open("save.dat")
        TopScore = int (v.readline())
        v.close()
        return TopScore

def askContinue():
    
    largeText = pygame.font.Font('freesansbold.ttf',25)
    Textsurf, TextRect = text_object('Lanjut?',largeText,white)
    TextRect.center = ((display_width / 2 ), (display_height / 1.5) - 120)
    screen.blit(Textsurf,TextRect)

def TextCrash():
    
    largeText = pygame.font.Font('freesansbold.ttf',80)
    Textsurf, TextRect = text_object('GAME OVER !!', largeText,white)
    TextRect.center = TextRect.center = ((display_width / 2 ), (display_height / 2) - 120)
    pygame.draw.rect(screen, red, (0,80,800,250))
    screen.blit(Textsurf,TextRect)


def press_quit(event):
    
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
        quit()
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            gameExit = True
            pygame.quit()
            quit()


def splashscreen():
    
    img = pygame.image.load('aaaa.png')

    pygame.mixer.music.load("intro.wav")
    pygame.mixer.music.play(0)

    screen.blit(img,(0,0))

    pygame.display.update()
    time.sleep(4)

def waitingscreen():
    pygame.mixer.music.load('waiting.mp3')
    pygame.mixer.music.play(-1)

    largeText = pygame.font.Font('freesansbold.ttf',20)
    wait = pygame.image.load('fix.jpg')
    Textsurf, TextRect = text_object('Press Any Key to start..', largeText, white)
    TextRect.center = ((400), (300))

    screen.blit(wait,(0,0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(Textsurf,TextRect)

    waiting = True
    while waiting:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    waiting = False
            else:
                press_quit(event)

        pygame.display.update()
