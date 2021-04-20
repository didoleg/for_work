def odd_nums(nums):
    for number in range(1, nums + 1, 2):
        yield number


odd_to_15 = odd_nums(15)
print(type(odd_to_15))
print(next(odd_to_15))

