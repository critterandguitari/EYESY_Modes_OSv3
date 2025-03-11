import os
import pygame
import random
import pygame.gfxdraw

#Knob1 - how complex shape is
#Knob2 - number of cousins
#Knob3 - space between cousins & alpha channel
#Knob4 - foreground colorkn
#Knob5 - background color

def setup(screen, eyesy):
    global pOints, trigger, pointNumber, pOints1, xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    x640 = int(xr * 0.5) #int((640*xr)/1280)
    x45 = int(xr * 0.035) #int((45*xr)/1280)
    x760 = int(xr * 0.593) #int((760*xr)/1280)
    x90 = int(xr * 0.07) #int((90*xr)/1280)
    pointNumber = 20
    pOints = [(random.randrange(0,int(xr*0.938)), random.randrange(0,int(yr*0.833))) for i in range(1, pointNumber)]
    trigger = False
    pOints.append(pOints[0])
    pOints1 = [(x640,x640), (x45,x760), (x90,x90)]

def draw(screen, eyesy):
    
    global pOints, trigger, pointNumber, pOints1, xr, yr
    eyesy.color_picker_bg(eyesy.knob5) 
    number = int(eyesy.knob2*5)
    smooth = 6
    place = int(eyesy.knob3*(xr * 0.14)) +10
    
    pOints1 = [(pOints[i][0] - place, pOints[i][1] - place) for i in range(1,pointNumber)]
    pOints1.append(pOints1[0])
    
    pOints2 = [(pOints1[i][0] + place+(place/4), pOints1[i][1] + place+(place/4)) for i in range(1,pointNumber)]
    pOints2.append(pOints2[0])
    
    pOints3 = [(pOints2[i][0] + place+(place/2), pOints2[i][1] - place+(place/2)) for i in range(1,pointNumber)]
    pOints3.append(pOints3[0])
    
    pOints4 = [(pOints3[i][0] - place+(place/1), pOints3[i][1] + place+(place/1)) for i in range(1,pointNumber)]
    pOints4.append(pOints4[0])
    
    
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.1)
    if eyesy.trig :
        trigger = True
        
    if trigger == True :
        pointNumber = int(eyesy.knob1*16)+4
        pOints = [(random.randrange(20,int(xr*0.97)), random.randrange(20,int(yr*0.95))) for i in range(1,pointNumber)]
        pOints.append(pOints[0])
        pOints1 = [(pOints[i][0] + place, pOints[i][1] + place) for i in range(1,pointNumber)]
        pOints1.append(pOints1[0])
        
    trigger = False
    
    pygame.gfxdraw.bezier(screen, pOints, smooth, color)
    if number>1 : 
        pygame.gfxdraw.bezier(screen, pOints1, smooth, color)
    if number>2 : 
        pygame.gfxdraw.bezier(screen, pOints2, smooth, color)
    if number>3 :
        pygame.gfxdraw.bezier(screen, pOints3, smooth, color)
    if number>4 :
        pygame.gfxdraw.bezier(screen, pOints4, smooth, color)
    
    
   #Trails
    veil = pygame.Surface((xr,yr))  
    veil.set_alpha(int(eyesy.knob3 * 20))
    veil.fill((eyesy.bg_color[0],eyesy.bg_color[1],eyesy.bg_color[2])) 
    screen.blit(veil, (0,0))
