import pygame
import os

WIDTH = 800
HEIGHT = int(WIDTH * 0.75)
FPS = 60
running = True
movingLeft = False
movingRight = False
GRAVITY = 0.75
bulletImg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'bullet.png')).convert_alpha()
shoot = False