# def main():
#     arg = [
#         'Hello, World',
#         True,
#         {'Name':'Gopher'}
#         False,
#         123
#     ]
#
#     arg[0] = 'No Hello World'
#     if arg[0]





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
# from pygame.display import update


# class WorkWithArray:
#     def init(self, array):
#         self._array = array
#
#     @property
#     def get_array(self):
#         return self._array
#
#     @get_array.setter
#     def get_array(self, value):
#         ...
# class GetArray(WorkWithArray):
#     def __init__(self, array):
#         super().__init__(array)
#
#     def get(self):
#         return self._array[-1]
#
# class UpdateArray(WorkWithArray):
#     def __init__(self,array):
#         super().__init__()
#
#     def replace_at(self, index, new_value):
#         if not 0 <= index < len(self._array):
#             raise IndexError("Индекс вне диапазона.")
#         if new_value in self._array:
#             raise ValueError("Такое значение уже есть в массиве.")
#         self._array[index] = new_value
#
# class PopArray(WorkWithArray):
#     def __init__(self,array):
#         super().__init__()
#
#
# get_arr = GetArray([1, 2, 3])
# result = get_arr.get()
# print(result)
#
# update_arr = UpdateArray([1, 2, 3])
# update_arr.remove_and_add(20, 40)
# print(update_arr.array)







# class WorkWithArray:
#     def __init__(self, array):
#         if not array:
#             raise ValueError("Массив не может быть пустым.")
#         if len(array) != len(set(array)):
#             raise ValueError("Массив содержит дублирующиеся значения.")
#         self._array = array
#
#     @property
#     def array(self):
#         return self._array
#
#     @array.setter
#     def array(self, value):
#         if not value:
#             raise ValueError("Массив не может быть пустым.")
#         if len(value) != len(set(value)):
#             raise ValueError("Массив содержит дублирующиеся значения.")
#         self._array = value
#
#
# class GetArray(WorkWithArray):
#     def __init__(self, array):
#         super().__init__(array)
#
#     def get(self):
#         return self._array[-1]
#
#
# class UpdateArray(WorkWithArray):
#     def __init__(self, array):
#         super().__init__(array)
#
#     def update(self, new_value):
#         if new_value in self._array:
#             raise ValueError("Нельзя добавлять дублирующее значение.")
#         self._array[-1] = new_value
#
#
# class PopArray(WorkWithArray):
#     def __init__(self, array):
#         super().__init__(array)
#
#     def pop(self):
#         return self._array.pop()
#
#
# # Пример использования:
# get_arr = GetArray([1, 2, 3])
# print("Get:", get_arr.get())
#
# upd_arr = UpdateArray([1, 2, 3])
# upd_arr.update(4)
# print("Update:", upd_arr.array)
#
# pop_arr = PopArray([1, 2, 3])
# print("Pop:", pop_arr.pop())
# print("After Pop:", pop_arr.array)



# def func(f):
#     def wrap():
#         print('a')
#         f()
#         print("y")
#
#     return wrap
#
# @func
# def say():
#     print('dec')
#
# say()





try:
    a = 4/2
    print(a)
except ZeroDivisionError:
    print('на ноль делить не нельзя')
except NameError:
    print('на букву делить нельзя')