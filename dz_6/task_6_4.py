import sys
from itertools import zip_longest

name_list = []
hobby_list = []
with open('user.csv', encoding='utf-8') as f:
    #row = f.readline()
    while True:
        row = f.readline()
        name = row.replace(',', '').strip('\n')
        if name != '':
            name_list.append(name)
        else:
            break

with open('hobby.csv', encoding='utf-8') as f:
    hobby = f.readline().strip()

if len(name_list) >= len(hobby_list):
    for key, val in zip_longest(name_list, hobby_list):
        with open('person hobby.txt', 'w', encoding='utf-8') as f:
            f.write(f'{key}: {val}\n')
else:
    sys.exit(1)




