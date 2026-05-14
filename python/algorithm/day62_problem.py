def get_odd_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = float('inf')
    max_num = -float('inf')

    for k, v in count.items():
        if k % 2 == 1:
            if v < min_count or (v == min_count and k > max_num):
                min_count = v
                max_num = k

    return max_num
numbers = [1, 1, 3, 5, 5, 7, 9, 9]
print(get_odd_numbers(numbers))