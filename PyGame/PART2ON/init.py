import pygame
import os
import constants as c

BACKGROUND = (0, 0, 0)
GREEN = (20, 255, 20)

def Init():
    pygame.init()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal depending on OS
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    c.bulletImg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'bullet.png')).convert_alpha()

    pygame.display.set_caption("Game Window")
    print(f"Game initialized with dimensions: {c.WIDTH}x{c.HEIGHT}")
    return screen

def drawBG(screen, BACKGROUND):
    screen.fill(BACKGROUND)
    pygame.draw.line(screen, GREEN, (0, 300), (c.WIDTH, 300))