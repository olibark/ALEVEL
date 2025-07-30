import pygame
import constants as const

pygame.init()

screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("Game Window")

while const.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            const.running = False