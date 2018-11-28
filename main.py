import pygame 
import shooting
import menu

#rect
WIDTH  = 1024
HEIGHT = 648

#main menu choices
Choices = {
    'START':0,
    'OPTION':1,
    'EXIT':2,
}


pygame.init()
myclock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myMenu = menu.Menu(screen)
myShooting = shooting.Shooting(screen)
ReturnMenuFlag = 1

while True:
    choices = myMenu.title()
    if choices == Choices["START"]:
        ReturnMenuFlag = myShooting.Main_Game()
        continue
    elif choices == Choices["OPTION"]:
        ReturnMenuFlag = myShooting.Main_Game()
        continue
    elif choices == Choices["EXIT"]:
        break

    if not ReturnMenuFlag:
        break


pygame.quit()


