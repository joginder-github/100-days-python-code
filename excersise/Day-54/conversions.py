print("Enter 'x' for exit.")
dec = input("Enter number in Decimal Format: ")
if dec == 'x':
    exit()
else:
    decimal = int(dec)
    print(decimal,"in Binary =",bin(decimal))
    print(decimal,"in Octal =",oct(decimal))
    print(decimal,"in Hexadecimal =",hex(decimal))


# output:

# Enter number in Decimal Format: 60
# 60 in Binary = 0b111100
# 60 in Octal = 0o74
# 60 in Hexadecimal = 0x3c