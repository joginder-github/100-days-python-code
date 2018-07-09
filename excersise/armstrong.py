x=int(input("enter any number"))
sum=0
temp=x
while temp > 0:
    b=temp%10
    sum += b**3
    temp//=10
if sum==x:
    print("Number is armstrong",sum)
else:
    print("Number is not armstrong",sum)        