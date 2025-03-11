import os
import pygame
import random

#Knob1 - rect width
#Knob2 - rect height
#Knob3 - corner shape & outline thickness 
#Knob4 - foreground color
#Knob5 - background color

trigger = False
myRect = pygame.Rect(10,10,10,10)
begin = True

def setup(screen, eyesy) :
    global xr, yr
    xr = eyesy.xres
    yr = eyesy.yres

def draw(screen, eyesy) :
    global trigger, myRect, xr, yr, begin
    eyesy.color_picker_bg(eyesy.knob5)    
    size100 = xr * 0.234 #.08#((100*xr)/1280)
    xhalf = xr/2
    yhalf = yr/2
    
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.5) 
    
    rectwidth = int((eyesy.knob1*1.5*size100)+10)
    rectheight = int((eyesy.knob2*1.5*size100)+10)
    
    myRect = pygame.Rect(myRect.topleft, (rectwidth, rectheight))
    
    
    if begin == True:
        myRect.center = (xhalf-rectwidth/2, yhalf-rectheight/2)
        myRect = pygame.Rect(myRect.center, (rectwidth, rectheight))
        begin = False
  

    if eyesy.trig :
        trigger = True
    if trigger == True :
        #Pick a new position
        set = random.randrange(0,8)
        
        if set == 0 :   #up 
            myRect.bottom = myRect.top            
        if set == 1 :   #upright
            myRect.bottomleft = myRect.topright  
        if set == 2 :   #upleft
            myRect.bottomright = myRect.topleft    
        if set == 3 :   #left
            myRect.right = myRect.left             
        if set == 4 :   #right
            myRect.left = myRect.right             
        if set == 5 :   #downright
            myRect.topleft = myRect.bottomright    
        if set == 6 :   #down
            myRect.top = myRect.bottom             
        if set == 7 :   #downleft
            myRect.topright = myRect.bottomleft  

    trigger = False    

    if myRect.center[0] <= 0-rectwidth/3 : myRect.center = (xhalf, yhalf)
    if myRect.center[0] >= xr+rectwidth/3 : myRect.center = (xhalf, yhalf)
    if myRect.center[1] <= 0-rectheight/3: myRect.center = (xhalf, yhalf)
    if myRect.center[1] >= yr+rectheight/3: myRect.center = (xhalf, yhalf)
    
    
    #Filled/Unfilled & Corner Radius Settings
    if eyesy.knob3 < .5 :
        strokeweight = int((0.5 - eyesy.knob3) * rectwidth)+1
        pygame.draw.rect(screen, color, myRect, strokeweight)
    
    if eyesy.knob3 >= .5 : 
        
        #check the corner radius not too big
        if rectwidth < xr * 0.281 : #360 : 
            corner = int(rectwidth/4)
        else: corner = int(xr * 0.068) #80
        
        strokeweight = int(abs(.5-eyesy.knob3) * (rectwidth))+1
        if int(strokeweight*2) < rectwidth and int(strokeweight*2) < rectheight : 
            pygame.draw.rect(screen, color, myRect, strokeweight, corner)
        else: 
            pygame.draw.rect(screen, color, myRect, 0, corner)
