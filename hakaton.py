'''
1: Айжан' жана 'Гүлзат' аттары жогоруда берилген sets
(топтор) тизмелеринен бар экендигин текшериниз;
'''
# friends = {'Айжан', 'Гулзат', 'Мээрим', 'Жийдегүл', 'Айгерим'}
# a = 'Айжан'
# b = 'Гулзат'
# if a and b not in friends:
#   print ('Они не в джрузях')
# else:
#   print('они в друзях')




'''
2: Эки sets топторун бириктириңиз;
'''
# friends = {'Айжан', 'Гүлзат', 'Мээрим', 'Жийдегүл', 'Айгерим'}
# my_friends = {'Каныкей', 'Гүлзат', 'Айбийке', 'Жийдегүл', 'Арууке'}
# union_set = friends | my_friends
# print(union_set)




'''
3: Эки sets топторунда тең бар аттарды табыңыз;
'''
# friends = {'Айжан', 'Гүлзат', 'Мээрим', 'Жийдегүл', 'Айгерим'}
# my_friends = {'Каныкей', 'Гүлзат', 'Айбийке', 'Жийдегүл', 'Арууке'}
# set1 = friends & my_friends
# print(set1)



'''
4: Бир гана friends setинде бар аттарды табыңыз;
'''
# friends = {'Айжан', 'Гүлзат', 'Мээрим', 'Жийдегүл', 'Айгерим'}
# my_friends = {'Каныкей', 'Гүлзат', 'Айбийке', 'Жийдегүл', 'Арууке'}
# only_in_friends = friends - my_friends
# print(only_in_friends)




'''
5: Бир гана бир топто бар аттарды көрсөтүңүз;
'''
# friends = {'Айжан', 'Гүлзат', 'Мээрим', 'Жийдегүл', 'Айгерим'}
# my_friends = {'Каныкей', 'Гүлзат', 'Айбийке', 'Жийдегүл', 'Арууке'}
# symmetric_difference_set = friends ^ my_friends
# print(symmetric_difference_set)




'''
6: Дубликаттарсыз жаңы автоунаалар тизмесин түзүңүз;
'''
# cars = ['Camri', 'Lexus570', 'BMW X5', 'Tundra', 'Lexus570', 'Prius', 'Camri', 'Audi A6', 'BMW X5']
# unique_cars = list(set(cars))
# print(unique_cars)








# def convert(amount, from_currency, to_currency):
#     rates = {
#         ('USD', 'EUR'): 0.95,   # пример курса между валютами
#         ('USD', 'CNY'): 7.08,
#         ('USD', 'RUB'): 74.2,
#         ('USD', 'KGS'): 87.45,
#         ('EUR', 'USD'): 1.05,
#         ('EUR', 'CNY'): 7.45,
#         ('EUR', 'RUB'): 78.05,
#         ('EUR', 'KGS'): 91.5951,
#         ('CNY', 'USD'): 0.141,
#         ('CNY', 'EUR'): 0.134,
#         ('CNY', 'RUB'): 10.47,
#         ('CNY', 'KGS'): 12.0471,
#         ('RUB', 'USD'): 0.013,
#         ('RUB', 'EUR'): 0.0128,
#         ('RUB', 'CNY'): 0.095,
#         ('RUB', 'KGS'): 0.9599,
#         ('KGS', 'USD'): 1 / 87.45,
#         ('KGS', 'EUR'): 1 / 91.5951,
#         ('KGS', 'CNY'): 1 / 12.0471,
#         ('KGS', 'RUB'): 1 / 0.9599,
#     }
#
#     if from_currency == to_currency:
#         return amount
#
#     # Если прямой курс между валютами существует
#     if (from_currency, to_currency) in rates:
#         return amount * rates[(from_currency, to_currency)]
#
#     # Если курса нет в таблице, то можно выводить ошибку
#     print(f"Не существует прямого курса между {from_currency} и {to_currency}.")
#     return None
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