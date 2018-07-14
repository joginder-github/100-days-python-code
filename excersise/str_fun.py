name,char=input("Enter your name and character separated by comma = ").split(",")
print("string length is",len(name))
print("string in lower case is",name.lower())
print("string length upper is",name.upper())
print("string length is",name.title())
print("occurrence of a character ",char," in string",name.lower().count(char.lower()))


# output:

# Enter your name and character separated by comma = JOGinder,E
# string length is 8
# string in lower case is joginder
# string length upper is JOGINDER
# string length is Joginder
# occurrence of a character  E  in string 1