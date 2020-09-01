# ДЗ
# 1)-написать lambda функцию, которая находит
# среднее арифметическое значение входных аргументов, этих входных аргументов может быть сколько угодно

# a=[1,2,3,4]
# aver=lambda *args:sum(*args)/len(*args)
#
# print(aver(a))


# 2)-написать lambda функцию которая принимает строку и возвращает лист слов, при этом каждое слово это лист его букв:
# к  примеру:"Hello from owu" = > [['H', 'e', 'l', 'l', 'o'], ['f', 'r', 'o', 'm'], ['o', 'w', 'u']]

# st=list(map(lambda i: i,"Hello from owu"))
# print(st)

# 3)создать два класса Owner и Pet(можете добавить еще свои поля):
# у владельца должны быть такие методы:
# -добавить питомца
# -удалить питомца
# -показать всех питомцев
# -показать питомцев по типу
#
# 4) создать реестр владельцев и питомцев + создать меню:
# -добавить владельца
# - удалить владельца
# - показать всех владельцев
# - показать всех владельцев и их питомцев
# - выбрать владельца:
# - добавить питомца
# - удалить питомца
# - показать всех питомцев
# - показать питомцев по типу
# class Owner:
#     def __init__(self, name='Misha', age=35, city='Lviv'):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.pets = []
#
#
# class Pet():
#     def __init__(self, name='Elephant', age=20, animal_type='wild'):
#         self.name = name
#         self.age = age
#         self.animal_type = animal_type
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#     def add_pet(self):
#         return  self.name , self.age ,self.animal_type
#
#     # def __del__(self):
#     #     print(f'Goodbye , {self.name}, {self.age}, {self.animal_type}')
#
#     def show_pets(self):
#         # print(f'{self.name}, {self.age}, {self.animal_type}')
#         list_of_pets = [Pet(), Pet()]
#         # print(list_of_pets)
#
#     def show_pets_type(self):
#         pass
#
# list_of_pets=[Pet(),Pet()]
# # print(list_of_pets)
#
# pet1=Pet('elephant',10,'wild')
# pet2=Pet('dog',2,'pets')
# print(pet1.add_pet(),
#       pet2.add_pet())



# Практична робота
# Создаем класс Fighter,
# cоздаем два бойца(экземпляр класса)
# делам формат поединка, каждый из бойцов поочередно наносит друг другу удары забирая случайное число жизни у своего соперника
# в конце выводится победитель

# import random
#
# class Fighter:
#     health=20
#     def Hit(self):
#         n = random.randint(0, 10)
#         self.health-=n
#
#
# Klichko=Fighter()
# Lomachenko=Fighter()
# i=1
# while True:
#     if Klichko.health <=0:
#         print("Lomachenko wins !")
#         break
#     if Lomachenko.health <=0:
#         print('Klichko wins !')
#         break
#
#     print(f'Round number {i}'  )
#     if i%2==0:
#         print('Lomachenko strike !')
#         Klichko.Hit()
#         print(f'Klichko has {Klichko.health} health')
#     else:
#         print('Klichko strike !')
#         Lomachenko.Hit()
#         print(f'Lomachenko has {Lomachenko.health} health')
#     print('*********************')
#     i+=1


