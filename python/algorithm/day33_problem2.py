def count_changes(numbers):
    count = 0
    prev = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            curr = 1
        elif numbers[i] < numbers[i - 1]:
            curr = -1
        else:
            continue

        if prev != 0 and curr != prev:
            count += 1

        prev = curr

    return count