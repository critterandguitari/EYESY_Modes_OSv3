import os
import pygame
import time
import random
import math

#Knob1 - line width
#Knob2 - number of lines
#Knob3 - square size
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global last_point, last_point1, y72, x180, xr, yr, zehn, color_rate, lines
    xr = eyesy.xres
    yr = eyesy.yres
    last_point = [xr/4, 0]
    last_point1 = [xr/4, 0]
    y72 = int(yr *0.1)
    x180 = xr*0.1406 
    zehn = xr*0.014 
    color_rate = 0
    lines = int(y72)
    if lines > 72 :
        lines = 72
    

def draw(screen, eyesy):
    global last_point, last_point1, y72, x180, zehn, xr, yr, color_rate, lines
    
    eyesy.color_picker_bg(eyesy.knob5)    
    linewidth = int(eyesy.knob1*zehn)+1
    spacehoriz = (x180*eyesy.knob2)+18
    spacevert = spacehoriz
    recsize = int(zehn*eyesy.knob3)
    sel = eyesy.knob4*2
    
    #global color shift on knob4 (comment out the other "set color on knob4" if/elif lines )
    #if sel < 1 :
    #    color = eyesy.color_picker(eyesy.knob4*2)
    #elif sel >= 1 :
    #    color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
    #    color = eyesy.color_picker(color_rate)
    
    
    #horizontal lines
    for j in range(0, lines) :
        
        #set color on knob4
        if sel < 1 :
            color = eyesy.color_picker(eyesy.knob4*2)
        elif sel >= 1 :
            color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
            color = eyesy.color_picker(color_rate)
        
        space = j*spacehoriz
        pygame.draw.line(screen, color, (0,space), (xr,space), linewidth)
    
    # top oscilloscope
    for m in range(0, lines) :
        
        #set color on knob4
        if sel < 1 :
            color = eyesy.color_picker(eyesy.knob4*2)
        elif sel >= 1 :
            color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
            color = eyesy.color_picker(color_rate)

        x = int(m*spacehoriz)+ 2
        y = 0
        auDio = int((eyesy.audio_in[m] * 0.00003058) * yr)
        if auDio < 0 : auDio = 0
        pygame.draw.line(screen, color, [x,y], [x, y + auDio], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-(recsize*0.5),y+auDio,recsize,recsize], 0)
    
    # bottom oscilloscope
    for i in range(0, lines) :
        
        #set color on knob4
        if sel < 1 :
            color = eyesy.color_picker(eyesy.knob4*2)
        elif sel >= 1 :
            color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
            color = eyesy.color_picker(color_rate)

        x = int((i*spacehoriz)+1)
        y = int(yr-recsize)
        auDio = int((eyesy.audio_in[i] * 0.00003058) * yr)

        if auDio > 0 : auDio = 0
        pygame.draw.line(screen, color, [x,y+recsize], [x, y - (auDio*-1)], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-int((recsize/2)+1),y+auDio,recsize,recsize], 0)
