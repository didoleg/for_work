import random

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']


def get_jokes(number_jokes=5, repeat_word='yes'):
    """Функция для случайной генерации шуток. Принимает на вход целые числа, соответствующие колличеству выводимых шуток а также параметр 'repeat_word',
    который позволяет регулировать повторы слов в шутках"""
    jokes = []
    if repeat_word == 'yes':
        for i in range(0, number_jokes):
            jokes_str = f'{nouns[random.randint(0, len(nouns) - 1)]} {adverbs[random.randint(0, len(adverbs) - 1)]} {adjectives[random.randint(0, len(adjectives) - 1)]}'
            jokes.append(jokes_str)
            i += 1
    else:
        for i in range(0, number_jokes):
            jokes_str = f'{nouns[random.randint(0, len(nouns) - 1)]} {adverbs[random.randint(0, len(adverbs) - 1)]} {adjectives[random.randint(0, len(adjectives) - 1)]}'
            jokes.append(jokes_str)

    print(jokes)


get_jokes()
