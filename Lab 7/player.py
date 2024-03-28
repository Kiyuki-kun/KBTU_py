import os
import pygame

pygame.init()

window_size = (300, 100)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)

music_directory = "C:/Users/Dimash/Downloads"
music_files = [f for f in os.listdir(music_directory) if f.endswith(".mp3")]
current_track_index = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    play_music()

def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press SPACE to play/pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    play_music()
            elif event.key == pygame.K_n:  # Press 'n' to play next track
                next_track()
            elif event.key == pygame.K_b:  # Press 'b' to play previous track
                prev_track()
            elif event.key == pygame.K_s:  # Press 's' to stop the music
                stop_music()

    window.fill(WHITE)

    pygame.display.update()

pygame.quit()
