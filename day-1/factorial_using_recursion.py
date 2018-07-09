def fact_recu(n):
    if n == 1:
        return n
    else:
        return n*fact_recu(n-1)

num=int(input("Enter any number = "))

if num < 0:
    print("Factorial does not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:        
    print("Factorial of ",num," is ",fact_recu(num))


# output:

# Enter any number = 5
# Factorial of  5  is  120