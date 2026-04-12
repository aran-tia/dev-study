def get_numbers(numbers):
    
    count = 0
    prev = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            curr = 1
        elif numbers[i] < numbers[i - 1]:
            curr = -1
        else:
            continue

        if prev == 1 and curr == -1:
            count += 1
            prev = 0
        else:
            prev = curr

    return count

numbers = [1, 3, 2, 4, 3, 5]
print(get_numbers(numbers))