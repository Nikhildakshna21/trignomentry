import pygame
import math
import time



pygame.init()

screen = pygame.display.set_mode((1300,673))

pygame.display.set_caption('legend of infinity fighters')

running = True
x=0
y=0

cx=0
cy=0

orbitr=75
orbitrinc = 0

mx,my=(0,0)   
vx,vy=(0.035,0.035)

ox,oy=(0,0)

trail = []

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    orbitrinc = 1
                elif event.button == 3:
                    orbitrinc = -1
        if event.type==pygame.MOUSEBUTTONUP:
            orbitrinc = 0

    if pygame.time.get_ticks()%5==0:
        mx,my=pygame.mouse.get_pos()
        x+=0.7/vx
        y+=0.7/vy
        cx+=math.sin(math.atan2(mx-cx,my-cy))/2
        cy+=math.cos(math.atan2(mx-cx,my-cy))/2
        vx = math.sqrt(((ox-cx)**2)+((oy-cy)**2))
        vy = math.sqrt(((ox-cx)**2)+((oy-cy)**2))
        #print(0.5/vx)
    orbitr+=(orbitrinc/10)
    ox=cx+(math.sin(x)*(orbitr))
    oy=cy-(math.cos(y)*(orbitr))
    screen.fill((130,130,130)) 
    pygame.draw.circle(screen,(0,0,0),(cx,cy),30)
    pygame.draw.circle(screen,(142,242,120),(ox,oy),25)
    #pygame.draw.circle(screen,(0,0,0),(mx,my),orbitr,1)
    #pygame.draw.line(screen,(0,0,0),(cx,cy),(ox,oy))

 