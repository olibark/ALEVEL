import os
import pygame
from constants import WIDTH, HEIGHT, running #thought would be cleaner than importing everything
import player

os.system('cls' if os.name == 'nt' else 'clear')  #clear terminal dependant on OS (as i have used many different os in develop)
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Window")
soldier = player.Soldier(200, 200, 5)
soldier2 = player.Soldier(400, 200, 5)


while running:
    player.Soldier.draw(soldier, screen)
    player.Soldier.draw(soldier2, screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
    pygame.display.flip()  #update the display
pygame.quit()