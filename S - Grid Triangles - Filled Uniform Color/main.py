import os
import pygame

#Knob1 - x offset
#Knob2 - y offset
#Knob3 - size of triangles
#Knob4 - foreground color
#Knob5 - background color


def setup(screen, eyesy) :
    global xr, yr
    xr = eyesy.xres
    yr = eyesy.yres
   

def draw(screen, eyesy) :
    global xr, yr
    
    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4)

    for i in range(0, 7) :
        xoffset = int(eyesy.knob1*(xr/8))
        yoffset = int(eyesy.knob2*(yr/5))
        
        for j in range(0, 10) :
            x = (j*(xr/8))-(xr/8)
            y = (i*(yr/5))-(yr/5)
            rad = abs( (eyesy.audio_in[j-i] * 0.00003058)* (xr*0.1) )
            width = int(eyesy.knob3*(xr * 0.063))+1 #int(eyesy.knob3*(80*xr)/xr)+1

            if (i%2) == 1 : 
                x = j*(xr/8)-(xr/8)+xoffset
            if (j%2) == 1 : 
                y = i*(yr/5)-(yr/5)+yoffset
                
            points = [((x-width)-rad, (y+width)+rad), (x, (y-width)-rad), ((x+width)+rad, (y+width)+rad)]
            pygame.draw.polygon(screen, color, points) 
