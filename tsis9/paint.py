import math

import pygame

#Инициоизировать  Pygame
pygame.init()

#Установление размера
sc = pygame.display.set_mode((600, 400))
check = True
check_draw = False
color = "white"
start_pos = (0, 0)
end_pps = (0, 0)

#Управление поведением игры
rect_flag = False
circle_flag = False
square_flag = False
r_triangle_flag = False
e_triangle_flag = False
rhombus_flag = False
width_line = 2
eraser = pygame.image.load(
    "HistoryEraser.png")
eraser = pygame.transform.scale(eraser, (100, 80))

#выбрать цвет для рисования или стирания
while check:
    sc.blit(eraser, (390, 310))
    pygame.draw.circle(sc, 'red', (50, 350), 40)
    pygame.draw.circle(sc, 'blue', (150, 350), 40)
    pygame.draw.circle(sc, 'green', (250, 350), 40)
    pygame.draw.circle(sc, 'white', (350, 350), 40)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            #Инициализировать флаги для выбора фигуры для рисования
            rect_flag = True
            check_draw = False
            circle_flag = False
            square_flag = False
            r_triangle_flag = False
            e_triangle_flag = False
            rhombus_flag = False
            #Если пользователь нажал клавишу "c", выберите форму круга
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            rect_flag = False
            check_draw = False
            circle_flag = True
            square_flag = False
            r_triangle_flag = False
            e_triangle_flag = False
            rhombus_flag = False
            #Если пользователь нажал клавишу "s", выберите форму круга
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            rect_flag = False
            check_draw = False
            circle_flag = False
            square_flag = True
            r_triangle_flag = False
            e_triangle_flag = False
            rhombus_flag = False
            #Если пользователь нажал клавишу "t" выберите форму круга

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            rect_flag = False
            check_draw = False
            circle_flag = False
            square_flag = False
            r_triangle_flag = True
            e_triangle_flag = False
            rhombus_flag = False
            #Если пользователь нажал клавишу "y" выберите форму круга

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            rect_flag = False
            check_draw = False
            circle_flag = False
            square_flag = False
            r_triangle_flag = False
            e_triangle_flag = True
            rhombus_flag = False
            #Если пользователь нажал клавишу "u" выберите форму круга

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_u:
            rect_flag = False
            check_draw = False
            circle_flag = False
            square_flag = False
            r_triangle_flag = False
            e_triangle_flag = False
            rhombus_flag = True
            #нажата ли левая кнопка мыши и установлен ли флаг прямоугольника.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and rect_flag:
            start_pos = event.pos
        #Проверьте, нажата ли левая кнопка мыши и установлен ли флажок круга.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and circle_flag:
            start_pos = event.pos
        #нажата ли левая кнопка мыши и установлен ли квадратный флажок.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and square_flag:
            start_pos = event.pos
        #нажата ли левая кнопка мыши и установлен ли флаг правого треугольника.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and r_triangle_flag:
            start_pos = event.pos
        #нажата ли левая кнопка мыши и установлен ли флажок равностороннего треугольника.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and e_triangle_flag:
            start_pos = event.pos
        #нажата ли левая кнопка мыши и установлен ли флажок ромба.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and rhombus_flag:
            start_pos = event.pos
        #нажата ли только левая кнопка мыши.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            check_draw = True
            rect_flag = False
            circle_flag = False
            square_flag = False
            r_triangle_flag = False
            e_triangle_flag = False
            rhombus_flag = False
        #код функциональный и правильно реализует отрисовку различных фигур на экране Pygame
        if event.type == pygame.MOUSEMOTION:
            if check_draw:
                end_pos = event.pos
                pygame.draw.line(sc, color, start_pos, end_pos, width_line)
                start_pos = end_pos
            if rect_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                sc.fill('black')
                pygame.draw.rect(sc, color, pygame.Rect(x, y, width_rect, height_rect), 2)
            if circle_flag:
                end_pos = event.pos
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]
                radius = int(math.sqrt(dx ** 2 + dy ** 2))
                cent = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                sc.fill('black')
                pygame.draw.circle(sc, color, cent, radius)
            if square_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                sc.fill('black')
                pygame.draw.rect(sc, color, pygame.Rect(x, y, width_rect, width_rect), 2)
            if r_triangle_flag:
                end_pos = event.pos
                point1 = start_pos
                point2 = (start_pos[0], end_pos[1])
                point3 = end_pos
                sc.fill('black')
                pygame.draw.polygon(sc, color, [point1, point2, point3], 0)
            if e_triangle_flag:
                end_pos = event.pos
                side_length = int(math.sqrt((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2))
                height = int(math.sqrt(3) * side_length / 2)
                point1 = start_pos
                point2 = (start_pos[0] + side_length, start_pos[1])
                point3 = (start_pos[0] + side_length // 2, start_pos[1] - height)
                sc.fill('black')
                pygame.draw.polygon(sc, color, [point1, point2, point3])
            if rhombus_flag:
                end_pos = event.pos
                mid_point_x = (start_pos[0] + end_pos[0]) // 2
                mid_point_y = (start_pos[1] + end_pos[1]) // 2
                side_length = int(math.sqrt((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2)) // 2

                point1 = start_pos
                point2 = (mid_point_x, mid_point_y - side_length)
                point3 = end_pos
                point4 = (mid_point_x, mid_point_y + side_length)
                sc.fill('black')
                pygame.draw.polygon(sc, color, [point1, point2, point3, point4], 0)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            check_draw = False
            rect_flag = False
            circle_flag = False
            square_flag = False
            r_triangle_flag = False
            e_triangle_flag = False
            rhombus_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 10 <= event.pos[0] <= 90 and 310 <= event.pos[1] <= 390:
                color = 'red'
                width_line = 2
            elif 110 <= event.pos[0] <= 190 and 310 <= event.pos[1] <= 390:
                color = "blue"
                width_line = 2
            elif 210 <= event.pos[0] <= 290 and 310 <= event.pos[1] <= 390:
                width_line = 2
                color = "green"
            elif 310 <= event.pos[0] <= 390 and 310 <= event.pos[1] <= 390:
                color = "white"
                width_line = 2
            elif 390 <= event.pos[0] <= 490 and 310 <= event.pos[1] <= 490:
                color = "black"
                width_line = 40
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            sc.fill(0)
    pygame.display.update()

pygame.quit()
