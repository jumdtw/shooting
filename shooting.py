#shooting game 
import pygame
import math
import random
from pygame.locals import * 

WIDTH = 1024
HEIGHT = 648
BLACK = (0,0,0)
WHITE = (255,255,255)
OUTSIDE = 9999

CREDIT = 3

#スプライトクラス
class Shooting:

    def __init__(self,screen):
        self.Screen = screen

    def Main_Game(self):
        class Spclass(pygame.sprite.Sprite):
            def __init__(self, x, y, angle, num):
                pygame.sprite.Sprite.__init__(self)
                tempimage = pygame.transform.rotate(charas[num].image, -angle)
                self.image = tempimage
                self.rect = self.image.get_rect() 
                self.rect.centerx = x
                self.rect.centery = y
                self.angle = angle
                self.hp = charas[num].hp
                self.enemy = charas[num].enemy
                self.time = 0

        #爆発クラス
        class Explosion(Spclass):
            def update(self):
                if self.time > 10:
                    self.rect.centerx = OUTSIDE

        #自弾クラス
        class Shot(Spclass):
            def update(self):
                self.rect.centery -= 8
                #当たり判定
                hitlist = pygame.sprite.spritecollide(self,allgroup,False)
                for sp in hitlist:
                    if sp.enemy == False or sp.hp == 99: continue
                    self.rect.centerx = OUTSIDE
                    sp.hp -= 1
                    break

        #敵弾クラス
        class Fireball(Spclass):
            def update(self):
                rad = math.radians(self.angle - 90)
                self.rect.centerx += (math.cos(rad)) * 4
                self.rect.centery += (math.sin(rad)) * 4

        #自機クラス
        class Player(Spclass):
            Score = 0
            Credit = CREDIT
            def update(self):
                #移動処理
                press = pygame.key.get_pressed()
                if(press[pygame.K_UP]):
                    self.rect.centery -= 4
                if(press[pygame.K_DOWN]):
                    self.rect.centery += 4              
                if(press[pygame.K_LEFT]):
                    self.rect.centerx -= 4
                if(press[pygame.K_RIGHT]):
                    self.rect.centerx += 4

                
                #センタリング
                if(self.rect.centerx < 16):
                    self.rect.centerx = 16
                if(self.rect.centery < 16):
                    self.rect.centery = 16
                if(self.rect.centerx > WIDTH - 16):
                    self.rect.centerx = WIDTH - 16
                if(self.rect.centery > HEIGHT - 16):
                    self.rect.centery = HEIGHT - 16

                press = pygame.key.get_pressed()
                if(press[pygame.K_SPACE] != 0)  and (self.time % 10 == 0) and (self.time > 3)   :
                    newsp = Shot(self.rect.centerx,self.rect.centery,0,1)
                    allgroup.add(newsp)
                hitlist  = pygame.sprite.spritecollide(self, allgroup, False)
                for sp in hitlist:
                    if sp.enemy == True:
                        if(sp.hp == 99):
                            self.hp -= 1
                            sp.rect.centerx = OUTSIDE
                        else:
                            self.hp -= 1
                            sp.hp -= 1 
                            break

        #enemy
        class Fighter(Spclass):

            def update(self):
                #ジグザグ
                self.rect.centery += 2
                self.rect.centerx += int((self.time % 200 ) / 100 ) * 2 - 1

                if allgroup.has(player) == 0 or random.randint(0, 100) != 0: return 
                dx = player.rect.centerx - self.rect.centerx
                dy = player.rect.centery - self.rect.centery
                angle = math.degrees(math.atan2(dy,dx)) + 90
                newsp = Fireball(self.rect.centerx, self.rect.centery, angle, 2)
                allgroup.add(newsp)

        class Boss(Spclass):
            def update(self):
                if(self.time < 100):
                    self.rect.centery += 1
                    return 
                rad = math.radians(self.time - 100)
                self.rect.centerx = (WIDTH/2) + (math.sin(rad) * 300)
                if(self.time % 3 ==0):
                    angle = (self.time * 17) % 360
                    newsp = Fireball(self.rect.centerx, self.rect.centery, angle, 2)
                    allgroup.add(newsp)

        class Characlass:
            def __init__(self,filename,hp,enemy):
                self.image = pygame.image.load(filename).convert()
                colorkey = self.image.get_at((0,0))
                self.image.set_colorkey(colorkey)
                self.hp = hp 
                self.enemy = enemy



        pygame.init()
        #screen = pygame.display.set_mode((WIDTH,HEIGHT))
        myfont = pygame.font.Font(None, 100)
        mifont = pygame.font.Font(None,35)
        myclock = pygame.time.Clock()
        charas = []
        charas.append(Characlass('./image/explobe.png',100,False))
        charas.append(Characlass('./image/chr_hero.png',1,False))
        charas.append(Characlass('./image/chr_enemy.png',99,True))
        charas.append(Characlass('./image/hero.png',1,False))
        charas.append(Characlass('./image/ME_sub.png',1,True))
        charas.append(Characlass('./image/ME_BOSS.png',30,True))
        charas.append(Characlass('./image/None_hero.png',100,False))

        stars = []
        CREDITimage = pygame.image.load('./image/Small_hero.png').convert()
        ReturnMenuFlag = 0
        for i in range(10):
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT -1)
            stars.append([x,y,2,2])

        allgroup = pygame.sprite.Group()
        endflag = 0
        while endflag == 0:
            allgroup.empty()
            player = Player(WIDTH/2, HEIGHT*3/4, 0, 3)
            allgroup.add(player)
            bosstimer = 60 * 20
            gameover = 0
            continueTime = 0
            ContinueFlag = 0
            while endflag ==0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        ReturnMenuFlag = 0
                        endflag -= 1
                        break
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            ReturnMenuFlag = 1
                            endflag -= 1
                            break
                self.Screen.fill(BLACK)
                for i in range(len(stars)):
                    stars[i][1] = (stars[i][1] + i + 1) % HEIGHT
                    pygame.draw.rect(self.Screen, WHITE, stars[i])
                bosstimer -= 1
                if bosstimer == 0:
                    boss = Boss(WIDTH/2,0,0,5)
                    allgroup.add(boss) 
                elif bosstimer < 0:
                    if allgroup.has(boss)==0:bosstimer=60*20
                #enemy 
                elif random.randint(0,45) == 0:
                    x = random.randint(0,WIDTH - 200) + 100
                    newsp = Fighter(x,0,180,4)
                    allgroup.add(newsp)

                #Scoreの描画
                score = player.Score
                imageScore = mifont.render(str(score),True,WHITE)
                self.Screen.blit(imageScore,(20,20))
                allgroup.update()
                #Creditの描画
                x = 20
                for credit in range(player.Credit):
                    self.Screen.blit(CREDITimage,(x,50))
                    x += 20

                for sp in allgroup.sprites():
                    sp.time += 1
                    x = sp.rect.centerx
                    y = sp.rect.centery
                    if sp.hp <= 0:
                        if(sp.enemy is True):
                            player.Score += 100
                        if(sp == player):
                            ContinueFlag = 1
                            sp.hp = 1
                            player.Credit -= 1
                        else:
                            allgroup.remove(sp)
                            newsp = Explosion(x,y,0,0)
                            allgroup.add(newsp)
                    if x<0 or x>WIDTH or y<0 or y>HEIGHT:
                        allgroup.remove(sp)
                
                #player点滅
                if ContinueFlag:
                    if (player.time % 5 == 0):
                        player.image = pygame.transform.rotate(charas[6].image, 0)
                    else:
                        player.image = pygame.transform.rotate(charas[3].image, 0)
                    continueTime += 1
                    if continueTime >= 100:
                        ContinueFlag = 0
                        continueTime = 0
                        player.image = pygame.transform.rotate(charas[3].image, 0)
                
                #スプライトの画像を描画
                allgroup.draw(self.Screen)
                #ガメオベラ処理
                if player.Credit == 0:
                    for sp in allgroup.sprites():
                        if sp == player:
                            x = sp.rect.centerx
                            y = sp.rect.centery
                            allgroup.remove(sp)
                            newsp = Explosion(x,y,0,0)
                            allgroup.add(newsp)

                    imagetext = myfont.render("Game Over", True, WHITE)
                    self.Screen.blit(imagetext,(WIDTH/2-200,HEIGHT/2))
                    gameover += 1
                    if gameover >= 120: 
                        endflag -= 1
                        ReturnMenuFlag = 1     

                #60fps
                myclock.tick(60)
                #画面更新
                pygame.display.flip()
        return ReturnMenuFlag

                