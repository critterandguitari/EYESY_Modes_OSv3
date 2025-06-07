import os
import pygame
import math
from collections import deque

#Knob1 - Audio 'history' amount
#Knob2 - Rotation direction & Speed. Center = no rotation. 
#Knob3 - Number of rectangles
#Knob4 - Offset angle
#Knob5 - Background color (might only see background while rotating)

# Initialize a global dictionary to store audio history for each index
audio_history = {}
current_history_length = None
current_rotation = 0  # Variable to keep track of the current rotation state

def setup(screen, eyesy):
    global min_height, corner, fill, yr, xr
    min_height = 5
    corner = 0
    fill = 0
    yr = eyesy.yres
    xr = eyesy.xres

def rotate_point(center, point, angle):
    #Rotate a point around a center by a given angle (in degrees).
    angle_rad = math.radians(angle)
    x, y = point
    cx, cy = center
    # Translate point to origin
    x -= cx
    y -= cy
    # Apply rotation
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    # Translate back
    return (new_x + cx, new_y + cy)

def draw(screen, eyesy):
    global audio_history, yr, xr, current_history_length, current_rotation

    eyesy.color_picker_bg(eyesy.knob5)

    # Number of rectangles
    count = int(eyesy.knob3 * 49) + 1 #99 is slow at 720p

    history_length = int((eyesy.knob1 * 20) + 1)

    # Check if history_length has changed
    if current_history_length != history_length:
        current_history_length = history_length
        # Recreate deques with the new maxlen
        for i in audio_history:
            audio_history[i] = deque(list(audio_history[i]), maxlen=history_length)

    # Reset rotation if knob2 is between 0.49 and 0.51
    if 0.49 <= eyesy.knob2 <= 0.51:
        current_rotation = 0
    else:
        # Determine rotation direction and rate based on knob2
        rotation_rate = 0
        if eyesy.knob2 < 0.48:
            rotation_rate = abs(eyesy.knob2 - 0.48) * -52  # Rotate counterclockwise
        elif eyesy.knob2 > 0.52:
            rotation_rate = (eyesy.knob2 - 0.52) * 52  # Rotate clockwise

        # Update the current rotation based on rotation_rate
        current_rotation += rotation_rate

    center = (xr / 2, yr / 2)

    # Draw nested rectangles
    for i in range(count):
        current_value = abs(eyesy.audio_in[i] / 32768)

        # Initialize history deque for the index if not already present
        if i not in audio_history:
            audio_history[i] = deque(maxlen=history_length)

        # Append the current value to the history
        audio_history[i].append(current_value)

        # Calculate the average of the history
        average_value = sum(audio_history[i]) / len(audio_history[i])
        color = eyesy.color_picker(average_value)

        # Calculate rectangle dimensions with dynamic spacing
        spacing_factor = 0.1  # Adjust this factor to control spacing
        rect_width = xr - (i * (xr / count) * (1 + spacing_factor * (50 - count) / 50))
        rect_height = yr - (i * (yr / count) * (1 + spacing_factor * (50- count) / 50))

        # Calculate rotation angle for the current rectangle
        rotation_angle = current_rotation + i * (eyesy.knob4 * 45)  # Add a small offset for each rectangle

        # Calculate the four corners of the rectangle
        half_width = rect_width / 2
        half_height = rect_height / 2

        # Define the rectangle's vertices before rotation
        points = [
            (-half_width, -half_height),
            (half_width, -half_height),
            (half_width, half_height),
            (-half_width, half_height)
        ]

        # Rotate each point
        rotated_points = [rotate_point((0, 0), point, rotation_angle) for point in points]

        # Translate points to the center of the screen
        rotated_points = [(point[0] + center[0], point[1] + center[1]) for point in rotated_points]

        # Draw the polygon
        pygame.draw.polygon(screen, color, rotated_points)
