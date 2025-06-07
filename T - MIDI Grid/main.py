import os
import pygame
import random

#Knob1 - MIDI Data (number, name, number & name, blank)
#Knob2 - Grid Settings (off, square --> circle, off)
#Knob3 - Feedback setting. all the way left is 'off'
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global xr, yr, last_screen, image, square_size, smallfont, font, corner_radius
    xr = eyesy.xres
    yr = eyesy.yres
    last_screen = pygame.Surface((xr, yr))
    image = last_screen
    square_size = (eyesy.xres * 0.9) / 16  # size of each square based on the x resolution with a border
    smallfont = pygame.font.Font(None, int(square_size / 2.2))  # Adjusted font size
    font = pygame.font.Font(None, int(square_size / 2))  # Adjusted font size
    corner_radius = 0
    

def draw(screen, eyesy):
    global xr, yr, last_screen, image, square_size, smallfont, font, corner_radius
    bg_color = eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4, 1.5)
    
    xF = 0.078 # max feedback distance in x dimension
    yF = 0.139 # max feedback distance in y dimension

    xrSm = xr - (xr * (eyesy.knob3*xF)) #sets feedback distance in x dim
    yrSm = yr - (yr * (eyesy.knob3*yF)) #sets feedback distance in y dim

    # Screengrab feedback loop
    thing = pygame.transform.scale(image, (int(xrSm), int(yrSm)))  # scales down screengrab
    if eyesy.knob3>0.1: #turn on feedback
        screen.blit(thing, (int(xr * (eyesy.knob3*(xF/2))), int(yr * (eyesy.knob3*(yF/2)))))  # re-centers screengrab

    # Square Parameters
    thickness = 1 # line thickness
    if eyesy.knob2 < 0.25:
        corner_radius = 0
    if 0.25 <= eyesy.knob2 < 0.85:
        corner_radius = int(scale_knob2_value(eyesy.knob2) * (square_size / 2))  # scaled corner radius size
    
    if eyesy.knob2 < 0.15 or eyesy.knob2 > .91:
        gridlines = False
    else:
        gridlines = True

    
    for i in range(128):
        row = i // 16
        col = i % 16
        x = col * square_size + (eyesy.xres - 16 * square_size) / 2
        y = row * square_size + (eyesy.yres - 8 * square_size) / 2

        # Draw the square
        rect = pygame.Rect(x, y, square_size, square_size)
        if eyesy.midi_notes[i]:
            pygame.draw.rect(screen, color, rect, 0, corner_radius)
        else:
            if gridlines:
                outline_color = (255, 255, 255)
                pygame.draw.rect(screen, outline_color, rect, thickness, corner_radius)

        # Determine the text to display based on knob1 value
        if eyesy.knob1 < 0.25:
            text_content = str(i)
        elif 0.25 <= eyesy.knob1 < 0.5:
            text_content = midi_note_names[127 - i]
        elif 0.5 <= eyesy.knob1 < 0.75:
            text_content = f"{i}\n{midi_note_names[127 - i]}"
        else: 
            text_content = chr(0x2003) #em space character

        # Draw the text
        if "\n" in text_content:
            # Split the text into two lines
            lines = text_content.split("\n")
            text1 = smallfont.render(lines[0], True, (255, 255, 255))
            text2 = smallfont.render(lines[1], True, (255, 255, 255))
            text_rect1 = text1.get_rect(center=(x + square_size / 2, y + square_size / 3))
            text_rect2 = text2.get_rect(center=(x + square_size / 2, y + 3 * square_size / 4.5))
            screen.blit(text1, text_rect1)
            screen.blit(text2, text_rect2)
        else:
            text = font.render(text_content, True, (255, 255, 255))
            text_rect = text.get_rect(center=(x + square_size / 2, y + square_size / 2))
            screen.blit(text, text_rect)

    # Screengrab feedback loop
    image = last_screen
    last_screen = screen.copy()

        
midi_note_names = [
    "G9", "F#9", "F9", "E9", "D#9", "D9", "C#9", "C9",
    "B8", "A#8", "A8", "G#8", "G8", "F#8", "F8", "E8", "D#8", "D8", "C#8", "C8",
    "B7", "A#7", "A7", "G#7", "G7", "F#7", "F7", "E7", "D#7", "D7", "C#7", "C7",
    "B6", "A#6", "A6", "G#6", "G6", "F#6", "F6", "E6", "D#6", "D6", "C#6", "C6",
    "B5", "A#5", "A5", "G#5", "G5", "F#5", "F5", "E5", "D#5", "D5", "C#5", "C5",
    "B4", "A#4", "A4", "G#4", "G4", "F#4", "F4", "E4", "D#4", "D4", "C#4", "C4",
    "B3", "A#3", "A3", "G#3", "G3", "F#3", "F3", "E3", "D#3", "D3", "C#3", "C3",
    "B2", "A#2", "A2", "G#2", "G2", "F#2", "F2", "E2", "D#2", "D2", "C#2", "C2",
    "B1", "A#1", "A1", "G#1", "G1", "F#1", "F1", "E1", "D#1", "D1", "C#1", "C1",
    "B0", "A#0", "A0", "G#0", "G0", "F#0", "F0", "E0", "D#0", "D0", "C#0", "C0",
    "B-1", "A#-1", "A-1", "G#-1", "G-1", "F#-1", "F-1", "E-1", "D#-1", "D-1", "C#-1", "C-1"
]


def scale_knob2_value(knob2_value):
    input_min = 0.25
    input_max = 0.80
    if knob2_value < input_min:
        return 0.0
    elif knob2_value > input_max:
        return 1.0
    else:
        return (knob2_value - input_min) / (input_max - input_min)
