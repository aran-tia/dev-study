def get_least_numbers(numbers):
    count = {}
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
        
    min_count = float('inf')
    min_num = -float('inf')
    for k, v in count.items():
        if v < min_count or (v == min_count and k > min_num):
            min_count = v
            min_num = k
    return min_num

numbers = [1, 1, 2, 2, 3, 4, 4]
print(get_least_numbers(numbers))

