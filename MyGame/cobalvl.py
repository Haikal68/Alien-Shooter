import pygame, random,time
import math
from var import *
from objek import *
from aksi import *

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    
    screen.blit(enemyImg[i], (x, y))

def caramain():
    background = pygame.image.load('cara.png')
    screen.blit(background, [0,0])

    caraMain = True

    while caraMain:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button("KEMBALI",340,470,140,50,darkred,red,game_intro)

        pygame.display.update()
        clock.tick(15)

def mulai():
    pygame.mixer.music.fadeout(5)
    pygame.mixer.music.load("musik.mp3")
    pygame.mixer.music.play(-1)
    game_loop()

def intro():
    pygame.mixer.music.load("gas.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    game_intro()

def keluar():
    intro = False
    pygame.display.quit()
    pygame.quit()
    sys.exit(0)

def game_intro():
    
    intro = True

    while intro:
        background = pygame.image.load("aaw.png")
        screen.blit(background ,[0,0])

        button("MULAI", 340,290,140,50,darkgreen,green,mulai)
        button("CARA MAIN",340,360,140,50,darkred,red,caramain)
        button("KELUAR",340,430,140,50,darkyellow,yellow,keluar)

        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                intro = False

def crash():
    TextCrash()
    askContinue()
    score_value = 0
    pygame.mixer.music.play(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
                quit()

        button("YA", 160,260,140,50, darkgreen , green , game_loop)
        button("TIDAK", 490,260,140,50,darkyellow,yellow,intro)

        pygame.display.update()


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def nabrak(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def game_loop():
    global bullet_state
    global score_value
    global enemyY
    global enemyX
    global enemyX_change
    global enemyY_change
    playerX = 370
    playerY = 480
    bulletX = 0
    bulletY = 480
    playerX_change = 0
    bulletX_change = 0
    bulletY_change = 10
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6
    snow_list = []

    for i in range(50):
        x = random.randrange(0, 800)    
        y = random.randrange(0, 800)
        snow_list.append([x, y])

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('silly.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)

    gameExit = False
    while not gameExit:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.K_q:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("gun.wav")
                        bulletSound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        for i in range(len(snow_list)):
                pygame.draw.circle(screen, white, snow_list[i], 3)
                snow_list[i][1] += 1
                if snow_list[i][1] > 800:
                    y = random.randrange(-50, -10)
                    snow_list[i][1] = y
                    x = random.randrange(0, 800)
                    snow_list[i][0] = x
        #pergerakan musuh
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                score_value = 0
                time.sleep(2)
                crash()

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]


            if enemyX[i] <= 0 and score_value >= 5 and score_value <= 10:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736 and score_value >= 5 and score_value <= 10:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]

            if enemyX[i] <= 0 and score_value >= 10 and score_value <= 20:
                enemyX_change[i] = 7
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736 and score_value >= 10 and score_value <= 20:
                enemyX_change[i] = -7
                enemyY[i] += enemyY_change[i]


            # Tabrakan
            collision = nabrak(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("peww.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()

splashscreen()
waitingscreen()
intro()