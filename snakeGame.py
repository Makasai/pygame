
# import modules
import pygame
import sys
import random
import time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(1)
else:
    print("(+) PyGame successfully initialized")

# Play window
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game')

# Colors  (r,g,b)
red = pygame.Color(255,0,0) # gameover
green = pygame.Color(0,255,0) # nake
black = pygame.Color(0,0,0) # score
white = pygame.Color(255,255,255) # background
brown = pygame.Color(165,42,42) # food

# FPS controller
fpsController = pygame.time.Clock()

snakePos = [100,50] # head of snake
snakeBody = [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

# Game Over
def gameOver():
    myFont = pygame.font.SysFont('calibri', 72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit(1)

# Main Logic of the game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.EVENT(QUIT))

        # validation of direction
        # you can't go left if you're going right - makes sense
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction == 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction == 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction == 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction == 'DOWN'

        # update snake position [x,y]
        if direction == 'RIGHT':
            snakePos[0] += 10
        if direction == 'LEFT':
            snakePos[0] -= 10
        if direction == 'UP':
            snakePos[1] -= 10
        if direction == 'DOWN':
            snakePos[1] += 10

        # Snake body mechanism
        snakeBody.insert(0,list(snakePos))
        if snakePos == foodPos:
            foodSpawn = False
        else:
            snakeBody.pop()

        if foodSpawn == False:
            foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
        foodSpawn = True

        playSurface.fill(white)
        for pos in snakeBody:
            pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

        pygame.display.flip()
        fpsController.tick(25)
