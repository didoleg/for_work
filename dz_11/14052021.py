# class DataBase:
#     def __init__(self, z, x, w, r, t):
#         pass
#
#     @staticmethod
#     def connect(x, y):
#         print('conning to', x, y)
#
#     def select(self):
#         print('select')
#
#
# # db_1 = DataBase()
# # db_1.connect(10, 20)
#
# DataBase.connect(10, 20)


# class MyClass:
#     x = 0
#
#     @classmethod
#     def my_method(cls):
#         print(cls.x)
#
#
# # a = MyClass()
# # a.my_method()
#
# MyClass.my_method()


class Customer:
    """это класс Покупатель"""

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


john = Customer('John', 54540540)
john.x = 0


# x = 0
# print(john.__dict__)
# print(x.__doc__)
# print(john.__class__.__name__)
# print(john.__class__)
# print(Customer)
# print(john.__module__)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Teacher(Person):
    @staticmethod
    def to_teach(subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)


class Pupil(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge = []

    def to_take(self, subj):
        self.knowledge.append(subj)


class Subject:
    def __init__(self, *subjects):
        self.subjects = subjects

    def __str__(self):
        return f'{self.subjects}'


s = Subject('math', 'physics')
t = Teacher('Ivan', 'Ivanov')
p_1 = Pupil('Sidr', 'Sidorov')
p_2 = Pupil('Petr', 'Petrov')
p_3 = Pupil('Kostya', 'Konstantinov')

t.to_teach(s, p_1, p_2)
t.to_teach(s, p_1, p_2)
# print(p_1.knowledge)
# print(p_2.knowledge)
# print(p_3.knowledge)


# import psutil
# print(psutil.disk_usage('C:'))
# print(psutil.virtual_memory())
# print(psutil.sensors_fans())


import random

class LotoCard:
    def __init__(self, player_type):
        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())
        # [' ', ' ',' ',' ', 80, 50, 60, 70, 5]
        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_stoke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._MAX_NUMBER_IN_CARD:
                        raise Exception(f'{self.player_type} победил!')
                    return True
        return False

    def __str__(self):
        MAX_FIELD_LEN = 3
        header = f'\n{self.player_type}:\n'
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD_LEN)
            body += '\n'
        return header + body

class LotaGame:
    pass

human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = LotaGame(human_player, computer_player)
game.start()

