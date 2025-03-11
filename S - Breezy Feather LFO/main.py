import os
import pygame
import pygame.gfxdraw

#Knob1 - rate of change for number of triangles
#Knob2 - feather angle
#Knob3 - y position step amount (bounce speed)
#Knob4 - foreground color
#Knob5 - background color


triangles = 10

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

yposr = LFO(0,500,10)
tris = LFO(2,70,1)

def setup(screen, eyesy) :
    global xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    yposr.start = int(yr - (yr*1.05))
    yposr.max = int(yr * 1.05)
    

def draw(screen, eyesy) :
    global triangles, xr, yr
    
    eyesy.color_picker_bg(eyesy.knob5)    
    color = eyesy.color_picker_lfo(eyesy.knob4) #on knob 4
    tris.max = int(xr * 0.047) #int((60*eyesy.xres)/eyesy.xres)
    tris.step = int(eyesy.knob1*(xr * 0.012)) #int(eyesy.knob1*((15*eyesy.xres)/eyesy.xres))
    triangles = tris.update()+2
    space = int(xr/(triangles-1))
    offset = int((eyesy.knob2*2-1)*space*4)
    yposr.step = int(eyesy.knob3*(yr * 0.1)) #int(eyesy.knob3*((72*eyesy.yres)/eyesy.yres))
    y = yposr.update()
    
    pygame.draw.line(screen, color, (0, y), (xr,y)) #so you can see something in case no audio input
    
    for i in range (0,triangles) :
        
        auDio = int(eyesy.audio_in[i] / 65)
        ax = i * space
        pygame.gfxdraw.filled_trigon(screen, ax, y, ax+int((space/2)+offset),auDio+y, ax + space, y, color)
