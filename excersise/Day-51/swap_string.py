print("Enter 'x' for exit.")
string1 = input("Enter First String to swap: ")
if string1 == 'x':
    exit()
else:
    string2 = input("Enter Second String to swap: ")
    print("\nBoth String before swap:")
    print("First String =",string1)
    print("Second String =",string2)
    temp = string1
    string1 = string2
    string2 = temp
    print("\nBoth String after swap:")
    print("First String =", string1)
    print("Second String =", string2)


# output:

# Enter 'x' for exit.
# Enter First String to swap: my name is joginder
# Enter Second String to swap: kiet college

# Both String before swap:
# First String = my name is joginder
# Second String = kiet college

# Both String after swap:
# First String = kiet college
# Second String = my name is joginder