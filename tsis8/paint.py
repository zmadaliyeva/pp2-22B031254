import pygame

#Инициализировать Pygame
pygame.init()

#установка размера экрана
screen_width = 800
screen_height = 600

#установка цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#установить размер кисти
brush_size = 5

#создать экран
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paint")

#установить цвет по умолчанию
color = black

#инициализировать флаг ластика
eraser = False

#установить рабочий флаг
running = True

#основной цикл
while running:

    #цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                color = red
                eraser = False
            elif event.key == pygame.K_g:
                color = green
                eraser = False
            elif event.key == pygame.K_b:
                color = blue
                eraser = False
            elif event.key == pygame.K_e:
                eraser = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # нажата левая кнопка мыши, рисование фигуры
                pos = pygame.mouse.get_pos()
                if eraser:
                    pygame.draw.circle(screen, white, pos, brush_size)
                else:
                    if pygame.key.get_pressed()[pygame.K_LSHIFT]:
                        # нажат левый шифт, рисуем прямоугольник
                        rect = pygame.Rect(pos[0], pos[1], brush_size*5, brush_size*5)
                        pygame.draw.rect(screen, color, rect)
                    else:
                        #левый шифт не нажат, рисование круга
                        pygame.draw.circle(screen, color, pos, brush_size)

    # обновить дисплей
    pygame.display.update()

#Выйти из Pygame
pygame.quit()