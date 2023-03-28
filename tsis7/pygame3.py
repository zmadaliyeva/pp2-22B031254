import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title
win_width, win_height = 400, 400
win_title = "Moving Ball"
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption(win_title)

# Set the initial position of the ball
ball_x, ball_y = win_width//2, win_height//2

# Set the radius of the ball
ball_radius = 25

# Set the ball color
ball_color = (255, 0, 0)

# Set the ball movement speed
move_speed = 20

# Main loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - move_speed - ball_radius >= 0:
                    ball_y -= move_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + move_speed + ball_radius <= win_height:
                    ball_y += move_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - move_speed - ball_radius >= 0:
                    ball_x -= move_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + move_speed + ball_radius <= win_width:
                    ball_x += move_speed

    # Draw the ball and the background
    window.fill((255, 255, 255))
    pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)

    # Update the window
    pygame.display.update()