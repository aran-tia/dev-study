def get_most_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = 0
    max_num = float('inf')

    for k, v in count.items():
        if k % 5 == 0 and k % 2 == 0:
            if v > max_count or (v == max_count and k < max_num):
                max_count = v
                max_num = k
        
    return max_num

numbers = [5, 10, 10, 20, 20, 20, 25, 30, 30]
print(get_most_numbers(numbers))