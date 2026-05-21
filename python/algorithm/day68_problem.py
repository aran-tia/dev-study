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
        if k % 3 == 0:
            if v > max_count or (v == max_count and k > max_num):
                max_count = v
                max_num = k

    return (max_count, max_num)

numbers = [3, 3, 6, 6, 9, 9, 9, 12, 12, 12]
print(get_most_numbers(numbers))