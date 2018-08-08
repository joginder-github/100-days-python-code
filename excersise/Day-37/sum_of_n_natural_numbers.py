l=[]
number=int(input("enter the last number till which sum to be printed="))
for i in range(1,number+1):
    data=i
    l.append(data)
print(l)
print("sum of numbers in list is",sum(l))

# output:

# enter the last number till which sum to be printed=10
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum of numbers in list is 55