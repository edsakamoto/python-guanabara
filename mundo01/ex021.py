#programa python que abra e reproduza audio de um arquivo de mp3

import pygame
pygame.init()
pygame.mixer.music.load('teste.mp3') #nome do arquivo do mp3
pygame.mixer.music.play()
pygame.event.wait()


