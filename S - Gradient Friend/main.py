import pygame
import random
import time
import math
import pygame.gfxdraw

#Knob1 - x position
#Knob2 - y position
#Knob3 - height
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    pass 

def draw(screen, eyesy):
    eyesy.color_picker_bg(eyesy.knob5)
    yr = eyesy.yres
    xr = eyesy.xres
    i = int(yr * 0.25) #int((180*yr)/eyesy.yres)
    
    for i in range(i):
        push = abs(int(eyesy.knob3*eyesy.audio_in[i%24]/(yr/2)))    
        boing = int(eyesy.knob3*i)+eyesy.audio_in[1]/500
        i = boing
        color = eyesy.color_picker_lfo(eyesy.knob4)
        radius = int(10+push + 10 * math.sin(i * .05 + time.time()))
        xpos = int(((((xr*eyesy.knob1 + 100*math.sin(i * .0006 + time.time()))+100)*xr)/eyesy.xres))
        ypos = int((((((5*eyesy.knob2-1)/2*yr+(yr/2)))-int(i*eyesy.knob2))*yr)/yr-4*i)-boing
        pygame.gfxdraw.filled_circle(screen, xpos, int(ypos-boing), radius+1, color)