import os
import pygame

#Knob1 - number of boxes
#Knob2 - box width
#Knob3 - box fill/line width
#Knob4 - foreground color
#Knob5 - background color

def setup(screen, eyesy):
    global min_height, yhalf, corner, fill
    min_height = 5
    yhalf = (eyesy.yres / 2)
    corner = 0
    fill = 0 

def draw(screen, eyesy):
    global min_height, yhalf, corner, fill
    
    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    #number of vu boxes
    precount = int(((eyesy.knob1*80)+20)) 
    count = check_even(precount) #keep it even for xres division

    spacing = eyesy.xres / count
    
    box_width = int(eyesy.knob2 * (spacing))+2
    box_width_half = int(box_width/2)
    box_offset = int((spacing-box_width)/2)
    
    #draw vu_boxes!
    for i in range(count):
        height = int(abs(eyesy.audio_in[i] * eyesy.yres / 32768) + min_height)
        
        #fill/stroke width & corner size
        if eyesy.knob3 < 0.5 :
            fill = int(box_width_half*eyesy.knob3)+1
            
            if height <= (min_height+fill)*2 :
                corner = int(0)
            else: corner = int(box_width_half*(eyesy.knob3*2))
        if eyesy.knob3 >= 0.5 :
            corner = int(box_width_half*(2-(eyesy.knob3*2)))
            fill = 0    
        
        vu_box = pygame.Rect(int((i*spacing)+box_width_half+box_offset), yhalf-(height/2), box_width, int(height))
        vu_box.centerx = vu_box.centerx - box_width_half
        pygame.draw.rect(screen, color, vu_box, fill, corner)


def check_even(number):
    # Initialize the last even number as 2
    if not hasattr(check_even, "last_even"):
        check_even.last_even = 2

    # Check if the number is even
    if number % 2 == 0:
        check_even.last_even = number
        return number
    else:
        return check_even.last_even
