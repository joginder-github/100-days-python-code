print("Enter 'x' for exit.")
km = input("Enter total kilometres: ")
if km == 'x':
    exit()
else:
    kilometres = float(km)
    conversion_factor = 0.621371
    miles = kilometres * conversion_factor
    print("%0.2f Kilometres = %0.2f Miles.\n" %(kilometres,miles))


# output:

# Enter 'x' for exit.
# Enter total kilometres: 100
# 100.00 Kilometres = 62.14 Miles.