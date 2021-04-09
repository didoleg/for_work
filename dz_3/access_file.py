import random


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
nouns_2 = ['лес ночью мягкий', 'город сегодня веселый', 'дом ночью зеленый', 'дом позавчера веселый', 'огонь сегодня утопичный']
for i in nouns_2:
    print(nouns[2])
    check_repeat = ' '.join(nouns_2)
    if nouns[2] in check_repeat:
        print('есть такое слово')



# else:
    #
    #     i = 0
    #     while i < number_jokes:
    #         nouns_word = nouns[random.randint(0, len(nouns))]
    #         adverbs_word = adverbs[random.randint(0, len(adverbs))]
    #         adjectives_word = adjectives[random.randint(0, len(adjectives))]
