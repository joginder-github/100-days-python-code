n=int(input("Enter a number: "))
a=[]
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))
 
print()


# output:

# Enter a number: 5
# 1 + 2 + 3 + 4 + 5 = 15