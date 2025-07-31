import pygame
import constants as c

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = c.bulletImg
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        self.rect.x += (self.speed * self.direction)
        
        # Remove bullet if it goes off screen
        if self.rect.right < 0 or self.rect.left > c.WIDTH:
            self.kill()

#create a group for bullets            
bulletGroup = pygame.sprite.Group()
