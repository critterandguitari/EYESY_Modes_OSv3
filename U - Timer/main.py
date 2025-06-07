import os
import pygame
import random
import time
import math

# Knob1 - hours (0-23)
# Knob2 - minutes (0-59)
# Knob3 - seconds (0-59)
# Knob4 - foreground color
# Knob5 - background color

def setup(screen, eyesy):
    global xr, yr, font, font2, countdown_active, last_trig_time, time_of_start, message_start_time
    global full_duration, hours, minutes, seconds, phrase_list, current_phrase, phrase_start_time, phrase_angle, phrase_position, phrase_speed, phrase_destination
    global phrase_history
    xr = eyesy.xres
    yr = eyesy.yres
    font = pygame.font.Font(None, int(yr / 5))  # Adjusted font size
    font2 = pygame.font.Font(None, int(yr / 11))  # Adjusted font size
    countdown_active = False
    last_trig_time = 0
    time_of_start = 0
    message_start_time = 0
    full_duration = 0
    hours = 0
    minutes = 0
    seconds = 0
    phrase_list = [
        "Yes!", "Looks good", "Sounds good!", "Turn it up", "Elemental!", "Badass", "Word", "Realness",
        "Your goals", "New", "&", "Increase", "Up", "Trajectory", "Phase it", "In it", "Keep going",
        "Awesome", "Next level", "Boost", "Energy", "Vibe", "Positive", "Momentum", "Flow", "Rhythm",
        "Synergy", "Harmony", "Balance", "Focus", "Drive", "Motivation", "Inspiration", "Creativity",
        "Innovation", "Progress", "Growth", "Development", "Evolution", "Let it echo","Transformation", "Breakthrough",
        "Milestone", "Achievement", "Success", "Victory", "Triumph", "Accomplishment", "Fulfillment",
        "Satisfaction", "Happiness", "Joy", "Excitement", "Enthusiasm", "Passion", "Dedication",
        "Commitment", "Determination", "Resilience", "Strength", "Courage", "Confidence", "Belief",
        "Fun", "Hope", "Optimism", "Gratitude", "Appreciation", "Respect", "Integrity", "Honesty",
        "Trust", "Loyalty", "Support", "Encouragement", "Empathy", "Compassion", "Kindness", "Generosity",
        "Humility", "Patience", "Wisdom", "Knowledge", "Understanding", "Insight", "Clarity", "Vision",
        "Purpose", "Mission", "Values", "Principles", "Standards", "Quality", "Excellence", "Perfection",
        "Precision", "Accuracy", "Efficiency", "Effectiveness", "Productivity", "Impact", "Agreement",
        "Aptitude", "Authenticity", "Blend", "Hybrid", "Technique", "Endeavor"
    ]
    current_phrase = ""
    phrase_start_time = 0
    phrase_angle = 0
    phrase_position = (0, 0)
    phrase_speed = 0
    phrase_destination = (0, 0)
    phrase_history = []

def draw(screen, eyesy):
    global xr, yr, font, font2, countdown_active, last_trig_time, time_of_start, message_start_time
    global full_duration, hours, minutes, seconds, phrase_list, current_phrase, phrase_start_time, phrase_angle, phrase_position, phrase_speed, phrase_destination
    global phrase_history

    bg_color = eyesy.color_picker_bg(eyesy.knob5)
    color = eyesy.color_picker_lfo(eyesy.knob4)

    current_time = time.time()
    if eyesy.trig:
        if current_time - last_trig_time < 0.5:
            countdown_active = False  # Stop the countdown
            hours = 0
            minutes = 0
            seconds = 0
            full_duration = 0
        else:
            if countdown_active:
                countdown_active = False  # Stop the countdown
            else:
                countdown_active = True  # Start the countdown
                full_duration = hours * 3600 + minutes * 60 + seconds
                time_of_start = current_time  # Record the start time
                message_start_time = current_time  # Record the message start time
                phrase_start_time = 0  # Reset phrase start time
        last_trig_time = current_time

    # Update the countdown time from knobs if the countdown is not active
    if not countdown_active:
        hours = int(eyesy.knob1 * 23)
        minutes = int(eyesy.knob2 * 59)
        seconds = int(eyesy.knob3 * 59)

    if countdown_active:
        elapsed_time = current_time - time_of_start
        remaining_seconds = max(0, full_duration - int(elapsed_time))

        hours = remaining_seconds // 3600
        minutes = (remaining_seconds % 3600) // 60
        seconds = remaining_seconds % 60

        if remaining_seconds == 0:
            countdown_active = False

        # Screen flashing logic
        if 10 < remaining_seconds <= 30:
            if int(current_time) % 2 == 0:
                screen.fill((0, 0, 0))  # Fill screen with black
            else:
                screen.fill((255, 255, 255))  # Fill screen with white
        elif 0 < remaining_seconds <= 10:
            if int(current_time * 2) % 2 == 0:
                screen.fill((0, 0, 0))  # Fill screen with black
            else:
                screen.fill((255, 255, 255))  # Fill screen with white

        # Handle phrase movement
        if full_duration > 45:  # If the timer is set to longer than 1 minute
            if phrase_start_time == 0 or (current_time - phrase_start_time > random.uniform(8, 15)):
                # Ensure the current phrase is not one of the last 47 phrases
                while True:
                    current_phrase = random.choice(phrase_list)
                    if current_phrase not in phrase_history:
                        break
                phrase_history.append(current_phrase)
                if len(phrase_history) > 47:
                    phrase_history.pop(0)

                phrase_speed = random.uniform(.5, 3)  # Random speed in pixels per second

                # Random starting position outside the screen boundaries
                start_side = random.choice(['left', 'right', 'top', 'bottom'])
                if start_side == 'left':
                    phrase_position = (-xr / 4, random.uniform(0, yr))
                    phrase_destination = (xr + xr / 4, phrase_position[1])
                elif start_side == 'right':
                    phrase_position = (xr + xr / 4, random.uniform(0, yr))
                    phrase_destination = (-xr / 4, phrase_position[1])
                elif start_side == 'top':
                    phrase_position = (random.uniform(0, xr*0.85), -yr / 5)
                    phrase_destination = (phrase_position[0], yr + yr / 5)
                elif start_side == 'bottom':
                    phrase_position = (random.uniform(0, xr*0.85), yr + yr / 5)
                    phrase_destination = (phrase_position[0], -yr / 5)

                phrase_start_time = current_time

            # Move the phrase
            elapsed_time_since_start = current_time - phrase_start_time
            distance = phrase_speed * elapsed_time_since_start
            total_distance = math.sqrt((phrase_destination[0] - phrase_position[0]) ** 2 + (phrase_destination[1] - phrase_position[1]) ** 2)

            if distance < total_distance:
                ratio = distance / total_distance
                phrase_position = (
                    phrase_position[0] + ratio * (phrase_destination[0] - phrase_position[0]),
                    phrase_position[1] + ratio * (phrase_destination[1] - phrase_position[1])
                )
            else:
                phrase_start_time = 0  # Reset to pick a new phrase

            # Debug print to check remaining seconds
            #print(f"Remaining seconds: {remaining_seconds}")

            # Render the phrase only if there are more than 30 seconds remaining
            if remaining_seconds > 30:
                phrase_render = font2.render(current_phrase, True, color)
                screen.blit(phrase_render, phrase_position)

    # Render time digits
    digit = xr * 0.04
    half_line = digit * 4  # xr * 0.094
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    digit_positions = [
        (xr / 2 - half_line + i * digit, yr / 2 - yr / 8)  # Adjust positions as needed
        for i in range(8)
    ]

    for i, char in enumerate(time_str):
        if char.isdigit():
            digit_render = font.render(char, True, color)
            screen.blit(digit_render, digit_positions[i])
        else:
            colon_render = font.render(char, True, color)
            screen.blit(colon_render, digit_positions[i])

    # Render "Countdown Started" message
    if countdown_active and current_time - message_start_time < 1.5:
        message = font2.render("Countdown Started", True, color)
        message_rect = message.get_rect(center=(xr / 2, yr / 2 + yr / 16))
        screen.blit(message, message_rect)
