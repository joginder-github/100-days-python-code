p=int(input("Enter the principal amount "))
r=float(input("Enter the rate of interest "))
n=int(input("Enter the no. of compounding years "))
t=int(input("Enter time in years "))
a=round(p*((1+(r/n))**(n*t)),4)
print("The compound interest calculated is ",a)


# output:

# Enter the principal amount 5000
# Enter the rate of interest .05
# Enter the no. of compounding years 12
# Enter time in years 10
# The compound interest calculated is  8235.0475