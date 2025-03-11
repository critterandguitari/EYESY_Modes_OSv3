import os
import pygame
import time
import random
import glob
import math

#R & crad

# Knob1 - line & circle sizes
# Knob2 - scope diameter
# Knob3 - rotation rate
# Knob4 - foreground color
# Knob5 - background color

rotation_angle = 0  # Initial rotation angle

def setup(screen, eyesy):
    global xr, yr, lx, ly, begin, j
    xr = eyesy.xres
    yr = eyesy.yres
    lx = xr / 2
    ly = yr / 2
    begin = 0
    j = 0

def draw(screen, eyesy):
    global xr, yr, lx, ly, rotation_angle, j
    eyesy.color_picker_bg(eyesy.knob5)

    # Determine the rotation speed and direction based on eyesy.knob4
    if eyesy.knob3 < 0.48:
        rotation_angle -= (0.48 - eyesy.knob3) * 50  # Counter-clockwise
    elif eyesy.knob3 > 0.52:
        rotation_angle += (eyesy.knob3 - 0.52) * 50  # Clockwise

    for i in range(0, 50):
        if i <= 24:
            j = j + 1
            seg(screen, eyesy, i, rotation_angle, j)
        if i >= 25:
            j = j - 1
            seg(screen, eyesy, i, rotation_angle, j)

def seg(screen, eyesy, i, angle, j):
    global images, lx, ly, xr, yr, begin

    crad = xr * 0.016 #((20 * eyesy.xres) / eyesy.xres)
    xoffset = 0
    x = i * (xr / 98)

    
    sizer = eyesy.knob1*3
    if sizer < 1 :
        line_size = 1
        circ_size = sizer*2 * crad
    if sizer >= 1 and sizer <= 2 :
        line_size = (sizer - 1)*22+1
        circ_size = 0
    if sizer > 2 : 
        line_size = (sizer - 2)*22+1
        circ_size = (sizer - 2) *2* crad+3

    R = ((eyesy.knob2*2) * (xr * 0.313))-(xr * 0.117)#R = ((eyesy.knob2 * 2) * ((400 * xr) / xr)) - ((150 * xr) / xr)
    R = R + (eyesy.audio_in[j] / 100)
    x = R * math.cos((i / 50.) * 6.28) + (xr / 2)
    y = R * math.sin((i / 50.) * 6.28) + (yr / 2)

    # Apply rotation
    rad_angle = math.radians(angle)
    rotated_x = (x - xr / 2) * math.cos(rad_angle) - (y - yr / 2) * math.sin(rad_angle) + xr / 2
    rotated_y = (x - xr / 2) * math.sin(rad_angle) + (y - yr / 2) * math.cos(rad_angle) + yr / 2

    if begin == 0:  # makes it look nice at startup
        ly = rotated_y
        lx = rotated_x
        begin = 1

    color = eyesy.color_picker(((i * eyesy.knob4)+.5)%1)
    pygame.draw.line(screen, color, [lx, ly], [rotated_x, rotated_y], int(line_size))

    ly = rotated_y
    lx = rotated_x

    pygame.draw.circle(screen, color, [int(rotated_x), int(rotated_y)], int(circ_size), 0)