print("Enter 'x' for exit.")
print("Enter the interval (starting and ending number): ")
start = input()
if start == 'x':
    exit()
else:
    end = input()
    lower = int(start)
    upper = int(end)
    for num in range(lower, upper+1):
        tot = 0
        temp = num
        while temp != 0:
            dig = temp % 10
            tot += dig ** 3
            temp //= 10
        if num == tot:
            print("Armstrong Number are ",num)


# output:

# Enter 'x' for exit.
# Enter the interval (starting and ending number):
# 1
# 500
# Armstrong Number are  1
# Armstrong Number are  153
# Armstrong Number are  370
# Armstrong Number are  371
# Armstrong Number are  407