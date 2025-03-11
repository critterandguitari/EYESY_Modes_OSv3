import os
import pygame
import time
import random
import glob

#Knob1 - image size
#Knob2 - y offset
#Knob3 - circle size
#Knob4 - foreground color
#Knob5 - background color

last_point = [0, 360]
images = []
image_index = 0

def setup(screen, eyesy):
    global images, xr, yr
    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print('loading image file: ' + filename)
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)
    xr = eyesy.xres
    yr = eyesy.yres

def draw(screen, eyesy):
    global last_point, xr, yr

    eyesy.color_picker_bg(eyesy.knob5)    
    for i in range(0, 50) :
        seg(screen, eyesy, i)   

def seg(screen, eyesy, i):
    global last_point, images, xr, yr
    
    xoffset = 0
    y1 = int(eyesy.knob2 * yr) + (eyesy.audio_in[i] / 35)
    x = i * (xr * 0.0203)#((i * 26)*xr)/xr
    color = eyesy.color_picker_lfo(eyesy.knob4)
    max_circle = xr * 0.078 #((100*xr)/xr)
    image_size = 1
    circle_size = 0
    line_width = 0
    
    if eyesy.knob3 <=.5 :
        circle_size = int(eyesy.knob3 * max_circle)+1
        line_width = 0
    if eyesy.knob3 >.501 :
        circle_size = abs(max_circle-int(eyesy.knob3 * max_circle)) 
        line_width =  abs(10-int(eyesy.knob3 * 10))

    pygame.draw.circle(screen,color,(x + xoffset, y1),circle_size, line_width)

    image = images[0]
    img_w = int(image.get_width() * eyesy.knob1)
    img_h = int(image.get_height() * eyesy.knob1)
    image = pygame.transform.scale(image, (img_w,img_h) )
    screen.blit(image, (x + xoffset-(img_w/2), y1-(img_h/2)))
