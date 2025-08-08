import pygame
import os


CLEAR = 'cls' if os.name == 'nt' else 'clear'
WIDTH = 800
HEIGHT = 600
FPS = 60
running = True
movingLeft = False
movingRight = False
GRAVITY = 0.75
bulletImg = None
grenadeImage = None
shooting = False
grenading = False