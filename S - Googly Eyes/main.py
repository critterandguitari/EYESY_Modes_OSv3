import os
import pygame
import time
import random
import math

#Knob1 - mouth thickness & eye size
#Knob2 - mouth width
#Knob3 - speed of eye bounce
#Knob4 - foreground color
#Knob5 - background color

rad = 5
xpos = 300
ypos = 300
color = (0,0,0)
last_point = [320, 0]
last_point1 = [320, 0]

class LFO : #uses three arguments: start point, max, and how far each step is.

    def __init__(self, start, max, step):
        self.start = start
        self.max = max
        self.step = step
        self.current = 0
        self.direction = 1

    def update(self):

        # when it gets to the top, flip direction
        if (self.current >= self.max) :
            self.direction = -1
            self.current = self.max  # in case it steps above max

        # when it gets to the bottom, flip direction
        if (self.current <= self.start) :
            self.direction = 1
            self.current = self.start  # in case it steps below min

        self.current += self.step * self.direction

        return self.current

lfo1 = LFO(-200,200,1)
lfo2 = LFO(-300,300,1)

def setup(screen, eyesy) :
    pass

def draw(screen, eyesy) : 
    global rad, xpos, ypos, color, last_point, last_point1
    eyesy.color_picker_bg(eyesy.knob5)    
    xr = eyesy.xres
    yr = eyesy.yres
    
    lfo1.start = xr * -0.15625 #((xr*-200)/xr)
    lfo1.max = xr * 0.15625 #((xr*200)/xr)
    lfo2.start = xr * -0.234375 #((xr*-300)/xr)
    lfo2.max = xr * 0.234375#((xr*300)/xr)
    
    xhalf = xr * 0.5 #((640*xr)/xr)
    x720 = xr * 0.563 #((720*xr)/xr) #720
    x1116 = xr * 0.6875 #((11*xr)/16)
    
    y3d = (yr/3)
    y600 = yr * 0.833 #((yr*600)/yr)
    y640 = yr * 0.889 #((640*yr)/yr)
    
    color = eyesy.color_picker(eyesy.knob4)
    audio1 = eyesy.audio_in[0] /450
    audio2 = eyesy.audio_in[1] /450
    widthmod = xr * 0.098 #((xr*25)/xr)
    linewidth= int(eyesy.knob1*widthmod)+1
    
    #mouth
    for i in range(0, 100) :
        
        xscale = (xhalf/99*i)
        xoffset = int(xhalf+xscale)*eyesy.knob2*i/100 + (x720-eyesy.knob2*xhalf) #mouth width
        yoffset = y600 - eyesy.audio_in[2]/y640
        auDio = eyesy.audio_in[i] / (500-int(eyesy.knob2*499))
        color = eyesy.color_picker_lfo(eyesy.knob4)
        
        if i == 0 : last_point = [(0*eyesy.knob2+ -auDio)+ (x720-eyesy.knob2*xhalf), (yoffset+ auDio)]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]
    
    #eyes
    radrat = xr * 0.098 #((125*xr)/xr)
    rad = int(eyesy.knob1*radrat)+20 #eye size
    xpos1 = (2*radrat)+audio1
    ypos1 = y3d-audio1
    xpos2 = x1116-audio2
    ypos2 = y3d-audio2
    xrad = (rad/2) * math.sin((eyesy.audio_in[20]*.0001)) 
    yrad = (rad/2) * math.cos((eyesy.audio_in[25]*.0001))
    
    step1mod = xr * 0.023 #((xr*30)/xr)
    step2mod = xr * 0.031 #((xr*40)/xr)
    lfo1.step = eyesy.knob3*step1mod #eye bounce speed
    lfo2.step = eyesy.knob3*step2mod
    roll1 = int(lfo1.update())
    roll2 = -int(lfo1.update())
    slide1 = int(lfo2.update())
    slide2 = -int(lfo2.update())
    
    pygame.draw.circle(screen, color, [xpos1+slide1,ypos1+roll1], rad)
    pygame.draw.circle(screen, (245,200,255), [xpos1+int(xrad)+slide1,ypos1-int(yrad)+roll1], rad/2)
    pygame.draw.circle(screen, color, [xpos2+slide2,ypos2+roll2], rad)
    pygame.draw.circle(screen, (245,200,255), [xpos2+int(xrad)+slide2,ypos2-int(yrad)+roll2], rad/2)
