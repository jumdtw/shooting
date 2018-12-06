import pygame
#KEYDOWNの定義など
from pygame.locals import * 
import random
import cwiid
import time

#rect 
WIDTH  = 1024
HEIGHT = 648

#color
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

#main menu choices
Choices = {
    'START':0,
    'OPTION':1,
    'EXIT':2,
}

select = {0:'Start',1:'Option',2:'Exit'}
class Menu:
    
    def __init__(self,screen,wii):
        pygame.init()
        self.SELECT = 0
        self.myclock = pygame.time.Clock()
        self.Screen = screen
        self.Titlefont = pygame.font.Font(None, 100)
        self.Selectfont = pygame.font.Font(None, 50)
        self.wii = wii

    def title(self):
        endflag = 1
        pygame.init()

        #0 start , 1 optino , 2 exit
        selectnum = 0
        #スタート画面にも星を描画
        stars = []
        for i in range(10):
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT -1)
            stars.append([x,y,2,2])

        #timer 
        timer = 0

        while endflag:
 
            if(selectnum >= 3):
                selectnum = 0
            elif(selectnum < 0):
                selectnum = 2

            self.Screen.fill(BLACK)
            #星を描画
            for i in range(len(stars)):
                stars[i][1] = (stars[i][1] + i + 1) % HEIGHT
                pygame.draw.rect(self.Screen, WHITE, stars[i])

            #選択肢の文字列を描画
            y = 300
            for i in range(len(select)):
                if(selectnum == i):
                    TEXTCOLOR = RED
                else:
                    TEXTCOLOR = WHITE
                Selecttext = self.Selectfont.render(select[i],True,TEXTCOLOR)
                self.Screen.blit(Selecttext,(460,y))
                y += 40

            #タイトル描画
            TITLEtext = self.Titlefont.render("Stars Wars", True, YELLOW)
            self.Screen.blit(TITLEtext,(WIDTH/2-140,HEIGHT/2-110)) 

            #キーイベント処理
            buttons = self.wii.state['buttons']
            if(buttons & cwiid.BTN_LEFT and timer%8 == 0):
                selectnum += 1
            elif(buttons & cwiid.BTN_RIGHT and timer%8 == 0):
                selectnum -= 1
            
            if(buttons & cwiid.BTN_2 and timer%8 == 0 and timer >= 30):
                self.SELECT = selectnum
                endflag -= 1
            
            timer += 1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.SELECT = Choices['EXIT']
                    endflag -= 1
          

            self.myclock.tick(60)
            pygame.display.flip()
        return selectnum


