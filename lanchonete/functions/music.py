import pygame
from const.paths import PATH_MUSIC

def music():
    pygame.mixer.init()
    pygame.init()
    
    pygame.mixer_music.load(PATH_MUSIC)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)