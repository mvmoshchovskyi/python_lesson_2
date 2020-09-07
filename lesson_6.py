# Создать класс File:
# -он должен принимать любое количество уникальных имен файлов но не меньше 2-х
# -создать метод который будет проверять существуют ли эти файлы, если нет то создать их
# -создать метод который принимает текст и выводит список файлов (записать текст в выбранный файл)
# -создать метод который выводит список файлов, и при выборе, выводит содержимое в консоль
# -создать метод который даёт возможность выбрать два файла и меняет их содержимое местами
#

class File:
    def __init__(self, file1, file2, *args):
        files = list({file1, file2, *args})
        self.files = files if len(files) >= 2 else ['file1.txt, file2.txt']
        self.files.sort()

    def check_files(self):
        for item in self.files:
            file = None
            try:
                file = open(item)
            except FileNotFoundError:
                file = open(item, 'w')
            finally:
                if file:
                    file.close()

    def __list_files(self):
        i = 0
        for item in self.files:
            print(f'{i}) {item}')
            i += 1
        return input('Сделайте свой выбор: ')

    def save_to_file(self, text):
        choice = self.__list_files()
        if choice.isdigit() and int(choice) in range(len(self.files)):
            with open(self.files[int(choice)], 'a') as file:
                file.writelines(text + '\n')
        else:
            print('не правильный ввод!!!!')

    def read_file(self):
        choice = self.__list_files()
        if choice.isdigit() and int(choice) in range(len(self.files)):
            with open(self.files[int(choice)]) as file:
                print(file.read())
        else:
            print('не правильный ввод!!!!')

    def swap_files(self):
        print('выберите 1-й файл')
        choice1 = self.__list_files()
        print('выберите 2-й файл')
        choice2 = self.__list_files()
        if choice1.isdigit() and choice2.isdigit():
            choice1 = int(choice1)
            choice2 = int(choice2)
            indexes = range(len(self.files))
            if choice1 in indexes and choice2 in indexes:
                with open(self.files[choice1]) as file:
                    data1 = file.read()
                with open(self.files[choice2]) as file:
                    data2 = file.read()
                with open(self.files[choice1], 'w') as file:
                    file.write(data2)
                with open(self.files[choice2], 'w') as file:
                    file.write(data1)


file = File('text1.txt', 'text2.txt', 'text3.txt')
file.check_files()
# file.save_to_file('hello world')
# file.read_file()
file.swap_files()
# Практична
# 1) є дві функції
# def add_to_list(list,item):
#     list.append(item)
#     return len(list)
#
# def create_list():
#     list =[]
#     return list
#
# 1) треба прямо в функції add_to_list дописати код який буде обробляти помилку якщо передали не ліст і буде запускати іншу функцію
# 2) якщо ніякої помилки не було в глобальну змінну записати True в іншому випадку False
# Пишемо програму для реїстрації юзерів і їхтел номерів.(Тобтотелефонну книгу)
# Данні які потрібно записувати: - ім 'я - прізвище - тип контакту(напр.дом.ном.тел.або роб.) - ном.телефона(може бути декілька)
# Створити меню:
# - створити нового юзера
# - список юзерів
# - видалити юзера
# - змінити телефон
# - вивести всю тел.книгу
# - Записати в файл  10  ористувачів
# - Вивести всіх користувачів
# - вивести користувача з конкретним номером
# - вивести всіх користувачів номер яких містить код 073
