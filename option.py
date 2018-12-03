import pygame
#KEYDOWNの定義など
from pygame.locals import * 
import random

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
    
    def __init__(self,screen):
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

    def option(self):

        endflag = 1
        Game_option = {}
        #exsample
        Cursor = [0,[2,2]]
        option_selected = 0

        for option in option_list:
            self.Option[option][2] = 2

        pygame.init()

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

            print(str(self.Cursor) + str(option_selected))
           
            self.Screen.fill(BLACK)
            #星を描画
            for i in range(len(stars)):
                stars[i][1] = (stars[i][1] + i + 1) % HEIGHT
                pygame.draw.rect(self.Screen, WHITE, stars[i])

            #選択肢の文字列を描画
            x = 130
            y = 200

            for option in option_list:

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.SELECT = Choices['EXIT']
                    endflag -= 1
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT: 
                        self.Cursor[1][option_selected] += 1
                    if event.key == K_LEFT:
                        self.Cursor[1][option_selected] -= 1
                    if event.key == K_DOWN:
                        self.Cursor[0] += 1
                        option_selected += 1
                    if event.key == K_UP:
                        self.Cursor[0] -= 1
                        option_selected -= 1

                    if event.key == K_SPACE:
                        endflag -= 1
                        break
            
            #print(str(self.Cursor) + str(option_selected))
            
            self.myclock.tick(60)
            pygame.display.flip()

        Game_option = Cursor[1]
        return Game_option 
