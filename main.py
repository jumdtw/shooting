import pygame 
import shooting
#import menu

WIDTH  = 1024
HEIGHT = 648

screen = pygame.display.set_mode((WIDTH,HEIGHT))

while True:
    #menu.Menu(screen)
    shooting.Shooting(screen)

