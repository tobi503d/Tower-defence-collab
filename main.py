import pygame
import sys
import random
from Button import buttonStyle, button
import Enemy

pygame.init()

#       --- Variables ---

#   dictionary

enemyStats = {
    "basic": {
        "hp": 10,
        "speed": 10,
        "defence": 10
    },
    "fast": {
        "hp": 10,
        "speed": 20,
        "defence": 5
    },
    "tank": {
        "hp": 15,
        "speed": 5,
        "defence": 20
    }
}

#   lists

enemyList = []


icon = pygame.image.load("Images/Logo.png")

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Defencing")
pygame.display.set_icon(icon)

buttonStyle = buttonStyle((0, 0, 255), (0, 255, 0), (0, 255, 255))

def startGame():
    print("Started game")

def setup():
    global startButton
    startButton = button(pygame.Rect(200, 100, 200, 100), "Start", buttonStyle, onClick=startGame)


def main():
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 0, 0))
        startButton.update(screen)


        pygame.display.flip() #draws everything
    pygame.quit()
    sys.exit()



main()