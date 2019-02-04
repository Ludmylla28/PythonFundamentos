import pygame
pygame.mixer.init()
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.get_busy()