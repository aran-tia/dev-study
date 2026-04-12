def get_odd_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = 0
    max_num = 0

    for k, v in count.items():
        if k % 2 == 1:
            if k % 3 == 0:
                if v > max_count:
                    max_count = v
                    max_num = k

    return max_num

numbers = [3, 3, 6, 9, 9, 9, 12, 15, 15]
print(get_odd_numbers(numbers))