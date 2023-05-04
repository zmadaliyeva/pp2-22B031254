import random
from threading import Timer

import pygame

import var
from lineEdit import LineEdit
from winWindow import WinWindow

pygame.init()
yellow = (255, 255, 102)
black = (0, 0, 0)
dis_width = 600
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
snake_block = 32
snake_speed = 8
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
background = pygame.image.load('ground.png')

game_close = False
k = False


foodBx = random.randrange(1,17) * 32
foodBy = random.randrange(3, 15) * 32

def Your_score(score):
    value = score_font.render(str(score), True, yellow)
    dis.blit(value, [70, 10])
    
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def generateFood(img, x, y):
    food = pygame.image.load(img)
    image_rect2 = food.get_rect(topleft = (x, y))
    dis.blit(food, image_rect2)
def generateFoodB(img, x, y):
    global foodBx, foodBy
    if(k):
        food = pygame.image.load(img)
        image_rect2 = food.get_rect(topleft = (x, y))
        dis.blit(food, image_rect2)
def change1():
    global k
    if(k == False):
        k = True
        Timer(random.randrange(10,17), change1).start()
    elif(k):
        k = False
        Timer(random.randrange(10,20), change1).start()
change1()

l = LineEdit(150, 300, 300 ,60, dis)
win = WinWindow(dis)

def gameLoop():
    x1 = 9 * snake_block
    y1 = 10 * snake_block
    x1_change = 0
    y1_change = 0
    snake_List = []
    
    foodx = random.randrange(1,17) * 32
    foody = random.randrange(3, 15) * 32
    foodBx = random.randrange(1,17) * 32
    foodBy = random.randrange(3, 15) * 32
    while var.start:
        dis.fill((0,0,0))
        value = font_style.render('Write Your name', True, yellow)
        dis.blit(value, [200, 240])
        l.update()
        clock.tick(20)
        pygame.display.update()
        
        
    while not var.game_over:
        global k, game_close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 < snake_block or x1 > snake_block*17 or y1 > 17*snake_block or y1 < 3 * snake_block:
            game_close = True

        while game_close == True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        var.game_over = True
                        game_close = False
            
            win.draw_win_window()
        
        x1 += x1_change
        y1 += y1_change
        dis.blit(background, (0, 0))

        generateFood("carrot.png", foodx, foody)
        generateFoodB("apple.png", foodBx, foodBy)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > var.Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(var.Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = random.randrange(1,17) * 32
            foody = random.randrange(3, 15) * 32
            var.Length_of_snake += 1
        if x1 == foodBx and y1 == foodBy and k == True:
            foodBx = random.randrange(1,17) * 32
            foodBy = random.randrange(3, 15) * 32
            var.Length_of_snake += 3
            k = False

        clock.tick(8)

    pygame.quit()
    quit()
gameLoop()