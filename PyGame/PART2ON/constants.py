import os, pygame

CLEAR = 'cls' if os.name == 'nt' else 'clear'
WIDTH = os.environ.get('WIDTH', 800)  # Default to 800 if not set
HEIGHT = os.environ.get('HEIGHT', 600)  # Default to 600 if not set
GRAVITY = 0.75
GROUND = 300
FPS = 60
TILESIZE = 40
EXPLOSION_DAMAGE = 50
WEAPON_COOLDOWN = 0.5 #seconds
BACKGROUND = (0, 0, 0)
GREEN = (20, 255, 20)

textFont = pygame.font.SysFont('Futura', 30)

running = True
movingLeft = False

movingRight = False
bulletImg = None
grenadeImage = None
explosionImage = None
ammoBoxImage = None
grenadeBoxImage = None
healthBoxImage = None

shooting = False
grenading = False
grenadeThrown = False
explosionScale = 4
explosionSpeed = 7

itemBoxes = {
    'ammo': ammoBoxImage, 
    'grenade': grenadeBoxImage,
    'health': healthBoxImage
}

MAX_HEALTH = 150
MAX_AMMO = 40
MAX_GRENADES = 10