import pygame
import math
from collections import deque
import pygame.gfxdraw

# Knob1 - Audio History
# Knob2 - Vertical Position
# Knob3 - Ellipse Count
# Knob4 - Foreground Color
# Knob5 - Background color

# Initialize a global dictionary to store audio history for each index
audio_history = {}
current_history_length = None

def setup(screen, eyesy):
    global yr, xr
    yr = eyesy.yres
    xr = eyesy.xres

def calculate_offset(knob_value, max_range, count):
    # Calculate offset with center detent and adjust dynamically based on the number of ellipses
    if 0.48 <= knob_value <= 0.52:
        return 0
    elif knob_value < 0.5:
        # Scale the offset inversely with the number of ellipses
        return (0.5 - knob_value) * (max_range) / (count * 0.5) *-1
    else:
        # Scale the offset inversely with the number of ellipses
        return (knob_value - 0.5) * (max_range) / (count * 0.5)

def draw(screen, eyesy):
    global audio_history, yr, xr, current_history_length

    eyesy.color_picker_bg(eyesy.knob5)

    # Calculate the number of ellipses based on knob3
    count = int(eyesy.knob3 * 99) + 1 

    history_length = int((eyesy.knob1 * 20) + 1)

    # Check if history_length has changed
    if current_history_length != history_length:
        current_history_length = history_length
        # Recreate deques with the new maxlen
        for i in audio_history:
            audio_history[i] = deque(list(audio_history[i]), maxlen=history_length)

    center = (xr / 2, yr / 2)

    # Calculate y_offset based on knob2 with center detent and dynamic adjustment
    y_offset = calculate_offset(eyesy.knob2, yr / 2, count)

    # Draw nested ellipses
    for i in range(count):
        current_value = abs(eyesy.audio_in[i] / 15000)  # Adjust the divisor for reactivity

        # Initialize history deque for the index if not already present
        if i not in audio_history:
            audio_history[i] = deque(maxlen=history_length)

        # Append the current value to the history
        audio_history[i].append(current_value)

        # Calculate the average of the history
        average_value = sum(audio_history[i]) / len(audio_history[i])
        color = eyesy.color_picker_lfo(eyesy.knob4, 0.008)  # Use average_value if needed

        # Calculate ellipse dimensions with even vertical spacing
        max_vertical_radius = yr / 2
        vertical_radius = max_vertical_radius - (i * (max_vertical_radius / count))
        horizontal_radius = vertical_radius * average_value  # Use audio history to determine horizontal radius

        # Draw the ellipse with y_offset
        pygame.gfxdraw.ellipse(screen, int(center[0]), int(center[1] + y_offset * i), int(horizontal_radius), int(vertical_radius), color)
