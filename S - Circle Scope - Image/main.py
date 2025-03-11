import os
import pygame
import time
import random
import glob
import math

# Knob1 - image size
# Knob2 - circle size
# Knob3 - line thickness
# Knob4 - foreground color
# Knob5 - background color

images = []
image_index = 0
rotation_angle = 0  # Initial rotation angle

def setup(screen, eyesy):
    global images, xr, yr, lx, ly, begin, j
    xr = eyesy.xres
    yr = eyesy.yres
    lx = xr / 2
    ly = yr / 2
    begin = 0
    j = 0

    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print('loading image file: ' + filename)
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, eyesy):
    global xr, yr, lx, ly, rotation_angle, j, color
    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    rotation_angle += 0.75  # Increment the rotation angle for constant spinning
    for i in range(0, 50):
        if  i <= 24:
            j = j + 1
            seg(screen, eyesy, i, rotation_angle, j)
        if i >= 25:
            j = j - 1
            seg(screen, eyesy, i, rotation_angle, j)

def seg(screen, eyesy, i, angle, j):
    global images, lx, ly, xr, yr, begin, color

    xoffset = 0
    x = i * (xr / 98)

    #R = ((eyesy.knob2 * 2) * ((400 * xr) / xr)) - ((150 * xr) / xr)
    R = ((eyesy.knob2 * 2) * (xr * 0.313) - (xr * 0.117)
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

    pygame.draw.line(screen, color, [lx, ly], [rotated_x, rotated_y], int(eyesy.knob3 * 25) + 1)

    ly = rotated_y
    lx = rotated_x

    image = images[0]
    image_height = int(image.get_height() * eyesy.knob1)
    image_width = int(image.get_width() * eyesy.knob1)
    image = pygame.transform.scale(image, (image_width, image_height))
    screen.blit(image, (rotated_x - (image_width / 2), rotated_y - (image_height / 2)))
