import os
import random

import pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
screen_width, screen_heigth = info.current_w, info.current_h
window_width, window_heigth = screen_width-800, screen_heigth-150

timer = pygame.time.Clock()
fps = 60

pygame.display.set_caption('Classic Donkey Kong Rebuild')
#pygame.display.set_icon('imagem') pra colocar o icone


screen = pygame.display.set_mode([window_width, window_heigth])

