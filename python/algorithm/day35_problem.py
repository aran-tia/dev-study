def get_number_once(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_num = 0
    

    for k, v in count.items():
        if v == 1 and k > max_num:
            max_num = k

    return max_num

numbers = [1, 2, 2, 3, 4, 4, 5]
print(get_number_once(numbers))