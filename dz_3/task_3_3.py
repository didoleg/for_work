def thesaurus(*args):
    name_dict = {}
    for name in args:
        if name[0] not in name_dict:
            name_dict.setdefault(f'{name[0]}', [f'{name}'])
        else:
            for key, val in name_dict.items():
                if key == name[0]:
                    val.append(f'{name}')

    print(name_dict)


thesaurus('Мария', 'Иван', 'Петр', 'Василий', 'Илья', 'Виталий', 'Ирина')
