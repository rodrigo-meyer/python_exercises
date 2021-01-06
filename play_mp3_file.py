#Não funciona. Linguagem desatualizada entre 2017, 2020 e 2021.

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play()

input()
pygame.event.wait()
