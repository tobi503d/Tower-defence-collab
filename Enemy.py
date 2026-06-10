from dataclasses import dataclass
from Enemy_data import enemyStats, enemyList
import pygame
import random

#      --- blueprint for enemies ---
@dataclass
class enemy:

    ID: int
    HP: int
    speed: int
    defence: int
    spawnX: int
    spawnY: int
    sprite: pygame.Surface
        
    
    def __repr__(self):
        return f"Enemy(ID={self.ID}, HP={self.HP}, speed={self.speed}, defence={self.defence})"
    


    def update(self, screen):

        self.spawnX += random.randint(-20, 20)
        self.spawnY += random.randint(-20, 20)

        self.rect = (self.spawnX, self.spawnY)

        screen.blit(self.sprite, self.rect)

        

    



def enemyObjectMaker(enemyType, spawnX, spawnY, sprite):
    
    try:
        tempID = enemyList[-1].ID +1
    except:
        tempID = 1

    tempObjekt = enemy(tempID, enemyStats[enemyType]["hp"], enemyStats[enemyType]["speed"], enemyStats[enemyType]["defence"], spawnX, spawnY, sprite)
    enemyList.append(tempObjekt)