import os
import pygame
import math
import time

#Knob1 - x position
#Knob2 - y position
#Knob3 - circle scaler
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    pass

def draw(screen, eyesy):
    eyesy.color_picker_bg(eyesy.knob5)
    x = int(eyesy.knob1*eyesy.xres)
    y = int(eyesy.knob2*eyesy.yres)
    circles = 10
    
    for i in range(1,circles) :
        
        x = x+i/3
        R = int((abs(eyesy.audio_in[i]/100)*eyesy.yres/eyesy.yres)*(eyesy.knob3*i))+10
        
        color = eyesy.color_picker((eyesy.knob4*i)%1.0)

        pygame.draw.circle(screen,color,(x,y),(R))
