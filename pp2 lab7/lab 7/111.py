import pygame, time, sys
pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

# Загружаем изображения
back = pygame.image.load("C:\\Users\\Alina\\Desktop\\pp2 lab7\\back.jpg")
seconds = pygame.image.load("C:\\Users\\Alina\\Desktop\\pp2 lab7\\seconds.png")
minutes = pygame.image.load("C:\\Users\\Alina\\Desktop\\pp2 lab7\\minutes.png")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.blit(back, (0, 0))  # Рисуем фон

    now = time.localtime()

    # Ускоряем минутную стрелку в 10 раз
    minute_angle = - (now.tm_min * 6 * 10)  # Умножаем угол для ускорения
    min_rotate = pygame.transform.rotate(minutes, minute_angle)
    min_pos = ((size[0] - min_rotate.get_width()) / 2, (size[1] - min_rotate.get_width()) / 2)
    screen.blit(min_rotate, min_pos)

    # Вычисляем угол вращения для секундной стрелки
    second_angle = - (now.tm_sec * 6)
    sec_rotate = pygame.transform.rotate(seconds, second_angle)
    sec_pos = ((size[0] - sec_rotate.get_width()) / 2, (size[1] - sec_rotate.get_width()) / 2)
    screen.blit(sec_rotate, sec_pos)

    pygame.display.flip()  # Обновляем экран

pygame.quit()
sys.exit()
