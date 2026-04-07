def get_number(numbers):
   
    prev = 0
    set_count = 0
    count = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            curr = 1
        elif numbers[i] < numbers[i - 1]:
            curr = -1
        else:
            continue 


        if prev == 1 and curr == -1:
            set_count += 1

        if set_count >= 3:
            count += 1
            set_count = 2

        prev = curr

    return count

numbers = [1, 3, 2, 4, 3, 5, 4, 6, 5]
print(get_number(numbers))