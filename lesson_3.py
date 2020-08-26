# Практична 2
# Нужно проверить, все ли числа в листе уникальны.
# лист нужно сделать со строки полученной с помощью input()
# пример
# "1, 2, 3, 4, 5" -> [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5] -> True
# [1, 2, 3, 4, 3] -> False
#
#
# list=input(' >')
# set_list=set(list)
# if len(list)==len(set_list):
#     print(True)
# else:
#     print(False)
#
# ввести строчку с input() и вывести самое длинное и повторяющееся слово
# пример:
"python the best of the best programming language, because is python"

# st=input('enter string: ').split()
# count=0
# for i in st:
#     if len(i)>count:
#         count=len(i)
#         word=i
# print('the longest word is: ',word)

# s=input(">")
# word=''
# maxLen=0
# maxWord=''
# for c in s+' ':
#     if c==' ':
#         if len(word) > maxLen:
#             maxWord = word
#         word=''
#     else:
#         word+=c
#
# print('найдовше слово :', maxWord)
# ***************************************************************************
# ДЗ - 3
# - створити функцію якавиводить ліст
# list = [1,2,3,4,5,6]
# def show_list(a):
#     print(a)
# show_list(list)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def min_num(a,b,c):
#     if b >= a <= c:
#         print(a)
#     elif a >= b <= c:
#         print(b)
#     else:
#         print(c)
# min_num(-8,-2,-11)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def max_num(a,b,c):
#     max = a
#     if b > max:
#         max = b
#     if c > max:
#         max = c
#     print(max)
# max_num(59,89,222)

# - створити функцію яка приймає будь - яку кількість чисел, повертає найменьше, а виводить найбільше
# def max_min(*args):
#     print(max(args))
#     return min(args)
#
# max_min(2,8,98,7,-3,0,58)

# - створити функцію яка виводить ліст
# list=[1,2,4,5,8]
# def n_list(a):
#     print(a)
# n_list(list)

# - створити функцію яка повертає найбільше число з ліста
# list=[8,45,7,98,25,45,]
#
# def max_list(l):
#     max=l[0]
#     for i in l:
#         if max<i:
#             max=i
#     print(max)
# max_list(list)

# - створити функцію яка повертає найменьше число з ліста
# list=[8,45,7,98,25,45,2]
# def min_list(l):
#     min=l[0]
#     for i in l:
#         if min>i:
#             min=i
#     print(min)
# min_list(list)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# list=[5,-2,-9,2,3]
#
# def num(a):
#     s=0
#     for i in a :
#         s+=i
#     print(s)
# num(list)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# Приклад
# [1, 2, 3, 4]
# [2, 3, 4, 5]
# результат
# [3, 5, 7, 9]

# l1=[1, 2, 3, 4]
# l2=[2, 3, 4, 5]
#
# def fun(a,b):
#     l3=[x+y for x,y in zip(a,b)]
#     print(l3)
# fun(l1,l2)


# -функція:
# def pr(): return 'Hello_boss_!!!'
# написати декоратор який замінює нижні підчеркування на пробіли і повертає це значення
# ????????????????



# ***********************************************************************************************
# практична 3
# Імітуємо роботу банкомату
# Є рахунок та дії над ним
# 1. Етап логінації - ввести логін + пароль
# 2 Меню :  (кожен пункт меню це функція)
# 1) Подивитись стан рахунку : виводить стан рахунку
# 2) Зняти кошти (ввести кількість коштів, + дивитись над тим щоб не залазити в борг)
# 3) покласти кошти (ви вводите скільки коштів потрібно покласти)
# 4) вихід
# print('******************************')
# pin=int(input('enter your pin:'))
# count=1000
#
# if pin == 1111:
#     print('MENU')
#     print('1-show your balance')
#     print('2-withdraw money')
#     print('3-transfer money')
#     print('4-exit')
#     choise = int(input('enter your choise:'))
#
#     if choise == 1:
#         print(f'your balance is {count}')
#
#
#     elif choise == 2:
#         cash = int(input('enter the cash below:'))
#         if cash > count:
#             print('you have not anouth money')
#         else:
#             print(f'you withdraw {cash} $ money')
#             print(f'your balance {count - cash} $')
#
#     elif choise == 3:
#         transfer = int(input('enter sum of transfer:'))
#         if transfer > count:
#             print('you have not anouth money')
#         else:
#             print(f'you send {count - transfer} money')
#     elif choise == 4:
#         print('thank you for service , have a nice day ')
#
# else:
#     print('your pin is invalid ')




