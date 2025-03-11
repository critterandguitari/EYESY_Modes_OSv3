import os
import pygame
import time
import random
import glob

#Knob1 - x position
#Knob2 - y position
#Knob3 - line & circle size
#Knob4 - foreground color
#Knob5 - background color

last_point = []

def setup(screen, eyesy):
    global images, xr,yr, last_point
    xr = eyesy.xres
    yr = eyesy.yres
    last_point = [0, (yr/2)]

def draw(screen, eyesy):
    global last_point, xr,yr
    eyesy.color_picker_bg(eyesy.knob5)    
    for i in range(0, 50) :
        seg(screen, eyesy, i)   

def seg(screen, eyesy, i):
    global last_point
    
    xoffset = int(xr/48)
    x19 = (10*xr)/xr
    y0 = screen.get_height() // 2
    y1 = int((screen.get_height() // 2) + ((eyesy.audio_in[i]*0.00003058)*(yr/2)))
    x = int(i * xoffset) 
    color = eyesy.color_picker_lfo(eyesy.knob4) 
    last_point = [(int(eyesy.knob1*xr)), (int(eyesy.knob2*yr))]
    pygame.draw.circle(screen,color,(x, y1),int(eyesy.knob3 * x19) + 3, 0)
    pygame.draw.line(screen, color, last_point, [x, y1], int(eyesy.knob3 * x19)+1)
