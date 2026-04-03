def get_numbers_length(numbers):

    max_count = 0
    current_count = 0

    for n in numbers:
        if n % 2 == 0:
            current_count += 1
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count

    return max_count

numbers = [2, 4, 6, 1, 2, 4, 8, 10, 3]
print(get_numbers_length(numbers))