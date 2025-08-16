import pygame, init, loop
import constants as c

(screen, enemyGroup,
    player, clock, healthBar) = init.Init()

while c.running:
    clock.tick(c.FPS)  # set FPS
    loop.main_loop(player, enemyGroup, screen, healthBar) #main loopaa

pygame.quit()