import os
import pygame
import glob
import math
import random

#Knob1 - x axis speed
#Knob2 - y axis speed
#Knob3 - image size
#Knob4 - foreground color
#Knob5 - background color

images = []
image_index = 0

trigger = False

grid1 = pygame.Surface((427,240))
grid2 = pygame.Surface((427,240))
grid3 = pygame.Surface((427,240))
grid4 = pygame.Surface((427,240))

x1_nudge=0
y1_nudge=0
x2_nudge=0
y2_nudge=0
x3_nudge=0
y3_nudge=0
x4_nudge=0
y4_nudge=0

begin = True


def setup(screen, eyesy) :
    global images, image_index, xr, yr

    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        img = pygame.image.load(filepath)
        images.append(img)
        try:
            pal = len(img.get_palette())
            print(filepath ,  " - " , len(img.get_palette()))
        except:
            print(filename ,  " no palette")
    print("loaded")

    xr = eyesy.xres
    yr = eyesy.yres

def draw(screen, eyesy) :
    global trigger, images, image_index, x1_nudge, y1_nudge, x2_nudge, y2_nudge, x3_nudge, y3_nudge, x4_nudge, y4_nudge, begin
    eyesy.color_picker_bg(eyesy.knob5)      

    xr3rd = xr/3
    yr3rd = yr/3
    xrhalf = xr/2
    yrhalf = yr/2
    
    scale_x = scale_y = int(eyesy.knob3 * (xr3rd-1) + 1) #x scale image on knob3; maximum width = 1/3 screen width
    
    #define x,y for image placement
    #x = xrhalf-(scale_x/2) 
    #y = yrhalf-(scale_y/2)
    x = (scale_x/2) 
    y = (scale_y/2)
    
    speedscalex = xr * 0.056 #(40*xr)/1280
    speedscaley = yr * 0.031 #(40*yr)/720
    x_speed = (2*speedscalex*eyesy.knob1)-speedscalex #set horizontal speed on knob1
    y_speed = (2*speedscaley*eyesy.knob2)-speedscaley #set vertical speed on knob2
    
    if begin == True:
        x1_nudge = int(random.randrange(xr*.1, xr*.4))
        y1_nudge = int(random.randrange(yr*.1, yr*.5))
        x2_nudge = int(random.randrange(xr*.1, xr*.4))
        y2_nudge = int(random.randrange(yr*.1, yr*.5))
        x3_nudge = int(random.randrange(xr*.2, xr*.4))
        y3_nudge = int(random.randrange(yr*.1, yr*.5))
        x4_nudge = int(random.randrange(xr*.2, xr*.4))
        y4_nudge = int(random.randrange(yr*.1, yr*.5))
        begin = False

    x1 = x+x1_nudge
    y1 = y+y1_nudge
    x2 = x+x2_nudge*1.25
    y2 = y+y2_nudge*1.25
    x3 = x+x3_nudge*1.5
    y3 = y+y3_nudge*1.5
    x4 = x+x4_nudge*2
    y4 = y+y4_nudge*2

    cidx = 0
    
    if eyesy.trig : #move images on trigger
        trigger = True
    if trigger == True :
        x1_nudge = (x1_nudge + x_speed)
        y1_nudge = (y1_nudge + y_speed)
        x2_nudge = (x2_nudge + x_speed)
        y2_nudge = (y2_nudge + y_speed)
        x3_nudge = (x3_nudge + x_speed)
        y3_nudge = (y3_nudge + y_speed)
        x4_nudge = (x4_nudge + x_speed)
        y4_nudge = (y4_nudge + y_speed)
        
    trigger = False
    
    #set color
    for i in range(len(images)) : 
        origimg = images[i] 
        try:
            cidx = 1
            pal = len(origimg.get_palette())
            #cidx = int(round(eyesy.knob3 * pal,0))
            origimg.set_palette_at(cidx,eyesy.color_picker_lfo(eyesy.knob4))
        except:
            cidx = 0
    
    #bring images back onto the screen once they march off:
    image = images[0]
    grid1 = pygame.transform.scale(image, (scale_x,scale_y))
    if x1 > xr : x1_nudge = -scale_x-x
    if x1 < -scale_x : x1_nudge = xr-x
    if y1 > yr : y1_nudge = -scale_y-y
    if y1 < -scale_y : y1_nudge = yr-y
    screen.blit(grid1, (x1, y1))
    
    image = images[1]
    grid2 = pygame.transform.scale(image, (scale_x,scale_y))
    if x2 > xr : x2_nudge = (-scale_x-x)/1.25
    if x2 < -scale_x : x2_nudge = (xr-x)/1.25
    if y2 > yr : y2_nudge = (-scale_y-y)/1.25
    if y2 < -scale_y : y2_nudge= (yr-y)/1.25
    screen.blit(grid2, (x2, y2))
    
    image = images[2]
    grid3 = pygame.transform.scale(image, (scale_x,scale_y))
    if x3 > xr : x3_nudge = (-scale_x-x)/1.5
    if x3 < -scale_x : x3_nudge = (xr-x)/1.5
    if y3 > yr : y3_nudge = (-scale_y-y)/1.5
    if y3 < -scale_y : y3_nudge = (yr-y)/1.5
    screen.blit(grid3, (x3, y3))
    
    image = images[3]
    grid4 = pygame.transform.scale(image, (scale_x,scale_y))
    if x4 > xr : x4_nudge = (-scale_x-x)/2+1
    if x4 < -scale_x : x4_nudge = (xr-x)/2
    if y4 > yr : y4_nudge = (-scale_y-y)/2
    if y4 < -scale_y : y4_nudge = (yr-y)/2
    screen.blit(grid4, (x4, y4))
