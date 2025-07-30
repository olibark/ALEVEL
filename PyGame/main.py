import os
import pygame
from constants import WIDTH, HEIGHT, running #thought would be cleaner than importing everything

os.system('cls' if os.name == 'nt' else 'clear')  #clear terminal dependant on OS (as i have used many different os in develop)
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Window")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False