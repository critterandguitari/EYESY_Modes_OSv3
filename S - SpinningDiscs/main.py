import os
import pygame
import glob

#this mode and images are originally from the Technobear:
#https://patchstorage.com/spinning-discs-640/

#Knob1 - rotation rate
#Knob2 - image select
#Knob3 - index color
#Knob4 - foreground color
#Knob5 - background color

image_index = 0
image_offset = 0 
images = []
angle = 0

def debug(screen, eyesy, dbg_str):
    color = eyesy.color_picker()
    font = pygame.freetype.Font(eyesy.mode_root + "/font.ttf", 16)
    (text, textpos) = font.render(dbg_str,color)
    textpos =(int(eyesy.xres*0.8), int(eyesy.ypos*0.1))
    screen.blit(text, textpos)

def setup(screen, eyesy) :
    global images, image_index
    for filepath in sorted(glob.glob(eyesy.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        img = pygame.image.load(filepath)
        images.append(img)
        try:
            pal = len(img.get_palette())
            print(filepath ,  " - " , len(img.get_palette()))
        except:
            print(filename ,  " no palette")
    print("loaded")


def draw(screen, eyesy) :
    global images, image_index, image_offset
    global angle
    
    eyesy.color_picker_bg(eyesy.knob5) 
    
    cidx = 0
    if eyesy.trig:
        image_offset += 1
        if image_offset >= len(images) : image_offset = 0
        
    image_index = int ((eyesy.knob2 * (len(images) - 1) ) + image_offset)
    if image_index >= len(images) : image_index = image_index - len(images)

    audioangle = 0
    for i in range(0,100) : audioangle +=  eyesy.audio_in[i] * 0.00035 if eyesy.audio_in[i] > 30 else 0 

    chg =   ((eyesy.knob1 * 180) + audioangle)  
    angle -= chg

    # debug(screen,eyesy,"chg " +str(chg) + "," + str(audioangle))
    #debug(screen,eyesy,str(int(chg))+ "    ")

    if angle < -360 : angle += 360
    origimg = images[image_index] 
    img = pygame.transform.rotate(images[image_index],angle)
    try:
        cidx = 1
        pal = len(origimg.get_palette())
        cidx = int(round(eyesy.knob3 * pal,0))
        img.set_palette_at(cidx,eyesy.color_picker_lfo(eyesy.knob4))
    except:
        cidx = 0


    y = int(0.5* eyesy.yres) - int(img.get_height() * .5)
    x = int(0.5 * eyesy.xres) - int(img.get_width() * .5)
    screen.blit(img, (x,y))
