import pygame, os
import constants as c
import player as pl

BACKGROUND = (0, 0, 0)
GREEN = (20, 255, 20)

STATS = {
    'player': {'x': 100, 'y': c.GROUND, 'scale': 5, 'speed': 6, 'ammo': 10, 'grenades': 10},
    'enemy': {'x': 500, 'y': c.GROUND, 'scale': 5, 'speed': 5, 'ammo': 10, 'grenades': 0},
    'enemy2': {'x': 600, 'y': c.GROUND, 'scale': 5, 'speed': 5, 'ammo': 10, 'grenades': 0}
}

def Init(stats = None):
    stats = stats or STATS
    pygame.init()
    clock = pygame.time.Clock()
    os.system(c.CLEAR)  # Clear terminal depending on OS
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    
    c.bulletImg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'bullet.png')).convert_alpha()
    c.grenadeImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'grenade.png')).convert_alpha()
    c.explosionImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'explosion', 'exp1.png')).convert_alpha()
    
    pygame.display.set_caption("Game Window")
    print(f"Game initialized with dimensions: {c.WIDTH}x{c.HEIGHT}")
    
    #(char_type, x, y, scale, speed, ammo, grenades) 
    player = pl.Player('player', **stats['player'])
    
    enemies = [
        pl.Player('enemy', **stats['enemy']),
        pl.Player('enemy', **stats['enemy2'])
    ]
    
    pl.enemyGroup.add(*enemies)
        
    drawBG(screen, BACKGROUND)
    return screen, enemies, player, clock

def drawBG(screen, BACKGROUND):
    screen.fill(BACKGROUND)
    pygame.draw.line(screen, GREEN, (0, c.GROUND), (c.WIDTH, c.GROUND))