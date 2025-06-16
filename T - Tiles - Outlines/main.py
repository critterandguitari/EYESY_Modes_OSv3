import pygame
import math
import random

# Knob1 - Number of displayed tiles
# Knob2 - Size of feedback screen
# Knob3 - Opacity of feedback screen (turn on Persist for best viewing!)
# Knob4 - Foreground Color
# Knob5 - Background Color
# Trigger - Generates new tiles

# Initialize trigger, grid points, and rotation speeds
trigger = False
grid_points = []
grid_rotation_speeds = []

color_rate=0

def setup(screen, eyesy):
    global xr, yr, xhalf, yhalf, grid_points, grid_rotation_speeds, last_screen
    
    xr = eyesy.xres
    yr = eyesy.yres
    xhalf = xr / 2
    yhalf = yr / 2
    last_screen = pygame.Surface((xr, yr))

    cols, rows = 16, 11
    size80 = xr * 0.063

    grid_points = [[None for _ in range(cols)] for _ in range(rows)]
    grid_rotation_speeds = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):

            x = col * size80
            y = row * size80
            square_rect = pygame.Rect(x, y, size80, size80)
            
            # Define initial polygon points for each square
            polygon_points1 = [square_rect.topright, square_rect.midtop, square_rect.center, square_rect.bottomright]   
            polygon_points2 = [square_rect.topleft, square_rect.midtop, square_rect.center, square_rect.bottomleft]
            polygon_points3 = [square_rect.topleft, square_rect.midtop, square_rect.midright, square_rect.center]
            polygon_points4 = [square_rect.midtop, square_rect.topright, square_rect.center, square_rect.midleft]
            polygon_points5 = [square_rect.midtop, square_rect.midleft, square_rect.midright, square_rect.midbottom, square_rect.bottomleft, square_rect.topright]
            polygon_points6 = [square_rect.topright, square_rect.center, square_rect.midright, square_rect.midbottom, square_rect.bottomright]
            polygon_points7 = [square_rect.topright, square_rect.midright, square_rect.center, square_rect.midtop] 
            polygon_points8 = [square_rect.topright, square_rect.midright, square_rect.midleft, square_rect.bottomleft, square_rect.midbottom, square_rect.midtop]
            polygon_points9 = [square_rect.topleft, square_rect.midtop, square_rect.midright, square_rect.midleft, square_rect.midbottom, square_rect.bottomright]
            polygon_points10 = [square_rect.topleft, square_rect.center, square_rect.midleft, square_rect.midbottom, square_rect.bottomleft]
            polygon_points11 = [square_rect.midtop, square_rect.midbottom, square_rect.midright, square_rect.midleft]
            polygon_points12 = [square_rect.midtop, square_rect.midbottom, square_rect.midleft, square_rect.midright]
            polygon_points13 = [square_rect.topright, square_rect.midright, square_rect.center, square_rect.midbottom, square_rect.bottomleft]
            polygon_points14 = [square_rect.topleft, square_rect.midleft, square_rect.center, square_rect.midbottom, square_rect.bottomright]
            polygon_points15 = [square_rect.topleft, square_rect.bottomleft, square_rect.center, square_rect.midbottom, square_rect.midright, square_rect.center, square_rect.midtop]
            polygon_points16 = [square_rect.topright, square_rect.bottomright, square_rect.center, square_rect.midbottom, square_rect.midleft, square_rect.center, square_rect.midtop]          
            polygon_points17 = [square_rect.topright, square_rect.bottomright, square_rect.midbottom, square_rect.midtop]
            polygon_points18 = [square_rect.midtop, square_rect.midbottom, square_rect.bottomright, square_rect.topleft]
            polygon_points19 = [square_rect.midtop, square_rect.midbottom, square_rect.bottomleft, square_rect.topright]
            
            #pointlist = [polygon_points1, polygon_points2, polygon_points3, polygon_points4, polygon_points5, polygon_points6, polygon_points7, polygon_points8]
            pointlist = [
                polygon_points1, polygon_points2, polygon_points3, polygon_points4, polygon_points5, polygon_points6, 
                polygon_points7, polygon_points8, polygon_points9, polygon_points10, polygon_points11, polygon_points12, 
                polygon_points13, polygon_points14, polygon_points15, polygon_points16, polygon_points17, polygon_points18, polygon_points19
            ]
            
            
            # Set initial points for each cell
            points = random.choice(pointlist)
            angle = random.choice([0, 90, 180, 270])
            center = square_rect.center
            grid_points[row][col] = [rotate_point(center, point, angle) for point in points]

def rotate_point(center, point, angle):
    """Rotate a point around a center by a given angle."""
    angle_rad = math.radians(angle)
    x, y = point
    cx, cy = center

    # Translate point to origin
    tx = x - cx
    ty = y - cy

    # Apply rotation
    rotated_x = tx * math.cos(angle_rad) - ty * math.sin(angle_rad)
    rotated_y = tx * math.sin(angle_rad) + ty * math.cos(angle_rad)

    # Translate back
    return rotated_x + cx, rotated_y + cy

def draw(screen, eyesy):
    global trigger, grid_points, grid_rotation_speeds, last_screen, last_num_columns_to_draw, color_rate

    eyesy.color_picker_bg(eyesy.knob5)

    cols, rows = 16, 11

    # Map knob1 value to an integer between 5 and 16
    num_columns_to_draw = int(5 + eyesy.knob1 * 11)

    # Auto-trigger if the number of columns to draw has changed
    if 'last_num_columns_to_draw' not in globals() or num_columns_to_draw != last_num_columns_to_draw:
        trigger = True
        last_num_columns_to_draw = num_columns_to_draw

    # Calculate the size of each column based on the number of columns to draw
    size80 = xr / num_columns_to_draw

    stroke = 3

    if eyesy.trig:
        trigger = True

    for row in range(rows):
        for col in range(min(num_columns_to_draw, cols)):  # Only draw up to num_columns_to_draw

            x = col * size80
            y = row * size80
            square_rect = pygame.Rect(x, y, size80, size80)

            # Define initial polygon points for each square
            polygon_points1 = [square_rect.topright, square_rect.midtop, square_rect.center, square_rect.bottomright]   
            polygon_points2 = [square_rect.topleft, square_rect.midtop, square_rect.center, square_rect.bottomleft]
            polygon_points3 = [square_rect.topleft, square_rect.midtop, square_rect.midright, square_rect.center]
            polygon_points4 = [square_rect.midtop, square_rect.topright, square_rect.center, square_rect.midleft]
            polygon_points5 = [square_rect.midtop, square_rect.midleft, square_rect.midright, square_rect.midbottom, square_rect.bottomleft, square_rect.topright]
            polygon_points6 = [square_rect.topright, square_rect.center, square_rect.midright, square_rect.midbottom, square_rect.bottomright]
            polygon_points7 = [square_rect.topright, square_rect.midright, square_rect.center, square_rect.midtop] 
            polygon_points8 = [square_rect.topright, square_rect.midright, square_rect.midleft, square_rect.bottomleft, square_rect.midbottom, square_rect.midtop]
            polygon_points9 = [square_rect.topleft, square_rect.midtop, square_rect.midright, square_rect.midleft, square_rect.midbottom, square_rect.bottomright]
            polygon_points10 = [square_rect.topleft, square_rect.center, square_rect.midleft, square_rect.midbottom, square_rect.bottomleft]
            polygon_points11 = [square_rect.midtop, square_rect.midbottom, square_rect.midright, square_rect.midleft]
            polygon_points12 = [square_rect.midtop, square_rect.midbottom, square_rect.midleft, square_rect.midright]
            polygon_points13 = [square_rect.topright, square_rect.midright, square_rect.center, square_rect.midbottom, square_rect.bottomleft]
            polygon_points14 = [square_rect.topleft, square_rect.midleft, square_rect.center, square_rect.midbottom, square_rect.bottomright]
            polygon_points15 = [square_rect.topleft, square_rect.bottomleft, square_rect.center, square_rect.midbottom, square_rect.midright, square_rect.center, square_rect.midtop]
            polygon_points16 = [square_rect.topright, square_rect.bottomright, square_rect.center, square_rect.midbottom, square_rect.midleft, square_rect.center, square_rect.midtop]
            polygon_points17 = [square_rect.topright, square_rect.bottomright, square_rect.midbottom, square_rect.midtop]
            polygon_points18 = [square_rect.midtop, square_rect.midbottom, square_rect.bottomright, square_rect.topleft]
            polygon_points19 = [square_rect.midtop, square_rect.midbottom, square_rect.bottomleft, square_rect.topright]
            
            pointlist = [
                polygon_points1, polygon_points2, polygon_points3, polygon_points4, polygon_points5, polygon_points6, 
                polygon_points7, polygon_points8, polygon_points9, polygon_points10, polygon_points11, polygon_points12, 
                polygon_points13, polygon_points14, polygon_points15, polygon_points16, polygon_points17, polygon_points18, polygon_points19
            ]

            if trigger:
                points = random.choice(pointlist)
                angle = random.choice([0, 90, 180, 270])
                center = square_rect.center
                grid_points[row][col] = [rotate_point(center, point, angle) for point in points]

            # Draw the square outline
            #pygame.draw.rect(screen, (0, 0, 0), square_rect, 1)
            
            color = eyesy.color_picker_lfo(eyesy.knob4, 1.1)

            # Draw the polygon if points exist
            if grid_points[row][col]:
                pygame.draw.polygon(screen, color, grid_points[row][col], stroke)

    if trigger:
        trigger = False

    lastScreenSize = xr * 0.16  # 200

    image = last_screen
    last_screen = screen.copy()
    thingX = int(xr - (eyesy.knob2 * lastScreenSize))
    thingY = int(yr - (eyesy.knob2 * (lastScreenSize * 0.5625)))
    placeX = int(xr / 2) - int(((thingX / 2) * xr) / xr)
    placeY = int(yr / 2) - int(((thingY / 2) * yr) / yr)

    thing = pygame.transform.scale(image, (thingX, thingY))  # feedback screen scale
    thing.set_alpha(int(eyesy.knob3 * 180))  # adjust transparency on knob3
    screen.blit(thing, (placeX, placeY))  # feedback screen blit
