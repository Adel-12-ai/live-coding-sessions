# полиндром
# a = 'anna'
# v = a[::-1]
# if v == a:
#     print('полиндром')
# else:
#     print('не полиндром')

# def p(a):
#     return a == a[::-1]
# print(p("anna"))




# Факториал
# a = int(input())
# r = 1
# for i in range(1,a+1):
#     r *= i
# print(r)




# a = [4,5,6,9,7]
# b = sorted(a)
# print(b)




# FizzBuzz с модификацией
# a = []
# b = []
# for i in range(1,101):
#     if i % 3 == 0:
#         b.append(i)
#         print(f"Fizz\n{b}")
#     elif i % 5 == 0:
#         a.append(i)
#         print(f"Buzz\n{a}")

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)




# Анаграмма
# def anagrams(s, a):
#     return sorted(s) == sorted(a)
# print(anagrams("eat", "ate"))



# Частотный словарь
# def d(s):
#     f = {}
#     for c in s:
#         f[c] = f.get(c, 0) + 1
#     return f
# print(d("hello"))

# a = 'hello'
# f = {}
# for i in a:
#     f[i] = f.get(i,0) + 1
# print(f)



# Класс “Автомобиль”
# class Car:
#     def __init__(self,model,stamp,year_of_release):
#         self.model = model
#         self.stamp = stamp
#         self.year_of_release = year_of_release
#     def d(self):
#         print(f"{self.model} "
#               f"{self.stamp} "
#               f"{self.year_of_release}")
# my = Car("cls",
#          "Mercedec_benz",
#          "2014")
# my.d()



# Удаление дубликатов
# def d(lst):
#     return list(set(lst))
# print(d([1, 2, 2, 3, 4, 4]))




#  Поиск второго максимума
# def ad(a):
#     s = max(a)
#     a.remove(s)
#     sec = max(a)
#     return sec
# print(ad([4,8,1,9]))





# class Sell:
#     def __init__(self,name,brand,price,memory,new):
#         self.name = name
#         self.brand = brand
#         self.price = price
#         self.memory = memory
#         self.new = new
#     def dis(self):
#         print(f"{self.name} {self.brand} {self.price} {self.memory} {self.new}")
# my = Sell("iphone","apple","1000.0","1T","True")
# my.dis()




# import calendar
# year = int(input("Введите год: "))
# month = int(input("Введите месяц: "))
# print(calendar.month(year, month))



# import time
# a = 4
# time.sleep(4)
# print(a)





# class Circle:
#     def __init__(self, circle, radius):
#         self.circle = circle
#         self.radius = radius
#     def ar(self):
#         return 3.14159 * self.radius ** 2
# radius = float(input('введите радиус: '))
# circle = Circle(radius)
# print(f"Площадь круга: {circle.ar()}")
# print(f"Длина окружности: {circle}")



# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius ** 2)
#     def circumference(self):
#         return 2 * math.pi * self.radius
# circle = Circle(5)
# print("Площадь круга:", circle.area())
# print("Длина окружности:", circle.circumference())






# a = {
#     "a": 78,
#     "b": 45,
#     "c": 99
# }
# v = sorted(a.items(), key=lambda item: item[1])
# print(v)




'''
Задачи для самостоятельного решения
1. Фрукты
Пользователь вводит число K - количество фруктов.
Затем он вводит K фруктов в формате: название фрукта и его количество. Добавьте все фрукты в словарь,
где название фрукта - это ключ, а количество - значение.

Например:
# Ввод:
>> 3 # Количество фруктов
>> Яблоко
>> 3
>> Апельсин
>> 3
>> Мандарин
>> 10
# Вывод:
>> {'Яблоко': 3, 'Апельсин': 3, 'Мандарин': 10}
'''
# K = int(input("Введите количество фруктов: "))
# fruits = {}
# for i in range(K):
#     fruit1 = input("Введите название фрукта: ")
#     fruit = int(input(f"Введите количество фрукта {fruit1}: "))
#     fruits[fruit1] = fruit
# print(fruits)





# a = input()
# b = input()
# v = input()
# if a == b:
#     print(f'результат, а и b:\n{a}:{b}')
# elif a == v:
#     print(f'результат, a и v:\n{a}:{v}')
# else:
#     print('ничего ')




# a = input()
# b = input()
# v = input()
# if a == 'pyhton':
#     print(f'result a:\npyhton:{a}')
# elif b == 'pyhton':
#     print(f'result b:\npyhton:{b}')
# else:
#     print(f'result v:\npyhton:{v}')





# num = [1,2,3,4,5]
# for i in num:
#     i += 1
#     print(i)




# n = [1,2,3,5,6]
# l = []
# for i in n:
#     if i % 2 == 0:
#         l.append(i)
# print(sum(l))





# a = 4856
# b = 376
# c = (a+b)-(a*b)
# print("c =",int(c))






# def pr(a,b):
#     return a + b
# print(pr(1,5))





# декораторы
# def dec(func):
#     def arras():
#         print('да выполнене print_hello')
#         func()
#         print('после выполненеия print_hello')
#     return arras()
# @dec
# def print_hello():
#     print('hello')
# print_hello()