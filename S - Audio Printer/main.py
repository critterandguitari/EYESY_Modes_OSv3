import os
import pygame
import random
import pygame
import math

#Knob1 - print direction & quantity (scans up, scans down, up/down)
#Knob2 - horizontal shift amount
#Knob3 - audio level (quiet - loud)
#Knob4 - foreground color
#Knob5 - background color

# Constants
xc = 100  # horizontal count (matching the length of eyesy.audio_in)
yc = 72   # vertical count

# Initialize a global list to store the history of audio input and colors
audio_history = []


def setup(screen, eyesy):
    global xr, yr, audio_history
    xr = eyesy.xres
    yr = eyesy.yres
    # Initialize the history with default values for rows
    audio_history = [[(0, (0, 0, 0))] * xc for _ in range(yc)]

def draw(screen, eyesy):
    global xr, yr, audio_history, square_size, v_square_size
    bg_color = eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4)

    # Calculate the size of each square based on the x resolution with a border
    square_size = xr / xc
    v_square_size = yr / yc

    # Square Parameters
    thickness = 1  # line thickness
    corner_radius = 0 # 0 = no radius

    # Shift the history down one row
    audio_history.pop(0)

    # set the threshold for capturing the audio input
    volume = 10000 - (eyesy.knob3 * 10000)
    
    # Create a new row based on audio input threshold
    new_row = []
    for i in range(xc):
        value = int(abs(eyesy.audio_in[i]))
        if value > volume:
            new_row.append((1, color))
        else:
            new_row.append((0, (0, 0, 0)))

    audio_history.append(new_row)

    # Calculate the horizontal shift based on knob2
    max_shift = 3.8 * square_size
    if eyesy.knob2 < 0.40: # shift left
        shift = (0.40 - eyesy.knob2) * max_shift *-1
    elif eyesy.knob2 > 0.60: # shift right
        shift = (eyesy.knob2 - 0.60) * max_shift
    else:
        shift = 0

    # Select the style of drawing the boxes (scan up, down, up/down)
    set = int(eyesy.knob1 * 2)

    for j in range(yc):
        for i in range(xc):
            x = i * square_size
            y = j * v_square_size

            # Determine the position based on the 'set'
            if set == 0:  # 2x bottom
                rect = pygame.Rect(x + ((yc - j) * shift), y, square_size, v_square_size)
            elif set == 1:  # 2x top
                rect = pygame.Rect(x + ((yc - j) * shift), yr - y - v_square_size, square_size, v_square_size)
            else:# set == 2:  # 1x top, 1x bottom
                rect = pygame.Rect(x + ((yc - j) * shift), y, square_size, v_square_size)
                rect2 = pygame.Rect(x + ((yc - j) * shift * -1), yr - y - v_square_size, square_size, v_square_size)

            audio_input, note_color = audio_history[j][i]

            if audio_input == 1:
                if set <= 1:
                    pygame.draw.rect(screen, note_color, rect, 0, corner_radius)
                else:
                    pygame.draw.rect(screen, note_color, rect, 0, corner_radius)
                    pygame.draw.rect(screen, note_color, rect2, 0, corner_radius)
