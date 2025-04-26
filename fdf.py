'''
крестики нолики
'''
# def print_board(board):
#     print("\n")
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 5)
#
# def check_winner(board, player):
#     # Проверка строк
#     for row in board:
#         if row.count(player) == 3:
#             return True
#     # Проверка столбцов
#     for col in range(3):
#         if board[0][col] == player and board[1][col] == player and board[2][col] == player:
#             return True
#     # Проверка диагоналей
#     if board[0][0] == player and board[1][1] == player and board[2][2] == player:
#         return True
#     if board[0][2] == player and board[1][1] == player and board[2][0] == player:
#         return True
#     return False
#
# def check_draw(board):
#     # Если нет пустых ячеек, то ничья
#     for row in board:
#         if " " in row:
#             return False
#     return True
#
# def tic_tac_toe():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     players = ["X", "O"]
#     turn = 0
#
#     while True:
#         print_board(board)
#         current_player = players[turn % 2]
#         print(f"Ход игрока {current_player}")
#
#         # Ввод координат
#         while True:
#             try:
#                 row, col = map(int, input("Введите номер строки и столбца (0-2), разделённые пробелом: ").split())
#                 if board[row][col] == " ":
#                     board[row][col] = current_player
#                     break
#                 else:
#                     print("Эта клетка уже занята. Попробуйте снова.")
#             except (ValueError, IndexError):
#                 print("Неверный ввод. Введите два числа от 0 до 2.")
#
#         if check_winner(board, current_player):
#             print_board(board)
#             print(f"Игрок {current_player} победил!")
#             break
#         elif check_draw(board):
#             print_board(board)
#             print("Ничья!")
#             break
#
#         turn += 1
#
# if __name__ == "__main__":
#     tic_tac_toe()



'''
менджер задач
'''
# def print_tasks(tasks):
#     if not tasks:
#         print("Задачи не найдены.")
#     else:
#         for index, task in enumerate(tasks, 1):
#             status = "Выполнено" if task["done"] else "Не выполнено"
#             print(f"{index}. {task['title']} - {status}")
#
#
# def add_task(tasks):
#     title = input("Введите название задачи: ")
#     task = {"title": title, "done": False}
#     tasks.append(task)
#     print(f"Задача '{title}' добавлена.")
#
#
# def remove_task(tasks):
#     print_tasks(tasks)
#     try:
#         task_index = int(input("Введите номер задачи для удаления: ")) - 1
#         if 0 <= task_index < len(tasks):
#             removed_task = tasks.pop(task_index)
#             print(f"Задача '{removed_task['title']}' удалена.")
#         else:
#             print("Задача с таким номером не найдена.")
#     except ValueError:
#         print("Некорректный ввод.")
#
#
# def mark_task_done(tasks):
#     print_tasks(tasks)
#     try:
#         task_index = int(input("Введите номер задачи для пометки как выполненную: ")) - 1
#         if 0 <= task_index < len(tasks):
#             tasks[task_index]["done"] = True
#             print(f"Задача '{tasks[task_index]['title']}' помечена как выполненная.")
#         else:
#             print("Задача с таким номером не найдена.")
#     except ValueError:
#         print("Некорректный ввод.")
#
#
# def task_manager():
#     tasks = []
#     while True:
#         print("\nМенеджер задач")
#         print("1. Показать задачи")
#         print("2. Добавить задачу")
#         print("3. Удалить задачу")
#         print("4. Пометить задачу как выполненную")
#         print("5. Выйти")
#
#         choice = input("Выберите действие: ")
#
#         if choice == "1":
#             print_tasks(tasks)
#         elif choice == "2":
#             add_task(tasks)
#         elif choice == "3":
#             remove_task(tasks)
#         elif choice == "4":
#             mark_task_done(tasks)
#         elif choice == "5":
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный выбор. Попробуйте снова.")
#
#
# if __name__ == "__main__":
#     task_manager()






'''
конвертер
'''
# def convert(amount, from_currency, to_currency):
#     rates = {
#         'USD': 87.45,
#         'EUR': 91.5951,
#         'CNY': 12.0471,
#         'RUB': 0.9599,
#         'KGS': 1
#     }
#     if from_currency not in rates or to_currency not in rates:
#         print("Неправильная валюта!")
#         return None
#     if from_currency == to_currency:
#         return amount
#     amount_in_soms = amount / rates[from_currency]
#     converted_amount = amount_in_soms * rates[to_currency]
#     return converted_amount
# from_currency = input("Введите исходную валюту (USD, EUR, CNY, RUB, KGS): ").upper()
# amount = float(input("Введите сумму для конвертации: "))
# to_currency = input("Введите целевую валюту (USD, EUR, CNY, RUB, KGS): ").upper()
# converted_amount = convert(amount, from_currency, to_currency)
# if converted_amount is not None:
#     print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


# def convert(amount, from_currency, to_currency):
#     rates = {
#         'USD': 87.58,
#         'EUR': 91.63,
#         'CNY': 12.03,
#         'RUB': 0.96,
#         'KGS': 1
#     }
#
#     if from_currency == 'KGS' and to_currency == 'KGS':
#         return amount
#
#     if from_currency not in rates or to_currency not in rates:
#         print("Неправильная валюта!")
#         return None
#
#     # Если исходная валюта KGS, то делим на курс
#     if from_currency == 'KGS':
#         return amount / rates[to_currency]
#
#     # Если целевая валюта KGS, то умножаем на курс
#     if to_currency == 'KGS':
#         return amount * rates[from_currency]
#
#     # Конвертация между другими валютами через KGS
#     amount_in_soms = amount / rates[from_currency]
#     converted_amount = amount_in_soms * rates[to_currency]
#     return converted_amount
#
#
# # Ввод пользователя
# from_currency = input("Введите исходную валюту (USD, EUR, CNY, RUB, KGS): ").upper()
# amount = float(input("Введите сумму для конвертации: "))
# to_currency = input("Введите целевую валюту (USD, EUR, CNY, RUB, KGS): ").upper()
#
# # Преобразование
# converted_amount = convert(amount, from_currency, to_currency)
# if converted_amount is not None:
#     print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

'''
Калькулятор
'''
# def calculator():
#     while True:
#         print("\nКалькулятор")
#         print("1. Сложение")
#         print("2. Вычитание")
#         print("3. Умножение")
#         print("4. Деление")
#         print("5. Выйти")
#
#         choice = input("Выберите операцию: ")
#
#         if choice == '5':
#             break
#
#         try:
#             num1 = float(input("Введите первое число: "))
#             num2 = float(input("Введите второе число: "))
#
#             if choice == '1':
#                 print(f"{num1} + {num2} = {num1 + num2}")
#             elif choice == '2':
#                 print(f"{num1} - {num2} = {num1 - num2}")
#             elif choice == '3':
#                 print(f"{num1} * {num2} = {num1 * num2}")
#             elif choice == '4':
#                 if num2 == 0:
#                     print("Ошибка! Деление на ноль.")
#                 else:
#                     print(f"{num1} / {num2} = {num1 / num2}")
#             else:
#                 print("Неверный выбор")
#         except ValueError:
#             print("Ошибка! Введите правильные числа.")




'''
Угадай число
'''
# import random
# def guess_number():
#     number = random.randint(1, 100)
#     attempts = 0
#     print("Угадай число от 1 до 100")
#     while True:
#         try:
#             guess = int(input("Введите ваше предположение: "))
#             attempts += 1
#             if guess < number:
#                 print("Слишком мало! Попробуйте снова.")
#             elif guess > number:
#                 print("Слишком много! Попробуйте снова.")
#             else:
#                 print(f"Поздравляю, вы угадали число {number} за {attempts} попыток!")
#                 break
#         except ValueError:
#             print("Пожалуйста, введите число.")
# guess_number()