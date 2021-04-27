import sys
from itertools import zip_longest

with open('user.csv', encoding='utf-8') as f1, open('hobby.csv', encoding='utf-8') as f2:
    for name, hobby in zip_longest(f1, f2):
        if name is not None:
            name = name.replace(',', '').strip()
            if hobby is not None:
                hobby = hobby.strip()
            with open('person hobby.txt', 'a', encoding='utf-8') as f:
                f.write(f'{name}: {hobby}\n')
        else:
            sys.exit(1)
print()


