x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

# using third variable temp
temp = x
x = y
y = temp

print('The value of x after swapping using third variable: {}'.format(x))
print('The value of y after swapping using third variable: {}'.format(y))

# swapping again result without using third variable

x=x+y
y=x-y
x=x-y

print('The value of x after swapping result without using third variable: {}'.format(x))
print('The value of y after swapping result without using third variable: {}'.format(y))


# output:

# Enter value of x: 8
# Enter value of y: 9
# The value of x after swapping using third variable: 9
# The value of y after swapping using third variable: 8
# The value of x after swapping result without using third variable: 8
# The value of y after swapping result without using third variable: 9