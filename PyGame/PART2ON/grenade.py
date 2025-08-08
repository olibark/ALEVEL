import pygame
import constants as c

class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, player):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -12
        self.speed = 10
        self.image = c.grenadeImage
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        
grenadeGroup = pygame.sprite.Group()