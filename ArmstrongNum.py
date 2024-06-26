def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)

    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    return number == sum_of_digits
num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
