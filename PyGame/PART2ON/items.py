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
            if self.itemType == 'health':
                player.health +=25
            elif self.itemType == 'grenade':
                player.grenades += 3
            elif self.itemType == 'ammo':
                player.ammo += 10
            
            
            
itemBoxGroup = pygame.sprite.Group() 