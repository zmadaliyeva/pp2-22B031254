import pygame
import os

# Initialize Pygame
pygame.init()

# Set the window size and title
win_width, win_height = 400, 100
win_title = "Music Player"
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption(win_title)

# Set the font and font size
font = pygame.font.Font(None, 30)

# Set the music directory and get a list of all the music files
music_dir = "music/"
music_files = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(".mp3")]

# Initialize the music player
pygame.mixer.music.load(music_files[0])
current_track = 0
playing = False

# Define the function to play the current track
def play_track():
    global playing
    pygame.mixer.music.play()
    playing = True

# Define the function to stop playing the current track
def stop_track():
    global playing
    pygame.mixer.music.stop()
    playing = False

# Define the function to play the next track
def next_track():
    global current_track
    current_track += 1
    if current_track >= len(music_files):
        current_track = 0
    pygame.mixer.music.load(music_files[current_track])
    play_track()

# Define the function to play the previous track
def prev_track():
    global current_track
    current_track -= 1
    if current_track < 0:
        current_track = len(music_files) - 1
    pygame.mixer.music.load(music_files[current_track])
    play_track()

# Main loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_track()
                else:
                    play_track()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()

    # Draw the current track name and status
    status_text = "Playing" if playing else "Paused"
    track_text = music_files[current_track]
    status_render = font.render(status_text, True, (0, 0, 0))
    track_render = font.render(track_text, True, (0, 0, 0))
    status_rect = status_render.get_rect(topleft=(10, 10))
    track_rect = track_render.get_rect(midtop=(win_width/2, 10))
    window.fill((255, 255, 255))
    window.blit(status_render, status_rect)
    window.blit(track_render, track_rect)

    # Update the window
    pygame.display.update()