import pygame
import random


#Инициализировать Pygame
pygame.init()

#Установление размера экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector")

#Установление цвет фона
bg_color = (200, 200, 200)

#Загружение изображения монеты и установка ее размера
coin_image = pygame.image.load("coin.png")
coin_size = (50, 50)
coin_image = pygame.transform.scale(coin_image, coin_size)

#Установика шрифта для подсчета монет
font = pygame.font.Font(None, 30)

#Инициализировать переменные для количества монет и списка монет
coin_count = 0
coins = []

#Определение функции для добавления монеты на экран в случайном месте
def add_coin():
    x = random.randint(0, screen_width - coin_size[0])
    y = random.randint(0, screen_height - coin_size[1])
    coins.append((x, y))

#Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очищение экрана и нарисование дороги 
    screen.fill(bg_color)
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, screen_width, screen_height/2))

    # Добавить монеты случайным образом
    if random.random() < 0.01:
        add_coin()

    # Проверка на столкновение с монетами и обновление количества монет
    for coin in coins:
        coin_rect = pygame.Rect(coin, coin_size)
        if coin_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            coins.remove(coin)
            coin_count += 1

    #Рисование монет и количество монет
    for coin in coins:
        screen.blit(coin_image, coin)
    coin_text = font.render(f"Coins collected: {coin_count}", True, (0, 0, 0))
    screen.blit(coin_text, (screen_width - coin_text.get_width() - 10, 10))

    #обновить дисплей
    pygame.display.update()

# Выйти из Pygame
pygame.quit()