def longest_mountain(numbers):
    max_len = 0
    up = 0
    down = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            if down > 0:
                up = 0
                down = 0
            up += 1
        elif numbers[i] < numbers[i - 1]:
            if up > 0:
                down += 1
        
        if up > 0 and down > 0:
            max_len = max(max_len, up + down + 1)

    return max_len
numbers = [1, 2, 3, 2, 1, 2, 3, 2]
print(longest_mountain(numbers))