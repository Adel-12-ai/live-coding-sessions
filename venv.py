# 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for el in a:
#     if el < 5:
#         print(el)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]




# import g4f
# while True:
#     user_input = input("User: ")
#     response = g4f.ChatCompletion.create(
#         model=("gpt-4"),
#         messages=[{
#             "role": "user",
#             "content": user_input
#         }]
#     )
#     print(response)




# a = {1:1,2:2,3:3,}
# print(sorted(a.values()))
# print(sorted(a.values(),reverse=True))




# a = {1:10, 2:20}
# b = {3:30, 4:40}
# c = {5:50, 6:60}
# result = {}
# for d in (a,b,c):
#     result.update(d)
# print(result)


# my_dict = {'a':500,'b':5874,'c':560,'d':400, 'e':5871}
# res = sorted(my_dict, key=my_dict.get,reverse=True)[:3]
# print(res)



# def palindrome(word):
#     return word == word[::-1]
# print(palindrome("aziza"))

# word = 'aziza'
# p = word == word[::-1]
# print(p)




# i = input().split()
# b = []
# for c in i:
#     b.append(c)
# print(b)

# i = input().split()
# print(list(i))


# for_tuple = tuple(map(int,input('Числа: ').split()))
# for_list = list(map(int,input('Числа: ').split()))
# print(for_tuple)
# print(for_list)





# n = [32,44,11]
# print(n[0])
# print(n[-1])



# n = int(input())
# for i in range(1, n + 1):
#     print(str(i) * i)



'''
сделайте так чтобы число секунда отображалось ввиде дни:часы:минуты:секунды
'''

# def time(seconds):
#     days = seconds // 86400
#     hours = (seconds % 86400) // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
#     return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"
# input_seconds = 987654
# formatted_time = time(input_seconds)
# print(formatted_time)




# def a(number):
#     for num in number:
#         if num == 237:
#             break
#         if num % 2 == 0:
#             print(num)
# print(a([12, 45, 22, 8, 237, 44, 56, 78]))



'''
напишите программу еоторая принимает два списка и выводит все элементы первого которых нет во втором
'''
# def dif(lst1, lst2):
#     return [item for item in lst1 if item not in lst2]
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# result = dif(list1, list2)
# print(result)


# n1=[32,11,21,90,78,66]
# n2=[76,55,14,90,78,33]
# res=[]
# for elem in n1:
#     if elem not in n2:
#         res.append(elem)
# print(res)


'''
сложте цифры всез целых чисел в списке
'''
# n1 = [9.2,'st',5,12,9.21,2]
# sum_int = []
# for el in n1:
#     if type(el) == int:
#         sum_int.append(el)
# print(sum(sum_int))





'''
посчитайте сколько раз символвоф встречютсья в строке
строка = "Apple"
'''
# string = "Apple"
# c = {}
# for char in string:
#     c[char] = c.get(char, 0) + 1
# print(c)

# word = 'Apple'
# c = 0
# b = input('Буква: ')
# for i in word:
#     if i == b:
#         c+=1
# print(f'Буква - "{b}" {c} шт')



# a = 'Переменная "a"'
# b = 'Переменная "b"'
# a,b=b,a
# print(a,b)




# n = [90,12,50,25,61,60]
# res = lambda n: [num for num in n if num % 15 == 0]
# print(res(n))


import tkinter as tk
import math


class AnimatedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Анимация на Tkinter")
        self.root.geometry("600x400")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="black")
        self.canvas.pack()

        self.center_x = 300
        self.center_y = 200
        self.radius = 50
        self.angle = 0

        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.animate()

    def on_mouse_move(self, event):
        self.radius = math.sqrt((event.x - self.center_x) ** 2 + (event.y - self.center_y) ** 2)

    def animate(self):
        self.canvas.delete("all")
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red")
        self.angle += 0.05
        if self.angle > 2 * math.pi:
            self.angle = 0
        self.root.after(20, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedApp(root)
    root.mainloop()