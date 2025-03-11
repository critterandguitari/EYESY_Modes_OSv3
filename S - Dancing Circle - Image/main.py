import os
import pygame
import time
import random
import glob
import math

#Knob1 - image size
#Knob2 - diameter of 'dance'
#Knob3 - circle size & unfilled/filled option
#Knob4 - foreground color
#Knob5 - background color

last_point = [0, 360]
i = 0
images = []
image_index = 0
lx = 0
ly = 0

def setup(screen, eyesy):
    global images, xr, yr, last_point
    xr = eyesy.xres
    yr = eyesy.yres
    last_point = [0, yr/2]
    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print('loading image file: ' + filename)
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, eyesy):
    global last_point, images, i, lx, ly, xr,yr
    eyesy.color_picker_bg(eyesy.knob5)
    #x300 = int((300*xr)/eyesy.xres)
    x300 = int(0.5*eyesy.xres)
    #x30 = int((30*xr)/eyesy.xres)
    x30 = int(0.2*eyesy.xres)
    xoffset = 0
    y1 = int(eyesy.knob2 * yr) + ((eyesy.audio_in[i]*0.00003058) *(yr/2))
    x = i * (xr/100)
    color = eyesy.color_picker_lfo(eyesy.knob4)

    R = (eyesy.knob2*x300)-(x300)
    R = R + ((eyesy.audio_in[i]*0.00003058)*(yr/2))
    x = R * math.cos((i /  100.) * 6.28) + (xr/2)
    y = R * math.sin((i /  100.) * 6.28) + (yr/2)
    
    max_circle = x300
    image_size = 1
    circle_size = 0
    line_width = 0
    if eyesy.knob3 <=.5 :
        circle_size = int(eyesy.knob3 * max_circle)
        line_width = 0
    if eyesy.knob3 >.501 :
        circle_size = abs(max_circle-int(eyesy.knob3 * max_circle)) 
        line_width =  abs(x30-int(eyesy.knob3 * x30))
    
    pygame.draw.circle(screen,color,(int(x),int(y)), circle_size, line_width)
    image = images[0]
    image_w = int(image.get_width() * eyesy.knob1*6)
    image_h = int(image.get_height() * eyesy.knob1*6)
    image = pygame.transform.scale(image, (image_w, image_h))
    screen.blit(image, (x-(image_w/2), y-(image_h/2)))
    
    i = (i + 1) % 100
