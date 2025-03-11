import os
import pygame
import random
pList = []
raNr = 0
trigger = False

#Knob1 - x offset
#Knob2 - y offset
#Knob3 - size of polygons
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy) :
    global xr, yr, x8, y5, pList, raNr, NraNr, ten, hundert, hten, color
    xr = eyesy.xres
    yr = eyesy.yres
    raNr = int(xr * 0.016) #(20*xr)/eyesy.xres
    NraNr = int(raNr* -1)
    x8 = xr/8
    y5 = yr/5
    pList = [[(random.randrange(NraNr,raNr),random.randrange(NraNr,raNr)) for i in range(0,6)] for i in range(0,70)]
    ten = xr * 0.008 #(10*xr)/eyesy.xres
    hten = ten/2
    hundert = xr * 0.078 #(100*xr)/eyesy.xres
    color = eyesy.color_picker(eyesy.knob4)
    

def draw(screen, eyesy) :
    global trigger, pList, xr, yr, x8, y5, pList, raNr, NraNr, ten, hundert, hten, color
    eyesy.color_picker_bg(eyesy.knob5)    
    if eyesy.trig :
        trigger = True
    if trigger == True :
        pList = [[(random.randrange(NraNr,raNr),random.randrange(NraNr,raNr)) for i in range(0,6)] for i in range(0,70)]
    trigger = False
    
    for i in range(0, 7) :
        xoffset = int(eyesy.knob1*x8)
        yoffset = int(eyesy.knob2*y5)
         
        for j in range(0, 10) :
            x = (j*(x8))-(x8)
            y = (i*(y5))-(y5)
            rad = (eyesy.audio_in[j+i]*0.00003052)*hundert
            w = (eyesy.knob3*7)+1

            if (i%2) == 1 : 
                x = j*(x8)-(x8)+xoffset
                color = eyesy.color_picker(eyesy.knob4)
            if (j%2) == 1 : 
                y = i*(y5)-(y5)+yoffset
                color = eyesy.color_picker((0.4+eyesy.knob4)%1.0)
            if ((j+i)%3) == 1 : 
                color = eyesy.color_picker((0.8+eyesy.knob4)%1.0)    
                
            points = [pList[int((i*j)+hten)][t] for t in range(0,6) ]
            placePoints = [((points[k][0]*w)+x,(points[k][1]*w)+y) for k in range(0,6)]
            morphPoints = [(placePoints[0][0]-rad,placePoints[0][1]-rad),
                           (placePoints[1][0]+rad,placePoints[1][1]-rad),
                           (placePoints[2][0]+rad,placePoints[2][1]),
                           (placePoints[3][0]+rad,placePoints[3][1]+rad),
                           (placePoints[4][0],placePoints[4][1]-rad),
                           (placePoints[5][0]-rad,placePoints[5][1]+rad)]
            
            pygame.draw.polygon(screen, color, morphPoints, int(eyesy.xres * 0.0027))
