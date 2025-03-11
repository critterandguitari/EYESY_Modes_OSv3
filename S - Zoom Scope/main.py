import os
import pygame
import math
import time

#Knob1 - scope points
#Knob2 - scope x position
#Knob3 - scope y position
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy) :
    global xr,yr,f,x2
    xr = eyesy.xres
    yr = eyesy.yres
    x2 = int(xr * 0.00156)#int((2*xr)/xr)
    if x2 <= 1 : x2 = 1
    f=2

def draw(screen, eyesy) :
    global xr,yr,f
    eyesy.color_picker_bg(eyesy.knob5)
    f = int(eyesy.knob1 * 94)+6
    for i in range(0, f) :
        seg(screen, eyesy, i)    

def seg(screen, eyesy, i) :
    global xr,yr,f,x2
    
    s1 = int((eyesy.audio_in[i]*0.00003058)*(yr/2))
    xs = int(xr/(f-4))
    
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.003)
    
    offx = int((eyesy.knob2 * xr)-(xr/2)) 
    offy = int(eyesy.knob3 * yr)
    
    pygame.draw.circle(screen,color,((i*xs)+offx, offy+s1),(5*xr)/xr, 0)
    pygame.draw.line(screen, color, [(i*xs)+offx, offy], [(i*xs)+offx, s1+offy], x2)
