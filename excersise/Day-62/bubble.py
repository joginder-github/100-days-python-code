a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp 
print('Second largest number is:',a[n-2])


# output:

# Enter number of elements:5
# Enter element:2
# Enter element:6
# Enter element:5
# Enter element:4
# Enter element:9
# Second largest number is: 6