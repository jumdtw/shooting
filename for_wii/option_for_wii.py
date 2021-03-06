import pygame
#KEYDOWNの定義など
from pygame.locals import * 
import random
import cwiid

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


option_list = ('Control','Level')
Game_option = []
#exsample
Option = {
    'Control':[0,'Control',2],
    'Level':[1,"Level",2],
}

class Option:
    
    def __init__(self,screen,wii):
        self.Option = {}
        self.Cursor = [0,[]]
        n = 0
        for option in option_list:
            #number name level
            self.Option[option] = [n,option,2]
            self.Cursor[1].append(2)
            n += 1
    
        pygame.init()
        self.Screen = screen
        self.SELECT = 0
        self.myclock = pygame.time.Clock()
        self.OptionName = pygame.font.Font(None, 80)
        self.Each_Option_level = pygame.font.Font(None, 70)
        self.wii = wii

    def option(self,return_Game_option):

        endflag = 1
        Game_option = {}
        #exsample
        option_selected = 0
        self.Cursor[0] = 0
        n = 0
        for option in option_list:
            self.Option[option] = [n,option,return_Game_option[n]]
            n+=1

        pygame.init()

        #timer 
        timer = 0

        #option画面にも星を描画
        stars = []
        for i in range(10):
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT -1)
            stars.append([x,y,2,2])

        while endflag:

            #縦
            if self.Cursor[0] < 0:
                self.Cursor[0] = len(option_list) - 1
            if self.Cursor[0] >= len(option_list):
                self.Cursor[0] = 0 

            #横
            for i in range(len(option_list)):
                if self.Cursor[1][i] <= 0:
                    self.Cursor[1][i] = 3
                elif self.Cursor[1][i] >= 4:
                    self.Cursor[1][i] = 1

            #level 
            if option_selected  < 0:
                option_selected = len(option_list) - 1
            elif option_selected >= len(option_list):
                option_selected = 0

           
            self.Screen.fill(BLACK)
            #星を描画
            for i in range(len(stars)):
                stars[i][1] = (stars[i][1] + i + 1) % HEIGHT
                pygame.draw.rect(self.Screen, WHITE, stars[i])

            
            #選択肢の文字列を描画
            x = 130
            y = 200

            for option in option_list:

                #Optionの状態変化
                if self.Option[option][0] == self.Cursor[0]:
                    self.Option[option][2] = self.Cursor[1][option_selected]
                
                if(self.Option[option][0]==self.Cursor[0]):
                    TEXTCOLOR = YELLOW
                else:
                    TEXTCOLOR = WHITE
                optionname = self.OptionName.render(self.Option[option][1]+':  ',True,TEXTCOLOR)
                self.Screen.blit(optionname,(x,y))

                #1 2 3 の描画
                x += 300 
                for i in range(3):

                    if( (i+1) == self.Option[option][2]):
                        TEXTCOLOR = RED
                    else:
                        TEXTCOLOR = WHITE

                    leveltext = self.Each_Option_level.render(str(i+1),True,TEXTCOLOR)
                    self.Screen.blit(leveltext,(x,y))
                    x += 200

                y += 200
                x = 130

            

            #キーイベント処理
            buttons = self.wii.state['buttons']
            if(buttons & cwiid.BTN_RIGHT and timer%8 == 0):
                self.Cursor[0] += 1
                option_selected += 1
            if(buttons & cwiid.BTN_LEFT and timer%8 == 0):
                self.Cursor[0] -= 1
                option_selected -= 1              
            if(buttons & cwiid.BTN_UP and timer%8 == 0):
                self.Cursor[1][option_selected] -= 1
            if(buttons & cwiid.BTN_DOWN and timer%8 == 0):
                self.Cursor[1][option_selected] += 1

            if(buttons & cwiid.BTN_2 and timer%8 == 0 and timer >= 30):
                endflag -= 1
                break

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.SELECT = Choices['EXIT']
                    endflag -= 1
             
            timer += 1

            self.myclock.tick(60)
            pygame.display.flip()

        Game_option = self.Cursor[1]
        return Game_option 
