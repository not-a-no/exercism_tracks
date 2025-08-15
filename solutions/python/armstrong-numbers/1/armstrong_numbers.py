def is_armstrong_number(number):
    str_number = str(number)
    total = 0
    for num in str_number:
        total += int(num)**len(str_number)
    return total == number


"""def is_armstrong_number(number):
    str_number = str(number)
    return sum(int(digit) ** len(str_number) for digit in str_number) == number"""