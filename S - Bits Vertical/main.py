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
    global ypos, lineAmt, lineAmt_old, xres, yres
    xres = eyesy.xres
    yres = eyesy.yres
    ypos = [random.randrange(int(-0.15*yres), yres) for i in range(0, lineAmt)]
    lineAmt = int(eyesy.knob1*59 + 1)
    lineAmt_old = lineAmt

def draw(screen, eyesy):
    global trigger, x, y, ypos, lineAmt, linelength, lineAmt_old, xres, yres
    eyesy.color_picker_bg(eyesy.knob5)    
    height = int(yres*1.03125) #720*40/1280 = 22.5 #int(yres+((eyesy.yres*40)/eyesy.xres))
    width = int(xres)
    lengthcon = int(yres * 0.833)#int((600*eyesy.yres)/eyesy.yres)
    linewidth = int((width + 40)/ lineAmt)
    linelength = int(eyesy.knob2*lengthcon + 1)
    yrangelow = int(-0.15*eyesy.yres)
    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    lineAmt = int(eyesy.knob1*59 + 1)
    
    if lineAmt_old != lineAmt:
        ypos = [random.randrange(yrangelow, height) for i in range(0, lineAmt)]
    lineAmt_old = lineAmt
    
    if eyesy.trig:
        trigger = True
        
    if trigger == True :
        lineAmt = int(eyesy.knob1*59 + 1)
        ypos = [random.randrange(yrangelow, height) for i in range(0, lineAmt)]
    
    trigger = False           
            
    for j in range(0, lineAmt) :
        
        auDio = eyesy.audio_in[j] / 180
        diag = (0.05*eyesy.xres)

        y = ypos[j] + linelength
        x = (j * linewidth) + (linewidth/2)- 1
        pygame.draw.line(screen, color, (x, ypos[j]+(auDio)), (x+ eyesy.knob3 * (diag*2)-diag, y+auDio), linewidth)
