def find_max_number(numbers):
    max = numbers[0]
    for number in numbers:
        if number < max:
            max = number
    return max
