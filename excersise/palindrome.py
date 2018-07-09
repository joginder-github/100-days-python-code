x=int(input("Enter any number "))
temp=x
rem=0
y=0
while temp > 0:
    rem=temp%10
    y=(y*10)+rem
    temp //=10
if y==x:
    print(y," is palindrome")
else:
    print(y," is not palindrome")


# output:

# Enter any number 121
# 121  is palindrome