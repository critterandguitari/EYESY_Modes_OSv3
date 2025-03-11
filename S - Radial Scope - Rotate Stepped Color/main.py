import os
import pygame
import time
import random
import math

# Knob1 - rotation rate and direction
# Knob2 - scope diameter 
# Knob3 - line width & circle size
# Knob4 - foreground color
# Knob5 - background color

rotation_angle = 0  # Initial rotation angle

def setup(screen, eyesy):
    global xr, yr, xr2, yr2, x800, x20, lx, ly, color_rate
    xr = eyesy.xres
    yr = eyesy.yres
    yr2 = yr * 0.5
    xr2 = xr * 0.5
    x800 = xr * 0.625  # (800*xr)/xr #at 1280, x800 = 800
    x20 = xr * .016  # (20*xr)/xr
    lx = xr / 2
    ly = yr / 2
    color_rate = 0

def draw(screen, eyesy):
    global xr, yr, xr2, yr2, x800, x20, rotation_angle, lx, ly, color_rate
    eyesy.color_picker_bg(eyesy.knob5)

    # Control rotation rate and direction with eyesy.knob1
    if 0.48 <= eyesy.knob1 <= 0.52:
        rotation_increment = 0  # No rotation
    else:
        rotation_increment = (eyesy.knob1 - 0.5) * 25  # Map knob1 value from 0-1 to -1 to 1

    rotation_angle += rotation_increment  # Increment the rotation angle based on knob1
    
    for i in range(0, 75):
        seg(screen, eyesy, i, rotation_angle)
    
    #print(color_rate)

def seg(screen, eyesy, i, angle):
    global xr, yr, xr2, yr2, x800, x20, color_rate
    
    #color_rate = (color_rate+(eyesy.knob4*.25)) %1.0 #can be synced with rotation rate
    #color_rate = (i*0.0133)%1 #once around
    color_rate = (i*(1/(75*(eyesy.knob4+0.001))))%1 #this is the jam
    color = eyesy.color_picker(color_rate)
    
    R1 = int(eyesy.knob2 * x800)
    R = R1 + (abs(eyesy.audio_in[i]) / ((x800 * 20 / (R1 + 1)) + 1))
    x = R * math.cos((i / 75.) * 6.28) + xr2
    y = R * math.sin((i / 75.) * 6.28) + yr2

    sel = eyesy.knob3 * 2
    max_circle = x20
    circle_size = 0
    line_width = 0

    # Apply rotation
    rad_angle = math.radians(angle)

    rotated_x = (x - xr / 2) * math.cos(rad_angle) - (y - yr / 2) * math.sin(rad_angle) + xr / 2
    rotated_y = (x - xr / 2) * math.sin(rad_angle) + (y - yr / 2) * math.cos(rad_angle) + yr / 2

    if sel < 1:
        line_width = int((1-sel) * x20) + 1
        circle_size = int((1-sel) * (x20 - 2)) + 1
        pygame.draw.line(screen, color, [xr2, yr2], [rotated_x, rotated_y], line_width)
        pygame.draw.circle(screen, color, (int(rotated_x), int(rotated_y)), int(circle_size), 0)
    if sel >= 1:
        line_width = int((sel-1) * x20) + 1
        circle_size = 0
        pygame.draw.line(screen, color, [xr2, yr2], [rotated_x, rotated_y], line_width)
        

