import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((650, 450), pygame.RESIZABLE)
pygame.display.set_caption("Music player")

# Get the list of songs in the music directory
songs = [s for s in os.listdir("music")]

# Set up font
font = pygame.font.SysFont("Times New Roman", 30)
text1 = font.render("Click SPACE to play/stop the music", True, (255, 255, 255))
text2 = font.render("Click LEFT to play the previous music", True, (255, 255, 255))
text3 = font.render("Click RIGHT to play the next music", True, (255, 255, 255))

# Initialize the mixer
pygame.mixer.init()
isPlaying = False
song_index = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if isPlaying:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load(os.path.join("music", songs[song_index]))
                    pygame.mixer.music.play()
                isPlaying = not isPlaying
            elif event.key == pygame.K_RIGHT:
                song_index = (song_index + 1) % len(songs)
                pygame.mixer.music.load(os.path.join("music", songs[song_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                song_index = (song_index - 1) % len(songs)
                pygame.mixer.music.load(os.path.join("music", songs[song_index]))
                pygame.mixer.music.play()

    screen.fill((0, 0, 0))

    screen.blit(text1, (100, 100))
    screen.blit(text2, (100, 200))
    screen.blit(text3, (100, 300))

    pygame.display.update()

