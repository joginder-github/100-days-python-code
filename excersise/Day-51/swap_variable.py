print("Enter 'x' for exit.")
var1 = input("Enter value of variable1: ")
if var1 == 'x':
    exit()
else:
    var2 = input("Enter value of variable2: ")
    print("\nSwapping of two variables started...")
    temp = var1
    var1 = var2
    var2 = temp
    print("Both the variables are successfully swapped!")
    print("\nValue of First and Second Variable after swapping:")
    print("First Variable =",var1,"\nSecond Variable =",var2,"\n")


# output:

# Enter 'x' for exit.
# Enter value of variable1: 56
# Enter value of variable2: 21

# Swapping of two variables started...
# Both the variables are successfully swapped!

# Value of First and Second Variable after swapping:
# First Variable = 21
# Second Variable = 56