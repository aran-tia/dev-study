def get_numbers(numbers):
    stage = 0
    count = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            curr = 1
        elif numbers[i] < numbers[i - 1]:
            curr = -1
        else:
            continue

        if stage == 0 and curr == 1:
            stage = 1
        elif stage == 1 and curr == -1:
            stage = 2
        elif stage == 2 and curr == 1:
            stage = 3
        elif stage == 3 and curr == -1:
            count += 1
            stage = 0

    return count
numbers = [1, 3, 2, 4, 3, 5, 4]
print(get_numbers(numbers))

