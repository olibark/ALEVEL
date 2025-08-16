import pygame, random, os
import constants as c
import bullet as b
class Player(pygame.sprite.Sprite): 
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        
        BASE = os.path.dirname(os.path.abspath(__file__))
        
        self.alive = True
        self.health = 100
        
        self.speed = speed
        self.char_type = char_type
        self.movingLeft = False
        self.movingRight = False
        self.jump = False
        self.inAir = True
        self.RUNNING = 1
        self.IDLE = 0
        self.velY = 0
        self.startScale = scale
        self.scale = scale
        self.direction = 1 if char_type == 'player' else random.choice([-1, 1])
        
        self.extraHealth = False
        self.maxHealth = c.MAX_HEALTH
        self.maxGrenades = c.MAX_GRENADES
        self.maxAmmo = c.MAX_AMMO
        self.shotCooldown = c.WEAPON_COOLDOWN
        
        self.grenades = grenades
        self.ammo = ammo
        self.start_ammo = ammo
        
        self.flip = False
        self.animationList = []
        self.frameIndex = 0
        self.action = 0
        self.updateTime = pygame.time.get_ticks()
        
        #load all images for players
        animationTypes = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animationTypes:
            tempList = []
            #count num of frames in each animation
            frames = len(os.listdir(os.path.join(BASE, 'img', self.char_type, animation)))
            for i in range(frames):
                img = pygame.image.load(os.path.join(
                    BASE, 'img', (f'{self.char_type}'), (f'{animation}'), f'{i}.png')
                    ).convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                tempList.append(img)
            self.animationList.append(tempList)
                
        self.image = self.animationList[self.action][self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        
    def move(self, screen):
        #reset movement variables
        dx = 0
        dy = 0
        
        if self.movingLeft:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        
        if self.movingRight:
            dx = self.speed
            self.flip = False
            self.direction = 1
        
        if self.jump and self.inAir == False:
            self.velY = -11
            self.jump = False
            self.inAir = True
        
        #add gravity
        self.velY += c.GRAVITY
        if self.velY > 10:  # limit falling speed
            self.velY
        dy += self.velY    
        
        #check collision with ground
        if self.rect.bottom + dy > c.GROUND: 
            dy = c.GROUND - self.rect.bottom
            self.inAir = False
            
        self.rect.x += dx
        self.rect.y += dy
        
        # Ensure player stays within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
    
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        #draw rect
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
    
    def setScale(self, scale):
        
        BASE = os.path.dirname(os.path.abspath(__file__))
        self.scale = scale
        self.animationList = []

        animationTypes = ['Idle', 'Run', 'Jump', 'Death']
        for action_name in animationTypes:
            tempList = []
            action_path = os.path.join(BASE, 'img', self.char_type, action_name)

            if not os.path.exists(action_path):
                print(f"Warning: {action_path} not found.")
                self.animationList.append(tempList)
                continue

            frame_count = len(os.listdir(action_path))
            for i in range(frame_count):
                img_path = os.path.join(action_path, f'{i}.png')
                img = pygame.image.load(img_path).convert_alpha()
                img = pygame.transform.scale(
                    img,
                    (int(img.get_width() * scale),
                    int(img.get_height() * scale)))
                tempList.append(img)

            self.animationList.append(tempList)

        # Safely restore image, keep current action/frame if possible
        self.frameIndex = min(self.frameIndex, len(self.animationList[self.action]) - 1)
        self.image = self.animationList[self.action][self.frameIndex]
        
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

        # Clamp to screen width
        screen_width = 800
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width


    def updateAnimation(self):
    # Update animation
        cooldown = 100
        self.image = self.animationList[self.action][self.frameIndex]
        
        if (pygame.time.get_ticks() - self.updateTime) > cooldown:
            self.updateTime = pygame.time.get_ticks()
            if self.action == 3:  # 3 = Death
                if self.frameIndex < len(self.animationList[self.action]) - 1:
                    self.frameIndex += 1  # Do not loop
            else:
                self.frameIndex += 1
                if self.frameIndex >= len(self.animationList[self.action]):
                    self.frameIndex = 0

            
    def updateAction(self, newAction):
        if newAction != self.action:
            self.action = newAction
            self.frameIndex = 0
            self.updateTime = pygame.time.get_ticks()
            
    def shoot(self):
        if self.shotCooldown <= 0 and self.ammo > 0:
            self.shotCooldown = c.WEAPON_COOLDOWN
            bullet = b.Bullet(
                self.rect.centerx + (0.6 * self.rect.size[0] * self.direction),
                self.rect.centery,
                self.direction, 
                self)
            b.playerBulletGroup.add(bullet)
            self.ammo -= 1 
    
    def update(self):
        self.checkAlive()
        self.updateAnimation()
        #update cooldown
        if self.shotCooldown > 0:
            self.shotCooldown -= 1
            
    def checkAlive(self):
        if self.health <= 0:
            self.alive = False
            self.health = 0
            self.speed = 0
            self.updateAction(3) #3 = death
        if self.health > 100:
            self.extraHealth = True
        else:
            self.extraHealth = False
            
    def ai(self, player, screen):
        if self.alive and player.alive:
            if self.direction == 1:
                aiMovingRight = True
            else: 
                aiMovingRight = False
            aiMovingLeft = not aiMovingRight #opposites
            self.move(screen)
enemyGroup = pygame.sprite.Group()
