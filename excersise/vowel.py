print("Enter '0' for exit.")
ch = input("Enter any character: ")
if ch == '0':
    exit()
else:
    if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I'
       or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    	    print(ch, "is a vowel.")
    else:
    	print(ch, "is not a vowel.")

# output:

# Enter '0' for exit.
# Enter any character: h
# h is not a vowel.