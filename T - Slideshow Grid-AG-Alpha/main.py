import os
import pygame
import glob

# IMPORTANT -- SCALE ALL IMAGES TO SCREEN WIDTH X SCREEN HEIGHT

images = []
image_index = 0
trigger = False
bgi = pygame.Surface((1280, 720))
bgi2 = pygame.Surface((1280, 720))
last_screen = pygame.Surface((1280,720))


def setup(screen, eyesy) :
    global images, fall, bg, image_index, xr, yr

    image_index = 0
    
    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')): 
        filename = os.path.basename(filepath)
        print('loading image file: ' + filename)
        img = pygame.image.load(filepath)
        img = img.convert_alpha()
        images.append(img)

    xr = eyesy.xres
    yr = eyesy.yres

def draw(screen, eyesy) :
    global images, image_index, last_screen, nest, bgi, bgi2, trigger, xr, yr
    eyesy.color_picker_bg(eyesy.knob5)    
    trigger = False
    
    if eyesy.trig :
        trigger = True
    if trigger == True :
        image_index += 1
    if image_index == len(images) : image_index = 0
    image = images[image_index]
    
    xrhalf = xr/2
    yrhalf = yr/2
    xrSm = xrhalf
    yrSm = yrhalf
    
    scale_x=int(eyesy.knob1 * xrSm)
    scale_y=int(eyesy.knob2 * yrSm)
    recenter_x = int(xrhalf-scale_x/2)
    recenter_y = int(yrhalf-scale_y/2)
    
    bgi = pygame.transform.scale(image, (xr, yr))
    bgi2 = pygame.transform.scale(last_screen, (scale_x, scale_y )) #scales .png image    
    if (eyesy.knob4 < .25) :
        bgi2 = pygame.transform.flip(bgi2, 0,0)
    if (eyesy.knob4 > .25) and (eyesy.knob4 < .5) :
        bgi2 = pygame.transform.flip(bgi2, 0,1)
    if (eyesy.knob4 > .5) and (eyesy.knob4 < .75) :
        bgi2 = pygame.transform.flip(bgi2, 1,0)
    if (eyesy.knob4 > .75) :
        bgi2 = pygame.transform.flip(bgi2, 1,1)
        
    bgi2.set_alpha(int(eyesy.knob3 * 255))
    
    screen.blit(bgi2, (int(recenter_x), int(recenter_y)))
    screen.blit(bgi, (0, 0))
    last_screen = screen.copy()
