import pygame 
import shooting
import menu
import option

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
myOption = option.Option(screen)
myShooting = shooting.Shooting(screen)
ReturnMenuFlag = 1
Game_option = [2,2]
while True:

    choices = myMenu.title()
 
    if (choices == 1): print('1')
    if (choices == Choices["START"]):
        ReturnMenuFlag = myShooting.Main_Game(Game_option)
        if not ReturnMenuFlag:
            break
    elif(choices == 1):
        Game_option = myOption.option(Game_option)
        if not ReturnMenuFlag:
            break
    elif(choices == Choices["EXIT"]):
        break

    


pygame.quit()


