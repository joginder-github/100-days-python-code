s=str(input("Enter any string = "))
str1 = ""
for i in s:
    str1 = i+str1
print("The original string is ",s,end="\n")
print("The reversed string is ",str1)  

# using star,stop,step argument
print("The reversed string is ",s[-1::-1])


# output:

# Enter any string = joginder
# The original string is  joginder
# The reversed string is  rednigoj