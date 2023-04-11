import random
from random import *

import pygame

pygame.init()
sc = pygame.display.set_mode((400, 600))
speed = 5
x = 165
y_c = 0
x_c = randint(0, 340)
y_e = 0
x_e = randint(0, 340)
f = pygame.font.SysFont('arial', 30)
score = 0
clock = pygame.time.Clock()
car = pygame.image.load("top-car.png").convert_alpha()
car = pygame.transform.scale(car, (car.get_width() // 6, car.get_height() // 6))
road = pygame.image.load("road.jpg")
road_cent = road.get_rect(center=(200, 300))
coin = pygame.image.load("coin.jpg")
coin_half = pygame.transform.scale(coin, (coin.get_width() // 40, coin.get_height() // 40))
coin_full = pygame.transform.scale(coin, (coin.get_width() // 25, coin.get_height() // 25))
enemy_car = pygame.image.load("enemy_car.png").convert_alpha()
enemy_car = pygame.transform.scale(enemy_car, (enemy_car.get_width() // 6, enemy_car.get_height() // 6))
enemy_car = pygame.transform.rotate(enemy_car, 180)
enemy_rect = enemy_car.get_rect()
car_rect = car.get_rect()
check = True
flright = False
flleft = False
coin_s = choice([0.5, 1])
if coin_s == 0.5:
    coin = coin_half
if coin_s == 1:
    coin = coin_full

#обновление игрового экрана
while check:
    sc.fill('white')
    sc.blit(road, road_cent)
    sc.blit(coin, (x_c, y_c))
    sc.blit(enemy_car, (x_e, y_e))
    sc.blit(car, (x, 460))
    score_table = f.render(str(score), True, 'red')
    sc.blit(score_table, (0, 0))
    # pygame.draw.rect(sc, 'white', pygame.Rect(x, y_e+100, 5, 5))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
            if event.key == pygame.K_a:
                flleft = True

            if event.key == pygame.K_d:
                flright = True
#нажимается ли в данный момент левая или правая клавиша.
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                flright, flleft = False, False,
#должен функционировать должным образом как часть более крупной игры.
    if x_c + 60 >= x + 35 >= x_c and 600 >= y_c >= 410:
        y_c = 0
        x_c = randint(0, 340)
        score += coin_s
        coin_s = choice([0.5, 1])
        if coin_s == 0.5:
            coin = coin_half
            #для каждого возможного случая перекрытия:
        if coin_s == 1:
            coin = coin_full
        if score % 3 == 0 and score != 0:
            speed += 2
        elif (score - 0.5) % 3 == 0 and (score - 0.5) != 0:
            speed += 2
    if x_e <= x <= x_e + 40 and y_e > 360:
        check = False
    elif x_e <= x + 60 <= x_e + 40 and y_e > 360:
        check = False
    elif x_e <= x + 30 <= x_e + 40 and y_e > 360:
        check = False
    if y_e > 600:
        y_e = 0
        x_e = randint(0, 340)
        score +=1
    if flright and x < 330:
        x += 10
    if flleft and x > 0:
        x -= 10
    y_c += speed
    y_e += speed
      #обновить дисплей
    pygame.display.update()
    clock.tick(60)
     # Выйти из Pygame
pygame.quit()
