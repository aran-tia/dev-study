def get_most_numbers(numbers):
    
    max_num = numbers[0]
    max_count = 1
    current_count = 1


    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > max_count or (current_count == max_count and numbers[i] < max_num):
            max_count = current_count
            max_num = numbers[i]
    return max_num



numbers = [1, 2, 2, 3, 3, 3, 2, 2, 4, 4, 4, 4]
print(get_most_numbers(numbers))