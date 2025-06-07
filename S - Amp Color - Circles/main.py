import os
import pygame
import math
import random
import time
from collections import deque

# Knob1 - Audio History
# Knob2 - Rotation Direction & Rate
# Knob3 - Nested Circle Count
# Knob4 - LFO Step Size
# Knob5 - background color
# Trigger - picks five new circle sizes & positions

# Initialize a global dictionary to store audio history for each index
audio_history = {}
current_history_length = None
current_rotation = 0  # Variable to keep track of the current rotation state
trigger = False
circles = []
lfo_angle = 0
lfo_direction = 1
pause_until = 0

def initialize_circles(xr, yr):
    #Initialize five random circles.
    circles = []
    for _ in range(5):
        diameter = random.uniform(0.03 * xr, 0.4 * xr)
        radius = diameter / 2
        x = random.uniform(radius, xr - radius)
        y = random.uniform(radius, yr - radius)
        circles.append((x, y, radius))
    return circles

def setup(screen, eyesy):
    global min_height, corner, fill, yr, xr, circles
    min_height = 5
    corner = 0
    fill = 0
    yr = eyesy.yres
    xr = eyesy.xres
    circles = initialize_circles(xr, yr)  # Initialize circles at launch

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

def calculate_ending_angle(count):
    #Calculate the ending angle based on the count.
    if count <= 8:
        return 7.5
    elif count >= 50:
        return 3.0
    else:
        # Linear interpolation between 7.5 and 3.0 degrees
        return 7.5 - (7.5 - 3.0) * (count - 8) / (50 - 8)

def update_lfo(eyesy, count):
    #Update the LFO angle based on knob4 and count.
    global lfo_angle, lfo_direction, pause_until

    ending_angle = calculate_ending_angle(count)
    step_size = eyesy.knob4 * 0.5

    current_time = time.time()

    if eyesy.knob4 == 0:
        # LFO is off
        lfo_angle = 0
    elif current_time < pause_until:
        # In pause period
        pass
    else:
        if lfo_direction == 1:
            lfo_angle += step_size
            if lfo_angle >= ending_angle:
                lfo_angle = ending_angle
                lfo_direction = -1
        else:
            lfo_angle -= step_size
            if lfo_angle <= 0:
                lfo_angle = 0
                # Set pause for 0.5 seconds
                pause_until = current_time + 0.5
                lfo_direction = 1

def draw(screen, eyesy):
    global audio_history, yr, xr, current_history_length, current_rotation, trigger, circles, lfo_angle

    eyesy.color_picker_bg(eyesy.knob5)

    # Check trigger condition
    if eyesy.trig:
        trigger = True

    if trigger:
        # Generate new random circles
        circles = []
        for _ in range(5):
            diameter = random.uniform(0.03 * xr, 0.4 * xr)
            radius = diameter / 2
            x = random.uniform(radius, xr - radius)
            y = random.uniform(radius, yr - radius)
            circles.append((x, y, radius))
        trigger = False

    # Number of circles
    count = int(eyesy.knob3 * 49) + 1

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

    # Update LFO
    update_lfo(eyesy, count)

    center = (xr / 2, yr / 2)

    # Draw nested circles
    for i in range(count):
        current_value = abs(eyesy.audio_in[i] / 22000) #make change 22000 to higher number if you want less reactivity

        # Initialize history deque for the index if not already present
        if i not in audio_history:
            audio_history[i] = deque(maxlen=history_length)

        # Append the current value to the history
        audio_history[i].append(current_value)

        # Calculate the average of the history
        average_value = sum(audio_history[i]) / len(audio_history[i])
        color = eyesy.color_picker(average_value)

        # Calculate circle dimensions with dynamic spacing
        spacing_factor = 0.1  # Adjust this factor to control spacing
        circle_radius = (xr / 2) - (i * (xr / (2 * count)) * (1 + spacing_factor * (100 - count) / 100))

        # Draw each circle with nested effect
        for x, y, radius in circles:
            # Scale the radius based on the current nesting level
            scaled_radius = radius * (circle_radius / (xr / 2))

            # Calculate rotation angle for the current circle
            rotation_angle = current_rotation + i * lfo_angle

            # Rotate the circle's position
            rotated_point = rotate_point(center, (x, y), rotation_angle)

            # Draw the circle
            pygame.draw.circle(screen, color, (int(rotated_point[0]), int(rotated_point[1])), int(scaled_radius))
