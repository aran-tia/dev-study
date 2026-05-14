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

        if curr == -1 and stage == 0:
            stage = 1
        elif curr == 1 and stage == 1:
            stage = 2
        elif curr == -1 and stage == 2:
            stage = 3
        elif curr == 1 and stage == 3:
            count += 1
            stage = 0

    return count
numbers = [5, 3, 4, 2, 3, 1, 2]
print(get_numbers(numbers))