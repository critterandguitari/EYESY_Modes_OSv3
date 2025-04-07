import os
import pygame
import random
import pygame.gfxdraw

# Knob1 - x offset for lines
# Knob2 - y offset for lines
# Knob3 - trails
# Knob4 - foreground color
# Knob5 - background color

def setup(screen, eyesy):
    global yr, xr, pointNumber, xhalf, margin, yoff
    global pointList1, pointList2, pointList3, pointList4, pointList5, pointList6
    global pointList7, pointList8, pointList9, pointList10, pointList11, pointList12

    # set up the vertical location of scope points...
    # ...so two points are in the top & bottom margins (outside of the screen height) for better visuals
    pointNumber = 24  # total scope points
    onScreenPoints = pointNumber - 4  # scope points 'centered' on screen
    pointInterval = int(eyesy.yres / onScreenPoints)
    yr = pointInterval * pointNumber  # total height of scope
    margin = int(yr / pointNumber) * 2

    xr = eyesy.xres
    xhalf = int(xr / 2)

    yoff = 0

    # create arrays for scopes
    pointList1 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList2 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList3 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList4 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList5 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList6 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList7 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList8 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList9 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList10 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList11 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]
    pointList12 = [(int(xhalf), int((yr / pointNumber) * i)) for i in range(0, pointNumber)]

def draw(screen, eyesy):
    global yr, xr, xhalf, margin, pointNumber, yoff
    global pointList1, pointList2, pointList3, pointList4, pointList5, pointList6
    global pointList7, pointList8, pointList9, pointList10, pointList11, pointList12

    # set colors
    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.1)

    smooth = 2  # bezier curve step interpolation setting

    hoffset = (eyesy.knob1 * (xhalf / 10))  # horizontal offset
    centering = (hoffset * 12) / 2

    # set the vertical offset of the scopes
    if eyesy.knob2 < 0.48:
        yoff = (0.48 - eyesy.knob2) * (eyesy.yres * -0.078)  # 100  ##to the top
    elif eyesy.knob2 > 0.52:
        yoff = (eyesy.knob2 - 0.52) * (eyesy.yres * 0.078)  # 100  ##to the bottom

    for i in range(0, pointNumber):
        width = int((eyesy.audio_in[i * 2] * eyesy.xres) / 32768)
        spot = (int(yr / pointNumber) * i) - margin  # move top side start two 'points' to the top for better visuals

        pointList1[i] = ((width + (xhalf - centering)), spot)
        pointList2[i] = ((width + (xhalf - centering) + (hoffset * 1)), spot + (yoff))
        pointList3[i] = ((width + (xhalf - centering) + (hoffset * 2)), spot + (yoff * 2))
        pointList4[i] = ((width + (xhalf - centering) + (hoffset * 3)), spot + (yoff * 3))
        pointList5[i] = ((width + (xhalf - centering) + (hoffset * 4)), spot + (yoff * 4))
        pointList6[i] = ((width + (xhalf - centering) + (hoffset * 5)), spot + (yoff * 5))
        pointList7[i] = ((width + (xhalf - centering) + (hoffset * 6)), spot + (yoff * 6))
        pointList8[i] = ((width + (xhalf - centering) + (hoffset * 7)), spot + (yoff * 7))
        pointList9[i] = ((width + (xhalf - centering) + (hoffset * 8)), spot + (yoff * 8))
        pointList10[i] = ((width + (xhalf - centering) + (hoffset * 9)), spot + (yoff * 9))
        pointList11[i] = ((width + (xhalf - centering) + (hoffset * 10)), spot + (yoff * 10))
        pointList12[i] = ((width + (xhalf - centering) + (hoffset * 11)), spot + (yoff * 11))

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

    # Trails
    veil = pygame.Surface((eyesy.xres, eyesy.yres))
    veil.set_alpha(int(eyesy.knob3 * 20))
    veil.fill((eyesy.bg_color[0], eyesy.bg_color[1], eyesy.bg_color[2]))
    screen.blit(veil, (0, 0))
