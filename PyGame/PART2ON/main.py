import pygame, init, loop
import constants as c

(screen, enemy, 
    player, clock) = init.Init()

while c.running:
    clock.tick(c.FPS)  # set FPS
    loop.main_loop(player, enemy, screen) #main loopaa

pygame.quit()

print("clean exit")