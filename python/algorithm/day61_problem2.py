def get_pattern(numbers):
    count = 0
    stage = 0

    for n in range(1, len(numbers)):
        if numbers[n] > numbers[n - 1]:
            curr = 1
        elif numbers[n] < numbers[n - 1]:
            curr = -1

        if stage == 0 and curr == 1:
            stage = 1
        elif stage == 1 and curr == -1:
            stage = 2
        elif stage == 2 and curr == 1:
            count += 1
            stage =0

    return count

numbers = [1, 3, 2, 4, 3, 5]
print(get_pattern(numbers))