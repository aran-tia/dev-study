def get_numbers_length3(numbers):
    count = []

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    current_count = 1
    count = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_count += 1
        else:
            if current_count >= 3:
                count += 1
            current_count = 1

    return count
numbers = [1, 2, 3, 1, 2, 3, 4, 1]
print(get_numbers_length3(numbers))
        