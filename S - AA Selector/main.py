import os
import pygame
import time
import random
import math

#check variables are being used. 

#Knob1 - number of layers
#Knob2 - layer offset on knob2, see below
#Knob3 - shape selector
#Knob4 - foreground color
#Knob5 - background color

size = 400
count = 0
R = 1
avg = 0
A=B=C=D=E=F=G=H=I=J=K=5

def setup(screen, eyesy):
    global x, y
    x = eyesy.xres
    y = eyesy.yres

def draw(screen, eyesy):
    global size, count, avg, x, y
    eyesy.color_picker_bg(eyesy.knob5)    
    for i in range(0, 100) :
        avg = abs(eyesy.audio_in[i]) + avg
    avg = avg / 100

    arcs = int(eyesy.knob1*9+1) #number of layers
    form = int(eyesy.knob3*6) #shape selector
    
    offset = eyesy.knob2 #layer offset on knob2, see below
    
    scaler = x * 0.781 #((1000*eyesy.xres)/eyesy.xres)
    
    color = eyesy.color_picker_lfo(eyesy.knob4)
    
    for i in range(arcs):
        
        if form < 1 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.sin(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.sin(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
    
        if 1<=form< 2 :
        
            A = abs(avg* 0.026) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.sin(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.sin(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.sin(i * .5 + time.time()))

        if 2 <= form < 3 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.tan(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
    
        if 3<=form< 4 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.cos(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.cos(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            
        if 4<=form < 5 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.tan(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
   
        if 5<=form  :
            A = abs(avg* 0.026) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.cos(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            
            
        corner = abs(int(eyesy.audio_in[1]* (eyesy.knob3*2-1)/2))
        
        x22 = x * 0.0172    #((22*eyesy.xres)/eyesy.xres)
        x86 = x * 0.0672    #((86*eyesy.xres)/eyesy.xres)
        x187 = x * 0.146    #((187*eyesy.xres)/eyesy.xres)
        x320 = x * 0.25     #((320*eyesy.xres)/eyesy.xres)
        x474 = x * 0.37     #((474*eyesy.xres)/eyesy.xres)
        x640 = x * 0.5      #((640*eyesy.xres)/eyesy.xres)
        x806 = x * 0.6296   #((806*eyesy.xres)/eyesy.xres)
        x960 = x * 0.75     #((960*eyesy.xres)/eyesy.xres)
        x1093 = x * 0.854   #((1093*eyesy.xres)/eyesy.xres)
        x1194 = x * 0.9328  #((1194*eyesy.xres)/eyesy.xres)
        x1258 = x * 0.9828  #((1258*eyesy.xres)/eyesy.xres)
        
        y12 = y * 0.0167    #((12*eyesy.yres)/eyesy.yres)
        y48 = y * 0.0667    #((48*eyesy.yres)/eyesy.yres)
        y105 = y * 0.1458   #((105*eyesy.yres)/eyesy.yres)
        y180 = y * 0.25     #((180*eyesy.yres)/eyesy.yres)
        y267 = y * 0.371    #((267*eyesy.yres)/eyesy.yres)
        y360 = y * 0.5      #((360*eyesy.yres)/eyesy.yres)
        y453 = y * 0.6291   #((453*eyesy.yres)/eyesy.yres)
        y540 = y * 0.75     #((540*eyesy.yres)/eyesy.yres)
        y615 = y * 0.8541   #((615*eyesy.yres)/eyesy.yres)
        y672 = y * 0.9333   #((672*eyesy.yres)/eyesy.yres)
        y708 = y * 0.9833   #((708*eyesy.yres)/eyesy.yres)
        
    #top arc
        pygame.draw.lines(screen, color, False, [[0, corner], [x22, A], [x86, B], [x187, C], [x320, D], [x474, E], [x640, F], [x806, G], [x960, H], [x1093, I], [x1194, J], [x1258, K], [x, corner]], 1)
    #bottom arc
        pygame.draw.lines(screen, color, False, [[0, y-corner], [x22, y-A], [x86, y-B], [x187, y-C], [x320, y-D], [x474, y-E], [x640, y-F], [x806, y-G], [x960, y-H], [x1093, y-I], [x1194, y-J], [x1258, y-K], [x,y-corner]], 1)
    #right arc
        pygame.draw.lines(screen, color, False, [[x+corner, 0], [x-A, y12], [x-B, y48], [x-C, y105], [x-D, y180], [x-E, y267], [x-F, y360], [x-G, y453], [x-H, y540], [x-I, y615], [x-J, y672], [x-K, y708], [x-corner, y]], 1)
    #left arc
        pygame.draw.lines(screen, color, False, [[corner, 0], [A, y12], [B, y48], [C, y105], [D, y180], [E, y267], [F, y360], [G, y453], [H, y540], [I, y615], [J, y672], [K, y708], [corner, y]], 1)

