import os
import pygame
import time
import random

#Knob1 - x position
#Knob2 - angle
#Knob3 - line width
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    pass

def draw(screen, eyesy):
    eyesy.color_picker_bg(eyesy.knob5)
    for i in range(0, 50) :
        seg(screen, eyesy, i)    

def seg(screen, eyesy, i) :
    
    color = eyesy.color_picker_lfo(eyesy.knob4)
    x0 = (int(eyesy.knob1*eyesy.xres))
    soundwidth = ((eyesy.audio_in[i] * eyesy.xres)/(eyesy.xres*35))
    x1 = x0 + soundwidth
    linespacing = eyesy.yres/50
    y = i * linespacing
    #newy = (0.8*eyesy.yres-(int(eyesy.knob2*1150*eyesy.yres/eyesy.yres)))
    newy = (0.8*eyesy.yres-(int(eyesy.knob2*(1.5972 * eyesy.yres))))  #1.5972
    linewratio = eyesy.xres * 0.016 #20*eyesy.xres/eyesy.xres
    linewidth = int(eyesy.knob3*linewratio)
  
    pygame.draw.line(screen, color, [x0, y +i], [x1, y+i+newy], 1+linewidth)
