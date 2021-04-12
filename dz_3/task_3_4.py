def thesaurus_adv(*args):
    name_dict = {}
    for people in args:
        name = people[0]
        surname = people[people.find(' ') + 1]
        if surname not in name_dict:
            name_dict.setdefault(f'{surname}', {f'{people[0]}': [f'{people}']})
        else:
            if surname in name_dict:
                for val in name_dict.values():
                    if name in val:
                        val[name].append(f'{people}')
                        break
                    else:
                        name_dict[surname].setdefault(f'{name}', [f'{people}'])
                        break
    print(name_dict)


thesaurus_adv('Мария Иванова', 'Иван Сергеев', 'Илья Сергеев', 'Василий Петров', 'Илья Успенский', 'Виталий Сергеев',
              'Ирина Петрова', 'Марьям Иващенко', 'Иван Измайлов', 'Петр Иванов')



