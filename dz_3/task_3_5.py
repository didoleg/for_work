from random import choice

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']


def get_jokes(number_jokes, repeat_word='yes'):
    """Функция для случайной генерации шуток. Принимает на вход 2а параметра:
        number_jokes: кол-во шуток, которые нужно сгенерировать (int)
        repeat_word: флаг, позволяющий включать и отключать режим повтора слов в шуткахб по умолчанию отключен (str)"""
    jokes = []
    if repeat_word == 'yes':
        for i in range(0, number_jokes):
            jokes.append(f'{choice(nouns)} {choice(adverbs)} 'f'{choice(adjectives)}')
    else:
        while len(jokes) < number_jokes:
            if len(jokes) > 0:
                for i in range(0, number_jokes):
                    nouns_rnd, adverbs_rnd, adjectives_rnd = choice(nouns), choice(adverbs), choice(adjectives)
                    joke = ', '.join(jokes)
                    if (nouns_rnd not in joke) and (adverbs_rnd not in joke) and (adjectives_rnd not in joke):
                        jokes.append(f'{nouns_rnd} {adverbs_rnd} {adjectives_rnd}')
            else:
                jokes.append(f'{choice(nouns)} {choice(adverbs)} 'f'{choice(adjectives)}')
    return jokes


print(get_jokes(5))
print(get_jokes(4, 'no'))

