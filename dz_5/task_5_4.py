scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [number for val, number in enumerate(scr) if val > 0 and scr[val - 1] < scr[val]]

print(result)
