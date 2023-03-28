import pygame
import datetime
import math

# Initialize Pygame
pygame.init()

# Set the window size and title
win_width, win_height = 400, 400
win_title = "Mickey Clock"
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption(win_title)

# Load the images of Mickey Mouse's hands for seconds and minutes
seconds_hand = pygame.image.load("mickey_hand.png")
minutes_hand = pygame.image.load("mickey_hand.png")

# Define the function that will rotate the hands using Pygame's transform.rotate function
def rotate_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image.get_rect(center=(win_width/2, win_height/2)).center)
    return rotated_image, rotated_rect

# Set the clock font and size
font = pygame.font.Font(None, 50)

# Main loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get the current time
    now = datetime.datetime.now()

    # Calculate the angle for the seconds and minutes hands
    seconds_angle = -math.radians(now.second * 6)  # 6 degrees per second
    minutes_angle = -math.radians(now.minute * 6) - seconds_angle / 60  # 6 degrees per minute

    # Rotate the hands
    seconds_hand_rotated, seconds_rect = rotate_hand(seconds_hand, math.degrees(seconds_angle))
    minutes_hand_rotated, minutes_rect = rotate_hand(minutes_hand, math.degrees(minutes_angle))

    # Draw the hands on the window
    window.fill((255, 255, 255))
    window.blit(seconds_hand_rotated, seconds_rect)
    window.blit(minutes_hand_rotated, minutes_rect)

    # Draw the current time on the window
    time_text = font.render(now.strftime("%I:%M:%S %p"), True, (0, 0, 0))
    time_rect = time_text.get_rect(center=(win_width/2, win_height/2 + 100))
    window.blit(time_text, time_rect)

    # Update the window
    pygame.display.update()