import sys

with open('bakery.csv', 'r') as f:
    if sys.argv[1] == None:
        print(f.seek(0))
    elif int(sys.argv[1]) > 0:
        print(f.seek(int(sys.argv[1])))
