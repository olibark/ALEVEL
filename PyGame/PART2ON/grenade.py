import pygame, os
import constants as c
import player as pl


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
    
    def update(self, player):
        self.vel_y += c.GRAVITY  # gravity
        dx = self.speed * self.direction
        dy = self.vel_y
        
        
        #check collision with ground
        if self.rect.bottom + dy > c.GROUND: 
            dy = c.GROUND - self.rect.bottom
            self.speed = 0
            
        #update grenade position
        self.rect.x += dx
        self.rect.y += dy
        
        #countdown timer
        self.timer -= 1
        if self.timer <= 0: 
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, c.explosionScale)
            explosionGroup.add(explosion)
            #do damage to anyone nearby
            if abs(self.rect.centerx - player.rect.centerx) < c.TILESIZE * 2 and \
                abs(self.rect.centery - player.rect.centery) < c.TILESIZE * 2:
                    player.health -= c.EXPLOSION_DAMAGE
            for enemy in pl.enemyGroup:
                if abs(self.rect.centerx - enemy.rect.centerx) < c.TILESIZE * 2 and \
                    abs(self.rect.centery - enemy.rect.centery) < c.TILESIZE * 2:
                        enemy.health -= c.EXPLOSION_DAMAGE
                
                

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        
        for i in range(1, 6):
            img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'explosion', f'exp{i}.png')).convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.images.append(img)
        
        self.frameIndex = 0
        self.image = self.images[self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.timer = 50
        self.counter = 0
        
    def update(self):
        #update explosion animation
        self.counter += 1 
        if self.counter >= c.explosionSpeed: 
            self.counter = 0
            self.frameIndex += 1
            if self.frameIndex >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frameIndex]
        
explosionGroup = pygame.sprite.Group()        
grenadeGroup = pygame.sprite.Group()