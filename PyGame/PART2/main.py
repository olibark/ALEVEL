import pygame
from constants import running, movingLeft, movingRight, FPS #thought would be cleaner than importing everything
import player as pl
import init
import loop

clock = pygame.time.Clock()
screen = init.Init()
init.drawBG(screen, init.BACKFROUND)

player = pl.Player('player', 200, 200, 5, 5)
enemy = pl.Player('enemy', 400, 200, 5, 5)

while running:
    
    clock.tick(FPS)  # set FPS

    loop.main_loop(player, enemy, screen, running) #main loopaa

pygame.quit()