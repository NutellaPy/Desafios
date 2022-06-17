# Crie um script q toque um arquivo mp3 
import pygame
pygame.mixer.init()
pygame.mixer.music.load('e021.wav')
pygame.mixer.music.play()
input()

