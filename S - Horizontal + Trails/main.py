import os
import pygame
import glob
import random
import math
import time

#Knob1 = Oscilloscope Shape & Size Selector - 3 divisions
#Knob2 = Size of 'Trails'
#Knob3 = 'Trails' Opacity
#Knob4 = Foreground Color - 8 positions
#Knob5 = Background Color

last_screen = pygame.Surface((1280,720))
xr = 320
yr = 240
lines = 100

def setup(screen, eyesy) :
    global last_screen, xr, yr
    
    xr = eyesy.xres
    yr = eyesy.yres
    last_screen = pygame.Surface((xr,yr))
    
    
def draw(screen, eyesy) :
    global last_screen, seg, xr, yr
    eyesy.color_picker_bg(eyesy.knob5)    


    for i in range(0, lines) :
        seg(screen, eyesy, i)
        
    lastScreenSize = xr*0.16#200

    image = last_screen
    last_screen = screen.copy()
    thingX = int(xr-(eyesy.knob2*lastScreenSize))
    thingY = int(yr-(eyesy.knob2*(lastScreenSize*0.5625)))
    placeX = int(xr/2)-int(((thingX/2)*xr)/xr)
    placeY = int(yr/2)-int(((thingY/2)*yr)/yr)

    thing = pygame.transform.scale(image, (thingX, thingY)) # mirror screen scale
    thing.set_alpha(int(eyesy.knob3 * 180)) # adjust transparency on knob3
    screen.blit(thing, (placeX, placeY)) # mirror screen scale
    
    
def seg(screen, eyesy, i) :    
    space = eyesy.xres/(lines-2)
    y0 = 0
    y1 = (eyesy.audio_in[i] / 90)
    x = i*space
    position = yr/2
    
    #set the size of the graphic elements with Knob 1:
    if eyesy.knob1 < 0.33 : 
        linewidth = int(((eyesy.knob1*3.5)*eyesy.xres)/(lines-75)+1)
        ballSize = 0 #no balls shown
    
    if eyesy.knob1 >= 0.33 and eyesy.knob1 < 0.66 :
        linewidth = 0 #no lines shown
        ballSize = int((((0.66-eyesy.knob1)*3)*eyesy.xres)/(lines-75)+1)
    
    if eyesy.knob1 >= 0.66 :
        linewidth = int(((eyesy.knob1-0.66)*1.5)*eyesy.xres/(lines-75))
        ballSize = int((((eyesy.knob1-0.66)*3)*eyesy.xres)/(lines-75))

    color = eyesy.color_picker_lfo(eyesy.knob4)
    pygame.draw.circle(screen,color,(x, y1+position),ballSize, 0)
    pygame.draw.line(screen, color, [x, y0+position], [x, y1+position], linewidth)
    
