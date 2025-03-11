import os
import pygame
import random
import math

#Knob1 - number of lines
#Knob2 - line length
#Knob3 - angle adjustment
#Knob4 - foreground color
#Knob5 - background color

trigger = False
x = 0
y = 0
linelength = 50
lineAmt = 60


def setup(screen, eyesy):
    global xpos, lineAmt, lineAmt_old, XR, YR
    XR = eyesy.xres
    YR = eyesy.yres
    xpos = [random.randrange(int(-0.16*eyesy.xres), eyesy.xres) for i in range(0, lineAmt+2)]
    lineAmt = int(eyesy.knob1*59 + 1)
    lineAmt_old = lineAmt

def draw(screen, eyesy):
    global trigger, x, y, xpos, lineAmt, linelength, lineAmt_old, XR, YR
    eyesy.color_picker_bg(eyesy.knob5)    
    height = YR
    width = int(eyesy.xres+(eyesy.xres*0.16))
    lengthcon = int(0.25*eyesy.xres)
    linelength = int(eyesy.knob2*lengthcon+10)
    linewidth = height / lineAmt
    xrangelow = int(-0.16*eyesy.xres)
    color = eyesy.color_picker_lfo(eyesy.knob4)

    lineAmt = int(eyesy.knob1*59 + 1)
    
    if lineAmt_old != lineAmt :
        xpos = [random.randrange(xrangelow, eyesy.xres) for i in range(0, lineAmt+2)]
    lineAmt_old = lineAmt
    
    if eyesy.trig:
        trigger = True
        
    if trigger == True :
        lineAmt = int(eyesy.knob1*59 + 1)
        xpos = [random.randrange(xrangelow, eyesy.xres) for i in range(0, lineAmt+2)]
        
    trigger = False

    for i in range(0, lineAmt) :
        
        auDio = int(abs(eyesy.audio_in[i] / 180))
        diag = int(0.07*eyesy.yres)
        
        x = xpos[i] + linelength
        y = (i * linewidth) + int(linewidth/2)#- 1
        pygame.draw.line(screen, color, (xpos[i]+(auDio), y), (int(x+auDio), y + int(eyesy.knob3 * (diag*2) - diag)), int(linewidth))
