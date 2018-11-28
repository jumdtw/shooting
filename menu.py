import pygame
from pygame.locals import * 
WIDTH  = 1024
HEIGHT = 648
BLUE = (0,0,255)
RED = (255,0,0)

class Menu:
    
    def __init__(self,screen):
        pygame.init()
        self.SELECT = 0
        self.myclock = pygame.time.Clock()
        self.Screen = screen
        self.Screen.fill(BLUE)
        self.Titlefont = pygame.font.Font(None, 100)
        self.Selectfont = pygame.font.Font(None, 50)

    def title(self):
        endflag = 1
        pygame.init()
        imagetext = self.Titlefont.render("Shooting", True, RED)
        self.Screen.blit(imagetext,(WIDTH/2-200,HEIGHT/2))
        while endflag:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: endflag -= 1
                if event.type == KEYDOWN:
                    if event.key == K_SPACE: endflag -= 1
            self.myclock.tick(60)
            pygame.display.flip()
        return self.SELECT


