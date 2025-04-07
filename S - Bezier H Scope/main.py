import os
import pygame
import random
import pygame.gfxdraw

#Knob1 - y offset for lines
#Knob2 - x offset for lines
#Knob3 - trails
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global xr, yr, pointNumber, yhalf, margin, xoff
    global pointList1, pointList2, pointList3, pointList4, pointList5, pointList6
    global pointList7, pointList8, pointList9, pointList10, pointList11, pointList12
    
    # set up the horizontal location of scope points...#
    #...so two points are in the l & r margins (outside of the screen width) for better visuals  #
    pointNumber = 24  #total scope points
    onScreenPoints = pointNumber - 4  #scope points 'centered' on screen
    pointInterval = int(eyesy.xres / onScreenPoints) 
    xr = pointInterval * pointNumber #total width of scope
    margin = int(xr/pointNumber)*2

    yr = eyesy.yres
    yhalf = int(yr/2)
    
    xoff = 0
    
    
    # create arrays for scopes
    pointList1 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList2 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList3 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList4 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList5 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList6 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList7 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList8 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList9 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList10 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList11 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    pointList12 = [(int((xr/pointNumber)*i), int(yhalf)) for i in range(0, pointNumber)]
    
    

def draw(screen, eyesy):
    
    global xr, yr, yhalf, margin, pointNumber, xoff
    global pointList1, pointList2, pointList3, pointList4, pointList5, pointList6
    global pointList7, pointList8, pointList9, pointList10, pointList11, pointList12
    
    # set colors
    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.1)
    
    smooth = 2 # bezier curve setting

    voffset  = (eyesy.knob1*(yhalf/10)) #vertical offset
    centering = (voffset * 12)/2
    
    # set the horizontal offset of the scopes
    if eyesy.knob2 < 0.48 : 
        xoff = (0.48 - eyesy.knob2) * (eyesy.xres * -0.078) #100  ##to the left
    elif eyesy.knob2 > 0.52 :
        xoff = (eyesy.knob2 - 0.52) * (eyesy.xres * 0.078)  #100  ##to the right
  
  
    for i in range (0, pointNumber):
        
        height = int((eyesy.audio_in[i*2] * eyesy.yres) / 32768)
        spot = (int(xr/pointNumber)*i)-margin #move left side start two 'points' to the left for better visuals
        
        pointList1[i] = (spot,          (height+(yhalf-centering)) )
        pointList2[i] = (spot+(xoff),   (height+(yhalf-centering)+(voffset*1)) )
        pointList3[i] = (spot+(xoff*2), (height+(yhalf-centering)+(voffset*2)) )
        pointList4[i] = (spot+(xoff*3), (height+(yhalf-centering)+(voffset*3)) )
        pointList5[i] = (spot+(xoff*4), (height+(yhalf-centering)+(voffset*4)) )
        pointList6[i] = (spot+(xoff*5), (height+(yhalf-centering)+(voffset*5)) )
        pointList7[i] = (spot+(xoff*6), (height+(yhalf-centering)+(voffset*6)) )
        pointList8[i] = (spot+(xoff*7), (height+(yhalf-centering)+(voffset*7)) )
        pointList9[i] = (spot+(xoff*8), (height+(yhalf-centering)+(voffset*8)) )
        pointList10[i]= (spot+(xoff*9), (height+(yhalf-centering)+(voffset*9)) )
        pointList11[i]= (spot+(xoff*10), (height+(yhalf-centering)+(voffset*10)) )
        pointList12[i]= (spot+(xoff*11), (height+(yhalf-centering)+(voffset*11)) )
        
    
    
    # Draw the scopes
    pygame.gfxdraw.bezier(screen, pointList1, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList2, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList3, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList4, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList5, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList6, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList7, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList8, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList9, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList10, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList11, smooth, color)
    pygame.gfxdraw.bezier(screen, pointList12, smooth, color)
    


    
    
   #Trails
    veil = pygame.Surface((eyesy.xres,eyesy.yres))  
    veil.set_alpha(int(eyesy.knob3 * 20))
    veil.fill((eyesy.bg_color[0],eyesy.bg_color[1],eyesy.bg_color[2])) 
    screen.blit(veil, (0,0))
    
    
