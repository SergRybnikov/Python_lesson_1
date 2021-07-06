def nums_gen():
    for num in range(1, n + 1):
        if num % 2 == 1:
            yield num

n = 15


odd_to_15 = nums_gen()
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))