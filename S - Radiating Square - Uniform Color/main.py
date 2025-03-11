import os
import pygame
import time
import random
import math

# Knob1 - x origin point LFO rate
# Knob2 - line width
# Knob3 - endpoint LFO rate
# Knob4 - foreground color
# Knob5 - background color

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
    global sqmover, adjust1, adjust2, xr,yr
    xr = eyesy.xres
    yr = eyesy.yres
    sqmover = LFO(-1*(yr/2),yr/2,0.01)
    adjust1 = LFO(-50,50,0.01)
    adjust2 = LFO(-100,100,0.01)

def draw(screen, eyesy) :
    global sqmover, adjust1, adjust2, xr,yr
    
    eyesy.color_picker_bg(eyesy.knob5)

    
    for i in range(0, 100) :
        width = int(eyesy.knob2 * (xr * 0.012))+1 #int(eyesy.knob2*((15*xr)/xr))+1
        #LFOs
        adjuster1 = adjust1.update()
        adjust1.step = eyesy.knob1/50
        adjuster2 = adjust2.update()
        adjust2.step = eyesy.knob1+.001
        if eyesy.knob1 == 0 : adjuster1 = adjuster2 = 0
        sqmover.step = eyesy.knob3 + .01
        angle = sqmover.update()
        if eyesy.knob3 == 0 : angle = 0
        
        #color
        color = eyesy.color_picker_lfo(eyesy.knob4)
        
        #lines
        if  i < 25:  
            x0 = (((490  + adjuster1*i)*xr)/xr)%xr
            x1 = x0 - int(eyesy.audio_in[i] / 100)
            y = (((210 + i * 12 + adjuster2)*yr)/yr)%yr
            pygame.draw.line(screen, color, [x0, y], [x1, (y - angle)], width)
    
        if i >= 25 and i < 50:
            x = (((190 + i * 12 + adjuster2)*xr)/xr)%xr
            y0 = (((510 + adjuster1*i)*yr)/yr)%yr
            y1 = y0 + int(eyesy.audio_in[i] / 100)
            pygame.draw.line(screen, color, [x, y0], [(x + angle), y1], width)        
                
        if i >= 50 and i < 75:
            x0 = (((790 + adjuster1*i)*xr)/xr)%xr
            x1 = (x0 + int(eyesy.audio_in[i] / 100))
            y = (((1110 - i * 12 + adjuster2)*yr)/yr)%yr
            pygame.draw.line(screen, color, [x0, y], [x1, (y + angle)], width)
                        
        if i >= 75 and i < 100:
            x = (((1690 - i * 12 + adjuster2)*xr)/xr)%xr
            y0 = (((210 + adjuster1*i)*yr)/yr)%yr
            y1 = y0 - abs(eyesy.audio_in[i] / 100)
            pygame.draw.line(screen, color, [x, y0], [(x - angle), y1], width)
        
        if i == 1:
            x = (((490 + adjuster2)*xr)/xr)%xr
            y0 = (((210 + adjuster1*i)*yr)/yr)%yr
            y1 = y0 - int(eyesy.audio_in[i] / 100)
            pygame.draw.line(screen, color, [x, y0], [(x - angle), y1], width)
