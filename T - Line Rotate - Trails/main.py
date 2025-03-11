import os
import pygame
import time
import random
import math

#Knob1 - linewidth
#Knob2 - direction
#Knob3 - trails
#Knob4 - foreground color
#Knob5 - background color

x21 = y21 = x2=y2=x3=y3=x11=y11=x1=y1=x4=y4=0
sound = 0

def setup(screen, eyesy) :
    global xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    

def draw(screen, eyesy) :
    global sound, xr, yr
    eyesy.color_picker_bg(eyesy.knob5)    
    if eyesy.trig :
        sound = (((2*eyesy.knob2-1)/10 + sound))

    a = math.pi*sound
    xc = xr/2
    yc = yr/2
    linewidth = int(xc - int(eyesy.knob1*(xc-1)))
    L1000 = int(xr * 0.781) #((1000*xr)/1280)
    L = eyesy.knob1*L1000 + linewidth
    if L > xr : L = xr
    
    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    if eyesy.knob2 < .5 :
        x21 = (L/2)*math.cos(a)
        y21 = (L/2)*math.sin(a)
        x2 = int(xc+x21)
        y2 = int(yc-y21)
        x3 = int(xc-x21)
        y3 = int(yc+y21)
        pygame.draw.line(screen, color, [x2,y2], [x3, y3], linewidth)
    
    if eyesy.knob2 > .5 :
        x11 = (L/2)*math.cos(a)
        y11 = (L/2)*math.sin(a)
        x1 = xc-x11
        y1 = yc+y11
        x4 = xc+x11
        y4 = yc-y11
        pygame.draw.line(screen, color, [x1,y1], [x4, y4], linewidth)
    
    #Trails
    veil = pygame.Surface((xr,yr))  
    veil.set_alpha(int(eyesy.knob3 * 200))
    veil.fill((eyesy.bg_color[0],eyesy.bg_color[1],eyesy.bg_color[2])) 
    screen.blit(veil, (0,0))
