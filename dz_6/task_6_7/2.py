import sys
arg = 4

with open('bakery.csv', 'r') as f:
    print(f.tell())
    line = f.readline().strip()
    while line:
        if arg == line[0]:

            break
    line = f.readline()

# with open('bakery.csv', 'w+') as f:
#     f.seek(0)
#     data_price[sys.argv[1]] = sys.argv[2]
#     for key, val in data_price.items():
#         f.write(f'{key}: {val}\n')

