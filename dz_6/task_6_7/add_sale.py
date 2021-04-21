import sys

price = sys.argv[1]

with open('bakery.csv', 'a+') as f:
    f.seek(0)
    price_num = len([line.strip() for line in f])
    f.write(f'{price_num + 1}: {price}\n')



