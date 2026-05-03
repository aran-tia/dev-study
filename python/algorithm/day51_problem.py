def get_odd_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = 0
    max_num = 0

    for k,v in count.items():
        if k % 2 == 1:
            if v > max_count or (v == max_count and k < max_num):
                max_count = v
                max_num = k

    return max_num

numbers = [1, 1, 3, 3, 3, 5, 5, 5, 7]
print(get_odd_numbers(numbers))
