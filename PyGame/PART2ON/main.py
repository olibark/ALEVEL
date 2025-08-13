import pygame, init, loop
import constants as c

(screen, enemies, 
    player, clock) = init.Init()

while c.running:
    clock.tick(c.FPS)  # set FPS
    loop.main_loop(player, enemies, screen) #main loopaa

pygame.quit()

print("clean exit")