import os
import pygame
import math
import random
from collections import deque

#Knob1 - Audio 'history' length - turn it up for 'smoother' colors
#Knob2 - bar width
#Knob3 - y position: switches between horizontal & veritical orientation
#Knob4 - [not used]
#Knob5 - background color

# Initialize a global dictionary to store audio history for each index
audio_history = {}
current_history_length = None

def setup(screen, eyesy):
    global min_height, corner, fill, yr, xr
    min_height = 5
    corner = 0
    fill = 0
    yr = eyesy.yres
    xr = eyesy.xres

def draw(screen, eyesy):
    global min_height, corner, fill, audio_history, yr, xr,current_history_length

    eyesy.color_picker_bg(eyesy.knob5)

    # Number of vu boxes
    count = 100

    spacing = eyesy.xres / count
    box_width = int(eyesy.knob2 * (spacing)) + 2
    box_offset = int((spacing - box_width) / 2)

    history_length = int((eyesy.knob1 * 20) + 1)

    # Check if history_length has changed
    if current_history_length != history_length:
        current_history_length = history_length
        # Recreate deques with the new maxlen
        for i in audio_history:
            # Convert the existing deque to a list and create a new deque with the new maxlen
            audio_history[i] = deque(list(audio_history[i]), maxlen=history_length)

    # Draw vu_boxes!
    for i in range(count):
        current_value = abs(eyesy.audio_in[i] / 32768)

        # Initialize history deque for the index if not already present
        if i not in audio_history:
            audio_history[i] = deque(maxlen=history_length)

        # Append the current value to the history
        audio_history[i].append(current_value)

        # Calculate the average of the history
        average_value = sum(audio_history[i]) / len(audio_history[i])
        color = eyesy.color_picker(average_value)

        #Set vertical position
        v_place = eyesy.knob3 * yr

        # Calculate the x position with consistent spacing
        x_position = int(i * spacing + box_offset)
        xx_position = int(-i * spacing - box_offset-spacing)

        # Draw a single box for each audio input
        vu_box = pygame.Rect(x_position, 0 + v_place, box_width, yr+v_place)
        pygame.draw.rect(screen, color, vu_box, 0)
        
        # Draw a single box for each audio input --- Horizontal
        vu_box = pygame.Rect(0,xx_position+ v_place, xr, box_width)
        pygame.draw.rect(screen, color, vu_box, 0)
        
        # Draw a single box for each audio input
        vu_box = pygame.Rect(x_position,0+v_place,box_width,yr+v_place)
        pygame.draw.rect(screen, color, vu_box, 0)
