def isPrime(n):
    if (n<2):
        return 0
    for i in range (2,n//2+1):
        if (n%i==0):
            return 0
    return 1
l=[]
b=int(input("enter higer range="))
for x in range(1,b+1):
    data=int(x)
    l.append(data)
print (l)
print("prime list")
for x in range(b):
    if isPrime(x):
        print(x,end=' ')

# output:

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime list
# 2 3 5 7