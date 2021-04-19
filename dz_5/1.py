scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [x + 1 if x % 2 == 0 else x for x in scr]
for val in range(1, len(scr)):
    print(val)
    #result = [scr[val] for num in scr if num < scr[val]]
#print(result)