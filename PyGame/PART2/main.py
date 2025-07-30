import os
import pygame
from constants import WIDTH, HEIGHT, running #thought would be cleaner than importing everything
import player
import init

screen = init.Init()
player1 = player.Player(200, 200, 5)

while running:
    player.Player.draw(player1, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    pygame.display.flip()  #update the display
pygame.quit()