# задачи из leedcode
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []
#         i, j = 0, 0
#         while i < len(word1) or j < len(word2):
#             if i < len(word1):
#                 result.append(word1[i])
#                 i += 1
#             if j < len(word2):
#                 result.append(word2[j])
#                 j += 1
#
#         return ''.join(result)
# solution = Solution()
# print(solution.mergeAlternately('abc', 'pqr'))
from django.db.models.expressions import result


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 + str2 != str2 + str1:
#             return ""
#
#         def gcd(x, y):
#             while y:
#                 x, y = y, x % y
#             return x
#
#         return str1[:gcd(len(str1), len(str2))]


# from typing import List
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         count = 0
#         length = len(flowerbed)
#
#         for i in range(length):
#             if flowerbed[i] == 0:
#                 if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
#                     flowerbed[i] = 1
#                     count += 1
#                     if count >= n:
#                         return True
#         return count >= n
#
#
# # Пример использования
# flowerbed = [1, 0, 0, 0, 1]
# n = 1
# sol = Solution()
# print(sol.canPlaceFlowers(flowerbed, n))  # Должно вывести: True
#
# flowerbed = [1, 0, 0, 0, 1]
# n = 1
# print(sol.canPlaceFlowers(flowerbed, n))  # Должно вывести: False




# class Solution:
#     def gcdOfStrings(self,strt1:str, str2: str)->str:
#         if str1+str2 != str2+str1:
#             return ""
#
#
#         def gcd(a,b):
#             while b:
#                 a,b=b,a%b
#             return a
#
#         gcd_len=gcd(len(str1), len(str2))
#         return str1[:gcd_len]


# надо исправить
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         gl = ('aeiouAEIOU')
#         for i in s:
#             if i in gl:
#                 gl += i
#         return gl
#     print(reverseVowels("IceCreAm"))



# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = set('aeiouAEIOU')
#         s_list = list(s)
#         left, right = 0, len(s) - 1
#
#         while left < right:
#             if s_list[left] in vowels and s_list[right] in vowels:
#
#                 s_list[left], s_list[right] = s_list[right], s_list[left]
#                 left += 1
#                 right -= 1
#             elif s_list[left] not in vowels:
#                 left += 1
#             else:
#                 right -= 1
#
#         return ''.join(s_list)
#
#
# sol = Solution()
# print(sol.reverseVowels("leetcode"))



# class Solution:
# def mergsAlternately(self, word1: str, word2:str)-> str:
#     result=''
#     for w1,w2 in zip(word1,word2):
#         result += w1+w2
#     result += word1[len(word2):] + word2[len(word1):]
#     return result
# print(mergsAlternately("abc",'pqr'))



# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#         count_new_flowers = 0
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 count_new_flowers += 1
#
#         if count_new_flowers >= n:
#             return True
#         else:
#             return False



'''
задача перемищение нулей
'''
# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         ab = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[ab], nums[i] = nums[i], nums[ab]
#                 ab += 1


'''
является последовательностью?
'''
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i,j = 0,0
#         while i<len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == len(s)




# def func(n):
#     for i in range(len(n)):
#         m=[]
#         s=[]
#         if i % 2 == 0:
#             print (i)
#             m.append(i)
#         else:
#             print (i)
#             s.append(i)
# print(func([4,7,5,9]))





# def add(numbers):
#     e = []
#     o = []
#     for num in numbers:
#         if num % 2 == 0:
#             e.append(num)
#         else:
#             o.append(num)
#     return e, o
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even, odd = add(numbers)
# print("Четные:", even)
# print("Нечетные:", odd)



# def abb(r):
#     res = ' '
#     for i in r:
#         p = res + i
#         return p
# print(abb('МИР'))



# def df(n):
#     s=min(n)
#     return s
# print(df([8,4,6,1]))




# def r():
#     word = "МИР"
#     print(word[::-1])
# r()

# def reverse_word():
#     word = "МИР"
#     rev = ""
#     for char in word:
#         rev = char + rev
#     print(rev)
# reverse_word()




# import webbrowser

# def open_url(lru):
#     webbrowser.open# задачи из leedcode





# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []
#         i, j = 0, 0
#         while i < len(word1) or j < len(word2):
#             if i < len(word1):
#                 result.append(word1[i])
#                 i += 1
#             if j < len(word2):
#                 result.append(word2[j])
#                 j += 1
#
#         return ''.join(result)
# solution = Solution()
# print(solution.mergeAlternately('abc', 'pqr'))
from django.db.models.expressions import result


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 + str2 != str2 + str1:
#             return ""
#
#         def gcd(x, y):
#             while y:
#                 x, y = y, x % y
#             return x
#
#         return str1[:gcd(len(str1), len(str2))]


# from typing import List
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         count = 0
#         length = len(flowerbed)
#
#         for i in range(length):
#             if flowerbed[i] == 0:
#                 if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
#                     flowerbed[i] = 1
#                     count += 1
#                     if count >= n:
#                         return True
#         return count >= n
#
#
# # Пример использования
# flowerbed = [1, 0, 0, 0, 1]
# n = 1
# sol = Solution()
# print(sol.canPlaceFlowers(flowerbed, n))  # Должно вывести: True
#
# flowerbed = [1, 0, 0, 0, 1]
# n = 1
# print(sol.canPlaceFlowers(flowerbed, n))  # Должно вывести: False




# class Solution:
#     def gcdOfStrings(self,strt1:str, str2: str)->str:
#         if str1+str2 != str2+str1:
#             return ""
#
#
#         def gcd(a,b):
#             while b:
#                 a,b=b,a%b
#             return a
#
#         gcd_len=gcd(len(str1), len(str2))
#         return str1[:gcd_len]


# надо исправить
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         gl = ('aeiouAEIOU')
#         for i in s:
#             if i in gl:
#                 gl += i
#         return gl
#     print(reverseVowels("IceCreAm"))



# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = set('aeiouAEIOU')
#         s_list = list(s)
#         left, right = 0, len(s) - 1
#
#         while left < right:
#             if s_list[left] in vowels and s_list[right] in vowels:
#
#                 s_list[left], s_list[right] = s_list[right], s_list[left]
#                 left += 1
#                 right -= 1
#             elif s_list[left] not in vowels:
#                 left += 1
#             else:
#                 right -= 1
#
#         return ''.join(s_list)
#
#
# sol = Solution()
# print(sol.reverseVowels("leetcode"))



# class Solution:
# def mergsAlternately(self, word1: str, word2:str)-> str:
#     result=''
#     for w1,w2 in zip(word1,word2):
#         result += w1+w2
#     result += word1[len(word2):] + word2[len(word1):]
#     return result
# print(mergsAlternately("abc",'pqr'))



# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#         count_new_flowers = 0
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 count_new_flowers += 1
#
#         if count_new_flowers >= n:
#             return True
#         else:
#             return False



'''
задача перемищение нулей
'''
# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         ab = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[ab], nums[i] = nums[i], nums[ab]
#                 ab += 1


'''
является последовательностью?
'''
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i,j = 0,0
#         while i<len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == len(s)




# def func(n):
#     for i in range(len(n)):
#         m=[]
#         s=[]
#         if i % 2 == 0:
#             print (i)
#             m.append(i)
#         else:
#             print (i)
#             s.append(i)
# print(func([4,7,5,9]))





# def add(numbers):
#     e = []
#     o = []
#     for num in numbers:
#         if num % 2 == 0:
#             e.append(num)
#         else:
#             o.append(num)
#     return e, o
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even, odd = add(numbers)
# print("Четные:", even)
# print("Нечетные:", odd)



# def abb(r):
#     res = ' '
#     for i in r:
#         p = res + i
#         return p
# print(abb('МИР'))



# def df(n):
#     s=min(n)
#     return s
# print(df([8,4,6,1]))




# def r():
#     word = "МИР"
#     print(word[::-1])
# r()

# def reverse_word():
#     word = "МИР"
#     rev = ""
#     for char in word:
#         rev = char + rev
#     print(rev)
# reverse_word()




# import webbrowser
# def open1_url(lru):
#     webbrowser.open(lru)
# my = input('введите адрес: ')
# if my == 'chatgpt':
#     open1_url('https://chatgpt.com/')
# if my == 'whatsapp':
#     open1_url('https://web.whatsapp.com/')
# if my == 'leedcode':
#     open1_url('https://leetcode.com/studyplan/leetcode-75/')
# if my == 'youtube':
#     open1_url('https://www.youtube.com/')
# if my == 'educlub':
#     open1_url('https://www.edclub.com/sportal/program-3/134.play')



# def sdd(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
# p = sdd(8)
# print (p)




'''
Калькулятор
'''
# while True: print(eval(input('введите выражение: ')))

# while True:
#     try:
#         print(eval(input('Введите выражение: ')))
#     except SyntaxError:
#         print()
#     except ZeroDivisionError:
#         print('На ноль нелья делить. Напишите занаво.')






'''
второй по величине
'''
# nums = [1, 3, 4, 5, 0, 2]
# nums.remove(max(nums))
# s = max(nums)
# print(s)





# анограммы
# from collections import defaultdict
# def group_anagrams(words):
#     anagrams = defaultdict(list)
#     for word in words:
#         sorted_word = ''.join(sorted(word))
#         anagrams[sorted_word].append(word)
#     return list(anagrams.values())
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = group_anagrams(words)
# print(result)

# def anagramCheck2(str1, str2):
#     return sorted(str1) == sorted(str2)
# print(anagramCheck2('python', 'ythonp'))






# клалендарь
# while True:
#     import calendar
#     try:
#         yy = int(input("Enter year: "))
#         mm = int(input("Enter month: "))
#         print(calendar.month(yy,mm))
#     except ValueError:
#         print('введите год а помтом месяц, строго числа')




'''
Проверка на простое число в Python
'''
# def PrimeChecker(a):
#     if a > 1:
#         for j in range(2, int(a/2) + 1):
#             if(a % j) == 0:
#                 print(a, "is not a prime number")
#                 break
#         else:
#             print(a, "is a prime number")
#     else:
#         print(a, "is not a prime number")
# a = int(input("Enter an input number:"))
# PrimeChecker(a)