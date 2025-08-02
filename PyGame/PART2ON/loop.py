import pygame, init
import constants as c
import bullet as b

def main_loop(player, enemy, screen):
    
    init.drawBG(screen, init.BACKGROUND)  # draw background
    #player and enemy draw order
    if player.scale >= enemy.scale:
        enemy.draw(screen)
        player.draw(screen)
    else:
        player.draw(screen)
        enemy.draw(screen)
    
    player.update()
    enemy.update()
    #update and draw groups
    b.bulletGroup.update(player, enemy)
    b.bulletGroup.draw(screen)
    
    if player.alive:
        if c.shooting:
            player.shoot()
        if player.inAir:
            player.updateAction(2)
        elif player.movingLeft or player.movingRight:
            player.updateAction(player.RUNNING)#1 = running
        else: 
            player.updateAction(player.IDLE)#0 = idle
        player.move(screen)
        
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            c.running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                c.running = False
            if event.key == pygame.K_a:
                player.movingLeft = True
            if event.key == pygame.K_d:
                player.movingRight = True
            if event.key == pygame.K_j:
                c.shooting = True
            if event.key == pygame.K_LSHIFT:
                if player.scale == 5:
                    player.setScale(3)
                else:
                    player.setScale(5)
            if event.key == pygame.K_LCTRL:
                if player.scale == 5:
                    player.setScale(7)
                else:
                    player.setScale(5)
            if event.key == pygame.K_SPACE and player.alive:
                if not player.jump:
                    player.jump = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.movingLeft = False
            if event.key == pygame.K_d:
                player.movingRight = False
            if event.key == pygame.K_j:
                c.shooting = False
    
    pygame.display.flip()  #update the display
                
            