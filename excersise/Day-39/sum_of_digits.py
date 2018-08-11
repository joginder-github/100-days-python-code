number=input("Enter any number=")
total=0
i=0
while i < len(number):
    total += int(number[i])
    i += 1
print("Number you entered is ",number)
print("Total of digits of number is ",total)


# output:

# Enter any number=12345
# Number you entered is  12345
# Total of digits of number is  15