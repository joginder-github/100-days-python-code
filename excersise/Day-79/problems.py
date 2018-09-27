# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 2050 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: 
# Consider use range(#begin, #end) method

# Solution:
l=[]
for i in range(2000, 2050):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))


# output:

# 2002,2009,2016,2023,2037,2044