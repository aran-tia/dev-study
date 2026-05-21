def get_most_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    current_count = 0
    min_num = 0

    for k, v in count.items():
        if k % 5 == 0:
            if v > current_count or (v == current_count and k < min_num):
                current_count = v
                min_num = k

    return min_num
numbers = [5, 5, 10, 10, 15, 15, 15, 20, 20, 20]
print(get_most_numbers(numbers))