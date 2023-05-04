# импортируем модули random, time и pygame
import pygame
import random
import time
import psycopg2

pygame.init() # инициализирует все модули pygame

# такие постоянные, как размер экрана (длина и ширина), несколько цветов
size = width, height = (800, 800)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (0, 244, 0)
PURPLE = (221, 160, 221)
GREEN1 = (152, 251, 152)
GREEN2 = (50, 205, 50)
done = False
font = pygame.font.SysFont("Verdana", 20) # шрифт - Verdana, размер - 20
font1 = pygame.font.SysFont("Verdana", 70) # шрифт - Verdana, размер - 120
font2 = pygame.font.SysFont("Verdana", 30) # шрифт - Verdana, размер - 30
font3 = pygame.font.SysFont("Verdana", 40) # шрифт - Verdana, размер - 30
font4 = pygame.font.SysFont("Verdana", 25) # шрифт - Verdana, размер - 30
level_text = font.render("LEVEL:", True, BLACK) # Создаем текст черного цвета - "LEVEL"
score_text = font.render("SCORE:", True, BLACK) # Создаем текст черного цвета - "SCORE"
user_text = font.render("USER:", True, BLACK)
game_over_text = font1.render("GAME OVER", True, BLACK) # Создаем текст для окончания игры
pause_text = font.render("PAUSE", True, BLACK)
continue_text = font.render("CONTINUE", True, BLACK)
exit_text = font.render("EXIT", True, BLACK)
enter_name_text = font3.render("Please, enter the user name:", True, BLACK)
len = 110
input_rect = pygame.Rect(230, 700, 200, 43)
active = False
text = ''
image = pygame.image.load('snakelogo.png')
scale = pygame.transform.scale(image, (image.get_width()*1.58, image.get_height()*1.2))
image1 = pygame.image.load('f.jpg')
sql1 = """
        SELECT * FROM snake_score
        """
new_user_text = font3.render("A new user created", True, BLACK)
welcome_text = font2.render("Welcome,", True, BLACK)
welcome_back_text = font2.render("Welcome back,", True, BLACK)
your_prev_score = font4.render("Your previous score is", True, BLACK)
your_prev_level = font4.render("Your previous level is", True, BLACK)

screen = pygame.display.set_mode(size) # создаем экран вышеупомянутыми размерами
screen.fill(WHITE) # экран заполняем белым
pygame.display.set_caption('Snake') # добавляем название игры в верхней части экрана заголовка
FPS = 30 # 30 кадров в секунду
clock = pygame.time.Clock() # для отслеживания времени

def insert_number(user_name, user_score, user_level):
        sql = """
        INSERT INTO snake_score(user_name, user_score, user_level)
        VALUES(%s, %s, %s)
        ON CONFLICT (user_name) DO UPDATE SET user_level = EXCLUDED.user_level, user_score = EXCLUDED.user_score
        """

        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (user_name, user_score, user_level))
            cur.execute(sql1)
            a = cur.fetchall()
            conn.commit()
            cur.close()
  
        except Exception as e:
            print(str(e))
        finally:
            if conn is not None:
                conn.close()

class Food: # создаем класс Food
    def __init__(self): # функция для инициализации
        self.x = random.randint(35, 760) # центр выбирается рандомно
        self.y = random.randint(95, 765)
        self.width = random.randint(10, 12) # ширина генерируется рандомно
    
    def gen(self): # функция, которая генерирует новую еду (рандомно выбирая координату по Ох и Оу и ширину)
        self.x = random.randint(35, 760)
        self.y = random.randint(95, 765)
        self.width = random.randint(10, 12)

    def draw(self): # функция, которая отрисовывает еду (прямоугольник на экране, зеленого цвета, координаты цента инициализированы выше, а длина = 15, а ширина инициализирована выше)
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 15, self.width))

F1 = Food() # вызываем класс Food

class Snake: # создаем класс Snake
    def __init__(self, x, y): # функция для инициализации
        self.elements = [[x, y]] # координаты центров окружностей
        self.size = 1 # размер змейки (количество окружностей)
        self.radius = 10 # радиус окружности
        self.dx = 6 # перемещение по Ох
        self.dy = 0 # перемещение по Оу
        self.speed = 24 # скорость змейки
        self.is_add = False # переменная по добавлению новых элементов (окружностей)
        self.direction = 'RIGHT' # направление движения змейки
        self.change_direction = self.direction # направление движения становится равным изменению направления 
        self.level = 1 # уровень
        self.score = 0 # счетчик съеденной еды
        self.a = 0

    def draw(self): # функция, которая отрисовывает элементы (окружности на экране желтого цвета, центр и радиус инициализированы выше)
        for element in self.elements:
            pygame.draw.circle(screen, YELLOW, element, self.radius)

    def add_to_snake(self): # функция, которая добавляет (увеличивает размер, счетчик еды, добавляет элементы (центры новых окружностей))
        self.size += 1
        global len
        self.elements.append([0, 0])
        self.ball = F1.width - 9 # переменная, которая показывает балл в зависимости от ширины еды
        self.score += self.ball
        self.is_add = False # переменная по добавлению новых элементов (окружностей) принимает значение False
        if self.score % 4 == 0 and self.score > 0: # если размер змейки кратен 4, то уровень повышается, а скорость увеличивается на 10
            # self.change_walls()
            self.a = random.randint(200, 300)
            len += 10
            self.level += 1
            self.speed += 20
        if self.ball == 2:
            if self.score % 4 != 0:
                if (self.score - 1) % 4 == 0:
                    # self.change_walls()
                    self.a = random.randint(200, 300)
                    len += 25
                    self.level += 1
                    self.speed += 10
        if self.ball == 3:
            if self.score % 4 != 0:
                if (self.score - 1) % 4 == 0 or (self.score - 2) % 4 == 0:
                    # self.change_walls()
                    len += 25
                    self.a = random.randint(200, 300)
                    self.level += 1
                    self.speed += 10

    def check_direction(self): # функция, которая меняет направление: если, например, направление - "вправо", а изменение направление - любое, но не "влево", тогда направление движения становится равным изменению движения
        if (self.direction == 'RIGHT' and self.change_direction != 'LEFT') or (self.direction == 'LEFT' and self.change_direction != 'RIGHT') or (self.direction == 'UP' and self.change_direction != 'DOWN') or (self.direction == 'DOWN' and self.change_direction != 'UP'):
            self.direction = self.change_direction

    def game_over(self): # функция для окончания игры: экран заполняется красным, и выходят тексты о том, что игра закончена и о конечных баллах и уровнях. а также, игра закрывается спустя 6 секунд
        screen.fill(RED)
        screen.blit(game_over_text, (180, 300))
        screen.blit(user_text, (330, 400))
        screen.blit(text_surface, (410, 400))
        screen.blit(level_text, (250, 450))
        screen.blit(score_text, (450, 450))
        t1 = font2.render(str(self.score), True, BLACK)
        screen.blit(t1, (470, 480))
        t2 = font2.render(str(self.level), True, BLACK)
        screen.blit(t2, (280, 480))
        pygame.display.flip()
        insert_number(text, S1.score, S1.level)
        time.sleep(6)
        pygame.quit()


    def move(self): # функция по передвижению
    #  pygame.draw.line(screen, BLACK, (20, S1.a), (20 + len, S1.a), 5)
    #                 pygame.draw.line(screen, BLACK, (20, S1.a + 70), (20 + len, S1.a + 70), 5)
    #                 pygame.draw.line(screen, BLACK, (20, S1.a + 200), (20 + len, S1.a + 200), 5)
    #                 pygame.draw.line(screen, BLACK, (780 - len, S1.a + 100), (780, S1.a + 100), 5)
    #                 pygame.draw.line(screen, BLACK, (780 - len, S1.a + 250), (780, S1.a + 250), 5)
        if self.is_add: # если переменная по добавлению новых элементов (окружностей) принимает значение True, то выполняется функция add_to_snake
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1): # пробегаемся от последнего элемента змейки до первого, чтобы каждый предыдущий элемент (окружность) принимал место следующего за ним
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        if self.direction == 'RIGHT': # если направление - "вправо" и змейка не выходит за границы экрана, то она двигается вправо (координаты элементов по Ох увеличиваются на 5), а в противном случае возвращается влево, на начальную координату по Ох
            if self.level > 1:
                if (self.elements[0][0] >= (780 - len - 10) and self.elements[0][0] <= (780 - len + 10) and self.elements[0][1] >= self.a + 90 and self.elements[0][1] <= self.a + 110) or (self.elements[0][0] >= (780 - len - 10) and self.elements[0][0] <= (780 - len + 10) and self.elements[0][1] >= self.a + 240 and self.elements[0][1] <= self.a + 260):
                    self.game_over()
                else:
                    if self.elements[0][0] <= 763 and self.elements[0][0] >= 31:
                        self.elements[0][0] += self.dx

                    else:
                        if self.level > 1:
                            if (self.elements[0][1] >= self.a + 60 and self.elements[0][1] <= self.a + 80) or (self.elements[0][1] >= self.a + 210 and self.elements[0][1] <= self.a + 230) or (self.elements[0][1] >= self.a - 10 and self.elements[0][1] <= self.a + 10):
                                self.game_over()
                            else:
                                self.elements[0][0] = 31
                        else:
                            self.elements[0][0] = 31
            else:
                if self.elements[0][0] <= 763 and self.elements[0][0] >= 31:
                    self.elements[0][0] += self.dx
                else:
                    self.elements[0][0] = 31
        elif self.direction == 'LEFT': # если направление - "влево" и змейка не выходит за границы экрана, то она двигается влево (координаты элементов по Ох уменьшаются на 5), а в противном случае возвращается вправо, на конечную координату по Ох
            if self.level > 1:
                if (self.elements[0][0] >= (20 + len) and self.elements[0][0] <= (30 + len) and self.elements[0][1] >= self.a - 10 and self.elements[0][1] <= self.a + 10) or (self.elements[0][0] >= (20 + len) and self.elements[0][0] <= (30 + len) and self.elements[0][1] >= self.a + 60 and self.elements[0][1] <= self.a + 80) or (self.elements[0][0] >= (20 + len) and self.elements[0][0] <= (30 + len) and self.elements[0][1] >= self.a + 190 and self.elements[0][1] <= self.a + 210):
                    self.game_over()
                else:
                    if self.elements[0][0] <= 763 and self.elements[0][0] >= 35:
                        self.elements[0][0] -= self.dx
                    else:
                        if self.level > 1:
                            if (self.elements[0][1] >= self.a + 90 and self.elements[0][1] <= self.a + 110) or (self.elements[0][1] >= self.a + 240 and self.elements[0][1] <= self.a + 260) or (self.elements[0][1] >= self.a + 200 and self.elements[0][1] <= self.a + 300):
                                self.game_over()
                            else:
                                self.elements[0][0] = 763
                        else:
                            self.elements[0][0] = 763
            else:
                if self.elements[0][0] <= 763 and self.elements[0][0] >= 35:
                    self.elements[0][0] -= self.dx
                else:
                    self.elements[0][0] = 763
        elif self.direction == 'UP': # если направление - "вверх" и змейка не выходит за границы экрана, то она двигается вниз (координаты элементов по Оу уменьшаются на 5), а в противном случае игра окончивается, вызываем вышеупомянутую функцию
            if self.level == 1:
                if self.elements[0][1] <= 770 and self.elements[0][1] >= 96:
                    self.elements[0][1] -= self.dy
                else:
                    if self.score < 3:
                        self.game_over()
                    else:
                        self.elements[0][1] = 770
            else:
                if (self.elements[0][0] >= 0 and self.elements[0][0] <= 30 + len and self.elements[0][1] >= self.a - 10 and self.elements[0][1] <= self.a + 10) or (self.elements[0][0] >= 770 - len and self.elements[0][0] <= 790 and self.elements[0][1] >= self.a + 90 and self.elements[0][1] <= self.a + 110) or (self.elements[0][0] >= 770 - len and self.elements[0][0] <= 790 and self.elements[0][1] >= self.a + 240 and self.elements[0][1] <= self.a + 260) or (self.elements[0][0] >= 0 and self.elements[0][0] <= 30 + len and self.elements[0][1] >= self.a + 190 and self.elements[0][1] <= self.a + 210) or (self.elements[0][0] >= 0 and self.elements[0][0] <= 30 + len and self.elements[0][1] >= self.a + 60 and self.elements[0][1] <= self.a + 70):
                    self.game_over()
                else:
                    if self.elements[0][1] <= 770 and self.elements[0][1] >= 96:
                        self.elements[0][1] -= self.dy
                    else:
                        if self.score < 3:
                            self.game_over()
                        else:
                            self.elements[0][1] = 770
        elif self.direction == 'DOWN': # если направление - "вниз" и змейка не выходит за границы экрана, то она двигается вниз (координаты элементов по Оу увеличиваются на 5), а в противном случае возвращается вверх, на начальную координату по Оу
            if self.level == 1:
                if self.elements[0][1] <= 770 and self.elements[0][1] >= 96:
                    self.elements[0][1] += self.dy
                else:
                    if self.score >= 3:
                        self.game_over()
                    else:
                        self.elements[0][1] = 96
            else:
                if (self.elements[0][0] >= 0 and self.elements[0][0] <= 30 + len and self.elements[0][1] >= self.a - 10 and self.elements[0][1] <= self.a + 10) or (self.elements[0][0] >= 770 - len and self.elements[0][0] <= 790 and self.elements[0][1] >= self.a + 90 and self.elements[0][1] <= self.a + 110) or (self.elements[0][0] >= 770 - len and self.elements[0][0] <= 790 and self.elements[0][1] >= self.a + 240 and self.elements[0][1] <= self.a + 260) or (self.elements[0][0] >= 0 and self.elements[0][0] <= 30 + len and self.elements[0][1] >= self.a + 190 and self.elements[0][1] <= self.a + 210) or (self.elements[0][0] >= 0 and self.elements[0][0] <= 30 + len and self.elements[0][1] >= self.a + 60 and self.elements[0][1] <= self.a + 70):
                    self.game_over()
                else:
                    if self.elements[0][1] <= 770 and self.elements[0][1] >= 96:
                        self.elements[0][1] += self.dy
                    else:
                        if self.score >= 3:
                            self.game_over()
                        else:
                            self.elements[0][1] = 96

    def eat(self, foodx, foody): # функция для подсчета съеденной еды, которой передаем 2 параметра, которые являются координатами центра еды (окружности)
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx - 12 <= x <= foodx + 20 and foody - 12 <= y <= foody + 20: # если центр элемента (окружности) лежит в данном интервале, то функция возвращает значение True
            return True
        return False

S1 = Snake(30, 96) # вызываем класс Snake
d = 6 # переменная для передвижения

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 400 and  pygame.mouse.get_pos()[0] <= 512 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 350:
                    pygame.quit()
                    quit()
                if pygame.mouse.get_pos()[0] >= 258 and  pygame.mouse.get_pos()[0] <= 370 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 350:
                    paused = False
        screen.fill(RED)
        screen.blit(user_text, (330, 400))
        screen.blit(text_surface, (410, 400))
        screen.blit(level_text, (250, 440))
        screen.blit(score_text, (450, 440))
        t1 = font2.render(str(S1.score), True, BLACK)
        screen.blit(t1, (470, 470))
        t2 = font2.render(str(S1.level), True, BLACK)
        screen.blit(t2, (280, 470))
        pygame.draw.rect(screen, BLACK, (258, 300, 112, 50), 1)
        screen.blit(continue_text, (260, 310))
        pygame.draw.rect(screen, BLACK, (400, 300, 112, 50), 1)
        screen.blit(exit_text, (430, 310))
        pygame.display.update()
        clock.tick(5)


time_delay = 15000
timer_event = pygame.USEREVENT + 1 # создаем новое событие timer_event, которое происходит каждые 15 секунд
pygame.time.set_timer(timer_event, time_delay)

# Игровой цикл, в котором программа продолжает цикл снова и снова, пока не произойдет событие типа QUIT
i = 100

def aq():
    do = False
    while not do:
        clock.tick(S1.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do = True
                insert_number(text, S1.score, S1.level)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 226 and pygame.mouse.get_pos()[0] <= 324 and pygame.mouse.get_pos()[1] <= 79 and pygame.mouse.get_pos()[1] >= 31:
                        pause()
            if event.type == timer_event: # если происходит событие timer_event, то заново генерируем еду (вызываем функцию gen из класса Food)
                F1.gen()
            if event.type == pygame.KEYDOWN: # если нажали какую-то клавишу клавиатуры
                if event.key == pygame.K_ESCAPE: # если нажали ESC, то выходим из игры
                    done = True
                if event.key == pygame.K_RIGHT and S1.dx != d: # если нажата кнопка "right" и перемещение направлено не влево, то направление = "right", а двигаться будет по Ох на 5 вправо
                    S1.direction = 'RIGHT'
                    S1.dx = d
                    S1.dy = 0
                if event.key == pygame.K_LEFT and S1.dx != d: # если нажата кнопка "left" и перемещение направлено не вправо, то направление = "left", а двигаться будет по Ох на 5 влево
                    S1.direction = 'LEFT'
                    S1.dx = d
                    S1.dy = 0
                if event.key == pygame.K_UP and S1.dy != d: # если нажата кнопка "up" и перемещение направлено не вниз, то направление = "up", а двигаться будет по Он на 5 вверх
                    S1.direction = 'UP'
                    S1.dx = 0
                    S1.dy = d
                if event.key == pygame.K_DOWN and S1.dy != d: # если нажата кнопка "down" и перемещение направлено не вверх, то направление = "down", а двигаться будет по Оу на 5 вниз
                    S1.direction = 'DOWN'
                    S1.dx = 0
                    S1.dy = d

        screen.blit(image1, (0, 0))
        levels = font.render(str(S1.level), True, BLACK) # текст, содержащий номер уровня
        scores = font.render(str(S1.score), True, BLACK) # текст, содержащий количество съеденной еды
        if S1.eat(F1.x, F1.y): # если еда была съедена (функция eat из класса Snake вернула значение True), то переменная is_add из класса Snake возвращает значение True, и тогда вызывается функция gen из класса Food (генерируем новую еду)
            S1.is_add = True
            F1.gen()
        S1.move() # вызываем функцию move для передвижения из класса Snake
        # screen.fill(WHITE) # заполняем экран белым цветом
        screen.blit(level_text, (710, 20)) # выводим текст "LEVEL" на указанную позицию
        screen.blit(levels, (735, 50)) # выводим значение level на указанную позицию
        screen.blit(score_text, (20, 20)) #  выводим текст "SCORE" на указанную позицию
        screen.blit(scores, (45, 50)) # выводим значение score на указанную позицию
        pygame.draw.line(screen, BLACK, (20, 10), (780, 10), 3) # линия для отделения верхней части экрана от текста (толщина = 3)
        if S1.score < 3:
            pygame.draw.line(screen, BLACK, (20, 85), (780, 85), 4) # линия для отделения верхней части экрана от текста (толщина = 2)
        else:
            pygame.draw.line(screen, BLACK, (20, 785), (780, 785), 4)
        if S1.level > 1:
                    pygame.draw.line(screen, BLACK, (20, S1.a), (20 + len, S1.a), 5)
                    pygame.draw.line(screen, BLACK, (20, S1.a + 70), (20 + len, S1.a + 70), 5)
                    pygame.draw.line(screen, BLACK, (20, S1.a + 200), (20 + len, S1.a + 200), 5)
                    pygame.draw.line(screen, BLACK, (780 - len, S1.a + 100), (780, S1.a + 100), 5)
                    pygame.draw.line(screen, BLACK, (780 - len, S1.a + 250), (780, S1.a + 250), 5)

        pygame.draw.rect(screen, BLACK, (20, 85, 760, 700), 3) # прямоугольник для выделения игрового поля
        pygame.draw.rect(screen, BLACK, (225, 30, 100, 50), 3)
        screen.blit(pause_text, (240, 40))
        S1.draw() # вызываем функцию draw для отрисовки змейки
        F1.draw() # вызываем функцию draw для отрисовки еды

        pygame.display.flip() # обновляем содержимое дисплея игры
    pygame.quit()


def new_user():
    did = False
    while not did:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                did = True
        screen.fill(GREEN1)
        text_surface = font2.render(text + '!', True, BLACK)
        screen.blit(scale, (0, 0))
        screen.blit(new_user_text, (170, 630))
        screen.blit(welcome_text, (220, 700))
        screen.blit(text_surface, (400, 700))
        pygame.display.flip()
        time.sleep(3)
        aq()
    pygame.quit()

def old_user():
    will = False
    while not will:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                did = True
        screen.fill(GREEN1)
        text_surface = font2.render(text + '!', True, BLACK)
        previous_score_text = font2.render(str(previous_score), True, BLACK)
        previous_level_text = font2.render(str(previous_level), True, BLACK)
        screen.blit(scale, (0, 0))
        screen.blit(new_user_text, (170, 630))
        screen.blit(welcome_back_text, (200, 690))
        screen.blit(text_surface, (450, 690))
        screen.blit(your_prev_score, (50, 740))
        screen.blit(previous_score_text, (340, 735))
        screen.blit(your_prev_level, (400, 740))
        screen.blit(previous_level_text, (680, 735))
        pygame.display.flip()
        time.sleep(5)
        aq()
    pygame.quit()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            insert_number(text, S1.score, S1.level)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN: # если нажали какую-то клавишу клавиатуры
            if event.key == pygame.K_SPACE and text != '':
                # aq()
                check(text)
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    screen.fill(GREEN1)
    pygame.draw.rect(screen, GREEN2, input_rect)
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(300, text_surface.get_width()+10)
    screen.blit(enter_name_text, (120, 630))
    screen.blit(scale, (0, 0))

    def check(text):
        cnt = 0
        t = False
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql1)
            a = cur.fetchall()
            for i in a:
                if text in i:
                    t = True
                    string = i
            if t:
                done = True
                global previous_score, previous_level
                previous_score = string[2]
                previous_level = string[3]
                print(previous_score)
                old_user()
                # print(prev_score)
            else:
                done = True
                new_user()
            conn.commit()
            cur.close()
        
        except Exception as e:
            print(str(e))
        finally:
            if conn is not None:
                conn.close()

    pygame.display.update()
    clock.tick(30)

pygame.quit() # отключает модуль pygame