def get_numbers(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result
numbers = [1, 2, 3, 4, 5, 6]
print(get_numbers(numbers))
