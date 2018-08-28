print("Enter 'x' for exit.")
string = input("Enter any string to count character: ")
if string == 'x':
    exit()
else:
    char = input("Enter a character to count to count from above string: ")
    val = string.count(char)
    print("Total = ",val)


# output:


# Enter 'x' for exit.
# Enter any string to count character: my name is joginder pal
# Enter a character to count to count from above string: i
# Total =  2