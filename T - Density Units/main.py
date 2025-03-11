import os
import pygame
import random

#Knob1 - rect diameter
#Knob2 - spacing
#Knob3 - filled/unfilled
#Knob4 - foreground colorkn
#Knob5 - background color

trigger = False

def setup(sscreen, eyesy):
    global pList, xr, yr, fill, corner
    xr = eyesy.xres
    yr = eyesy.yres
    x100 = int(xr * 0.078)
    y100 = int(yr * 0.139)
    pList = [(random.randrange(-1*x100,eyesy.xres+x100),random.randrange(-1*y100,eyesy.yres+y100)) for i in range(0,100)]
    fill = 0
    corner = 0

def draw(screen, eyesy):
    global trigger, pList, xr, yr
    eyesy.color_picker_bg(eyesy.knob5)    
    sizescale = int(xr * 0.156) #((200*eyesy.xres)/1280)
    xhalf = int(xr/2)#((640*eyesy.xres)/1280)
    yhalf = int(yr/2)#((360*eyesy.yres)/720)
    dscale = int(xr * 0.078) #int((100*eyesy.xres)/1280)
    size = int(eyesy.knob1*sizescale)+1
    xdensity = int(eyesy.knob2*xhalf+20)
    ydensity = int(eyesy.knob2*yhalf+20)
    
    if eyesy.knob3 < 0.5 :
        fill = int(size*eyesy.knob3)+1
        corner = int(size*(eyesy.knob3*2))
        
    if eyesy.knob3 >= 0.5:
        corner = int(size*(2-(eyesy.knob3*2)))
        fill = 0    
    
    if eyesy.trig :
        trigger = True
    
    if trigger == True :
        pList = [(random.randrange(-dscale+xdensity,eyesy.xres+dscale-xdensity+10),random.randrange(-dscale+ydensity,eyesy.yres+dscale-ydensity+10)) for i in range(0,dscale)]

    for j in range(0, 30) :     
        color = eyesy.color_picker_lfo(eyesy.knob4, 0.006)
        pygame.draw.rect(screen, color, [pList[j][0]-(size/2),pList[j][1]-(size/2),size,size], fill, corner)

    trigger = False

