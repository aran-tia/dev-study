def get_lowest_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_num = -float('inf')
    min_count = float('inf')

    for k, v in count.items():
        if k % 2 == 0 and k % 3 == 0:
            if v < min_count or (v == min_count and k > min_num):
                min_count = v
                min_num = k

    return min_num

numbers = [3, 6, 6, 9, 12, 12, 12, 18, 18]
print(get_lowest_numbers(numbers))
