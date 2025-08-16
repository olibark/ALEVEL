import pygame
import constants as c

def drawBG(screen, BACKGROUND):
    screen.fill(BACKGROUND)
    pygame.draw.line(screen, c.GREEN, (0, c.GROUND), (c.WIDTH, c.GROUND))
    
def drawText(text, colour, screen, x, y):
    textFont = c.textFont
    img = textFont.render(text, True, colour)
    screen.blit(img, (x, y))
    
class DrawHealthBar:
    def __init__(self, x, y, health, maxHealth, extraHealth, screen):
        self.x = x
        self.y = y
        self.health = health
        self.maxHealth = maxHealth
        self.extraHealth = extraHealth

    def draw(self, health, player, screen):
        # update current health
        self.health = health

        # draw background representing total possible health
        pygame.draw.rect(screen, c.RED, (self.x, self.y, self.maxHealth - 50, 20))

        # draw normal health in green (capped at 100)
        normal_health = min(self.health, 100)
        pygame.draw.rect(screen, c.GREEN, (self.x, self.y, normal_health, 20))

        # draw extra health in yellow appended to the bar
        extra_health = max(0, self.health - 100)
        if extra_health > 0:
            pygame.draw.rect(screen, c.YELLOW, (self.x + 100, self.y, extra_health, 20))

def drawBars(player, screen, healthBar):
    healthBar.draw(player.health, player, screen)
    
    drawText(f"Ammo: {player.ammo}", c.WHITE, screen, 10, 40)
    for i in range(player.ammo):
        screen.blit(c.bulletImage, (160 + (i * 10), 56))
        
    drawText(f"Grenades: {player.grenades}", c.WHITE, screen, 10, 70)
    for i in range(player.grenades):
        screen.blit(c.grenadeImage, (200 + (i * 10), 85))
        
