# def add(a,b):
#     c = a + b
#     return c
# n = add(5, 2)
# print (n)


# a = lambda c: True if c%2==0 else False
# print (a(8))



# ::-1
# def add(a):
#     c = a[::-1]
#     return c
# print (add('МИР'))

# n = 'МИР'
# res = ' '
# for i in n:
#     res = i+res
# print(res)

# вывод слово МИР наоборот РИМ
# def rim(a):
#     res = ''
#     for i in a:
#         res = i+res
#
#     return res
#
# print (rim('МИР'))




# сортирует
# def add(a):
#     c = sorted(a)
#     return c
# print(add([5,4,3,2,1]))


# def add(a):
#     n = len(a)
#     i = 0
#     while i<n-1:
#         j=0
#         while j<n-1:
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#             j=+1
#         i+=1
#
# print (add([5,2,1,3,4]))


# функция
# def add(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(n-1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a
# print(add([5, 2, 1, 3, 4]))


# a=[5,2,1,3,4]
# n=len(a)
# i=0
# while i<n-1:
#     j=0
#     while j<n-1:
#         if a[j]>a [j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         j+=1
#     i+=1
# print (a)


# def my_sorted(numbers):
#     while numbers != sorted(numbers):
#         for number in range(len(numbers) - 1):
#             if numbers[number] > numbers[number + 1]:
#                 numbers[number], numbers[number + 1] = numbers[number]


# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = ""
#         for w1, w2 in zip(word1, word2):
#             result += w1+w2
#         result+=w1 + w2
#     result += word1[len(word2):] + word2[len(word1):]
#     return result




# def abb(r):
#     res = ""
#     for i in r:
#         res = i+res
#     return res
# print (abb('МИР'))



# def my_sorted(numbers):
#     n = sorted(numbers)
#     return n
# print(my_sorted([5,7,4]))



# def my_sorted(numbers):
#     while numbers != sorted:




'''
режим hardcore у доски
'''
# def el(n):
#     s = len(n)
#     return s
# print (el('asgh'))


# def ass(n):
#     left=sorted([i for i in n if i % 2==0],reverse=True) #чётные числа
#     right=sorted([i for i in n if i % 2 !=0]) #не чётные числа
#     result=left+right
#     return result
# print (ass([8,2,7,5,9]))




# def solve(numbers):
#     left = sorted([i for i in numbers if i % 2 == 0], reverse=True)
# print (solve([8,2,6,4]))


# def even(numbers):
#     result = []
#     for num in numbers:
#         if num % 2 == 0:
#             result.append(num + 1)
#     return result
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd = even(numbers)
# print(odd)




# name = input("Введите имя: ")
# if len(name) >= 3:
#     print(name[0].lower() == name[2].lower())
# else:
#     print("Имя слишком короткое")


# name = input("Введите имя: ")
# if len(name) >= 3:
#     first = name[name.index(name[0])]
#     third = name[name.index(name[2])]
#     print(first.lower() == third.lower())
# else:
#     print("Имя слишком короткое")




# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# shortes = min(days, key=len)
# length = len(shortes)
# print(f"Самый короткий день: {shortes}\nКоличество букв: {length}")



# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# shortest = days[0]
# min_length = len(shortest)
# for day in days:
#     if len(day) < min_length:
#         shortest = day
#         min_length = len(day)
# print(f"Самый короткий день: {shortest}\nКоличество букв: {min_length}")



# n = int(input('Канча соз киргизесиз: '))
# days = []
# for i in range(n):
#     day = input(f'Введите день {i+1}: ')
#     days.append(day)
# shortest_day = days[0]
# min_length = len(shortest_day)
# for day in days:
#     if len(day) < min_length:
#         shortest_day = day
#         min_length = len(day)
# print(f"Самый короткий день: {shortest_day}\nКоличество букв: {min_length}")






# class Person:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return f"Привет, меня зовут {self.name} и мне {self.age} лет."
# person1 = Person("Алекс", 30)
# print(person1.greet())





# friends = {'Айжан', 'Гулзат', 'Мээрим', 'Жийдегүл', 'Айгерим'}
# a = 'Айжан'
# b = 'Гулзат'
# if a and b not in friends:
#   print ('Они не в джрузях')
# else:
#   print('они в друзях')













"""
Написать класс который, имеет поле array
и реализует инкапсуляцию по отношению array,
так чтобы она не оставалось пустым
и не присваивалось туда дублирующиеся значения

Написать набор классов,
которые реализуют методы:
 - get() - получает последний элемент из массива - array
 - update() - обновляет последний элемент из массива - array
 - pop() - удаляет последний элемент из массива - array
"""

class WorkWithArray:
    def __init__(self, array):
        if not array:
            raise ValueError("Массив не может быть пустым.")
        if len(array) != len(set(array)):
            raise ValueError("Массив содержит дублирующиеся значения.")
        self._array = array

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value):
        if not value:
            raise ValueError("Массив не может быть пустым")
        if len(value) != len(set(value)):
            raise ValueError("Массив содержит дублирующиеся значения")
        self._array = value


class GetArray(WorkWithArray):
    def __init__(self, array):
        super().__init__(array)

    def get(self):
        return self._array[-1]


class UpdateArray(WorkWithArray):
    def __init__(self, array):
        super().__init__(array)

    def update(self, new_value):
        if new_value in self._array:
            raise ValueError('Этот элемент уже существует')
        self._array[-1] = new_value


class PopArray(WorkWithArray):
    def __init__(self, array):
        super().__init__(array)

    def pop(self):
        return self._array.pop()


get_arr = GetArray([1, 2, 3])
print(get_arr.get())

# get_arr.get(3)
# print(get_arr.array)

upd_arr = UpdateArray([1, 2, 3 ])
upd_arr.update(4)
print(upd_arr.array)

pop_arr = PopArray([1, 2, 3])
print(pop_arr.pop())
print( pop_arr.array)