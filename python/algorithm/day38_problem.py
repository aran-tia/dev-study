def get_triple_numbers(numbers):
    count = {}

    for n in numbers:
        if n % 3 == 0:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
    
    max_count = 0
    max_num = 0
    
    for k, v in count.items():
        if v > max_count:
            max_count = v
            max_num = k

    return max_num

numbers = [3, 6, 6, 9, 9, 9, 2, 4, 4]
print(get_triple_numbers(numbers))
    