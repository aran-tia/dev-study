def get_most_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_num = 0
    max_count = 0

    for k, v in count.items():
        if k % 5 == 0:
            if v > max_count:
                max_count = v
                max_num = k

    return max_num

numbers = [5, 10, 10, 15, 15, 15, 2, 4, 4]
print(get_most_numbers(numbers))