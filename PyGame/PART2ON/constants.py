import os

CLEAR = 'cls' if os.name == 'nt' else 'clear'
WIDTH = os.environ.get('WIDTH', 800)  # Default to 800 if not set
HEIGHT = os.environ.get('HEIGHT', 600)  # Default to 600 if not set

FPS = 60
running = True
movingLeft = False
movingRight = False
GRAVITY = 0.75
bulletImg = None
grenadeImage = None
shooting = False
grenading = False


