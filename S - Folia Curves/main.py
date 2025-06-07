import os
import pygame
import time
import math
import pygame.gfxdraw

# Knob1 - Drawing option selection
# Knob2 - Max. rotation speed. If knob is turned all the way right, the rotation speed is stopped and the angle is set to 0.
# Knob3 - 'Trails' amount. Need to turn on 'Persist' button to see the effect.
# Knob4 - foreground color
# Knob5 - background color

def setup(screen, eyesy):
    global xr, yr, l100, audio_history, rotation_angles
    xr = eyesy.xres
    yr = eyesy.yres
    l100 = xr * 0.037  # xr * 0.078

    # Initialize the audio history for each slot
    audio_history = [[0] * 7 for _ in range(63)]

    # Initialize the rotation angles for each box
    rotation_angles = [0] * 63

def rotate_point(cx, cy, x, y, angle):
    # Rotate a point around a center
    radians = math.radians(angle)
    cos_angle = math.cos(radians)
    sin_angle = math.sin(radians)
    translated_x = x - cx
    translated_y = y - cy
    rotated_x = translated_x * cos_angle - translated_y * sin_angle
    rotated_y = translated_x * sin_angle + translated_y * cos_angle
    return rotated_x + cx, rotated_y + cy

def draw(screen, eyesy):
    global xr, yr, l100, audio_history, rotation_angles

    # Color settings
    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4, 0.05)

    # Calculate the spacing between the boxes
    grid_width = 9
    grid_height = 7
    box_width = l100
    box_height = l100
    horizontal_spacing = (xr - grid_width * box_width) / (grid_width + 1)
    vertical_spacing = (yr - grid_height * box_height) / (grid_height + 1)

    # Draw the grid of boxes
    for row in range(grid_height):
        for col in range(grid_width):
            # Calculate the position of the box
            x = horizontal_spacing * (col + 1) + col * box_width
            y = vertical_spacing * (row + 1) + row * box_height

            # Get the y-position offset from the audio input
            index = row * grid_width + col
            current_value = (eyesy.audio_in[index] * yr) / 32768

            # Update the history and calculate the average
            audio_history[index].pop(0)
            audio_history[index].append(current_value)
            a1 = sum(audio_history[index]) / len(audio_history[index])

            # Update the rotation angle based on a1
            max_rotation_speed = eyesy.knob2 * 200  # Maximum rotation speed in degrees per frame
            rotation_speed = (a1 / yr) * max_rotation_speed * 2  # Scale a1 to the range [-max_rotation_speed, max_rotation_speed]
            rotation_angles[index] += rotation_speed

            # Limit the rotation angle to [-180, 180]
            rotation_angles[index] = max(min(rotation_angles[index], 180), -180)

            if eyesy.knob2 == 1:
                rotation_angles = [0] * 63

            # Calculate the rotated vertices of the box
            center_x = x + box_width / 2
            center_y = y + box_height / 2
            vertices = [
                (x, y),
                (x, y + box_height),
                (x + box_width, y + box_height),
                (x + box_width, y)
            ]
            rotated_vertices = [rotate_point(center_x, center_y, vx, vy, rotation_angles[index]) for vx, vy in vertices]

            # Determine the drawing option based on eyesy.knob1
            if eyesy.knob1 < 0.15:
                # 1 - single
                additional_line = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                pygame.gfxdraw.bezier(screen, additional_line, 4, color)
            elif 0.15 <= eyesy.knob1 < 0.3:
                # 2 - broken lozenge
                additional_line = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                additional_line2 = [
                    rotate_point(center_x, center_y, x + box_width, y + box_width, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + box_width - a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y + box_width, rotation_angles[index])
                ]
                pygame.gfxdraw.bezier(screen, additional_line, 4, color)
                pygame.gfxdraw.bezier(screen, additional_line2, 4, color)
            elif 0.3 <= eyesy.knob1 < 0.45:
                # 3 - angle
                additional_line = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                additional_line3 = [
                    rotate_point(center_x, center_y, x, y + box_width, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + a1, y + box_width / 2, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                pygame.gfxdraw.bezier(screen, additional_line, 4, color)
                pygame.gfxdraw.bezier(screen, additional_line3, 4, color)
            elif 0.45 <= eyesy.knob1 < 0.6:
                # 4 - bird beak
                additional_line = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                additional_line2 = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y - a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                pygame.gfxdraw.bezier(screen, additional_line, 4, color)
                pygame.gfxdraw.bezier(screen, additional_line2, 4, color)
            elif 0.6 <= eyesy.knob1 < 0.75:
                # 5 - house
                pygame.draw.aalines(screen, color, False, rotated_vertices)
                additional_line = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                pygame.gfxdraw.bezier(screen, additional_line, 4, color)
            elif 0.75 <= eyesy.knob1 < 0.9:
                # 6 - lozenge
                pygame.draw.aalines(screen, color, False, [rotated_vertices[0], rotated_vertices[1]])
                pygame.draw.aalines(screen, color, False, [rotated_vertices[2], rotated_vertices[3]])

                additional_line = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                additional_line2 = [
                    rotate_point(center_x, center_y, x + box_width, y + box_width, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + box_width - a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y + box_width, rotation_angles[index])
                ]
                pygame.gfxdraw.bezier(screen, additional_line, 4, color)
                pygame.gfxdraw.bezier(screen, additional_line2, 4, color)
            else:
                # 7 - star
                additional_line = [
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                additional_line2 = [
                    rotate_point(center_x, center_y, x + box_width, y + box_width, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width / 2, y + box_width - a1, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y + box_width, rotation_angles[index])
                ]
                additional_line3 = [
                    rotate_point(center_x, center_y, x, y + box_width, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + a1, y + box_width / 2, rotation_angles[index]),
                    rotate_point(center_x, center_y, x, y, rotation_angles[index])
                ]
                additional_line4 = [
                    rotate_point(center_x, center_y, x + box_width, y + box_width, rotation_angles[index]),
                    rotate_point(center_x, center_y, x - a1 + box_width, y + box_width / 2, rotation_angles[index]),
                    rotate_point(center_x, center_y, x + box_width, y, rotation_angles[index])
                ]
                pygame.gfxdraw.bezier(screen, additional_line, 4, color)
                pygame.gfxdraw.bezier(screen, additional_line2, 4, color)
                pygame.gfxdraw.bezier(screen, additional_line3, 4, color)
                pygame.gfxdraw.bezier(screen, additional_line4, 4, color)

    # Trails
    veil = pygame.Surface((eyesy.xres, eyesy.yres))
    veil.set_alpha(int(eyesy.knob3 * 45))
    veil.fill((eyesy.bg_color[0], eyesy.bg_color[1], eyesy.bg_color[2]))
    screen.blit(veil, (0, 0))
