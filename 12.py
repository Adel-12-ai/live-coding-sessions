# numbers = [4, 5, 9, 2, 4]
# even_numbers = [num for num in numbers if num % 2 == 0 and num < 9]
# print(even_numbers)



# def dif(lst1, lst2):
#     return [item for item in lst1 if item not in lst2]
# list1 = [1,1,2,3,5,8,13,21,34,55,89]
# list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# result = dif(list1, list2)
# print(result)




# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# v = []
# for i in a:
#     if i == b:
#         v += 1
# print (v)




# data = {'a': 3, 'b': 1, 'c': 2, 'd': 5}
# sorted1 = dict(sorted(data.items(), key=lambda item: item[1]))
# sorted2 = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
# print(f"по возрастанию: {sorted1}")
# print(f"по убыванию: {sorted2}")





# a = {'a': 3, 'b': 1, 'c': 2, 'd': 5}
# s1 = (sorted(a.items(), key=))



# a = {'a': 3, 'b': 1, 'c': 2, 'd': 5}
# print(sorted(a.values()))
# print(sorted(a.values(),reverse=True))



# a = [4,8,3,5,9]
# b = []
# for i in a:
#     if i % 2== 0:
#         b.append(i)
#         print(b)
#     elif a == 5:
#         break




# my_dict = {'a':500,'b':5874,'c':560,'d':400, 'e':5871}
# res = sorted(my_dict, key=my_dict.get,reverse=True)[:3]
# print(res)




'''Напишите проверку на то, является ли строка палиндром.
Палиндром - это слово или фразы, которые одинаково читаются слева направо и сперва налево.'''
# a = 'anna'
# b = a[::-1]
# if b == a:
#     print('пол')
# else:
#     print('не пол')






'''
Задача 6
Вы принимаете от пользователя последовательность чисел, разделённых запятой.
Составьте список и кортеж с этими числами.
'''
# numbers = input()
# list1 = numbers.split(",")
# tuple1 = tuple(list1)
# print(f"Список: {list1}")
# print(f"Кортеж: {tuple1}")

# a = list(map(int,input('write number: ').split(',')))
# d = tuple(map(int,input('write number: ').split(',')))
# print(a)
# print(d)





'''
Задача 7
Выведите первый и последний элемент списка.
numbers = [32, 44, 11, True, 'odd', False]
'''
# numbers = [32, 44, 11, True, 'odd', False]
# print(numbers[0],numbers[-1])




'''
Задача 7
Выведите первый и последний элемент списка.
'''
# numbers = [32, 44, 11, True, 'odd', False]
# a = int(input())
# for i in range(1, a + 1):
#     print(str(i) * i)





'''
Задача 9
Напишите программу, 
которая выводит чётные числа из заданного списка и останавливается, 
если встречает число 237.
numbers = [43, 54, 12, 63, 237, 90, 21]
'''
# def a(number):
#     for num in number:
#         if num == 237:
#             break
#         if num % 2 == 0:
#             return num
# print(a([43, 54, 12, 63, 237, 90, 21]))


# def a(number):
#     result = []
#     for num in number:
#         if num == 237:
#             break
#         if num % 2 == 0:
#             result.append(num)
#     return result
# print(a([43, 54, 12, 63, 237, 90, 21]))




'''
Задача 10
Напишите программу, 
которая принимает два списка и выводит все элементы первого, 
которых нет во втором.
'''
# a = list(map(int,input('write number: ').split(',')))
# d = list(map(int,input('write number: ').split(',')))
# res=[]
# for i in a:
#     if i not in d:
#         res.append(i)
# print(res)

# метод агая
# numbers1 = list(map(int,input('Введите первое списка').split()))
# numbers2 = list(map(int,input('Введите второе списка').split()))
# c = []
# for i in numbers1:
#     if i in numbers2:
#         continue
#     else:
#         c.append(i)
# print(c)






# from main import pr
# pr(1,5)