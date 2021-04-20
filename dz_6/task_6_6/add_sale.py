import sys

price = sys.argv[1]

with open('bakery.csv', 'r') as f:
    price_num = len([line.replace('\n', '') for line in f])

with open('bakery.csv', 'a') as f:
    f.write(f'{price_num + 1}: {price}\n')
