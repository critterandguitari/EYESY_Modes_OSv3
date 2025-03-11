import os
import pygame
xr = 0
yr = 0
x8 = 0
y5 = 0

#Knob1 - x offset
#Knob2 - y offset
#Knob3 - size of circles
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy) :
    global xr, yr, x8, y5, color
    xr = eyesy.xres
    yr = eyesy.yres
    x8 = xr/8
    y5 = yr/5
    color = eyesy.color_picker(eyesy.knob4)

def draw(screen, eyesy) :
    global xr, yr, x8, y5, color
    eyesy.color_picker_bg(eyesy.knob5)

    for i in range(0, 7) :
        xoffset = int(eyesy.knob1*(x8))
        yoffset = int(eyesy.knob2*(y5))

        for j in range(0, 10) :
            x = (j*(x8))-(x8)
            y = (i*(y5))-(y5)
            rad = abs((eyesy.audio_in[j+i] / 32768) * xr *.2)
            restRad = int(eyesy.knob3 * (xr * 0.023))+1 #30

            if (i%2) == 1 : 
                x = j*(x8)-(x8)+xoffset
                color = eyesy.color_picker(eyesy.knob4)
            if (j%2) == 1 : 
                y = i*(y5)-(y5)+yoffset
                color = eyesy.color_picker((0.4+eyesy.knob4)%1.0)
            if ((j+i)%3) == 1 : 
                color = eyesy.color_picker((0.8+eyesy.knob4)%1.0)

            pygame.draw.circle(screen, color, [x, y], rad+restRad)
