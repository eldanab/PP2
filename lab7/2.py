import pygame
import os

pygame.init()

screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
pygame.display.set_caption("Music player")

songs = [s for s in os.listdir("music")]

pygame.mixer.init()
isPlaying = False
song_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
# "SPACE - stopping and playing"
# "RIGHT - next song"
# "LEFT - previous song"

