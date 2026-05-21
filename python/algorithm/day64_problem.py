def get_most_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

        min_count = float('inf')
        max_num = -float('inf')

        for k, v in count.items():
            if k % 3 == 0:
                if v <  min_count or (v == min_count and k > max_num):
                    min_count = v
                    max_num = k

    return max_num
    
numbers = [3, 3, 6, 9, 9, 12, 15]
print(get_most_numbers(numbers))