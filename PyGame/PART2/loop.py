import pygame
import player as pl
import init
import constants

def main_loop(player, enemy, screen, running):
    
    init.drawBG(screen, init.BACKFROUND)  # draw background
    if player.scale > enemy.scale:
        pl.Player.draw(enemy, screen)
        pl.Player.draw(player, screen)
    else:
        pl.Player.draw(player, screen)
        pl.Player.draw(enemy, screen)
    player.move(screen)
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                player.movingLeft = True
            if event.key == pygame.K_d:
                player.movingRight = True
            if event.key == pygame.K_LSHIFT:
                player.setScale(3)  # Scale down the player
            if event.key == pygame.K_LCTRL:
                player.setScale(7)  # Scale up the player
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.movingLeft = False
            if event.key == pygame.K_d:
                player.movingRight = False
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_LCTRL:
                player.setScale(5)
    pygame.display.flip()  #update the display
                
            