x=int(input("Enter any number = "))
pos=0
for i in range(2,x):
    if x%i==0:
        pos=1
        break
if pos==0:
    print(x," is prime")
else:
    print(x," is not prime")    


# output:

# Enter any number = 13
# 13  is prime