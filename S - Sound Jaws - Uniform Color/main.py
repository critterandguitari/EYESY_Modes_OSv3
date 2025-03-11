import os
import pygame
import random
import pygame.gfxdraw

# Knob1 - number of teeth
# Knob2 - teeth shape
# Knob3 - how close together teeth are (clench)
# Knob4 - foreground color
# Knob5 - background color

num = 25
clench = 0
teeth = 1
toff = 1
r=0
g=0
b=0
counter = 0

def setup(screen, eyesy) :
    global xr, yr, last_screen, color_rate
    xr = eyesy.xres
    yr = eyesy.yres
    last_screen = pygame.Surface((xr,yr))
    color_rate = 0

def draw(screen, eyesy) : 
    global xr, yr, last_screen, r, g, b, counter, color_rate
    eyesy.color_picker_bg(eyesy.knob5)    
    xrSm = xr - (xr * 0.078) #xr - 100*xr/xr
    yrSm = yr - (yr * 0.139) #yr - 100*yr/yr
    
    #screengrab feedback loop
    image = last_screen
    last_screen = screen.copy()
    thing = pygame.transform.scale(image,((xrSm),(yrSm))) #scales down screengrab
    screen.blit(thing, (int(xr * 0.039 ),int(yr * 0.069))) #re-centers screengrab 50, 50
   
    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    #teeth and clench
    teeth = int(eyesy.knob1 * 10)
    teethwidth = int(((xr-(xr*.1)*teeth)*xr)/xr)
    if teethwidth == 0 : teethwidth = int(((.1*xr)*xr)/xr)
    clench = int(eyesy.knob3 * (0.156*xr) - int(teethwidth/2))
    if teethwidth > xr/2 : clench = int((eyesy.knob1*(0.156*xr))-(xr*0.39))
    shape = int(eyesy.knob2*3)
    if shape < 1 : clench = int(eyesy.knob1*(0.156*xr) - (xr*0.078))
    
    #top row
    for i in range(0, 10) :
        x = (i * teethwidth)+teethwidth/2
        y0 = 0
        audioL = abs(eyesy.audio_in[i] / 85)      #AUDIO IN L
        y1 = y0 + audioL + clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, int(x-teethwidth/2), int(y1), int(x), int(y1+teethwidth/2), int(x+teethwidth/2), int(y1), color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, int(x), int(y1), int(teethwidth/2), color)    
    
    #bottom row
    for i in range(10, 20) :
        x = ((i-10) * teethwidth) + teethwidth/2
        y0 = yr
        audioR = abs(eyesy.audio_in[i] / 85)      #AUDIO IN R
        y1 = y0 - audioR - clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, int(x-teethwidth/2), int(y1), int(x), int(y1-teethwidth/2), int(x+teethwidth/2), int(y1), color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, int(x), int(y1), int(teethwidth/2), color)


