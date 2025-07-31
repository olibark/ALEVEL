import pygame
import os

class Player(pygame.sprite.Sprite): 
    def __init__(self, char_type, x, y, scale, speed):
        
        pygame.sprite.Sprite.__init__(self)
        
        BASE = os.path.dirname(os.path.abspath(__file__))
        
        self.char_type = char_type
        self.x = x
        self.y = y
        self.movingLeft = False
        self.movingRight = False
        self.scale = scale
        self.char_type = char_type
        self.RIGHT = 1
        self.LEFT = 1
        self.speed = speed
        self.direction = self.RIGHT
        self.flip = False
        self.animationList = []
        self.index = 0
        self.updateTime = pygame.time.get_ticks()
        #self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        for i in range(5):
            img = pygame.image.load(os.path.join(BASE, 'img', (f'{self.char_type}'), 'Idle', f'{i}.png'))
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animationList.append(img)
        self.image = self.animationList[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def move(self, screen):
        
        dx = 0
        dy = 0
        
        if self.movingLeft:
            dx = -self.speed
            self.flip = True
            self.direction = self.LEFT
        
        if self.movingRight:
            dx = self.speed
            self.flip = False
            self.direction = self.RIGHT
            
        self.rect.x += dx
        self.rect.y += dy
        
        # Ensure player stays within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
    
    def draw(self, screen ):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    
    def setScale(self, scale):
        BASE = os.path.dirname(os.path.abspath(__file__))
        img = pygame.image.load(os.path.join(BASE, 'img', self.char_type, 'Idle', '0.png'))
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        
        # Get new rect but keep current center
        old_center = self.rect.center
        self.scale = scale
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        # Clamp the new rect to screen bounds
        screen_width = 800  # or use a passed-in value if you prefer
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

    def update(self):
        #update animation
        cooldown = 100
        