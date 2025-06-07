import os
import pygame
import math
import random

#Knob1 - Boid size
#Knob2 - Bar width
#Knob3 - Bar style (filled/unfilled, curved/90-degree corners)
#Knob4 - foreground color
#Knob5 - background color

# Initialize a global dictionary to store audio history for each index
audio_history = {}

# Boid settings
NUM_BOIDS = 250
BOID_SPEED = 20

class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * BOID_SPEED
        self.size = 1  # Default size, will be updated in draw function
        self.color_value = random.random()  # Random value for consistent color picking

    def update(self, screen_width, screen_height, obstacles, size):
        self.size = size  # Update size dynamically
        # Update position
        self.position += self.velocity

        # Wrap around screen edges
        if self.position.x > screen_width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = screen_width

        if self.position.y > screen_height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = screen_height

        # Check for collisions with obstacles and bounce
        for obstacle in obstacles:
            boid_rect = pygame.Rect(self.position.x - self.size, self.position.y - self.size, self.size * 2, self.size * 2)
            if boid_rect.colliderect(obstacle):
                self.bounce(obstacle)

    def bounce(self, obstacle):
        # Calculate the overlap on x and y axes
        overlap_x = min(self.position.x + self.size, obstacle.right) - max(self.position.x - self.size, obstacle.left)
        overlap_y = min(self.position.y + self.size, obstacle.bottom) - max(self.position.y - self.size, obstacle.top)

        # Determine the direction of the bounce
        if overlap_x < overlap_y:
            # Bounce horizontally
            if self.position.x < obstacle.centerx:
                self.velocity.x = -abs(self.velocity.x)  # Bounce left
            else:
                self.velocity.x = abs(self.velocity.x)  # Bounce right
        else:
            # Bounce vertically
            if self.position.y < obstacle.centery:
                self.velocity.y = -abs(self.velocity.y)  # Bounce up
            else:
                self.velocity.y = abs(self.velocity.y)  # Bounce down

    def draw(self, screen, eyesy):
        # Use the consistent random value to pick the color
        self.color = eyesy.color_picker(self.color_value)
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.size)

def setup(screen, eyesy):
    global min_height, yhalf, corner, fill, boids
    min_height = 5
    yhalf = (eyesy.yres / 2)
    corner = 0
    fill = 0
    boids = [Boid(random.uniform(0, eyesy.xres), random.uniform(0, eyesy.yres)) for _ in range(NUM_BOIDS)]

def draw(screen, eyesy):
    global min_height, yhalf, corner, fill, audio_history, boids

    eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4)

    # Calculate boid size based on knob1
    boid_size = int(eyesy.knob1 * 24) + 1  # Map knob1 value to range 1-25

    # Number of vu boxes
    count = 32  # Fixed count for demonstration

    spacing = eyesy.xres / count

    box_width = int(eyesy.knob2 * (spacing)) + 2
    box_width_half = int(box_width / 2)
    box_offset = int((spacing - box_width) / 2)

    obstacles = []

    # Draw vu_boxes!
    for i in range(count):
        current_value = abs(eyesy.audio_in[i] * eyesy.yres / 32768)

        # Initialize history list for the index if not already present
        if i not in audio_history:
            audio_history[i] = []

        # Append the current value to the history
        audio_history[i].append(current_value)

        # Ensure the history list doesn't exceed 10 elements
        if len(audio_history[i]) > 2:
            audio_history[i].pop(0)

        # Calculate the average of the history
        average_value = sum(audio_history[i]) / len(audio_history[i])
        height = int(average_value + min_height)

        # Fill/stroke width & corner size
        if eyesy.knob3 < 0.5:
            fill = int(box_width_half * eyesy.knob3) + 1

            if height <= (min_height + fill) * 2:
                corner = int(0)
            else:
                corner = int(box_width_half * (eyesy.knob3 * 2))
        if eyesy.knob3 >= 0.5:
            corner = int(box_width_half * (2 - (eyesy.knob3 * 2)))
            fill = 0

        # Calculate the x position with consistent spacing
        x_position = int(i * spacing + box_offset)

        # Draw a single box for each audio input
        vu_box = pygame.Rect(
            x_position,
            yhalf - (height / 2),
            box_width,
            height
        )
        obstacles.append(vu_box)
        pygame.draw.rect(screen, color, vu_box, fill, corner)

    # Update and draw boids with dynamic size and consistent color
    for boid in boids:
        boid.update(eyesy.xres, eyesy.yres, obstacles, boid_size)
        boid.draw(screen, eyesy)
