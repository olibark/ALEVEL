import pygame, init
import constants as c
import bullet as b
import grenade as g

def main_loop(player, enemyGroup, screen):
    
    init.drawBG(screen, init.BACKGROUND)  # draw background
    #player and enemy draw order
    maxEnemyScale = max((enemy.scale for enemy in enemyGroup), default = 0)
    if len(enemyGroup) > 0 and player.scale >= maxEnemyScale:
        for enemy in enemyGroup:
            enemy.draw(screen)
        player.draw(screen)
    else:
        player.draw(screen)
        for enemy in enemyGroup:
            enemy.draw(screen)

    player.update()
    for enemy in enemyGroup:
        enemy.update()
    #update and draw groups
    b.bulletGroup.update(player, enemyGroup)
    g.grenadeGroup.update(player, enemyGroup)
    g.explosionGroup.update()
    b.bulletGroup.draw(screen)
    g.grenadeGroup.draw(screen)
    g.explosionGroup.draw(screen)
    
    if player.alive:
        if c.shooting:
            player.shoot()
        #throw grenade
        elif c.grenading and c.grenadeThrown == False and player.grenades > 0:
            grenade = g.Grenade(player.rect.centerx + (player.rect.size[0] * 0.5 * player.direction),
                                player.rect.top, player.direction, player)
            g.grenadeGroup.add(grenade)
            c.grenadeThrown = True
            player.grenades -= 1
            print(player.grenades)
        if player.inAir:
            player.updateAction(2)
        elif player.movingLeft or player.movingRight:
            player.updateAction(player.RUNNING)#1 = running
        else: 
            player.updateAction(player.IDLE)#0 = idle
        player.move(screen)
    
    for enemy in enemyGroup:
        enemy.move(screen)
    
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
                    
            if event.key == pygame.K_i:
                c.grenading = True
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.movingLeft = False
            if event.key == pygame.K_d:
                player.movingRight = False
            
            if event.key == pygame.K_j:
                c.shooting = False
    
            if event.key == pygame.K_i:
                c.grenading = False
                c.grenadeThrown = False
    pygame.display.flip()  #update the display
                
            