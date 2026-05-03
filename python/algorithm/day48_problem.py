def get_most_numbers(numbers):
    count = {}
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    max_count = 0
    max_num = 0

    for k, v in count.items():
        if v > max_count or (v == max_count and k < max_num):
            max_count = v
            max_num = k

    return max_num

numbers = [4, 1, 2, 2, 3, 3, 1, 1]
print(get_most_numbers(numbers))