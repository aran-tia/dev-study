def get_pattern(numbers):
    count = 0
    stage = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            curr = 1
        elif numbers[i] < numbers[i - 1]:
            curr = -1

        if stage == 0 and curr == -1:
            stage = 1
        elif stage == 1 and curr == 1:
            stage = 2
        elif stage == 2 and curr == -1:
            stage = 3
        elif stage == 3 and curr == 1:
            stage = 4
        elif stage == 4 and curr == -1:
            count += 1
            stage = 0

    return count
numbers = [5, 3, 4, 2, 3, 1, 2, 0]
print(get_pattern(numbers))