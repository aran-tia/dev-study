def get_numbers(numbers):
    
    current_count = 1
    count = 0

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            current_count += 1
        else:
            if current_count >= 3:
                count += 1
                current_count = 1
        if current_count >= 3:
            count += 1

    return count

numbers = [5, 4, 3, 2, 4, 3, 2, 1]
print(get_numbers(numbers))