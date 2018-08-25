print("Enter 'x' for exit.")
side = input("Enter side length of Square: ")
if side == 'x':
    exit()
else:
    side_length = int(side)
    area_square = side_length*side_length
    print("\nArea of Square =",area_square)


# output:

# Enter 'x' for exit.
# Enter side length of Square: 5

# Area of Square = 25