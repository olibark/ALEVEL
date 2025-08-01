import pygame
import os

WIDTH = 1000
HEIGHT = int(WIDTH * 0.75)
FPS = 60
running = True
movingLeft = False
movingRight = False
GRAVITY = 0.75
bulletImg = None
shooting = False