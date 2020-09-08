# Практична
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)

from datetime import datetime
class Register:

    __time=''
    __info={}
    __count=0

    def __init__(self):
        Register.__count += 1
        Register.__time+=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        Register.__info[Register.__count,Register.__time] = {self.__class__.__name__: self.__dict__}

    @classmethod
    def get_info(cls):
        return cls.__info


class Plan(Register):

    def __init__(self,travell_time,ticket_price,time_registry,class_services):
        super().__init__()
        self.travell_time=travell_time
        self.ticket_price=ticket_price
        self.time_registry=time_registry
        self.class_services=class_services

    def flight_time(self,time_registry,travell_time):
      return time_registry+travell_time


class Car(Register):

    def __init__(self ,travell_time, number_pacengers, cost_fuel, distance):
        super().__init__()
        self.travell_time = travell_time
        self.number_pacengers=number_pacengers
        self.cost_fuel=cost_fuel
        self.distance=distance

    def cost_travell(self,cost_fuel,distance):
        return cost_fuel*distance

class Train(Register):

    __train_info = {}

    def __init__(self,travell_time,ticket_price,place):
        super().__init__()
        self.travell_time = travell_time
        self.ticket_price = ticket_price
        self.place=place
        Train.__train_info= {self.__class__.__name__: self.__dict__}

    @classmethod
    def get_info(cls):
        return cls.__train_info

plan=Plan(4,5,10,3)
car=Car(5,2,0,6)
train=Train(8,10,'first')
print(Register.get_info())
print(car.cost_travell(2, 5))
print(plan.flight_time(2,8))
print(train.get_info())

# ДЗ
#  Створити клас rectangle
# 1) об'єкт приймає два параметри - дві сторони х у
# 2) описати методи арифметичні
#   + сума площин двок об'єктів
#   - різниця площин
# 3) логічні оператори:
#   == повертає true якщо рівні по площині
#   != якщо не рівні
#   >, < відповідно
# 4) len() - сума сторін
#

# class Rectangle:
#     def __init__(self, x, y):
#         self.list = [x, y]
#
#     def __add__(self, other):
#         return self.list[0] * self.list[1] + other.list[0] * other.list[1]
#
#
#     def __sub__(self, other):
#       return self.list[0] * self.list[1] - other.list[0] * other.list[1]
#
#     def __eq__(self, other):
#         return self.list[0] * self.list[1] == other.list[0] * other.list[1]
#
#     def __ne__(self, other):
#         return self.list[0] * self.list[1] != other.list[0] * other.list[1]
#
#     def __lt__(self, other):
#         return self.list[0] * self.list[1] > other.list[0] * other.list[1]
#
#     def __gt__(self, other):
#          return self.list[0] * self.list[1] < other.list[0] * other.list[1]
#
#     def __len__(self):
#          return self.list[0] + self.list[1]
#
# rectangle1=Rectangle(2,3)
# rectangle2=Rectangle(3,2)
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1== rectangle2)
# print(rectangle1 != rectangle2)
# print(len(rectangle1))
# Поліморфізм
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Rectangle {self.x}x{self.y}'
#
#     def get_area(self):
#         return self.x*self.y
#
#
# class Square:
#     def __init__(self, x):
#         self.x = x
#
#     def __str__(self):
#         return f'Square {self.x}x{self.x}'
#
#     def get_area(self):
#         return (self.x)*2
#
# class Circle:
#
#     def __init__(self,r):
#         self.r = r
#
#     def __str__(self):
#         return f'Circle radius={self.r}'
#
#     def get_area(self):
#         return 3.14*self.r**2
#
# rectangle1=Rectangle(2,3)
# square1=Square(4)
# circle1=Circle(3)
#
# figures = [rectangle1,square1,circle1]
# for figure in figures:
#      print(figure,figure.get_area())

# ######################################################################
#
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

# list = []
#
# class Letter:
#     __count = 0
#
#     def __init__(self):
#         Letter.__count += 1
#         self.__text=''
#
#     @property
#     def my_text(self):
#         return self.__text
#
#
#     @my_text.setter
#     def my_text(self, text):
#         self.__text = text
#
#     def save(self, list):
#         list.append(self.__text)
#
#     @classmethod
#     def show_count(cls):
#         print(f'cont: {cls.__count}')
#
#
# letter = Letter()
# letter.my_text = 'Hello'
# print(letter.my_text)
# letter.save(list)
# letter.my_text = 'World'
# letter.save(list)
# letter2 = Letter()
# Letter.show_count()
# print(list)



# ******************

# count1 = Letter(1)
# count2 = Letter(1)
# print(count2.my_count)

# class User:
#
#     def __init__(self,age):
#         self.__age=age
#
#     @property
#     def my_age(self):
#             return self.__age
#
#     @my_age.setter
#     def my_age(self,value):
#         self.__age=value
#
#     @my_age.deleter
#     def my_age(self):
#         del self.__age
#
#     # my_age=property(get_age, set_age,del_age)
#
#
# user=User(15)
# print(user.my_age)
# user.my_age=35
# print(user.my_age)
# print(user.__dict__)
# del user.my_age
# print(user.__dict__)

# class Age:
#
#     def __init__(self, age):
#         self.age = age
#
#     # def __str__(self):
#     #     return f'{self.age}'
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#     def __len__(self):
#         return 87
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __mul__(self, other):
#         return self.age * other.age
#
#
#
# age1 = Age(11)
# age2= Age(2)
# print(len(age1))
# print(age1+age2)
# print(age1*age2)
# print((age1,age2))


