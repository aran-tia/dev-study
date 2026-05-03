def get_longest_numbers(numbers):
    count = []
    current_count = 0
    max_count = 0

    for n in numbers:
        if n % 2 == 0:
            current_count += 1

            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count

numbers = [2, 4, 6, 1, 8, 10, 12, 14, 3]
print(get_longest_numbers(numbers))

        

        