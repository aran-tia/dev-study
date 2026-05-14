def get_most_numbers(numbers):
    count = {}
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_num = float('inf')
    max_count = 0

    for k, v in count.items():
        if k % 4 == 0:
            if v > max_count or (v == max_count and k < max_num):
                max_count = v
                max_num = k

    return max_num
    
numbers = [4, 4, 8, 8, 12, 12, 12, 16, 16, 16]
print(get_most_numbers(numbers))