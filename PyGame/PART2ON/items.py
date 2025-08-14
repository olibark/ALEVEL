import pygame, os
import constants as c

class Item(pygame.sprite.Sprite):
    def __init__(self,itemType, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.itemType = itemType
        self.image = c.itemBoxes[self.itemType]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + c.TILESIZE //2, y + (c.TILESIZE - self.image.get_height()))
    
    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            #check box
            if self.itemType == 'health' and player.health < player.maxHealth:
                healthDiff = player.maxHealth - player.health
                if healthDiff >= 50:
                    player.health += 50
                else:
                    player.health += healthDiff
                
            elif self.itemType == 'grenade':
                grenadeDiff = player.maxGrenades - player.grenades
                if grenadeDiff >= 3:
                    player.grenades += 3
                else:
                    player.grenades += grenadeDiff 
                    
            elif self.itemType == 'ammo':
                ammoDiff = player.maxAmmo - player.ammo
                if ammoDiff >= 15:
                    player.ammo += 15
                else:
                    player.ammo += ammoDiff
            
            
            
itemBoxGroup = pygame.sprite.Group() 