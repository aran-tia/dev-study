def get_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = 0
    max_num = 0

    for k, v in count.items():
        if k % 4 == 0 and v > max_count:
            max_count = v
            max_num = k
    
    return max_num

numbers = [4, 8, 12, 12, 12, 16, 16, 2]
print(get_numbers(numbers))