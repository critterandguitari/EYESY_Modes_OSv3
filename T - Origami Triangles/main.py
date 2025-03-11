import os
import pygame
import random

#Knob1 - x position
#Knob2 - y position
#Knob3 - density
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy) :
    global trigger, pointz, xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    trigger = False
    pointz = [[600,400],[640,340],[680,400]]

def draw(screen, eyesy) :
    global trigger, pointz, xr, yr
    
    eyesy.color_picker_bg(eyesy.knob5)    
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.075)
    
    posx = int(eyesy.knob1*xr)
    posy = int(eyesy.knob2*yr)
    density = int(eyesy.knob3 * (xr * 0.469))#int(eyesy.knob3*((600*eyesy.xres)/1280))
        
    if eyesy.trig :
        trigger = True
    if trigger == True :
        x = random.randrange(0,3)
        pointz[x] = (random.randrange(posx-density,posx+density+10), random.randrange(posy-density,posy+density+10))
       
    trigger = False    
    
    pygame.draw.polygon(screen, color, pointz, 0)
