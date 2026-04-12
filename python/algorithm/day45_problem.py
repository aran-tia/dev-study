def get_odd_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = float('inf')
    min_num = -float('inf')

    for k, v in count.items():
        if k % 2 == 1 and k % 3 == 0:
            if v < min_count or (v == min_count and k > min_num):
                min_count = v
                min_num = k

    return min_num

numbers = [3, 3, 6, 9, 9, 12, 15, 15]
print(get_odd_numbers(numbers))


        