import os
import pygame
import math
import random

#Knob1 - vertical line width
#Knob2 - horizontal line width
#Knob3 - speed
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

def setup(screen, eyesy):
    global b1,b2,b3,b4,y,xr,yr,x100, x_lines_first
    xr = eyesy.xres
    yr = eyesy.yres
    x100 = xr * 0.078 #(100*xr)/xr
    b1 = LFO(0,xr,10) #top x line
    b2 = LFO(0,xr,19) #bottom x line
    b3 = LFO(0,(yr/2),2) #top y line
    b4 = LFO((yr/2),yr,2)#bottom y line
    y = 0
    x_lines_first = True  # Initialize the draw order

    
def draw(screen, eyesy):
    global b1,b2,b3,b4,y,xr,yr,x100, x_lines_first
    eyesy.color_picker_bg(eyesy.knob5)    
    y = abs(eyesy.audio_in[50] / 85)
    
    color = eyesy.color_picker(eyesy.knob4)
    color2 = eyesy.color_picker((eyesy.knob4+0.25)%1.00)
    color3 = eyesy.color_picker((eyesy.knob4+0.50)%1.00)
    color4 = eyesy.color_picker((eyesy.knob4+0.75)%1.00)
    
    size1 = int(eyesy.knob1 * x100) +1
    size2 = int(eyesy.knob2 * (x100/2)) +1
    
    #update the horizontal lines so they end/start at yres/2 depending on line width
    b3.max = (yr/2)-(size2/2)
    b4.start = (yr/2)+(size2/2)
    
    #b1.step = int(eyesy.knob3 * ((16*xr)/xr))+5  #top x line
    #b2.step = int(eyesy.knob3 * ((31*xr)/xr))+5  #bottom x line
    #b3.step = int(eyesy.knob3 * (x100/20))+2  #top y line
    #b4.step = int(eyesy.knob3 * (x100/20))+2 #bottom y line
    b1.step = int(eyesy.knob3 * (xr * 0.0125))+5  #top x line #16
    b2.step = int(eyesy.knob3 * (xr * 0.0242))+5  #bottom x line
    b3.step = int(eyesy.knob3 * (x100/20))+2  #top y line
    b4.step = int(eyesy.knob3 * (x100/20))+2 #bottom y line

    posx1 = b1.update() #top x line
    posx2 = b2.update() #bottom x line
    posy1 = b3.update() #top y line
    posy2 = b4.update() #bottom y line
    
    # Check if b1 LFO reaches the start or max point
    if posx1 == b1.start or posx1 == b1.max:
        # 50% chance to set x_lines_first to True or False
        x_lines_first = random.random() < 0.5
    
    # Draw based on the x_lines_first boolean
    if x_lines_first:
        pygame.draw.line(screen, color, [posx1, (yr/4)-y], [posx1, (yr/2)], size1) #top x line
        pygame.draw.line(screen, color2, [posx2, (yr/2)], [posx2, (yr*0.75)+y], size1) #bottom x line
        pygame.draw.line(screen, color3, [0, posy1], [xr, posy1], size2) #top y line
        pygame.draw.line(screen, color4, [0, posy2], [xr, posy2], size2) #bottom x line
    else:
        pygame.draw.line(screen, color3, [0, posy1], [xr, posy1], size2) #top y line
        pygame.draw.line(screen, color4, [0, posy2], [xr, posy2], size2) #bottom x line
        pygame.draw.line(screen, color, [posx1, (yr/4)-y], [posx1, (yr/2)], size1) #top x line
        pygame.draw.line(screen, color2, [posx2, (yr/2)], [posx2, (yr*0.75)+y], size1) #bottom x line
    

