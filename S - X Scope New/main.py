import os
import pygame
import math
import pygame.gfxdraw

#Knob1 - line width
#Knob2 - shadow angle & position
#Knob3 - scope angle & position
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global xr,yr,li,xr8,yr8, linewidth
    xr = eyesy.xres
    yr = eyesy.yres
    xr8 = xr/10
    yr8 = yr/10
    li = xr * 0.016 #(20*xr)/xr
    last_pointj = [0,0]
    linewidth= int(eyesy.knob1*li)+1
    

def draw(screen, eyesy):
    global xr,yr,li,xr8,yr8, linewidth
    eyesy.color_picker_bg(eyesy.knob5)
    squ = int(yr-(yr/4))
    shadow = int(eyesy.knob2*(xr * 0.094)) #int(eyesy.knob2*((120*xr)/xr))
    xshadow = math.cos((eyesy.knob2)*6.28)*shadow
    yshadow = math.sin((eyesy.knob2)*6.28)*shadow
    shadowColor = ((eyesy.bg_color[0]*eyesy.knob2)/1.1, (eyesy.bg_color[1]*eyesy.knob2)/1.1, (eyesy.bg_color[2]*eyesy.knob2)/1.1)
    linewidth= int(eyesy.knob1*li)+1
    gixoff =  int((xr-squ)/2)
    gjxoff =  int(((xr-squ)/2)+squ)
    
    for i in range(0, 30) : #shadow L-R
        
        xstep = int((squ / 30)+0.49999) 
        yoff = int((yr8+(yr8/3))+yshadow) *eyesy.knob3*5-yr/3 + yr/8
        auDio = int((eyesy.audio_in[i]*0.00003058) * squ)
        NauDio = auDio*-1
        color = shadowColor #eyesy.color_picker(eyesy.knob4)
        ixoff =  int(((xr-squ)/2)+xshadow)
        if i == 0 : last_pointi = [ixoff + auDio, yoff + NauDio ]
        if i == 29 :
            pygame.draw.line(screen, color, last_pointi, [(ixoff+squ) + auDio, (squ+yoff) + NauDio], linewidth)
        else :
            pygame.draw.line(screen, color, last_pointi, [((i*xstep)+ixoff) + auDio, ((i*xstep)+yoff) + NauDio], linewidth)
            last_pointi = [((i*xstep)+ixoff) + auDio, ((i*xstep)+yoff) + NauDio]
        
    for j in range(0, 30) : #shadow L-R
        
        xstep = int((squ / 30)+0.49999)  
        jxoff =  int((((xr-squ)/2)+squ)+xshadow) 
        yoff = yr/3-int((yr8+(yr8/3))+yshadow) * eyesy.knob3*5 + yr/8
        auDio = int((eyesy.audio_in[j]*0.00003058) * squ)
        NauDio = auDio*-1
        color = shadowColor #eyesy.color_picker(eyesy.knob4)
        if j == 0 : last_pointj = [jxoff + NauDio, yoff + NauDio ]
        if j == 29 :
            pygame.draw.line(screen, color, last_pointj, [ixoff + NauDio, (squ+yoff) + NauDio], linewidth)
        else :
            pygame.draw.line(screen, color, last_pointj, [(jxoff-(j*xstep)) + NauDio, ((j*xstep)+yoff) + NauDio], linewidth)
            last_pointj = [(jxoff-(j*xstep)) + NauDio, ((j*xstep)+yoff) + NauDio]
        
    for i in range(0, 30) : #LINE L-R
        
        xstep = int((squ / 30)+0.49999) 
        yoff = int(yr8+(yr8/3))*eyesy.knob3*5-yr/3 + yr/8
        auDio = int((eyesy.audio_in[i]*0.00003058) * squ)
        NauDio = auDio*-1
        color = eyesy.color_picker_lfo(eyesy.knob4)
        if i == 0 : last_pointi = [gixoff + auDio, yoff + NauDio ]
        if i == 29 :
            pygame.draw.line(screen, color, last_pointi, [(gixoff+squ) + auDio, (squ+yoff) + NauDio], linewidth)
        else :
            pygame.draw.line(screen, color, last_pointi, [((i*xstep)+gixoff) + auDio, ((i*xstep)+yoff) + NauDio], linewidth)
            last_pointi = [((i*xstep)+gixoff) + auDio, ((i*xstep)+yoff) + NauDio]
        
    for j in range(0, 30) : #LINE L-R
        
        xstep = int((squ / 30)+0.49999) 
        yoff = yr/3 - int(yr8+(yr8/3)) * eyesy.knob3*5 + yr/8
        auDio = int((eyesy.audio_in[j]*0.00003058) * squ)
        NauDio = auDio*-1
        color = eyesy.color_picker_lfo(eyesy.knob4)
        if j == 0 : last_pointj = [gjxoff + NauDio, yoff + NauDio ]
        
        if j == 29 :
            pygame.draw.line(screen, color, last_pointj, [gixoff + NauDio, (squ+yoff) + NauDio], linewidth)
        else :
            pygame.draw.line(screen, color, last_pointj, [(gjxoff-(j*xstep)) + NauDio, ((j*xstep)+yoff) + NauDio], linewidth)
            last_pointj = [(gjxoff-(j*xstep)) + NauDio, ((j*xstep)+yoff) + NauDio]
