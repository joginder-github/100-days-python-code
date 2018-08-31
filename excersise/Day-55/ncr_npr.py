import math
print("Enter 'x' for exit.")
nval = input("Enter value of n: ")
if nval == 'x':
    exit()
else:
    rval = input("Enter value of r: ")
    n = int(nval)
    r = int(rval)
    npr = math.factorial(n)/math.factorial(n-r)
    ncr = npr/math.factorial(r)
    print("ncR =",ncr)
    print("nPr =",npr)


# output:

# Enter 'x' for exit.
# Enter value of n: 5
# Enter value of r: 3
# ncR = 10.0
# nPr = 60.0