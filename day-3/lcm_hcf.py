x=int(input("enter first number"))
y=int(input("enter second number"))

if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x%i==0) and (y%i==0)):
        hcf=i
print("The HCF of ",x," & ",y, "is ",hcf)            
    
if x>y:
    n1=x
else:
         lcm=y
while(True):
    if ((lcm%x==0) and (lcm%y==0)):
        print("The LCM of ",x," & ",y, "is ",lcm)
        break
    lcm=lcm+1   