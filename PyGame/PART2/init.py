import pygame
import os
import constants

BACKFROUND = (0, 0, 0)

def Init():
    pygame.init()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal depending on OS
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Game Window")
    print(f"Game initialized with dimensions: {constants.WIDTH}x{constants.HEIGHT}")
    return screen

def drawBG(screen, BACKGROUND):
    screen.fill(BACKGROUND)