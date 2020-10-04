import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

# Background
background = pygame.image.load('gameplay.png')

# Sound
mixer.music.load("musik.mp3")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Alien Wars")
icon = pygame.image.load('uf.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ufos.png')

# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

#warna
black = (0,0,0)
gray = (10,10,10)
white = (255,255,255)
red = (255,0,0)
darkred = (120,0,0)
green = (0,255,0)
darkgreen = (0,120,0)
yellow = (220,220,25)
darkyellow = (120,120,0)
transparan = (255,255,255,128)

clock = pygame.time.Clock()