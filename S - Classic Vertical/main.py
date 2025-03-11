import os
import pygame
import math
import time

#Knob1 - line width
#Knob2 - circle size
#Knob3 - width control
#Knob4 - foreground color
#Knob5 - background color

def setup(screen,eyesy):
    global spacing, lines
    lines = 100
    spacing = (eyesy.yres / lines)

def draw(screen, eyesy):
    eyesy.color_picker_bg(eyesy.knob5)    
    for i in range(0, lines) :
        
        seg(screen, eyesy, i)
    
def seg(screen, eyesy, i) :
    global spacing, lines
    
    x0 = 0
    x1 = (eyesy.audio_in[i] / 32768) * eyesy.xres * (eyesy.knob3 + .5)
    y = (i * spacing) 
    linewidth = int(eyesy.knob1*spacing)
    position = int(.5*eyesy.xres)
    ballSize = int(eyesy.knob2*(spacing*7))
    
    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    pygame.draw.circle(screen,color,(x1+position, y),ballSize, 0)
    pygame.draw.line(screen, color, [x0+position, y], [x1+position, y], linewidth)
