scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = []
for val, number in enumerate(scr):
    if scr[val - 1] < scr[val]:
        res.append(scr[val])
print(res)

result_1 = [number for val, number in enumerate(scr) if scr[val - 1] < scr[val]]
result_1 = [number for val, number in enumerate(scr) if val == 0 number]
print(result)
