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
    global last_point, last_point1, xr, yr, zehn, color_rate
    xr = eyesy.xres
    yr = eyesy.yres
    last_point = [xr/4, 0]
    last_point1 = [xr/4, 0]
    zehn = int(xr * 0.0078125)
    color_rate = 0
    

def draw(screen, eyesy):
    global last_point, last_point1, zehn, xr, yr, color_rate
    eyesy.color_picker_bg(eyesy.knob5)    
    linewidth = int(eyesy.knob1*zehn)+1
    lines = int((39*eyesy.knob2)+1)+4
    
    spacehoriz = int(xr/(lines-2))
    spacevert = int(yr/(lines-2))
    recsize = int(zehn*eyesy.knob3)*2
    sel = eyesy.knob4*2
    
    #global color shift on knob4 (comment out the other "set color on knob4" if/elif lines )
    #if sel < 1 :
    #    color = eyesy.color_picker(eyesy.knob4*2)
    #elif sel >= 1 :
    #    color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
    #    color = eyesy.color_picker(color_rate)
    
    #horizontal lines
    for j in range(0,lines) :
        
        #set color on knob4
        if sel < 1 :
            color = eyesy.color_picker(eyesy.knob4*2)
        elif sel >= 1 :
            color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
            color = eyesy.color_picker(color_rate)
        
        pygame.draw.line(screen, color, (-1,j*spacevert), (xr,j*spacevert), linewidth)
    
    #top oscilloscope
    for m in range(0, lines) :
        x = int(m*spacehoriz)
        y = 0
        auDiom = (eyesy.audio_in[m] * 0.00003058) * yr
        
        #set color on knob4
        if sel < 1 :
            color = eyesy.color_picker(eyesy.knob4*2)
        elif sel >= 1 :
            color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
            color = eyesy.color_picker(color_rate)
        
        pygame.draw.line(screen, color, [x,y], [x, yr/2 - auDiom], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-(recsize*0.5),yr/2-auDiom,recsize,recsize], 0)
    
    #bottom oscilloscope
    for i in range(0, lines) :
        x = int(i*spacehoriz)
        y = yr/2
        auDio = (eyesy.audio_in[int(i+(lines*0.5))] * 0.00003058) * yr
        
        #set color on knob4
        if sel < 1 :
            color = eyesy.color_picker(eyesy.knob4*2)
        elif sel >= 1 :
            color_rate = (color_rate + (abs(sel-1)*.1)) %1.0
            color = eyesy.color_picker(color_rate)

        pygame.draw.line(screen, color, [x,yr], [x, (y-auDio)], linewidth)
        if recsize >= 1 and y-auDio > y:
            pygame.draw.rect(screen, color, [x-(recsize*0.5),(y-auDio)-recsize,recsize,recsize], 0)
