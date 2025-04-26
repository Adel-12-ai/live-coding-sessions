# print("Hello World")
# a = int('input(введите первое число:')
# b = int('input(введите второе число')
#
# operation = input('введите операцию')
#
# result = 0
#
# if  operation  =='+':
#     result = a + b
#
# if operation == '-':
#     result = a - b
#
# elif operation == '*':
#     result
# from numpy.f2py.crackfortran import expectbegin

# name = ''
# if name == 'Sam':
#     print('Hello Sam')
#
# elif name == 'Name':
#         print('Hello Name')
#
# else:
#     print('Нет такого имени')
#
#
# Login = input('Введите логин: ')
# password = input('Введите пароль: ')
#
# if login == 'example':
#     if password == '123':
#         print('Open')
#
#     else:
#         print('Неверный пароль')
# else:
#     print('Неверные данные')




'''
исключения в pyhton
'''
"""
1. try
try:
    num = int(input('Число: '))
    print (num)
except ValueError:
    print ('Ожидалось что вы вводите число.')
"""

"""
2. finaly
try:
    num = int(input('Число: '))
    print (num)
except ValueError:
    print ('Ожидалось что вы вводите число.')
finally:
    print('Блок finaly')
    print('Будет выведено в любом случае')
"""



# try:
#     num = int(input('Число: '))
#     print (num)
# except ValueError:
#     print ('Ожидалось что вы вводите число.')
# finally:
#     print('Блок finaly')
#     print('Будет выведено в любом случае')
#
#
#
#
# try:
#     a = int(input('Введите число: '))
#     b = int(input('Введите число: '))
#     print(a/b)
# except ZeroDivisionError:
#     print ('Вы делите на 0, а на ноль нельза делать ')
# except ValueError:
#     print ('Ожидалось что вы вводите число.')
#
#
#
#
# try:
#     with open("file/text.txt",'w') as file:
#         file.write('awe')
# except FileNotFoundError:
#     print ('Такой директории нге существует')





# ZeroDivisionError
# try:
#     a = 5
#     b = 0
#     print(a / b)
# except ZeroDivisionError:
#     print('Вы делите на ноль.')
#
# ValueError
# try:
#     num = int(input('Введите число: '))
#     print(num)
# except ValueError:
#     print('Был введен не то что ожидалось(целое число)')
#
# FileNotFoundError
# try:
#     with open('file/text.txt', 'w') as file:
#         file.write('awe')
# except FileNotFoundError:
#     print('Такой директории не существует')





# while True:
#     try:
#         a, b = map(int, input("Введите два числа: ").split())
#         result = a / b
#         print(f"Результат: {result}")
#         break
#     except ZeroDivisionError:
#         print("Ошибка: на ноль делить нельзя! Попробуйте снова.")
#     except ValueError:
#         print("Ошибка: введите два целых числа!")





# def divide_numbers(a,b):
#     while True:
#         try:
#             result = a / b
#             print(f"Результат: {result}")
#             return result
#         except ZeroDivisionError:
#             print("Ошибка: на ноль делить нельзя! Попробуйте снова.")
#         except ValueError:
#             print("Ошибка: введите два целых числа!")
# print(divide_numbers(5,0))





# def div(a,b):
#     while True:
#         try:
#             a, b = map(int, input("Введите два числа: ").split())
#             result = a / b
#             print(f"Результат: {result}")
#             break
#         except ZeroDivisionError:
#             print("Ошибка: на ноль делить нельзя! Попробуйте снова.")
#         except ValueError:
#             print("Ошибка: введите два целых числа!")
# print(div(8,0))




'''
Функция принимает два числа от пользователя
чтобы эти два числа разделить на друг-друга,
если он ввел корректно (то есть оба числа - не ноль) - все обработается корректно.
Если нет, то выплываливаем конкретное (соответствующее исключение)
и просим ввести данные снова (пока не введет корректные данные).
'''
# def func(a, b):
#     result = a / b
#     return f'Результат: {result}'
#
# while True:
#     try:
#         my_func = func(
#             int(input('Первое число: ')),
#             int(input('Второе число: '))
#         )
#         print(my_func)
#         break
#     except ValueError:
#         print('Неправильное значение')
#     except ZeroDivisionError:
#         print('Деление на ноль')





# from direct.showbase.ShowBase import ShowBase
# from math import sin, cos, pi
#
# class MyApp(ShowBase):
#     def __init__(self):
#         super().__init__()
#
#         # Создаем куб
#         self.cube = self.loader.loadModel("models/box")
#         self.cube.reparentTo(self.render)
#         self.cube.setScale(1, 1, 1)
#         self.cube.setPos(0, 10, 0)
#
#         # Камера настраивается на куб
#         self.camera.setPos(0, -20, 5)
#         self.camera.lookAt(self.cube)
#
#         # Системы для движения
#         self.angle_degrees = 0
#
#         # Задаем событие для обновления сцены
#         self.taskMgr.add(self.update, "update")
#
#     def update(self, task):
#         # Обновляем угол поворота
#         self.angle_degrees += 1
#         if self.angle_degrees > 360:
#             self.angle_degrees = 0
#
#         # Поворачиваем куб
#         self.cube.setH(self.angle_degrees)
#
#         return task.cont
#
# app = MyApp()
# app.run()








import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки змейки
snake_block = 20
snake_speed = 10

# Шрифт
font_style = pygame.font.SysFont("bahnschrift", 25)

# Функция для отображения текста
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Основная функция игры
def gameLoop():
    game_over = False
    game_close = False

    # Начальная позиция змейки
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Начальная скорость
    x1_change = 0
    y1_change = 0

    # Тело змейки
    snake = []
    length_of_snake = 1

    # Позиция еды
    foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Вы проиграли! Press Q для выхода или C для новой игры", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake.append(snake_head)
        if len(snake) > length_of_snake:
            del snake[0]

        for x in snake[:-1]:
            if x == snake_head:
                game_close = True

        for segment in snake:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

gameLoop()