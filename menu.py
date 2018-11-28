import pygame
from pygame.locals import * 
import random

WIDTH  = 1024
HEIGHT = 648
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
select = ['Start','Option','Exit']
class Menu:
    
    def __init__(self,screen):
        pygame.init()
        self.SELECT = 0
        self.myclock = pygame.time.Clock()
        self.Screen = screen
        self.Screen.fill(BLACK)
        self.Titlefont = pygame.font.Font(None, 100)
        self.Selectfont = pygame.font.Font(None, 50)

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

        while endflag:
            self.Screen.fill(BLACK)
            
            
            #星を描画
            for i in range(len(stars)):
                stars[i][1] = (stars[i][1] + i + 1) % HEIGHT
                pygame.draw.rect(self.Screen, WHITE, stars[i])

            #選択肢の文字列を描画
            y = 300
            for i in select:
                Selecttext = self.Selectfont.render(i,True,WHITE)
                self.Screen.blit(Selecttext,(400,y))
                y += 40

            #タイトル描画
            TITLEtext = self.Titlefont.render("Shooting", True, YELLOW)
            self.Screen.blit(TITLEtext,(WIDTH/2-200,HEIGHT/2-150)) 

            #キーイベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT: endflag -= 1
                if event.type == KEYDOWN:
                    if event.key == K_SPACE: endflag -= 1
                    if event.key == K_DOWN: endflag -= 1
                    if event.key == K_UP: endflag -= 1


            
            self.myclock.tick(60)
            pygame.display.flip()
        return self.SELECT


