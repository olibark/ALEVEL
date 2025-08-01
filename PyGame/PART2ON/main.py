import pygame, init, loop
from constants import FPS
import constants as CONST

screen, player, enemy, clock = (init.Init()[0], init.Init()[1],
                                init.Init()[2], init.Init()[3])
init.drawBG(screen, init.BACKGROUND)


while CONST.running:
    clock.tick(FPS)  # set FPS
    loop.main_loop(enemy, player, screen) #main loopaa

pygame.quit()