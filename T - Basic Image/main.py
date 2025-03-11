import os
import pygame
import glob

#Knob1 - x pos
#Knob2 - y pos
#Knob3 - scale
#Knob4 - opacity
#Knob5 - background color

#important! make sure images are scaled to display resolution beforehand; smaller is faster
images = []
image_index = 0

def setup(screen, eyesy) :
    global images, fall, bg, xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
    bg = pygame.Surface((xr,yr))

    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print('loading image file: ' + filename)
        img = pygame.image.load(filepath)
        images.append(img)

def draw(screen, eyesy) :
    global images, image_index, bg, xr, yr
    eyesy.color_picker_bg(eyesy.knob5)    
    
    if eyesy.trig :
        image_index += 1
        if image_index == len(images) : image_index = 0
        img = images[image_index]
        ximg = int(img.get_width() * eyesy.knob3)
        yimg = int(img.get_height() * eyesy.knob3)
        img = pygame.transform.scale(img, (ximg, yimg) )
        
        img.fill((255, 255, 255, eyesy.knob4 * 255), None, pygame.BLEND_RGBA_MULT)

        y = int(eyesy.knob2 * yr) - int(img.get_height() * .5)
        x = int(eyesy.knob1 * xr) - int(img.get_width() * .5)
        screen.blit(img, (x,y))
