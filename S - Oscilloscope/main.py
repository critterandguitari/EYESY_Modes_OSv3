import os
import pygame
import time
import math

#Knob1 - line thickness
#Knob2 - y position
#Knob3 - shadow distance & opacity
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global last_point, first_point, xr,yr,x200, x110,a75,x15
    xr = eyesy.xres
    yr = eyesy.yres
    last_point = [0, (yr/2)]
    first_point = []
    x200 = int((200*xr)/xr)
    x110 = int((25*xr)/xr)
    a75 = int((500*xr)/xr)
    x15 = int((xr/50)+1)


def draw(screen, eyesy):
    global last_point, first_point, xr,yr,x200, x110, a75,x15
    eyesy.color_picker_bg(eyesy.knob5)    
    #Lines
    for i in range(0, 50) :
        lineseg(screen, eyesy, i)

def lineseg(screen, eyesy, i):
    global last_point, first_point, xr,yr,x200, x110, a75,x15
    
    linewidth = int(eyesy.knob1*x110)+1
    y1 = int((eyesy.knob2 * yr) + ((eyesy.audio_in[i]* 0.00003058)* a75))
    x = i * x15
    color = eyesy.color_picker_lfo(eyesy.knob4)

    if i == 0 : 
        last_point = [(x110*-1), (yr/2)]
    else :
        last_point = last_point
    
    pygame.draw.line(screen, (int(eyesy.knob3*255),int(eyesy.knob3*255),int(eyesy.knob3*255)), [last_point[0]-150*eyesy.knob3 , last_point[1]+150*eyesy.knob3], [x-150*eyesy.knob3 , y1+150*eyesy.knob3], linewidth)
    pygame.draw.line(screen, color, last_point, [x , y1], linewidth)

    last_point = [x , y1]
