def get_count_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_num = 0
    min_count = float('inf')

    for k, v in count.items():
        if v >= 2 and v < min_count:
            min_count = v
            min_num = k
    return min_num

numbers = [1, 2, 2, 3, 3, 3, 4, 4]
print(get_count_numbers(numbers))
