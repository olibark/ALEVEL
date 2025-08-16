import os



CLEAR = 'cls' if os.name == 'nt' else 'clear'
WIDTH = 800
HEIGHT = 600  
GRAVITY = 0.75
GROUND = 300
FPS = 60
TILESIZE = 40
EXPLOSION_DAMAGE = 50
WEAPON_COOLDOWN = 0.5 #seconds
BACKGROUND = (0, 0, 0)
GREEN = (20, 255, 20)
WHITE = (255, 255, 255)
RED = (230, 20, 20)
YELLOW = (255, 255, 0)

# Font placeholder; initialized after pygame.init()
textFont = None

running = True
movingLeft = False

movingRight = False
bulletImage = None
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