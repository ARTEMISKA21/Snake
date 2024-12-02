import random
import os
import time
import sys
import keyboard

width = 20
height = 10
snake = [(5, 5), (5, 4), (5, 3)]
direction = (0, 1)
food = (random.randint(0, height - 1), random.randint(0, width - 1))

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(height):
        for x in range(width):
            if (y, x) in snake:
                print("O", end="")
            elif (y, x) == food:
                print("X", end="")
            else:
                print(".", end="")
        print()
    print("Используйте стрелки для управления. Нажмите 'q' для выхода.")

def update_snake():
    global food
    head_y, head_x = snake[0]
    new_head = (head_y + direction[0], head_x + direction[1])

    if (new_head in snake or
            new_head[0] < 0 or new_head[0] >= height or
            new_head[1] < 0 or new_head[1] >= width):
        print("Игра окончена!")
        sys.exit()

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, height - 1), random.randint(0, width - 1))
        while food in snake:
            food = (random.randint(0, height - 1), random.randint(0, width - 1))
    else:
        snake.pop()

while True:
    print_board()

    if keyboard.is_pressed('q'):
        print("Вы вышли из игры.")
        break

    if keyboard.is_pressed('up'):
        direction = (-1, 0)
    elif keyboard.is_pressed('down'):
        direction = (1, 0)
    elif keyboard.is_pressed('left'):
        direction = (0, -1)
    elif keyboard.is_pressed('right'):
        direction = (0, 1)

    update_snake()
    time.sleep(0.1)
