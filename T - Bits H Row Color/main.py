import os
import pygame
import random

#Knob1 - number of lines
#Knob2 - line length
#Knob3 - shadow control
#Knob4 - foreground colorkn
#Knob5 - background color

def setup(screen, eyesy):
    global trigger, x, y, height, width, xpos, lineAmt, xpos1, linelength, displace, xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    height = yr
    width = xr
    linelength = int(xr * 0.039) #((50*xr)/1280)

    lineAmt = int((eyesy.knob1*(yr * 0.139))+2)#int(eyesy.knob1*((100*yr)/720) + 2)

    displace = int(xr * 0.008)#((10*xr)/1280)
    xpos = [random.randrange(int(-1*(xr*0.156)),xr) for i in range(0, int(lineAmt + 2))]
    xpos1 = [(xpos[i]+displace) for i in range(0, int(lineAmt + 2))]
    x = y = 0
    trigger = False

def draw(screen, eyesy):
    global trigger, x, y, height, width, xpos, lineAmt, xpos1, linelength, displace, xr, yr 
    
    eyesy.color_picker_bg(eyesy.knob5)  
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.15)
    linewidth = int(height / lineAmt)
    linelength = int(eyesy.knob2*(xr * 0.234)+1) #int(eyesy.knob2*((300*xr)/1280)+1)
    
    minus = (eyesy.knob3*0.5)+0.5
    shadowColor = (eyesy.bg_color[0]*minus, eyesy.bg_color[1]*minus, eyesy.bg_color[2]*minus)
    
    if eyesy.trig:
        trigger = True
        
    if trigger == True :
        lineAmt = int((eyesy.knob1*(yr * 0.139))+2)
        xpos = [random.randrange(int(-1*(xr*0.156)),xr) for i in range(0, int(lineAmt + 2))]
        xpos1 = [(xpos[i]+displace) for i in range(0, lineAmt + 2)]
    
    for k in range(0, int(lineAmt + 2)) :
        x = xpos1[k] + linelength
        y = (k * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, shadowColor, (xpos1[k], y+displace), (x, y+displace), linewidth)
    
    for j in range(0, int(lineAmt + 2)) :
        x = xpos[j] + linelength
        y = (j * linewidth) + int(linewidth/2)- 1
        color = eyesy.color_picker_lfo(eyesy.knob4, 0.15)
        pygame.draw.line(screen, color, (xpos[j], y), (x, y), linewidth)        
    trigger = False
