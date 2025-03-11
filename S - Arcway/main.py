import os
import pygame
import random
import math

#knob1 - line width/length
#knob2 - rate of rotation. left half controls counter clockwise rotation; right half controls clockwise. 
#knob3 - offset of bottom disc
#knob4 - color of discs
#knob5 - background color

def setup(screen, eyesy):
    global rotation_factor, yres, xres, toplimit, leftlimit, square_x, xres_half, yres_half
    xres = eyesy.xres
    yres = eyesy.yres
    xres_half = int(eyesy.xres / 2)
    yres_half = int(eyesy.yres / 2)
    toplimit = int(yres * 0.153) #110 pixels
    leftlimit = int(xres * 0.305) #390
    square_x = int(xres * 0.391) #500
    rotation_factor = 0   # Initialize rotation factor

def draw(screen, eyesy):
    global rotation_factor, xres, yres, color, toplimit, leftlimit, square_x, xres_half, yres_half
    eyesy.color_picker_bg(eyesy.knob5) #set background
    #color2 = eyesy.color_picker_lfo(eyesy.knob4) #the color of the top 'disc'. real slow changes if outside for loop below
    
    start_angle = 0
    stop_angle = math.pi/50   
    width = int(eyesy.knob1*65)+1 #width of lines
    sizer = int(xres * 0.098)
    
    #rate of rotation
    if eyesy.knob2 <= 0.5:
            rotation_factor += eyesy.knob2*2
    else:
            rotation_factor -= (eyesy.knob2*2 - 1)
    
    rotation_detune = eyesy.knob3 #offset the bottom disc

    
    for i in range(100):
        #BOTTOM DISC
        #color of bottom disc. bounce the gradient so no hard color shifts
        if i < 49 : 
            color = eyesy.color_picker(i*.02)
        else:
            color = eyesy.color_picker((99-i)*.02)
        rect = pygame.Rect(xres_half-int(xres * 0.195), int(yres_half-(square_x/2)), square_x, square_x) #int(yres * 0.347)
        rect = rect.move((sizer*math.cos(2*math.pi*i/100)+(eyesy.audio_in[i]/500) - 0.1 * width, sizer*math.sin(2*math.pi*i/100)+(eyesy.audio_in[i]/500) - 0.1 * width))
        pygame.draw.arc(screen, color, rect, start_angle + 2*math.pi*(rotation_factor-rotation_detune), stop_angle + 2*math.pi*(rotation_factor-rotation_detune), width) 
        
        #TOP DISC
        color2 = eyesy.color_picker_lfo(eyesy.knob4) #the color of the top 'disc'
        rect = pygame.Rect(xres_half-int(xres * 0.195), int(yres_half-(square_x/2)), square_x, square_x) #int(yres * 0.347)
        rect = rect.move((sizer*math.cos(2*math.pi*i/100)+(eyesy.audio_in[i]/500) + 0.1 * width, sizer*math.sin(2*math.pi*i/100)+(eyesy.audio_in[i]/500) + 0.1 * width)) 
        pygame.draw.arc(screen, color2, rect, start_angle + 2*math.pi*rotation_factor, stop_angle + 2*math.pi*rotation_factor, width)
        
        start_angle += math.pi/50
        stop_angle += math.pi/50

