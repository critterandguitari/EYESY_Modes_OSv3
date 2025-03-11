import os
import pygame
import time
import random

#Knob1 - left scope angles
#Knob2 - left scopes y position
#Knob3 - line thickness
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy) :
    global xr, yr  
    xr = eyesy.xres
    yr = eyesy.yres

def draw(screen, eyesy) :
    global xr, yr
    
    eyesy.color_picker_bg(eyesy.knob5)    
    color = eyesy.color_picker_lfo(eyesy.knob4) #on knob4

    yhalf = yr/2
    ythird = yr/3
    y2third = (2*yr)/3
    step16 = xr * 0.0125 #((16*xr)/xr)
    wid = xr * 0.0328 #((xr*42)/xr)
    steppy = int(eyesy.knob1 * step16)
    leftpoint = int(eyesy.knob2 * yr)
    linewidth = int(eyesy.knob3*wid+1)
    screendiv = (xr/60)
    
    #bottom
    for i in range (0,30) :
        ay0 = ythird + leftpoint - (steppy * i)
        ay1 = ythird + leftpoint - (steppy * i) + (eyesy.audio_in[i] / 128)
        ax = i * screendiv 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
    
    #top
    for i in range (30,60) :
        ay0 = y2third - leftpoint + (steppy * (i-30))
        ay1 = y2third - leftpoint + (steppy * (i-30))+ (eyesy.audio_in[i] / 128)
        ax = (i-30) * screendiv 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
    
    #right   
    for i in range (60,94) :
        ay0 = yhalf
        ay1 = yhalf + (eyesy.audio_in[i] / 80)
        ax = (i-30) * screendiv#21.3
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
