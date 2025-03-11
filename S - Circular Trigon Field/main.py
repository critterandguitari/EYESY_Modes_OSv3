import os
import pygame
import time
import random
import math
import pygame.gfxdraw

#Knob1 - diameter/radius
#Knob2 - second point position
#Knob3 - third point position
#Knob4 - foreground color
#Knob5 - background color

note_down = False
lx = 0
ly = 0

def setup(screen, eyesy):
    global xr, yr
    xr = eyesy.xres
    yr = eyesy.yres

def draw(screen, eyesy):
    eyesy.color_picker_bg(eyesy.knob5)
    for i in range(0, 50) :
        seg(screen, eyesy, i)    

def seg(screen, eyesy, i) :
    global lx, ly, xr, yr
    
    
    x200 = xr * 0.156 #((200*xr)/eyesy.xres)
    x640 = xr * 0.5 #((640*xr)/eyesy.xres)
    x960 = xr * 0.75 #((960*xr)/eyesy.xres)
    x800 = xr * 0.625 #((800*xr)/eyesy.xres)
    xran = int(xr * 0.0609) # ((78*xr)/eyesy.xres)
    
    y260 = yr * 0.44    #0.361#((260*yr)/eyesy.yres)
    color = eyesy.color_picker_lfo(eyesy.knob4)
    R = int(eyesy.knob1 * x800)
    R = R + (eyesy.audio_in[i] / 100)
    x = R * math.cos((i /  50.) * 6.28) + x640
    y = R * math.sin((i /  50.) * 6.28) + y260
    
    if ((i % 2)) :
        pygame.gfxdraw.filled_trigon(screen, int(x), int(y), int(x) + int(eyesy.knob2*x200) + random.randrange(0,xran), int(y) + int(eyesy.knob2*x200), int(x) - int(eyesy.knob3*x200), int(y) + int(eyesy.knob3*x200), color)
    else :
        outline = (random.randrange(0,100))*.01
        color = eyesy.color_picker(outline)
        pygame.gfxdraw.trigon(screen, int(x), int(y), int(x) + int(eyesy.knob2*x200) + random.randrange(0,xran), int(y) + int(eyesy.knob2*x200), int(x) - int(eyesy.knob3*x200), int(y) + int(eyesy.knob3*x200), color)
