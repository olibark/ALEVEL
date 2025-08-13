import pygame, os
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

    def update(self, player, enemyGroup):
        self.vel_y += c.GRAVITY  # gravity
        dx = self.speed * self.direction
        dy = self.vel_y

        # check collision with ground
        if self.rect.bottom + dy > c.GROUND:
            dy = c.GROUND - self.rect.bottom
            self.speed = 0

        # update grenade position
        self.rect.x += dx
        self.rect.y += dy

        # countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.centerx, self.rect.centery, c.explosionScale)
            explosionGroup.add(explosion)
            # NOTE: No damage here. Damage is handled by Explosion.update(...).


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        for i in range(1, 6):
            img = pygame.image.load(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'explosion', f'exp{i}.png')
            ).convert_alpha()
            img = pygame.transform.scale(
                img,
                (int(img.get_width() * scale), int(img.get_height() * scale))
            )
            self.images.append(img)

        self.frameIndex = 0
        self.image = self.images[self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.timer = 50
        self.counter = 0
        self.damageApplied = False

    def update(self, player, enemyGroup):
        # Apply damage once, at the start of the explosion
        if not self.damageApplied:
            if pygame.sprite.collide_rect(self, player) and getattr(player, "alive", True):
                player.health -= c.EXPLOSION_DAMAGE
            for enemy in enemyGroup:
                if pygame.sprite.collide_rect(self, enemy) and getattr(enemy, "alive", True):
                    enemy.health -= c.EXPLOSION_DAMAGE
            self.damageApplied = True

        # update explosion animation
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
