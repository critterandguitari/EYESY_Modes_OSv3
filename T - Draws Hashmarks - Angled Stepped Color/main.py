import os
import pygame
import random
import math
import time

#Knob1 - horizontal line count
#Knob2 - line thickness
#Knob3 - veritcal line count
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global xr, yr, trigger, vertLines, xpos, x, y, height, width, angle
    
    xr = eyesy.xres
    yr = eyesy.yres
    trigger = False
    vertLines = 20
    xpos = 0
    x = 0
    y = 0
    height = 0
    width = 0
    angle = 0

def draw(screen, eyesy):
    global vertLines, trigger, xpos, x, y, height, width, xr, yr, angle
    
    eyesy.color_picker_bg(eyesy.knob5)    

    linewidth = int((((eyesy.knob2*7) + 1)*yr)/yr)+1
    lines = int(9*eyesy.knob1+1)+90
    min200 = int(xr * 0.156) #((200*xr)/1280)
    min100 = int(xr * 0.078) #((100*xr)/1280)
    max1000 = int(xr * 0.781) #((1280*xr)/1280)
    max700 = int(yr * 0.972) #((700*yr)/720)
    ran50 = int(xr * 0.039) #((50*xr)/1280)
    ran70 = int(xr * 0.055) #((70*xr)/1280)
    
    if eyesy.trig :
        trigger = True
    
    #vertical lines    
    if trigger == True :
        
        vertLines = random.randrange(int(eyesy.knob3*ran50)+2,int(eyesy.knob3*ran70)+8)
        x = random.randrange(-1*min200, max1000)
        y = random.randrange(-1*min200, max700)
        width = random.randrange(-1*min100, max1000)
        height = random.randrange(-1*min100, max1000)
        angle = random.randrange(0, 75)
        for l in range(0, vertLines) :
            xpos = x + (l + 1)*(width/vertLines) 
            
    for k in range(0, vertLines) :
        
        xpos = x + (k + 1)*(width/vertLines)
        color = eyesy.color_picker_lfo(eyesy.knob4, 0.25) #stepped color
        pygame.draw.line(screen, color, (xpos+angle, y), (xpos-angle, height), linewidth)
        
    trigger = False   
    
    #horizontal lines
    if eyesy.knob1 > 0 :
        for j in range(0, lines) :
        
            linespace = yr-(lines-1)*(yr-2)/100
            color = eyesy.color_picker_lfo(eyesy.knob4, 0.25) #stepped color
            pygame.draw.line(screen, color, (0,(j*linespace)+linespace/2), (xr,(j*linespace)+linespace/2), linewidth)
