import pygame
import sys
import random
from Button import buttonStyle, button
from Enemy import enemy, enemyObjectMaker
from Enemy_data import enemyList

pygame.init()

buttonStyle = buttonStyle((0, 0, 255), (0, 255, 0), (0, 255, 255))

icon = pygame.image.load("Images/Logo.png")
map1 = pygame.transform.scale(pygame.image.load("Images/Map_1.png"), (1280, 720))
basicEnemySprite = pygame.transform.scale(pygame.image.load("Images/Basic_enemy.png"), (45, 45))

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Defencing")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

displayWidth, displayHeight = screen.get_size()

onStartScreen = True
onMap1 = False
paused = False

enemySpawnX, enemySpawnY = (300, 300)

def startGame():
    global onStartScreen, onMap1

    print("Started game")
    onStartScreen = False
    onMap1 = True

def setup():
    global startButton, currentTicks, currentTicksDeath
    startButton = button(pygame.Rect(displayWidth/2, displayHeight/2, 200, 100), "Start", buttonStyle, 72, onClick=startGame)
    currentTicks = pygame.time.get_ticks()
    currentTicksDeath = pygame.time.get_ticks()

def enemySpawn():
    global currentTicks, currentTicksDeath
    #loop starts here

    if pygame.time.get_ticks() - currentTicks >= 2*1000: #2 sec
        enemyObjectMaker("basic", enemySpawnX, enemySpawnY, basicEnemySprite)
        currentTicks = pygame.time.get_ticks()
        # spawn enemy
        print("Spawned enemy")
        print(len(enemyList))
        
    if pygame.time.get_ticks() - currentTicksDeath >= 1*1000: #1 sec
        for x in range(len(enemyList)):
            enemyList[x].HP -= 1
        currentTicksDeath = pygame.time.get_ticks()

def main():
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        if not paused:
            if onStartScreen:
                screen.fill((255, 0, 0))
                startButton.update(screen)
            elif onMap1:
                screen.blit(map1, (0, 0))
                enemySpawn()

            for x in range(len(enemyList)):
                enemyList[x].update(screen)


        


        global temp
        temp = 0
        for x in range(len(enemyList)):
            x -= temp
            if enemyList[x].HP <= 0:
                enemyList.pop(x)
                temp += 1
                print("enemy killed")


        pygame.display.update() #draws everything

        clock.tick(60)
    pygame.quit()
    sys.exit()



main()