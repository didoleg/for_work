import sys

with open('bakery.csv', 'r') as f:
    if len(sys.argv) < 2:
        print(f.read())
    elif len(sys.argv) == 2:
        data = [line.strip() for line in f]
        for val, num in enumerate(data):
            if sys.argv[1] == num[0]:
                for price in data[val:]:
                    print(price[price.find(' ') + 1:])
    elif len(sys.argv) > 2:
        data = [line.strip() for line in f]
        for val, num in enumerate(data):
            if sys.argv[1] == num[0]:
                left_val = val
            if sys.argv[2] == num[0]:
                right_val = val + 1
        for price in data[left_val:right_val]:
            print(price[price.find(' ') + 1:])

