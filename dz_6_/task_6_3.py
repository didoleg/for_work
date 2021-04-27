import sys

from itertools import zip_longest

with open('user.csv', encoding='utf-8') as f:
    name_list = [line.replace(',', '').strip() for line in f]

with open('hobby.csv', encoding='utf-8') as f:
    hobby_list = [line.strip() for line in f]

if len(name_list) >= len(hobby_list):
    person_hobby = {name: hobby for name, hobby in zip_longest(name_list, hobby_list)}
    with open('person hobby.txt', 'a+') as f:
        for key, val in person_hobby.items():
            f.write(f'{key}: {val}\n')
else:
    sys.exit(1)

print(person_hobby)
