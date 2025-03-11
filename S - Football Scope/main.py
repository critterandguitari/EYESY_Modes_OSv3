import os
import pygame
import time
import random

#Knob1 - x position
#Knob2 - y position
#Knob3 - diameter of circles
#Knob4 - foreground color
#Knob5 - background color

color_rate = 0
line_count = 100

def setup(screen, eyesy):
    pass

def draw(screen, eyesy):
    global line_count
    eyesy.color_picker_bg(eyesy.knob5)
    for i in range(0, line_count) :
        seg(screen, eyesy, i)    

def seg(screen, eyesy, i) :
    global color_rate, linecount

    x0 = int(eyesy.knob2 * eyesy.yres)
    x1 = (int(eyesy.knob1 * eyesy.xres) ) + (eyesy.audio_in[i] / 50)
    circlespace = eyesy.xres/line_count
    circlebuff = 0
    circleradmax = int(eyesy.xres *0.01)
    y = i * circlespace
    y_off= -100

    if eyesy.knob4 < 0.5:
        color_rate = (color_rate + ((eyesy.knob4-0.5)*.001))%1.00
        color = eyesy.color_picker((i*0.01+color_rate)%1.00)
    if eyesy.knob4 > 0.5:
        color=eyesy.color_picker(1-(eyesy.knob4*2))
    
    pygame.draw.circle(screen,color,(x1, y + circlebuff+y_off),int(eyesy.knob3 * circleradmax), 0)
    pygame.draw.line(screen, color, [y + circlebuff, x0], [x1, y + circlebuff+y_off], 2)
