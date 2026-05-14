def get_least_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_num = -float('inf')
    min_count = float('inf')

    for k, v in count.items():
        if k % 2 == 0:
            if v < min_count or (v == min_count and k > min_num):
                min_count = v
                min_num = k

    return min_num

numbers = [2, 2, 4, 6, 6, 8, 10]
print(get_least_numbers(numbers))
