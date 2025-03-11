import os
import pygame
import math
import random

# Knob1 - vertical bounce amount
# Knob2 - line width
# Knob3 - speed
# Knob4 - foreground color
# Knob5 - background color

class LFO:  # uses three arguments: start point, max, and how far each step is.

    def __init__(self, start, max, step):
        self.start = start
        self.max = max
        self.step = step
        self.current = 0
        self.direction = 1

    def update(self):
        self.current += self.step * self.direction

        # when it gets to the top, flip direction
        if self.current >= self.max:
            self.direction = -1
            self.current = self.max  # in case it steps above max

        # when it gets to the bottom, flip direction
        if self.current <= self.start:
            self.direction = 1
            self.current = self.start  # in case it steps below min

        return self.current

def setup(screen, eyesy):
    global b1, b2, b3, b4, y, xr, yr, x100, y20, draw_b1_first
    xr = eyesy.xres
    yr = eyesy.yres
    x100 = xr * 0.078 # x100 = (100 * xr) / xr
    y1 = 0
    y2 = 0
    b1 = LFO(0, xr, 10)
    b2 = LFO(0, xr, 19)
    b3 = LFO(0, yr, 2)
    draw_b1_first = True  # Initialize the draw order


def draw(screen, eyesy):
    global b1, b2, b3, y1, y2, xr, yr, x100, draw_b1_first
    eyesy.color_picker_bg(eyesy.knob5)

    y1 = eyesy.audio_in[50] / 150  # Audio in L
    y2 = eyesy.audio_in[50] / 150  # Audio in R
    color = eyesy.color_picker(eyesy.knob4)
    color2 = eyesy.color_picker((eyesy.knob4 + 0.50) % 1.00)

    width = int(eyesy.knob2 * x100) + 1

    b1.step = (eyesy.knob3 * (x100 / 3)) + 1
    b2.step = (eyesy.knob3 * (x100 / 2)) + 1
    b3.step = (eyesy.knob1 * (x100 / 9)) + 1

    posx1 = b1.update()
    posx2 = b2.update()
    rise = b3.update() + 1

    # Check if b1 LFO reaches the start or max point
    if posx1 == b1.start or posx1 == b1.max:
        # 50% chance to set draw_b1_first to True or False
        draw_b1_first = random.random() < 0.5

    # Draw based on the draw_b1_first boolean
    if draw_b1_first:
        pygame.draw.line(screen, color, [posx1, rise - y1], [posx1, rise + y1], width)
        pygame.draw.line(screen, color2, [posx2, rise - 2 * y2], [posx2, rise + 2 * y2], width * 2)
    else:
        pygame.draw.line(screen, color2, [posx2, rise - 2 * y2], [posx2, rise + 2 * y2], width * 2)
        pygame.draw.line(screen, color, [posx1, rise - y1], [posx1, rise + y1], width)
        
