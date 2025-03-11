import os
import pygame
import glob
import pygame.gfxdraw
import math

#Knob1 - x travel direction
#Knob2 - y travel direction
#Knob3 - rotation amount when triggered 
#Knob4 - foreground color
#Knob5 - background color

bkgrnd = pygame.Surface((1280, 720))
trot = 0
x1 = 640
y1 = 360
trigger = False

def setup(screen, eyesy):
    global bkgrnd, x1, y1, xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    x1 = xr/2
    y1 = yr/2
    bkgrnd = pygame.Surface((xr, yr))

def draw(screen, eyesy) :
    global bkgrnd, shape, trot, trigger, x1, y1, xr, yr
    eyesy.color_picker_bg(eyesy.knob5)    
 
    rotrate = 15-eyesy.knob3*30

    if eyesy.trig :
        trigger = True
    if trigger == True :
        trot = trot + rotrate
    trigger = False    
    
    p100 = int(xr * 0.078) #int((100*xr)/1280)
    p200 = int(xr * 0.156) #int((200*xr)/1280)
    p400 = int(xr * 0.313) #int((400*xr)/1280)

    color = eyesy.color_picker_lfo(eyesy.knob4)
    
        
    shape = pygame.Surface((p200,p400))
    pygame.gfxdraw.filled_trigon(shape, 0,p400,p100,0,p200,p400, color)    
    shape = pygame.transform.scale(shape, (p200, p400))
    shape.set_colorkey ((0,0,0))
    shape = pygame.transform.rotate(shape, trot)
    new_width = shape.get_width()
    new_height = shape.get_height()
    x = (0 + new_width / 2)
    y = (0 + new_height / 2)
    speedx = (eyesy.knob1 * 50 - 25)
    speedy = (eyesy.knob2 * 50 - 25)
    screen.blit(shape, (x1-x, y1-y ))
    
    x1 = x1 + speedx
    y1 = y1 + speedy
    if x1 < 0 : x1 = xr
    if x1 > xr : x1 = 0
    if y1 < 0 : y1 = yr
    if y1 > yr : y1 = 0
