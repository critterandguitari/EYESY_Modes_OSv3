import os
import pygame
import random


#Knob1 - number/location of MIDI Note Stream (bottom, top, top&bottom, 2xtop&bottom )
#Knob2 - Angle
#Knob3 - Square --> Circle
#Knob4 - foreground color
#Knob5 - background color

xc = 128 # horizontal count
yc = 72 # vertical count

# Initialize a global list to store the history of MIDI notes and colors
midi_history = []

def setup(screen, eyesy):
    global xr, yr, midi_history
    xr = eyesy.xres
    yr = eyesy.yres
    # Initialize the history with default values for rows
    midi_history = [[(False, (0, 0, 0))] * xc for _ in range(yc)]

def draw(screen, eyesy):
    global xr, yr, midi_history
    bg_color = eyesy.color_picker_bg(eyesy.knob5)

    # Calculate the size of each square based on the x resolution with a border
    square_size = xr / xc
    v_square_size = yr / yc 

    color = eyesy.color_picker_lfo(eyesy.knob4)

    # Square Parameters
    thickness = 1  # line thickness
    corner_radius = int(eyesy.knob3 * (square_size / 2))  # corner radius size

    # Shift the history down one row
    midi_history.pop(0)
    midi_history.append([(eyesy.midi_notes[i], color) for i in range(128)])
    
    # Calculate the shift based on knob1
    max_shift = 1.8 * square_size
    shift = eyesy.knob2 * max_shift

    
    set = int(eyesy.knob1 * 3)

    for j in range(yc):
        for i in range(xc):
            x = i * square_size
            y = j * v_square_size  
            
            # Draw the square 
            if set == 0: # 2x bottom
                rect = pygame.Rect(x+((72-j)*shift), y, square_size, v_square_size)
                rect2 = pygame.Rect(x+((72-j)*shift*-1), y, square_size, v_square_size) #original
            elif set == 1:  # 2x top
                rect =  pygame.Rect(x+((72-j)*shift),    yr-y-square_size, square_size, v_square_size) 
                rect2 = pygame.Rect(x+((72-j)*shift*-1), yr-y-square_size, square_size, v_square_size) 
                #rect = pygame.Rect(x+((72-j)*shift), y, yr-y-square_size, square_size) ## this make it grow horizontally
            elif set == 2:  # 1x top, 1x bottom
                rect = pygame.Rect(x+((yc-j)*shift), y, square_size, v_square_size)
                rect2 = pygame.Rect(x+((yc-j)*shift*-1), yr-y-square_size, square_size, v_square_size) #top
            else: # 2x top & 2x bottom 
                rect = pygame.Rect(x+((72-j)*shift), y, square_size, v_square_size) #bottom
                rect2 = pygame.Rect(x+((72-j)*shift*-1), y, square_size, v_square_size) #original #bottom
                rect3 =  pygame.Rect(x+((72-j)*shift),    yr-y-square_size, square_size, v_square_size) #top
                rect4 = pygame.Rect(x+((72-j)*shift*-1), yr-y-square_size, square_size, v_square_size) #top
 
            midi_note, note_color = midi_history[j][i]
            if midi_note:
                if set <= 2:
                    pygame.draw.rect(screen, note_color, rect, 0, corner_radius)
                    pygame.draw.rect(screen, note_color, rect2, 0, corner_radius)
                else:
                    pygame.draw.rect(screen, note_color, rect, 0, corner_radius)
                    pygame.draw.rect(screen, note_color, rect2, 0, corner_radius)
                    pygame.draw.rect(screen, note_color, rect3, 0, corner_radius)
                    pygame.draw.rect(screen, note_color, rect4, 0, corner_radius)

            
