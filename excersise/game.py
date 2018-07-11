pos=0
for i in range(1,4):
    if i==1:
        x=int(input("Enter any number = "))
    else:
        x=int(input("Try again = "))
    if x%2==0:
        pos=1
        break  
if pos==1:
    print("You win")
else:
    print("You loose")        


# output:

# Enter any number = 3
# Try again = 9
# Try again = 5
# You loose