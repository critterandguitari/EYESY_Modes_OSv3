import os
import pygame
import random

#Knob1 - linewidth
#Knob2 - direction
#Knob3 - trails
#Knob4 - foreground color
#Knob5 - background color

trigger = False

class LFO : #uses three arguments: start point, max, and how far each step is.

    def __init__(self, start, max, step):
        self.start = start
        self.max = max
        self.step = step
        self.current = 0
        self.direction = 1

    def update(self):
        self.current += self.step * self.direction

    # when it gets to the top, flip direction
        if (self.current >= self.max) :
            self.direction = -1
            self.current = self.max  # in case it steps above max

    # when it gets to the bottom, flip direction
        if (self.current <= self.start) :
            self.direction = 1
            self.current = self.start  # in case it steps below min
        
        return self.current

denser = LFO(1,360,10)

def setup(screen, eyesy):
    global xr, yr, xhalf, yhalf, pos
    xr = eyesy.xres
    yr = eyesy.yres
    xhalf = (xr/2)
    yhalf = (yr/2)
    pos = [(random.randrange(xhalf,xhalf+2),random.randrange(yhalf,yhalf+2)) for i in range(0,12)]
    denser.max = yhalf


def draw(screen, eyesy):
    global trigger, pos, xr, yr, xhalf, yhalf
    eyesy.color_picker_bg(eyesy.knob5)   
    balls = int(eyesy.knob2*10)+1
    denser.step = int(eyesy.knob3*12)
    x20 = int(xr * 0.016)#((20*xr)/1280)
    xdensity = denser.update()*2
    ydensity = denser.update()
    size = abs(int(eyesy.knob1*x20)*denser.update()/30+1)
    
    if eyesy.trig :
        trigger = True
    
    if trigger == True :
        pos = [(random.randrange(abs(xhalf-xdensity),abs((xhalf+2)+xdensity+10)),random.randrange(abs(yhalf-ydensity),abs((yhalf+2)+ydensity+10))) for i in range(0,12)]
    
    for i in range (0, balls):
        color = eyesy.color_picker_lfo(eyesy.knob4)
        pygame.draw.circle(screen,color,pos[i],size, 0)

    trigger = False
