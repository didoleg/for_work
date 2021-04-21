import sys
import pickle
from itertools import zip_longest

with open('user.csv', encoding='utf-8') as f:
    name_list = [line.replace(',', '').strip() for line in f]

with open('hobby.csv', encoding='utf-8') as f:
    hobby_list = [line.strip() for line in f]

if len(name_list) >= len(hobby_list):
    person_hobby = {name: hobby for name, hobby in zip_longest(name_list, hobby_list)}
    with open('person hobby binary.txt', 'wb') as f:
        pickle.dump(hobby_list, f)
else:
    sys.exit(1)


