import pprint
def thesaurus_adv(*args):
    name_dict = {}
    for people in args:
        surname = people[people.find(' ') + 1]
        if surname[0] not in name_dict:
            name_dict.setdefault(f'{surname[0]}', {f'{people[0]}': [f'{people}']})
        print(name_dict)
        # else:
        #     for key_1, val_1 in name_dict.items():
        #         print(val_1)


thesaurus_adv('Мария Иванова', 'Иван Сергеев', 'Петр Иванов', 'Василий Петров', 'Илья Успенский', 'Виталий Сергеев',
              'Ирина Петрова')
