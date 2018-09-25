d1={'A':1,'B':2}
d2={'C':3}
print(d1)
print(d2)
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)


# output:

# {'A': 1, 'B': 2}
# {'C': 3}
# Concatenated dictionary is:
# {'A': 1, 'B': 2, 'C': 3}