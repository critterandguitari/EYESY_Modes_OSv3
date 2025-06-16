import os
import pygame
import random

# Knob1 - Rectangle filled/outline thickness
# Knob2 - Size of feedback screen
# Knob3 - Opacity of feedback screen (turn on Persist for best viewing!)
# Knob4 - Foreground color
# Knob5 - Background color
# Trigger - New rotations for rectangles

trigger = False
rotation_states = []

def setup(screen, eyesy):
    global xr, yr, last_screen, rotation_states, num_columns, num_rows
    xr = eyesy.xres
    yr = eyesy.yres
    last_screen = pygame.Surface((xr, yr))

    # Initialize rotation states 
    num_columns = 16
    num_rows = 11
    rotation_states = [random.choice([0, 90, 180, 270]) for _ in range(num_columns * num_rows)]
    
def draw(screen, eyesy):
    global trigger, xr, yr, rotation_states, last_screen, num_columns, num_rows
    eyesy.color_picker_bg(eyesy.knob5)
    size80 = xr * 0.063  # 80 @ 1280
    xhalf = xr / 2
    yhalf = yr / 2

    color = eyesy.color_picker_lfo(eyesy.knob4, 0.5)

    rectwidth = int(size80)
    rectheight = int(size80)

    stroke = int(eyesy.knob1 * 20)

    grid = []
    for row in range(num_rows):
        for col in range(num_columns):
            rect_x = col * rectwidth
            rect_y = row * rectheight
            rect = pygame.Rect(rect_x, rect_y, rectwidth, rectheight/2)
            grid.append(rect)

    if eyesy.trig:
        trigger = True

    if trigger:
        rotation_states = []
        for rect in grid:
            angle = random.choice([0, 90, 180, 270])
            rotation_states.append(angle)

        trigger = False

    for i, rect in enumerate(grid):
        if i < len(rotation_states):
            angle = rotation_states[i]
            center = rect.center

            if angle == 90:
                rotated_rect = pygame.Rect(0, 0, rect.height, rect.width)
            elif angle == 180:
                rotated_rect = pygame.Rect(0, 0, rect.width, rect.height)
            elif angle == 270:
                rotated_rect = pygame.Rect(0, 0, rect.height, rect.width)
            else:
                rotated_rect = pygame.Rect(0, 0, rect.width, rect.height)

            rotated_rect.center = center
            pygame.draw.rect(screen, color, rotated_rect, stroke)

    lastScreenSize = xr * 0.16  # 200

    image = last_screen
    last_screen = screen.copy()
    thingX = int(xr - (eyesy.knob2 * lastScreenSize))
    thingY = int(yr - (eyesy.knob2 * (lastScreenSize * 0.5625)))
    placeX = int(xr / 2) - int(((thingX / 2) * xr) / xr)
    placeY = int(yr / 2) - int(((thingY / 2) * yr) / yr)

    thing = pygame.transform.scale(image, (thingX, thingY))  # feedback screen scale
    thing.set_alpha(int(eyesy.knob3 * 180))  # adjust transparency on knob3
    screen.blit(thing, (placeX, placeY))  # feedback screen blit

