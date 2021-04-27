import sys

with open('bakery.csv', 'r') as f:
    if len(sys.argv) > 2:
        data_price = {line[0:line.find(':')]: line[line.find(' '):].strip() for line in f}
        if sys.argv[1] not in data_price:
            print(f'Запись под № {sys.argv[1]} отсутствует в базе, введите номер от 1 до {len(data_price)}')

with open('bakery.csv', 'w+') as f:
    f.seek(0)
    data_price[sys.argv[1]] = sys.argv[2]
    for key, val in data_price.items():
        f.write(f'{key}: {val}\n')

