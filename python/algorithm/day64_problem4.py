def get_updown_numbers(numbers):
    current_count = 1
    max_count = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_count += 1
        elif numbers[i] < numbers[i - 1]:
            current_count = 1

        if current_count > max_count:
            max_count = current_count

    return max_count

numbers = [1, 2, 3, 1, 2, 3, 4]
print(get_updown_numbers(numbers))