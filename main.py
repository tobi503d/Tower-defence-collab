#Game name "defencin"

import pygame
import random

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









#      --- blueprint for enemies ---
class enemy:
    def __init__(self, ID_, HP_, speed_, defense_):
        self.ID = ID_
        self.HP = HP_
        self.speed = speed_
        self.defence = defense_
    
    def __repr__(self):
        return f"Enemy(ID={self.ID}, HP={self.HP}, speed={self.speed}, defence={self.defence})"


def enemyObjectMaker(enemyType):
    
    try:
        tempID = enemyList[-1].ID +1
    except:
        tempID = 1

    tempObjekt = enemy(tempID, enemyStats[enemyType]["hp"], enemyStats[enemyType]["speed"], enemyStats[enemyType]["defence"])
    enemyList.append(tempObjekt)







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
