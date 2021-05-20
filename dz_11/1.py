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

class LotoGame(LotoCard):
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self. computer_player = computer_player

    def get_number(self):
        used_numbers = []
        number = random.randint(1, 91)
        if number not in used_numbers:
            used_numbers.append(number)
        return number

    def start(self):

        human_player.has_number(self.get_number())








human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

loto_game = LotoGame(human_player, computer_player)
print(loto_game.get_number())
print(loto_game.start())

print(human_player)
print(computer_player)

