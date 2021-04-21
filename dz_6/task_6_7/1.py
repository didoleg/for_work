import sys

with open('bakery.csv', 'a+') as f:
    f.seek(0)
    if len(sys.argv) > 2:
        data_price = {line[0]: line[line.find(' '):].strip() for line in f}
        data_price[sys.argv[1]] = sys.argv[2]
        for key, val in data_price.items():
            f.write(f'{key}: {val}\n')

