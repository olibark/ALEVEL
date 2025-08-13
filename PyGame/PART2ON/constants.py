import os

CLEAR = 'cls' if os.name == 'nt' else 'clear'
WIDTH = os.environ.get('WIDTH', 800)  # Default to 800 if not set
HEIGHT = os.environ.get('HEIGHT', 600)  # Default to 600 if not set
GRAVITY = 0.75
GROUND = 300
FPS = 60
TILESIZE = 40
EXPLOSION_DAMAGE = 50
WEAPON_COOLDOWN = 0.5 #seconds

running = True
movingLeft = False
movingRight = False
bulletImg = None
grenadeImage = None
explosionImage = None
shooting = False
grenading = False
grenadeThrown = False
explosionScale = 6
explosionSpeed = 7