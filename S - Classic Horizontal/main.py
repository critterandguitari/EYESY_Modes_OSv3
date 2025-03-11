import os
import pygame
import math
import time

#Knob1 - line width
#Knob2 - circle size
#Knob3 - height control
#Knob4 - foreground color
#Knob5 - background color

lines = 100

def setup(screen,eyesy) :
    pass

def draw(screen, eyesy):
    eyesy.color_picker_bg(eyesy.knob5)
    for i in range(0, lines) :
        seg(screen, eyesy, i)
        
def seg(screen, eyesy, i) :
    
    space = eyesy.xres/(lines-2)
    y0 = 0
    y1 = (eyesy.audio_in[i] / 32768) * eyesy.yres * (eyesy.knob3 + .5)
    x = i*space
    linewidth = int(eyesy.knob1*eyesy.xres/lines)
    position = eyesy.yres/2
    ballSize = int(eyesy.knob2*eyesy.xres/(lines-75))

    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    pygame.draw.circle(screen,color,(x, y1+position),ballSize, 0)
    pygame.draw.line(screen, color, [x, y0+position], [x, y1+position], linewidth)
