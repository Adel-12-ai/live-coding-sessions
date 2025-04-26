# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#
#
# # Функция, которая будет запускаться при команде /start
# def start(update, context):
#     update.message.reply_text("Привет, я твой Telegram-бот!")
#
#
# # Функция для эхо-сообщений (повторяет сообщения пользователя)
# def echo(update, context):
#     update.message.reply_text(update.message.text)
#
#
# # Основная функция, которая будет запускать бота
# def main():
#     # Вставьте сюда ваш токен, который вы получили от BotFather
#     token = '7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY'
#
#     # Создаем объект Updater, который будет обрабатывать обновления
#     updater = Updater(token, use_context=True)
#
#     # Получаем диспетчер для обработки команд
#     dispatcher = updater.dispatcher
#
#     # Регистрируем обработчики
#     dispatcher.add_handler(CommandHandler('start', start))  # Команда /start
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))  # Эхо для текстовых сообщений
#
#     # Запуск бота
#     updater.start_polling()
#     updater.idle()  # Бот будет работать в фоновом режиме
#
#
# if _name_ == '_main_':
#     main()










# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
#
# # Функция, которая будет запускаться при команде /start
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Привет, я твой Telegram-бот!")
#
# # Функция для эхо-сообщений (повторяет сообщения пользователя)
# def echo(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(update.message.text)
#
# # Основная функция, которая будет запускать бота
# def main() -> None:
#     token = '7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY'  # Вставьте сюда ваш токен
#     updater = Updater(token)
#
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(CommandHandler('start', start))  # Команда /start
#     dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Эхо для текстовых сообщений
#
#     # Запуск бота
#     updater.start_polling()
#     updater.idle()  # Бот будет работать в фоновом режиме
#
# if _name_ == '_main_':
#     main()





# from telegram import Update
# from telegram.ext import CommandHandler, MessageHandler, filters, Application, CallbackContext
#
# # Функция, которая будет запускаться при команде /start
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Привет, я твой Telegram-бот!")
#
# # Функция для эхо-сообщений (повторяет сообщения пользователя)
# def echo(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(update.message.text)
#
# # Основная функция, которая будет запускать бота
# def main() -> None:
#     token = '7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY'  # Вставьте сюда ваш токен
#
#     # Используем Application вместо Updater
#     application = Application.builder().token(token).build()
#
#     # Регистрируем обработчики
#     application.add_handler(CommandHandler('start', start))  # Команда /start
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Эхо для текстовых сообщений
#
#     # Запуск бота
#     application.run_polling()  # Запуск бота с использованием polling
#
# if _name_ == '_main_':
#     main()





# from telegram import Update
# from telegram.ext import Application, CommandHandler, CallbackContext
#
# # Функция, которая будет запускаться при команде /start
# async def start(update: Update, context: CallbackContext) -> None:
#     # Отправка приветственного сообщения
#     await update.message.reply_text("Привет, я твой Telegram-бот!")
#
# # Основная функция, которая будет запускать бота
# async def main() -> None:
#     # Ваш токен
#     token = '7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY'
#
#     # Создание объекта Application
#     application = Application.builder().token(token).build()
#
#     # Добавление обработчика команды /start
#     application.add_handler(CommandHandler("start", start))
#
#     # Запуск бота
#     await application.run_polling()
#
# if _name_ == '_main_':
#     import asyncio
#     asyncio.run(main())



# from telegram import Update
# from telegram.ext import Application, CommandHandler, CallbackContext

# Функция, которая будет запускаться при команде /start
# async def start(update: Update, context: CallbackContext) -> None:
#     await update.message.reply_text("Привет, я твой Telegram-бот!")
#
# # Основная функция, которая будет запускать бота
# async def main() -> None:
#     token = '7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY'  # Вставьте сюда ваш токен
#
#     # Создание объекта Application
#     application = Application.builder().token(token).build()
#
#     # Добавление обработчика команды /start
#     application.add_handler(CommandHandler("start", start))
#
#     # Запуск бота
#     await application.run_polling()
#
# if _name_ == '_main_':
#     import asyncio
#
#     # Запускаем асинхронную функцию
#     asyncio.run(main())




# import telebot
# import sqlite3
#
# bot=telebot.TeleBot('7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY')
# name=None
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id,'Привет сейчас тебя зарегестрируем! Введите имя')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name=message.text.strip()
#     bot.send_message(message.chat.id, 'Введит')
#     bot.register_next_step_handler(message,user_pass)
#
#
#
# def user_pass(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     cur.execute(f"INSERT INTO users(name, pass) VALUES('%s', %s)" % (name,password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardMarkup('Список пользывателей', callback_data='users'))
#     bot.send_message(message.chat.id, 'ПОльзователь зарегестрирован!', reply_markup=markup)
#     # bot.register_next_step_handler(message, user_pass)
#
#
# bot.polling(none_stop=True)





# import telebot
# import sqlite3
#
# bot = telebot.TeleBot('7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY')
# name = None
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегистрируем! Введи имя')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_pass)
#
# def user_pass(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     cur.execute("INSERT INTO users(name, pass) VALUES(?, ?)", (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
#
# bot.polling(none_stop=True)









# import telebot
# import sqlite3
#
# bot = telebot.TeleBot('7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY')
# name = None
#
# # Укажите свой ID в Telegram
# ADMIN_ID = 6427122337  # Замените на свой ID
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегистрируем! Введи имя')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_pass)
#
# def user_pass(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     # Используем параметризованный запрос для предотвращения SQL-инъекций
#     cur.execute("INSERT INTO users(name, pass) VALUES(?, ?)", (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
#
# # Обработчик callback-запросов
# @bot.callback_query_handler(func=lambda call: call.data == 'users')
# def handle_users_list(call):
#     # Проверка, если запрос отправлен от администратора
#     if call.message.chat.id == ADMIN_ID:
#         conn = sqlite3.connect('Syntaxwizard.sql')
#         cur = conn.cursor()
#
#         cur.execute("SELECT name, pass FROM users")
#         users = cur.fetchall()
#
#         conn.commit()
#         cur.close()
#         conn.close()
#
#         if users:
#             user_list = "\n".join([f"Имя: {user[0]}, Пароль: {user[1]}" for user in users])
#             bot.send_message(call.message.chat.id, f"Список пользователей и паролей:\n{user_list}")
#         else:
#             bot.send_message(call.message.chat.id, "Нет зарегистрированных пользователей.")
#     else:
#         bot.send_message(call.message.chat.id, "У вас нет доступа к этой информации.")
#
# bot.polling(none_stop=True)





# import telebot
# import sqlite3
# import random
# from datetime import datetime
#
# bot = telebot.TeleBot('7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY')
#
# # Создаем таблицы для хранения данных
# def create_tables():
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             last_message TEXT,
#             message_count INTEGER
#         )
#     ''')
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS messages(
#             id INTEGER PRIMARY KEY,
#             message_text TEXT,
#             timestamp TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
# create_tables()
#
# # Функция для добавления нового пользователя
# def add_user(user_id, name):
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#     cur.execute('INSERT OR IGNORE INTO users (id, name, last_message, message_count) VALUES (?, ?, ?, ?)',
#                 (user_id, name, '', 0))
#     conn.commit()
#     conn.close()
#
# # Функция для обновления сообщений пользователя
# def update_user_message(user_id, message_text):
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#     cur.execute('UPDATE users SET last_message = ?, message_count = message_count + 1 WHERE id = ?',
#                 (message_text, user_id))
#     conn.commit()
#     conn.close()
#
#     # Сохраняем сообщение в базе данных
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     cur.execute('INSERT INTO messages (message_text, timestamp) VALUES (?, ?)', (message_text, timestamp))
#     conn.commit()
#     conn.close()
#
# # Функция для получения популярного сообщения
# def get_popular_message():
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#     cur.execute('SELECT message_text FROM messages ORDER BY RANDOM() LIMIT 1')  # Просто случайное популярное сообщение
#     message = cur.fetchone()
#     conn.close()
#     return message[0] if message else "Неизвестное сообщение."
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     add_user(message.chat.id, message.chat.first_name)
#     bot.send_message(message.chat.id, "Привет! Я буду запоминать твои сообщения. Чем могу помочь?")
#
# @bot.message_handler(func=lambda message: True)
# def echo(message):
#     # Обновляем информацию о сообщении пользователя
#     update_user_message(message.chat.id, message.text)
#
#     # Пытаемся угадать твои предпочтения
#     if random.random() > 0.7:
#         popular_message = get_popular_message()
#         bot.send_message(message.chat.id, f"Кстати, вот популярное сообщение: {popular_message}")
#     else:
#         bot.send_message(message.chat.id, f"Ты написал: {message.text}. Я запомнил это!")
#
# bot.polling(none_stop=True)



# import telebot
# import sqlite3
# bot = telebot.TeleBot('7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY')
# name = None
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегистрируем! Введи имя')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_pass)
#
# def user_pass(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     # Используем параметризованный запрос для предотвращения SQL-инъекций
#     cur.execute("INSERT INTO users(name, pass) VALUES(?, ?)", (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
#
# # Обработчик callback-запросов
# @bot.callback_query_handler(func=lambda call: call.data == 'users')
# def handle_users_list(call):
#     conn = sqlite3.connect('Syntaxwizard.sql')
#     cur = conn.cursor()
#
#     cur.execute("SELECT name FROM users")
#     users = cur.fetchall()
#
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     if users:
#         user_list = "\n".join([user[0] for user in users])
#         bot.send_message(call.message.chat.id, f"Список пользователей:\n{user_list}")
#     else:
#         bot.send_message(call.message.chat.id, "Нет зарегистрированных пользователей.")
#
# bot.polling(none_stop=True)
# #
# #
# import telebot
# import sqlite3
# import random
# from datetime import datetime
#
# bot = telebot.TeleBot('7903315410:AAG8Qf-hbF_QUr15c0iZp-g9Y1FAzDBpJpY')
#
#
# # Создаем таблицы для хранения данных
# def create_tables():
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             last_message TEXT,
#             message_count INTEGER
#         )
#     ''')
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS messages(
#             id INTEGER PRIMARY KEY,
#             message_text TEXT,
#             timestamp TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
#
# create_tables()
#
#
# # Функция для добавления нового пользователя
# def add_user(user_id, name):
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#     cur.execute('INSERT OR IGNORE INTO users (id, name, last_message, message_count) VALUES (?, ?, ?, ?)',
#                 (user_id, name, '', 0))
#     conn.commit()
#     conn.close()
#
#
# # Функция для обновления сообщений пользователя
# def update_user_message(user_id, message_text):
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#
#     # Обновляем сообщение и счетчик
#     cur.execute('UPDATE users SET last_message = ?, message_count = message_count + 1 WHERE id = ?',
#                 (message_text, user_id))
#
#     # Сохраняем сообщение в базе данных
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     cur.execute('INSERT INTO messages (message_text, timestamp) VALUES (?, ?)', (message_text, timestamp))
#
#     conn.commit()
#     conn.close()
#
#
# # Функция для получения случайного популярного сообщения
# def get_popular_message():
#     conn = sqlite3.connect('bot_data.db')
#     cur = conn.cursor()
#     cur.execute('SELECT message_text FROM messages ORDER BY RANDOM() LIMIT 1')  # Просто случайное популярное сообщение
#     message = cur.fetchone()
#     conn.close()
#     return message[0] if message else "Неизвестное сообщение."
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     add_user(message.chat.id, message.chat.first_name)
#     bot.send_message(message.chat.id, "Привет! Я буду запоминать твои сообщения. Чем могу помочь?")
#
#
# @bot.message_handler(func=lambda message: True)
# def echo(message):
#     # Обновляем информацию о сообщении пользователя
#     update_user_message(message.chat.id, message.text)
#
#     # Пытаемся угадать твои предпочтения
#     if random.random() > 0.7:
#         popular_message = get_popular_message()
#         bot.send_message(message.chat.id, f"Кстати, вот популярное сообщение: {popular_message}")
#     else:
#         bot.send_message(message.chat.id, f"Ты написал: {message.text}. Я запомнил это!")
#
#
# bot.polling(none_stop=True)