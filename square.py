import sys
import time
import pygame
import random


SCREENSIZEX = 1000 # размеры окна
SCREENSIZEY = 600

window = pygame.display.set_mode((SCREENSIZEX, SCREENSIZEY + 30))
pygame.display.set_caption('Футбол') # Изначально был теннис
screen = pygame.Surface((SCREENSIZEX, SCREENSIZEY)) # размеры рабочей поверхности
info_string = pygame.Surface((SCREENSIZEX, 30)) # инфо 
pygame.font.init() # шрифт
inf_font = pygame.font.SysFont('Comic Sans MS', 24, True)

# созднание объектов
class Sprite: 
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))

# столкновение        
def Intersect(x1, x2, y1, y2, sizex, sizey):
    if (x1 > x2-sizex) and (x1 < x2+sizex) and (y1 > y2-sizey) and (y1 < y2+sizey):
        return 1 
    else:
        return 0

ball = Sprite(350, 200, 'images/h1.png')
ball.up = True
ball.right = True
ball.step = 0
zet = Sprite(20, 0, 'images/z.png')
zet.up = True
zet2 = Sprite(SCREENSIZEX - 40, 0, 'images/z1.png')
zet2.step = 0
counter1 = 0
counter2 = 0
rchoice = [0.2, 0.3]
board1 = Sprite(0, 0, 'images/board1.png')
board2 = Sprite(SCREENSIZEX - 10, 0, 'images/board2.png')
pygame.mouse.set_visible(False) # отключаем курсор
square = pygame.Surface((15, SCREENSIZEY))
square.fill((255, 255, 255))
circle = pygame.draw.circle(screen, (255, 255, 255), (500, 300), 150, 40)

done = True
while done:
    for e in pygame.event.get(): #выход
        if e.type == pygame.QUIT:
            done = False
            sys.exit()
            
        if e.type == pygame.MOUSEMOTION: #движение мышью
            m = pygame.mouse.get_pos()
            if m[1] > 0  and m[1] < SCREENSIZEY - 70:
                zet.y = m[1]

#Столкновения с краем окна
    if ball.right == True:
        ball.x -= 1.6 - (ball.step*-1)
        if ball.x <= 0:
            ball.right = False
            counter2 += 1
            time.sleep(1)
            zet2.step = 0
            ball.step = 0
    else:
        ball.x += 1.6 + ball.step
        if ball.x >= SCREENSIZEX - 40:
            ball.right = True
            counter1 += 1
            time.sleep(1)
            zet2.step = 0
            ball.step = 0
            
    if ball.up == True:
        ball.y -= 1.6 - (ball.step*-1)
        if ball.y <= 0:
            ball.up = False
    else:
        ball.y += 1.6 + ball.step
        if ball.y >= SCREENSIZEY - 40:
            ball.up = True

    if zet2.y <= 0:
        zet2.y +=1
    elif zet2.y < ball.y - 35:
        zet2.y += 1.6 + zet2.step
    else:
        zet2.y -= 1.6 + zet2.step


##столкновения с объектами          
    if Intersect(zet.x, ball.x, zet.y, ball.y, 20, 70) == True:
        ball.right = False
        ball.step +=0.3
        if zet2.step <=2.8:
            zet2.step+=0.3
        elif zet2.step > 2.8:
            zet2.step+=random.choice(rchoice)
        

    if Intersect(ball.x, zet2.x, ball.y, zet2.y, 40, 40) == True:
        ball.right = True
        ball.step +=0.3
        if zet2.step <=2.8:
            zet2.step+=0.3
        elif zet2.step > 2.8:
            zet2.step+=random.choice(rchoice)

    
    screen.fill((45, 80, 40))
    info_string.fill((30, 90, 150))
    screen.blit(square, (SCREENSIZEX/2 - 5, 0))
    pygame.draw.circle(screen, (255, 255, 255), [500, 300], 180, 15)
    board1.render()
    board2.render()
    zet.render()
    zet2.render()
    ball.render()
    info_string.blit(inf_font.render('СЧЕТ   ' + str(counter1) + ' : ' + str(counter2), 1, (180, 80, 10)), (400, 0))
    window.blit(info_string, (0, 0))
    window.blit(screen, (0,30))
    pygame.display.flip()
