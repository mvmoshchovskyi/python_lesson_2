# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# a = input(">")
# num = ''
# for char in a:
#     if char.isdigit():
#         num = num + char + ","
#
# print(num)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st=input('>')
# l=len(st)
# integer=[]
# i=0
# while i < l:
#     c_int=''
#     a=st[i]
#     while '0'<=a<='9':
#         c_int+=a
#         i+=1
#         if i < l:
#             a=st[i]
#         else:
#             break
#     i+=1
#     if c_int !='':
#       integer.append(c_int)
# print(integer)


# #################################################################################
# 3)прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544' #введена строка
#
# 'a' -> 1  #вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
# """

# text = input('>')
# l = []
#
# for i in text:
#     if i not in l:
#         print(i + '-> ' + str(text.count(i)))
#         l.append(i)

# дз 2 часть(list comprehension):
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# greeting2=[i.upper() for i in greeting]
# print(greeting2)


# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l=[i**2 for i in range(51) if i%2 != 0 ]
# print(l)

# 3)  есть лист:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# создать новый лист и записать в него 'GT' если элемент в numbers больше 4 и 'LT' если элемент меньше или равен 4
# пример:
# ['LT', 'LT', 'LT', 'LT', 'GT', 'GT', 'GT', 'GT']

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# n=['LT' if i < 5  else 'GT' for i in numbers ]
# print(n)

# ТУТ З 'LT' не зовсім виходить ?????????????????????????????????

# n=[]
# for i in numbers:
#     if i<5:
#         n.append('LT')
#     else:
#         n.append('GT')
# print(n)






# 4) есть два листа:
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
#
# записать в лист тюплы (x,y) если x+y == 0
# пример:
# [(1, -1), (2, -2), (5, -5)]

# n=[(x, y) for x in list1 for y in list2 if x + y == 0]
# print(n)

# практична
list=[{"data":"30.07.2020","name":"car","price":3000},
      {"data":"02.08.2020","name":"tv","price":800},
      {"data":"15.08.2020","name":"phone","price":500},
      {"data":"20.08.2020","name":"radio","price":200},
      {"data":"22.08.2020","name":"shoes","price":50}]

while True:
    print('МЕНЮ:')
    print('1. список всіх записів')
    print('2. загальна вартість всіх покупок')
    print('3. найдорожча покупка')
    print('4. пошук по назві товару')
    print('5. пошук по днях')
    print('6. вихід')

    choice = input('Зробіть свій вибір: ')
    if choice not in '123456':
        print("not such number in list")
        continue

    elif choice == '1':
        n=0
        for dict in list:
            n+=1
            print('номер п/п:',n, dict)
            # for k, v in dict.items():
            #     print(k, v)


    elif choice == '2':
        sum = 0
        for dict in list:
            for k, v in dict.items():
                if k == "price":
                    sum += v
        print('загальна вартість покупок: ',int(sum))


    elif choice == '3':
        list1 = []
        for dict in list:
            for k,v in dict.items():
                if k=="price":
                    list1.append(v)
                    m=max(list1)
                    if v==m:
                        print('найдорожча покупка:',dict)
        # print("найдорожча покупка:",m)


    elif choice == '4':
        n = input('enter name of the goods :')
        list1 = []
        for dict in list:
            for k, v in dict.items():
                if  n == v:
                    list1.append(dict)
        if list1:
                    print('за вашим запитом знайдено:',list1)
        else :
            print('за вашим запитом нічого не знайдено')
                # НЕ РОЗУМІЮ В ЯКОМУ МІСЦІ ПОСТАВИТИ ELSE ЩОБ ТІЛЬКИ ОДИН РАЗ БУВ КОМЕНТАР

    elif choice == '5':
        date = input('enter date :')
        # НЕЗНАЮ В ЯКОМУ ФОРМАТІ КРАЩЕ ЗАПИСУВАТИ ДАТУ ?
        list1 = []
        for dict in list:
            for k, v in dict.items():
                if date == v:
                    list1.append(dict)
        if list1:
              print('за вашим запитом знайдено:', list1)
        else :
              print('ВВЕДІТЬ ІНШУ ДАТУ')

    elif choice == '6':
        break


