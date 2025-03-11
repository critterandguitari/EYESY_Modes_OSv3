import os
import pygame
import time
import random
import math

# Knob1 - Square Size
# Knob2 - Shadow Control
# Knob3 - Y Position
# Knob4 - foreground color
# Knob5 - background color

def setup(screen, eyesy):
    global xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    
def draw(screen, eyesy):
    global xr, yr
    eyesy.color_picker_bg(eyesy.knob5)
    for i in range(0, 25) :
        seg(screen, eyesy, i)    

def seg(screen, eyesy, i) :
    global xr, yr

    x = int(eyesy.knob3*xr) + (eyesy.audio_in[i * 4] / 35)
    y = i * (yr * 0.0402)#i * ((29*yr)/yr)
    size125 = xr * 0.098 #((125*xr)/xr)
    squaresize = int(eyesy.knob1*size125)+1
    shad25 = xr * 0.020 #((25*xr)/xr)
    
    #Shadow Squares
    color = (0,0,0)
    pygame.draw.line(screen, color, [x + (shad25-int(eyesy.knob2*2*shad25)), y+(shad25-int(eyesy.knob2*2*shad25))], [x + (shad25-int(eyesy.knob2*2*shad25)), y+squaresize], squaresize)
    
    #Squares
    color = eyesy.color_picker_lfo(eyesy.knob4)
    pygame.draw.line(screen, color, [x, y], [x, y+squaresize], squaresize)
