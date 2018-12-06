import pygame 
import cwiid
import shooting_for_wii
import menu_for_wii
import option_for_wii

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

myfont = pygame.font.Font(None, 100)
imagetext = myfont.render("Connecting", True, (255,255,255))
screen.blit(imagetext,(WIDTH/2-200,HEIGHT/2))
pygame.display.flip()

wii = cwiid.Wiimote()
wii.rpt_mode = cwiid.RPT_BTN

myMenu = menu_for_wii.Menu(screen,wii)
myOption = option_for_wii.Option(screen,wii)
myShooting = shooting_for_wii.Shooting(screen,wii)
ReturnMenuFlag = 1
Game_option = [2,2]

while True:
    choices = myMenu.title()
    if choices == Choices["START"]:
        ReturnMenuFlag = myShooting.Main_Game(Game_option)
        if not ReturnMenuFlag:
            break
    if choices == Choices["OPTION"]:
        Game_option = myOption.option(Game_option)
        if not ReturnMenuFlag:
            break
    if choices == Choices["EXIT"]:
        break


    


pygame.quit()


