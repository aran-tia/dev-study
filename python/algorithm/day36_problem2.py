def get_number_mountain(numbers):

    max_count = 1
    current_count = 1
    current_start = numbers[0]
    max_start = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_count += 1
        else:
            current_count = 1
            current_start = numbers[i]
        
        if current_count > max_count:
            max_count = current_count
            max_start = current_start

    return max_start

numbers = [1, 2, 3, 1, 2, 3, 4, 1]
print(get_number_mountain(numbers))