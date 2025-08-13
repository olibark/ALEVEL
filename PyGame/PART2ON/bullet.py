import pygame
import constants as c
import player as pl

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = c.bulletImg
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.center = (x, y)
        self.direction = direction

    def update(self, player, enemy):
        self.rect.x += (self.speed * self.direction)
        
        # Remove bullet if it goes off screen
        if self.rect.right < 0 or self.rect.left > c.WIDTH:
            self.kill()
        
        if pygame.sprite.spritecollide(player, bulletGroup, False):
            if player.alive:
                player.health -= 20
                self.kill()
                
        for enemy in pl.enemyGroup:     
            if pygame.sprite.spritecollide(enemy, bulletGroup, False):
                if enemy.alive:
                    enemy.health -= 20
                    self.kill()
                    
#create a group for bullets            
bulletGroup = pygame.sprite.Group()
