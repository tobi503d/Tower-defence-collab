from dataclasses import dataclass
from Tower_data import towerStats
import pygame

@dataclass
class tower:
    
    price: int
    dmg: int
    speed: float
    towerRange: int
    aoe: int
    spawnLocation: int
    sprite: pygame.Surface



    def update(self, ):
        pass




def towerObjectMaker(towerType, spawnLocation, sprite):

    Object = tower(towerStats[towerType]["price"], towerStats[towerType]["dmg"], towerStats[towerType]["speed"], towerStats[towerType]["range"], towerStats[towerType]["aoe"], spawnLocation, sprite)
    