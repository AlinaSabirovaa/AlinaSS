import pygame, time, sys

# Initialize pygame
pygame.init()

# Set up the screen
size = (800, 600)
screen = pygame.display.set_mode(size)

# Load images
back = pygame.image.load("C:\\Users\\Alina\\Desktop\\pp2 lab7\\back.jpg")
seconds = pygame.image.load("C:\\Users\\Alina\\Desktop\\pp2 lab7\\seconds.png")
minutes = pygame.image.load("C:\\Users\\Alina\\Desktop\\pp2 lab7\\minutes.png")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.blit(back, (0, 0))  # Draw background

    now = time.localtime()

    # Calculate the rotation angle for the minute hand (counterclockwise)
    minute_angle = (now.tm_min * 6)
    min_rotate = pygame.transform.rotate(minutes, minute_angle)
    min_pos = ((size[0] - min_rotate.get_width()) / 2, (size[1] - min_rotate.get_height()) / 2)
    screen.blit(min_rotate, min_pos)

    # Calculate the rotation angle for the second hand (counterclockwise)
    second_angle = (now.tm_sec * 6)
    sec_rotate = pygame.transform.rotate(seconds, second_angle)
    sec_pos = ((size[0] - sec_rotate.get_width()) / 2, (size[1] - sec_rotate.get_height()) / 2)
    screen.blit(sec_rotate, sec_pos)

    pygame.display.flip()  # Update the screen

pygame.quit()
sys.exit()
