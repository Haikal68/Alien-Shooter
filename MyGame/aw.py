import pygame

#inisialisasi Pygame
pygame.init()

#Membuat Screen
screen = pygame.display.set_mode((800,600))

#Judul Dan Icon
pygame.display.set_caption("Alien Nyasar")
icon = pygame.image.load('uf.png')
pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load('ufos.png')
posisiX = 370
posisiY = 480
keys = {
    "top": False, 
    "bottom": False,
    "left": False,
    "right": False 
}

gerak_posisi = 0
gerak_atas = 0

def player(x,y):
    screen.blit(playerimg,(x, y))


#Game Loop
running = True
while running:
    screen.fill((23,42,21))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        #Gerakin Player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys["top"] = True
            elif event.key == pygame.K_a:
                keys["left"] = True
            elif event.key == pygame.K_s:
                keys["bottom"] = True
            elif event.key == pygame.K_d:
                keys["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys["top"] = False
            elif event.key == pygame.K_a:
                keys["left"] = False
            elif event.key == pygame.K_s:
                keys["bottom"] = False
            elif event.key == pygame.K_d:
                keys["right"] = False
    # - End of event loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # 9. Move the player ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if keys["top"]:
                posisiY -= 20 # kurangi nilai y
            elif keys["bottom"]:
                posisiY += 20 # tambah nilai y 
            if keys["left"]:
                posisiX -= 20 # kurangi nilai x
            elif keys["right"]:
                posisiX += 20 # tambah nilai x
        
        
 
    
    
    posisiY += gerak_atas
    posisiX += gerak_posisi
    if posisiX <=0:
        posisiX = 0
    elif posisiX >= 736:
        posisiX = 736

    player(posisiX,posisiY)
    pygame.display.update()
    