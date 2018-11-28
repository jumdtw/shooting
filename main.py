import pygame 
import shooting
import menu

WIDTH  = 1024
HEIGHT = 648

pygame.init()
myclock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myMenu = menu.Menu(screen)

while True:
    myMenu.title()
    shooting.Shooting(screen)
    break

pygame.quit()


