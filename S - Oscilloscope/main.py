import os
import pygame
import time
import math

#Knob1 - line thickness
#Knob2 - y position
#Knob3 - shadow distance & opacity
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global last_point, first_point, xr,yr,x200, x110,a75,x15
    xr = eyesy.xres
    yr = eyesy.yres
    last_point = [0, (yr/2)]
    x200 = int(xr * 0.156) #int((200*xr)/xr)
    x110 = int(xr * 0.234) #int((300*xr)/xr)
    a75 = int(xr * 0.391) #int((500*xr)/xr)
    x15 = int(xr * 0.020)+1 #int((xr/50)+1)


def draw(screen, eyesy):
    global last_point, xr, yr, x200, x110, a75,x15, color
    
    eyesy.color_picker_bg(eyesy.knob5)    
    
    #Shadow 
    for i in range(0, 50) :
        bglineseg(screen, eyesy, i)
    
    #Scope
    for i in range(0, 50) :
        lineseg(screen, eyesy, i)

def lineseg(screen, eyesy, i):
    global last_point, xr, yr, x200, x110, a75, x15
    
    linewidth = int(eyesy.knob1*x110)+1
    y1 = int((eyesy.knob2 * yr) + ((eyesy.audio_in[i*2]* eyesy.yres) / 32768))
    x = i * x15
    
    #feel free to increase lfo rate to 0.1 (or higher!) if you want faster color changes
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.01) 

    if i == 0 : 
        last_point = [(x110*-1), (yr/2)]
    else :
        last_point = last_point
    
    pygame.draw.circle(screen, color, last_point, (linewidth*0.49))
    if i == 49: #add the last circle
        pygame.draw.circle(screen,color ,(x , y1) , (linewidth*0.49))
    pygame.draw.line(screen, color, last_point, [x , y1], linewidth)

    last_point = [x , y1]
    
def bglineseg(screen, eyesy, i):
    global last_point, first_point, xr,yr,x200, x110, a75,x15
    
    shadow = int(xr * 0.078)
    
    linewidth = int(eyesy.knob1*x110)+1
    y1 = int((eyesy.knob2 * yr) + ((eyesy.audio_in[i*2]* eyesy.yres) / 32768))
    x = i * x15

    if i == 0 : 
        last_point = [(x110*-1), (yr/2)]
    else :
        last_point = last_point
    col1 = (eyesy.bg_color[0]*eyesy.knob3)/1.0
    col2 = (eyesy.bg_color[1]*eyesy.knob3)/1.0
    col3 = (eyesy.bg_color[2]*eyesy.knob3)/1.0
    
    
    pygame.draw.circle(screen,(col1, col2, col3) , (last_point[0]-shadow*eyesy.knob3, last_point[1]+shadow*eyesy.knob3), (linewidth*0.49))
    if i == 49: #add the last circle
        pygame.draw.circle(screen,(col1, col2, col3) , (x-shadow*eyesy.knob3 , y1+shadow*eyesy.knob3), (linewidth*0.49))
    pygame.draw.line(screen, (col1, col2, col3), [last_point[0]-shadow*eyesy.knob3 , last_point[1]+shadow*eyesy.knob3], [x-shadow*eyesy.knob3 , y1+shadow*eyesy.knob3], linewidth)
    
    
    last_point = [x , y1]
