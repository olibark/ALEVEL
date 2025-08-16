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