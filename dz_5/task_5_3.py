from itertools import zip_longest


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

if len(tutors) >= len(klasses):
    new = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
else:
    new = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

print(*new)

