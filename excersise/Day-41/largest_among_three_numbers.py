print("Enter 'x' for exit.")
print("Enter any three numbers: ")
num1 = input()
if num1 == 'x':
    exit()
else:
    num2 = input()
    num3 = input()
    number1 = int(num1)
    number2 = int(num2)
    number3 = int(num3)
    largest = number1
    count = 1
    if largest < number2:
        if number2 > number3:
            largest = number2
        else:
            largest = number3
    elif largest < number3:
        if number3 > number2:
            largest = number3
        else:
            largest = number2
    else:
        largest = number1
    if number1 == number2:
        if number1 == number3:
            count = 0
    if count == 0:
        print("\nAll numbers are equal to each other.")
    else:
        print("\nLargest of the given three numbers is",largest)


# output:

# Enter 'x' for exit.
# Enter any three numbers:
# 5
# 6
# 2

# Largest of the given three numbers is 6