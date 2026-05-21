def get_least_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = float('inf')
    max_num = -float('inf')

    for k, v in count.items():
        if k % 2 == 0:
            if v < min_count or (v == min_count and k > max_num):
                max_num = k
                min_count = v

    return max_num

numbers = [2, 2, 4, 6, 6, 8, 10]
print(get_least_numbers(numbers))
