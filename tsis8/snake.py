import pygame
import random

#Инициализировать Pygame
pygame.init()

#Установка размера экрана и заголовока
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

#Установка цвета игры
bg_color = (255, 255, 255)
snake_color = (0, 0, 0)
food_color = (255, 0, 0)

#Установика шрифта для оценки и уровня
font = pygame.font.Font(None, 30)

#Установка игровые переменные
snake_speed = 5
snake_size = 10
food_size = 10
food_pos = (0, 0)
score = 0
level = 1

#Определение функции для создания случайной позиции еды
def generate_food(snake_list):
    while True:
        food_x = random.randrange(snake_size, screen_width - food_size, food_size)
        food_y = random.randrange(snake_size, screen_height - food_size, food_size)
        food_rect = pygame.Rect(food_x, food_y, food_size, food_size)
        if not any(food_rect.colliderect(snake_rect) for snake_rect in snake_list):
            return food_rect

#Установка начального положение и направление змеи
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_dir = "right"
snake_list = [(snake_x, snake_y)]

#Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Обрабатывать пользовательский ввод для направления змеи
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != "right":
        snake_dir = "left"
    elif keys[pygame.K_RIGHT] and snake_dir != "left":
        snake_dir = "right"
    elif keys[pygame.K_UP] and snake_dir != "down":
        snake_dir = "up"
    elif keys[pygame.K_DOWN] and snake_dir != "up":
        snake_dir = "down"

    #Переместить змею в текущем направлении
    if snake_dir == "left":
        snake_x -= snake_speed
    elif snake_dir == "right":
        snake_x += snake_speed
    elif snake_dir == "up":
        snake_y -= snake_speed
    elif snake_dir == "down":
        snake_y += snake_speed

    #Проверка на столкновение со стенами
    if snake_x < snake_size or snake_x > screen_width - snake_size or \
            snake_y < snake_size or snake_y > screen_height - snake_size:
        running = False

    #Обновление положение змеи
    snake_list.insert(0, (snake_x, snake_y))
    snake_list = snake_list[:score+1]

    #Проверка на столкновение с едой и созданаие новой еды
    if pygame.Rect(snake_x, snake_y, snake_size, snake_size).colliderect(food_pos):
        food_pos = generate_food(snake_list)
        score += 1
        if score % 3 == 0:
            level += 1
            snake_speed += 1

    #Очищение экрана и рисование змеи и еду
    screen.fill(bg_color)
    for pos in snake_list:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, food_color, food_pos)

    #Рисование счета и уровеня в правом верхнем углу.
    score_text = font.render(f"Score: {score}", True, snake_color)
    screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))
    level_text = font.render(f"Level: {level}", True, snake_color)
    screen.blit(level_text, (screen_width - level_text.get_width() - 10, 40))

    #Обновление отображение и дожидание следующего кадра
    pygame.display.update()
    pygame.time.wait(1000 // 60)

#Выйти из Pygame
pygame.quit()
