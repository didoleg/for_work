import sys
from itertools import zip_longest

name_list = sys.argv[1]
hobby_list = sys.argv[2]
person_hobby = sys.argv[3]


with open(f'{name_list}', encoding='utf-8') as f1, open(f'{hobby_list}', encoding='utf-8') as f2:
    for name, hobby in zip_longest(f1, f2):
        if name is not None:
            name = name.replace(',', '').strip()
            if hobby is not None:
                hobby = hobby.strip()
            with open(f'{person_hobby}', 'a', encoding='utf-8') as f:
                f.write(f'{name}: {hobby}\n')
        else:
            sys.exit(1)




