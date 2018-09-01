for i in range(1,4):
    print("Enter 'x' for exit.")
    num = input("Enter any number: ")
    if num == 'x':
        exit()
    try:
        number = int(num)
    except ValueError:
        print("Try to enter a number..exiting..")
    else:
        if number < 0:
        	print("It is a negative number.")
        elif number == 0:
    	    print("It is a zero.")
        elif number > 0:
    	    print("It is a positive number.")
        else:
            print(number, "is strange.")


# output:

# Enter 'x' for exit.
# Enter any number: -6
# It is a negative number.
# Enter 'x' for exit.
# Enter any number: 0
# It is a zero.
# Enter 'x' for exit.
# Enter any number: 5
# It is a positive number.