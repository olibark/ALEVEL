import pygame
import constants as c

textFont = c.textFont

def drawBG(screen, BACKGROUND):
    screen.fill(BACKGROUND)
    pygame.draw.line(screen, c.GREEN, (0, c.GROUND), (c.WIDTH, c.GROUND))
    
def drawText(text, colour, screen, x, y):
    textFont = c.textFont
    img = textFont.render(text, True, colour)
    screen.blit(img, (x, y))
    
def drawBars(player, enemyGroup, screen):
    drawText(f"Health: {player.health}", c.WHITE, screen, 10, 10)
    drawText(f"Ammo: {player.ammo}", c.WHITE, screen, 10, 30)
    drawText(f"Grenades: {player.grenades}", c.WHITE, screen, 10, 50)