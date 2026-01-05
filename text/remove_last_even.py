def remove_last_even(numbers):
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] % 2 == 0:
            numbers.pop(i)
            return numbers
        return numbers


num = remove_last_even([2, 3, 4, 5, 6, 7])
print(num)
