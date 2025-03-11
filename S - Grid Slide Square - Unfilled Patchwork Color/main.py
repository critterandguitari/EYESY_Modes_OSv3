import os
import pygame
import math
import time

#Knob1 - LFO step amount
#Knob2 - LFO start position
#Knob3 - size of squares
#Knob4 - foreground color
#Knob5 - background color

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

def setup(screen, eyesy) :
    global xr, yr, x8, y5, hund, otwen, drei, acht, sqmover, color, linew
    xr = eyesy.xres
    yr = eyesy.yres
    x8 = xr/8
    y5 = yr/5
    hund = xr * 0.07734 #(99*xr)/xr
    otwen = xr * 0.09375 #(120*xr)/xr
    drei = int(xr * 0.00234)#(3*xr)/xr
    acht = int(xr * 0.00625) #(8*xr)/xr
    sqmover = LFO(otwen*-1,otwen,10)
    if drei == 0 : 
        drei =1
    color = eyesy.color_picker(eyesy.knob4)
    linew = int(xr*0.0026)

def draw(screen, eyesy) :
    global xr, yr, x8, y5, hund, otwen, drei, acht, sqmover, color, linew
    eyesy.color_picker_bg(eyesy.knob5)
    for i in range(0, 7) :
        
        sqmover.step = eyesy.knob1*drei
        sqmover.max = int(eyesy.knob2*otwen)
        sqmover.start = int(eyesy.knob2*-otwen)
        xoffset = -sqmover.update()
        yoffset = sqmover.update()*0.8
         
        for j in range(0, 10) :
            x = (j*(x8))-(x8)
            y = (i*(y5))-(y5)
            rad = abs(eyesy.audio_in[j-i] / hund)
            width = int(eyesy.knob3*hund)+1
            
            
            if (i%2) == 1 : 
                x = j*(x8)-(x8)+xoffset
                color = eyesy.color_picker(eyesy.knob4)
            if (j%2) == 1 : 
                y = i*(y5)-(y5)+yoffset
                color = eyesy.color_picker(1-eyesy.knob4)
            if ((j+i)%3) == 1 :
                color = eyesy.color_picker((0.8+eyesy.knob4)%1.0)
                
            rect = pygame.Rect(0,0,width,width)
            rect.center = (x,y)
            rect.inflate_ip(rad,rad)
            
            pygame.draw.rect(screen, color, rect, linew) 
