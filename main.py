#Game name "defencin"

import pygame
import random

pygame.init()

icon = pygame.image.load("Images/Logo.png")

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Defencing")
pygame.display.set_icon(icon)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

#       --- all of the above is just to keep the game running ---


buttonName = image()
buttonName.button(2, 3, image)
buttonName.button(2, 3, 43, 54, 223)

#      --- blueprint for enemies ---
class enemy:
    def __init__(self, HP_, speed_, defense_):
        self.HP = HP_
        self.speed = speed_
        self.defence = defense_


#       ---enemies---
basicEnemy = enemy(10, 10, 10)
fastEnemy = enemy(5, 20, 10)
slowEnemy = enemy(20, 5, 10)






