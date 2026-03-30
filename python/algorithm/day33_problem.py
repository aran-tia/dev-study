def get_max_numbers(numbers):
    count = {}
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_num = 0

    for k, v in count.items():
        if v >= 2 and k > max_num:
            max_num = k

    return max_num

numbers = [1, 3, 2, 3, 4, 2, 5, 5]
print(get_max_numbers(numbers))