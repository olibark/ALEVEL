import pygame, init, loop
import constants as c

(screen, player
,enemy, clock) = (init.Init()[0], init.Init()[1],
                  init.Init()[2], init.Init()[3])
init.drawBG(screen, init.BACKGROUND)


while c.running:
    clock.tick(c.FPS)  # set FPS
    loop.main_loop(enemy, player, screen) #main loopaa

pygame.quit()