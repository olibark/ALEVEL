import pygame, init, loop
from constants import FPS
import constants as CONST #thought would be cleaner than importing everything
import player as pl

clock = pygame.time.Clock()
screen = init.Init()
init.drawBG(screen, init.BACKGROUND)

player = pl.Player('player', 200, 200, 5, 5)
enemy = pl.Player('enemy', 400, 200, 5, 5)
while CONST.running:
    
    clock.tick(FPS)  # set FPS
    loop.main_loop(player, enemy, screen) #main loopaa

pygame.quit()