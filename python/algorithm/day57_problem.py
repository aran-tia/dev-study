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
        if k % 5 == 0:
            if v < min_count or (v == min_count and k > min_num):
                min_count = v
                min_num = k

    return min_num
numbers = [5, 5, 10, 15, 15, 20, 25]
print(get_least_numbers(numbers))
    