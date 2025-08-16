import pygame, os
import constants as c
import player as pl
import items as it
import background as bg

STATS = {
    'player': {'x': 100, 'y': c.GROUND, 'scale': 5, 'speed': 6, 'ammo': 20, 'grenades': 10},
    'enemy': {'x': 500, 'y': c.GROUND, 'scale': 5, 'speed': 5, 'ammo': 10, 'grenades': 0},
    'enemy2': {'x': 600, 'y': c.GROUND, 'scale': 5, 'speed': 5, 'ammo': 10, 'grenades': 0}
}

def Init(stats = None):
    stats = stats or STATS
    pygame.init()
    clock = pygame.time.Clock()
    # Initialize fonts now that pygame is ready
    c.textFont = pygame.font.SysFont('Futura', 30)
    os.system(c.CLEAR)  # Clear terminal depending on OS
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    
    c.bulletImg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'bullet.png')).convert_alpha()
    c.grenadeImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'grenade.png')).convert_alpha()
    c.explosionImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'explosion', 'exp1.png')).convert_alpha()
    c.ammoBoxImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'ammo_box.png')).convert_alpha()
    c.grenadeBoxImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'grenade_box.png')).convert_alpha()
    c.healthBoxImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'icons', 'health_box.png')).convert_alpha()
    
    c.itemBoxes = {
        'ammo': c.ammoBoxImage,
        'grenade': c.grenadeBoxImage,
        'health': c.healthBoxImage,
    }
    
    pygame.display.set_caption("Shooter")
    print(f"Game initialized with dimensions: {c.WIDTH}x{c.HEIGHT}")
    
    #(char_type, x, y, scale, speed, ammo, grenades) 
    player = pl.Player('player', **stats['player'])
    
    itemBox = it.Item('health', 100, c.GROUND - 40, player)
    it.itemBoxGroup.add(itemBox)
    itemBox = it.Item('ammo', 200, c.GROUND - 40, player)
    it.itemBoxGroup.add(itemBox)
    itemBox = it.Item('grenade', 300, c.GROUND - 40, player)
    it.itemBoxGroup.add(itemBox)
    itemBox = it.Item('health', 400, c.GROUND - 40, player)
    it.itemBoxGroup.add(itemBox)
    
    enemies = [
        pl.Player('enemy', **stats['enemy']),
        pl.Player('enemy', **stats['enemy2'])
    ]

    pl.enemyGroup.add(*enemies)

    bg.drawBG(screen, c.BACKGROUND)
    
    return screen, pl.enemyGroup, player, clock

