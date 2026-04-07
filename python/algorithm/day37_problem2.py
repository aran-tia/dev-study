def count_z_pattern(numbers):
    count = 0
    prev = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            curr = 1
        else:
            curr = -1

        if prev == -1 and curr == 1:
            count += 1

        prev = curr

    return count

numbers = [1, 3, 2, 4, 3, 5]
print(count_z_pattern(numbers))