import os
import pygame
import glob
import random

#Knob1 - x pos
#Knob2 - y pos
#Knob3 - x scale
#Knob4 - y scale
#Knob5 - background color

image_index = 0

def setup(screen, eyesy) :
    global last_screen, xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    last_screen = pygame.Surface((xr,yr))
    

def draw(screen, eyesy) :
    global last_screen, xr, yr
    eyesy.color_picker_bg(eyesy.knob5)    
    cscale = int(xr*.04)
   
    
    if eyesy.trig :
        color = eyesy.color_picker((random.randrange(0,100)*.01))
        x = random.randrange(int((cscale/2)*-1),xr)
        y = random.randrange(int((cscale/2)*-1),yr)
        pygame.draw.circle(screen,color,[x,y],cscale)

    image = last_screen
    last_screen = screen.copy()
    thing = pygame.transform.scale(image, (int(eyesy.knob3 * xr), int(eyesy.knob4 * yr) ) )
    thing = pygame.transform.flip(thing, 1,0)
    screen.blit(thing, (int(eyesy.knob1 * xr), int(eyesy.knob2 * yr)))
