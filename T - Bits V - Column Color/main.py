import os
import pygame
import random

#Knob1 - number of lines
#Knob2 - line length
#Knob3 - shadow control
#Knob4 - foreground colorkn
#Knob5 - background color

def setup(screen, eyesy):
    global trigger, x, y, height, width, ypos, lineAmt, ypos1, linelength, displace, xr, yr
    x = 0
    y = 0
    xr = eyesy.xres
    yr = eyesy.yres
    height = yr
    width = xr+65
    lineAmt = int((eyesy.knob1*(xr * 0.078)) + 2)
    linelength = int(yr * 0.069) #((50*yr)/720)
    displace = int(yr * 0.014) #((10*yr)/720)
    ypos = [random.randrange(int(-1*(yr * 0.278)),yr) for i in range(0, lineAmt + 2)]
    ypos1 = [(ypos[i]+displace) for i in range(0, lineAmt + 2)]
    trigger = False

def draw(screen, eyesy):
    global trigger, x, y, height, width, ypos, lineAmt, ypos1, linelength, displace, xr, yr 
    eyesy.color_picker_bg(eyesy.knob5)  
    xr = eyesy.xres
    yr = eyesy.yres
    linewidth = int(width / lineAmt)
    linelength = int(eyesy.knob2*(yr * 0.417)+1)
    
    minus = (eyesy.knob3*0.5)+0.5
    shadowColor = (eyesy.bg_color[0]*minus, eyesy.bg_color[1]*minus, eyesy.bg_color[2]*minus)
    
    if eyesy.trig :
        trigger = True
        
    if trigger == True :
        lineAmt = int((eyesy.knob1*(xr * 0.078)) + 2)
        ypos = [random.randrange(int(-1*(yr * 0.278)),yr) for i in range(0, lineAmt + 2)]
        ypos1 = [(ypos[i]+displace) for i in range(0, lineAmt + 2)]

    for k in range(0, lineAmt + 2) :
        y = ypos1[k] + linelength
        x = (k * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, shadowColor, (int(x+displace), int(ypos1[k])), (int(x+displace), int(y)), linewidth)
    
    for j in range(0, lineAmt + 2) :
        y = ypos[j] + linelength
        x = (j * linewidth) + int(linewidth/2)- 1
        color = eyesy.color_picker_lfo(eyesy.knob4, 0.1)
        pygame.draw.line(screen, color, (x, ypos[j]), (x, y), linewidth)        
    
    trigger = False
