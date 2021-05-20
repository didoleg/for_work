import random


def get_number():
    used_numbers = []
    number = random.randint(1, 91)
    if number not in used_numbers:
        used_numbers.append(number)
    return number



print(get_number())