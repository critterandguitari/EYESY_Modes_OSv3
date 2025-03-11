import os
import pygame
import glob
import random

#Knob1 - ball size
#Knob2 - trails distance
#Knob3 - trails opacity
#Knob4 - foreground colorkn
#Knob5 - background color

def setup(screen, eyesy) :
    global last_screen, xr, yr
    
    xr = eyesy.xres
    yr = eyesy.yres
    last_screen = pygame.Surface((xr,yr))

def draw(screen, eyesy) :
    global last_screen
    eyesy.color_picker_bg(eyesy.knob5)   
    
    if eyesy.trig :
        color = eyesy.color_picker_lfo(eyesy.knob4, 0.01)
        x = random.randrange(0,xr)
        y = random.randrange(0,yr)
        pygame.draw.circle(screen,color,[x,y],int((xr * 0.078)*eyesy.knob1+10)) # ball size on knob1

    image = last_screen
    last_screen = screen.copy()

    thingX = int((xr - (xr * 0.039))*eyesy.knob2) # int((xr-50)*eyesy.knob2)
    thingY = int((yr - (yr * 0.069))*eyesy.knob2) # int((yr-50)*eyesy.knob2)
    placeX = (xr/2)-int(eyesy.knob2*(xr * 0.480)) #(xr/2)-int(eyesy.knob2*((615*xr)/1280))
    placeY = (yr/2)-int(eyesy.knob2*(yr * 0.465)) #(yr/2)-int(eyesy.knob2*((335*yr)/720))
    thing = pygame.transform.scale(image, (thingX, thingY)) # mirror screen scale
    thing.set_alpha(int(eyesy.knob3 * 180)) # adjust transparency on knob3
    screen.blit(thing, (placeX, placeY)) # mirror screen scale
