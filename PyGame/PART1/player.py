import pygame
import os


class Soldier(pygame.sprite.Sprite): 
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        BASE = os.path.dirname(os.path.abspath(__file__))
        img = pygame.image.load(os.path.join(BASE, 'img', 'player', 'Idle', '0.png'))
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def draw(self, screen ):
        
        screen.blit(self.image, self.rect)