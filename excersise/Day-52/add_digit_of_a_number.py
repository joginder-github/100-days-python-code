print("Enter 'x' for exit.")
num = input("Enter any number: ")
if num == 'x':
    exit()
try:
    number = int(num)
except ValueError:
    print("Kindly try to enter a number..exiting..")
else:
    sum = 0
    temp = number
    while number > 0:
    	rem = number % 10
    	sum += rem
    	number //= 10
    print("Sum of all digits of", temp, "is", sum)


# output:


# Enter 'x' for exit.
# Enter any number: 1234
# Sum of all digits of 1234 is 10