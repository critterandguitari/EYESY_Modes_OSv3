import pygame
import random
import time
import math
import pygame.gfxdraw

#Knob1 - cloud x position 
#Knob2 - cloud y position
#Knob3 - pattern shape and swell range
#Knob4 - foreground color
#Knob5 - background color

color_rate = 0

def setup(screen, eyesy):
    pass

def draw(screen, eyesy):
    global color_rate
    
    eyesy.color_picker_bg(eyesy.knob5)
    xr = eyesy.xres
    x240 = xr * 0.188 #((240*xr)/eyesy.xres)
    xhalf = xr/2
    yr = eyesy.yres
    yhalf = yr/2
    y480 = yr * 0.667 #((480*yr)/eyesy.yres)
    xpos1 = int(eyesy.knob1*4*x240)-2*x240
    cool = int(yhalf)

	
    for i in range(cool): 
        xpos = int(x240 + int(xhalf*math.sin(.5 + time.time())*eyesy.knob3))
        ypos = int((eyesy.knob2*y480) + eyesy.audio_in[i%99]/100 + int(30* math.cos(1 * 1 + time.time())))
        color_rate += (eyesy.knob4*0.02)
        color = eyesy.color_picker(color_rate)
        radius = int((30 + 20 * math.sin(i*eyesy.knob3 * 3 + time.time()))*yr)/yr
        xpos = int(xr / 2 + xpos * math.sin(i * 1 + time.time()))
        pygame.gfxdraw.filled_circle(screen, int(xpos+xpos1), int(i+ypos), int(radius), color)