import os
import pygame
import time
import random
import math

#x 128th, 8th, thick

#Knob1 - line rate of rotation & direction
#Knob2 - line length
#Knob3 - line thickness
#Knob4 - foreground color shift rate & direction
#Knob5 - background color

color_rate=0
speed=0

def setup(screen, eyesy):
    global xr, yr, x128, x8th
    xr = eyesy.xres
    yr = eyesy.yres
    x128 = int(xr * 0.1) #int((128*xr)/eyesy.xres)
    x8th = int(xr * 0.00625) #(8*xr)/eyesy.xres
    
def draw(screen, eyesy):
    global xr, yr, x128, x8th, color_rate, speed
    eyesy.color_picker_bg(eyesy.knob5)
    thick = int(eyesy.knob3*(xr * 0.078))+1 #int(eyesy.knob3*((100*xr)/eyesy.xres))+1
    peak = 0
    lines = 5
    
    # Determine the rotation speed and direction based on eyesy.knob1
    if eyesy.knob1 < 0.48:
        speed = speed-(0.48-eyesy.knob1)*500#((20*xr)/eyesy.xres)
    elif eyesy.knob1 > 0.52:
        speed = speed+(eyesy.knob1-0.52)*500#((20*xr)/eyesy.xres)
    
    for i in range(lines) : 
    
        # Determine the color speed and direction based on eyesy.knob4
        if eyesy.knob4 < 0.48:
            color_rate = (color_rate - ((0.48-eyesy.knob4)*.09))%1.00
        elif eyesy.knob4 > 0.52:
            color_rate = (color_rate + ((eyesy.knob4-0.52)*.09))%1.00
        
        color = eyesy.color_picker((i*0.2+color_rate)%1.00)
        
        if eyesy.audio_in[i*10] > peak:
                peak = eyesy.audio_in[i*10]
                
        R = (4 * eyesy.knob2 * (peak / x128))+20
        x = R * math.cos((speed /  1000.) * 6.28) + (xr/2) + i*xr/lines-2*xr/lines
        y = R * math.sin((speed /  1000.) * 6.28) + (yr/2)
        pygame.draw.line(screen, color, [(i*xr/lines)+xr/10, (yr/2)], [x, y], thick)
