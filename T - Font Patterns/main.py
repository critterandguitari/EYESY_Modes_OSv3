import os
import pygame
import time
import random

#Knob1 - horizontal offset
#Knob2 - size
#Knob3 - font set
#Knob4 - foreground color
#Knob5 - background color

pygame.font.init()  # Initialize the font module
count = 0
trigger = False
unistr = chr(random.randint(0x25a0, 0x25ff))
textpos = (0,0)

def setup(screen, eyesy):
    global color, size, xr, yr, y
    size = 50
    xr = eyesy.xres
    yr = eyesy.yres
    y = 0

def draw(screen, eyesy):
    global count, trigger, unistr, textpos, color, size, xr, yr, y
    eyesy.color_picker_bg(eyesy.knob5)    

    x320 = int(xr * 0.250)  #((320*xr)/1280)
    x160 = int(xr * 0.125)  #((160*xr)/1280)
    x260 = int(xr * 0.3)    #((260*xr)/1280) #but made a little bigger than original
    x80 = int(xr * 0.063)   #((80*xr)/1280)
    y90 = int(yr * 0.125)   #((90*yr)/720)
    y45 = int(yr * 0.063)   #((45*yr)/720)
    shift = int(eyesy.knob1*x320-x160)
    size = int(eyesy.knob2 * x260) + 5
    font = pygame.font.Font(eyesy.mode_root + "/font.ttf", size)
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.05) #uniform color
    text = font.render(unistr, False, (color)) # 'False' = anti-aliasing is off. turning it on will slow everthing down a lot.   
    
    if eyesy.trig :
        trigger = True
        
    if trigger == True :
        unistr = get_unicode_character(int(eyesy.knob3 * 11)+1)
        
    for j in range(0,10):
        for i in range(0,9) :
            odd = i%2
            if odd == 0 :
                x = (i * x160 + x160 + shift) - x160
                y = (j * y90) - y45
                
            if odd == 1 :
                x = (i * x160 + x160) - x160
                y = (j * y90) - y45
            
            textpos = text.get_rect(center = (x,y))
            screen.blit(text, textpos)
    trigger = False

def get_unicode_character(set) :
    
    if set == 1 :
        # geometric shapes
        return chr(random.randint(0x25a0, 0x25ff))
        
    if set == 2 :
        # arrows
        return chr(random.randint(0x219C, 0x21BB))
        
    if set == 3 :
        # math
        return chr(random.randint(0x223D, 0x224D))
        
    if set == 4 :
        # ogham
        return chr(random.randint(0x1680, 0x169C))
        
    if set == 5 :
        # box drawing
        return chr(random.randint(0x2500, 0x257f))
        
    if set == 6 :
        # Brail
        return chr(random.randint(0x2800, 0x28FF))
        
    if set == 7 :
        # I Ching
        return chr(random.randint(0x4DC2, 0x4DCF))
        
    if set == 8 :
        # from math -- sharp symbols
        return chr(random.randint(0x2A80, 0x2ABC))

    if set == 9 :
        # vai syllables
        return chr(random.randint(0xA500, 0xA62B))
    
    if set == 10 :
        #chess
        return chr(random.randint(0xE010, 0xE04F))
        
    if set == 11 :
        #different boxes
        return chr(random.randint(0x2580, 0x25AF))
        
    if set == 12 : 
        #select random glyph from the above subsets
        return chr(random.choice([
            random.randint(0x2580, 0x25AF), # Different Boxes
            random.randint(0xE010, 0xE04F), # Chess
            random.randint(0xA500, 0xA62B), # Vai syllables
            random.randint(0x2A80, 0x2ABC), # Sharp Symbols
            random.randint(0x4DC2, 0x4DCF), # I Ching
            random.randint(0x2800, 0x28FF), # Brail
            random.randint(0x2500, 0x257f), # Box Drawing
            random.randint(0x1680, 0x169C), # Ogham
            random.randint(0x223D, 0x224D), # Math
            random.randint(0x219C, 0x21BB), # Arrows
            random.randint(0x25a0, 0x25ff)  # Geometric Shapes
            ]))
