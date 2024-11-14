import pygame
import os

# Initialize pygame
pygame.init()

# Set up the screen
size = (450, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Music Player')

# Load images
background_img = pygame.image.load("C:\\Users\Alina\\Desktop\\pp2 lab7\\\\2.png")
image = pygame.image.load("C:\\Users\Alina\\Desktop\\pp2 lab7\\1.png")

# Get the list of .mp3 files in the directory
music = [f.name for f in os.scandir("C:\\Users\Alina\\Desktop\\pp2 lab7\\") if f.is_file() and f.name.endswith('.mp3')]

if not music:
    print("No music files found.")
else:
    print(f"Found music files: {music}")

# Font for displaying song name
font = pygame.font.SysFont('Tahoma', 19, True)

# Set up pygame mixer
pygame.mixer.init()

# If music is found, play the first song
if music:
    pygame.mixer.music.load(music[0])
    pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Space to pause or play
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:  # Right arrow to next song
                current_song = (music.index(pygame.mixer.music.get_pos()) + 1) % len(music)
                pygame.mixer.music.load(music[current_song])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:  # Left arrow to previous song
                current_song = (music.index(pygame.mixer.music.get_pos()) - 1) % len(music)
                pygame.mixer.music.load(music[current_song])
                pygame.mixer.music.play()

    # Draw background and image
    screen.blit(background_img, (0, 0))
    screen.blit(image, (0, 0))

    # Display the song name
    song_name = font.render(music[0], True, 'white')
    screen.blit(song_name, (78, 405))

    pygame.display.flip()

pygame.quit()
