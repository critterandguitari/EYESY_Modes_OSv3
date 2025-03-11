import os
import pygame
import time
import random
import math

#Knob1 - first scope y position
#Knob2 - second scope y position
#Knob3 - line width
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy) :
    global xr, yr
    xr = eyesy.xres
    yr = eyesy.yres

def draw(screen, eyesy) :
    global xr, yr

    eyesy.color_picker_bg(eyesy.knob5)

    w100 = (yr*0.045) #max line width

    #first scope
    for i in range (0,50) :
        x0 = int(eyesy.knob1*xr) 
        x1 = x0 + (eyesy.audio_in[i] / 35)
        y = i * (yr/48)
        color = eyesy.color_picker_lfo(eyesy.knob4)
        
        pygame.draw.line(screen, color, [x0, y], [x1, y], int(eyesy.knob3*w100+1))
        
    #second scope
    for i in range (51,100) :
        x0 = int(eyesy.knob2*xr)
        x1 = x0 + (eyesy.audio_in[i] / 35)
        y = (i - 50) * (yr/48)
        color = eyesy.color_picker_lfo(eyesy.knob4)
        
        pygame.draw.line(screen, color, [x0, y], [x1, y], int(eyesy.knob3*w100+1))
