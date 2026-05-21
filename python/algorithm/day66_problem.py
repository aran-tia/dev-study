def get_most_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

        max_count = 0
        min_num = float('inf')

    for k,v in count.items():
        if k % 4 == 0:
            if v > max_count or (v == max_count and k < min_num):
                max_count = v
                min_num = k

    return min_num
numbers = [4, 4, 8, 8, 12, 12, 16, 16, 16] 
print(get_most_numbers(numbers))   