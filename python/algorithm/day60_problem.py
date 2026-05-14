def get_most_numbers(numbers):
    count = {}
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = 0
    min_num = float('inf')

    for k, v in count.items():
        if k % 2 == 1:
            if v > max_count or (v == max_count and k < min_num):
                min_num = v
                max_count = k

    return min_num
numbers = [1, 1, 3, 3, 5, 5, 5, 7, 7, 7]
print(get_most_numbers(numbers))