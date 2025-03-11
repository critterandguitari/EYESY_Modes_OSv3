import os
import pygame
import time
import random
import glob
import math

#Knob1 - image size
#Knob2 - circle size
#Knob3 - line thickness
#Knob4 - foreground color
#Knob5 - background color

images = []
image_index = 0

def setup(screen, eyesy):
    global images,xr, yr, lx, ly, begin
    xr =eyesy.xres
    yr =eyesy.yres
    lx = xr/2
    ly = yr/2
    begin = 0 
    
    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print('loading image file: ' + filename)
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, eyesy):
    global xr,yr, lx, ly, color
    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4)
    for i in range(0, 50) :
        seg(screen, eyesy, i)
 
    
def seg(screen, eyesy, i):
    global images, lx, ly, xr, yr, begin, color
    
    xoffset = 0
    x = i * (xr/98)

    R = ((eyesy.knob2*2) * (xr * 0.313))-(xr * 0.117) #((eyesy.knob2*2)*((400*xr)/xr))-((150*xr)/xr)
    R = R + (eyesy.audio_in[i] / 100)
    x = R * math.cos((i /  50.) * 6.28) + (xr/2)
    y = R * math.sin((i /  50.) * 6.28) + (yr/2)
    
    if begin == 0: #makes it look nice at startup
        ly = y
        lx = x
        begin = 1
    
    pygame.draw.line(screen, color, [lx, ly], [x, y], int(eyesy.knob3*25)+1)
    
    ly = y
    lx = x

    image = images[2]
    image_height = int(image.get_height() * eyesy.knob1)
    image_width =int(image.get_width() * eyesy.knob1)
    image = pygame.transform.scale(image, (image_width, image_height))
    screen.blit(image, (x-(image_width/2), y-(image_height/2)))
