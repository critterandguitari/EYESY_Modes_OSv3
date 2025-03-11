import pygame
import random
import time
import math
import pygame.gfxdraw

#Knob1 - cloud height
#Knob2 - cloud width
#Knob3 - pattern shape and swell range
#Knob4 - foreground color
#Knob5 - background color

color_rate = 0

def setup(screen, eyesy):
    global xr,yr,x12
    xr = eyesy.xres
    yr = eyesy.yres
    x12 = xr * 0.009375 #(12*xr)/eyesy.xres
    

def draw(screen, eyesy):
    global xr,yr,x12, color_rate
    eyesy.color_picker_bg(eyesy.knob5)
    cool = int(eyesy.knob1*(yr-10))+10 # number of circles and height
    yoff = int((yr/2)-eyesy.knob1*(yr/2))
    xtra = int(eyesy.knob2*(xr-2))+2 # width control
    segs = 99 # number of audio data points to look at
    sel  = eyesy.knob4*5 # color select switch
    swell = eyesy.knob3*0.999 + .001 # radius and scope shape
    
    for i in range(cool):
            audiopuff = int((eyesy.audio_in[i%segs]*0.00003058)*(yr/2))
            color_rate += (eyesy.knob4*0.002)%1.00
            color = eyesy.color_picker(((i*0.02)+color_rate)%1.00)
            radius = int(x12 + x12 * math.sin(i * .1*swell + time.time()))
            xpos = int(((xr/2) - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+audiopuff, i+yoff, abs(radius), color)
    