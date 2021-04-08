number_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два',
               'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
               'nine': 'девять', 'ten': 'десять'}


def num_translate(number):
    if number not in number_dict:
        print(None)
    else:
        print(number_dict[f'{number}'])


num_translate(input('Введите число для перевода: '))



