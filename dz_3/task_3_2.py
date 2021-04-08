number_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два',
               'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
               'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(number):
    if number.istitle():
        number = number.lower()
        if number not in number_dict:
            print(None)
        else:
            print(number_dict[f'{number}'].capitalize())
    else:
        if number not in number_dict:
            print(None)
        else:
            print(number_dict[f'{number}'])


num_translate_adv(input('Введите число для перевода: '))



