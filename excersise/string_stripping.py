name = "     joginder     "
dots = ".................."
# lstrip() method
print("printing name with spaces at left and right",name+dots)
print("printing name after removing left spaces",name.lstrip()+dots)
print("printing name after removing right spaces",name.rstrip()+dots)
print("printing name after removing all spaces using replace method",name.replace(" ","")+dots)
print("printing name after removing all spaces using strip methos",name.strip()+dots) 


# output:

# printing name with spaces at left and right      joginder     ..................
# printing name after removing left spaces joginder     ..................
# printing name after removing right spaces      joginder..................
# printing name after removing all spaces using replace method joginder..................
# printing name after removing all spaces using strip methos joginder..................