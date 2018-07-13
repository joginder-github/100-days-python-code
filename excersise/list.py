numbers=[]
print("Enter 5 numbers")
for i in range(1,6):
    numbers.insert(i,int(input("")))
print("successfully inserted")

string=['one', 'two', 'three', 'four', 'five']

join=numbers+string
print(numbers)
print(join)
numbers.extend(string)
print(numbers)
numbers.append(string)
print(string)
print(numbers)



# output:

# Enter 5 numbers
# 1
# 2
# 3
# 4
# 5
# successfully inserted
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 'one', 'two', 'three', 'four', 'five']
# [1, 2, 3, 4, 5, 'one', 'two', 'three', 'four', 'five']
# ['one', 'two', 'three', 'four', 'five']
# [1, 2, 3, 4, 5, 'one', 'two', 'three', 'four', 'five', ['one', 'two', 'three', 'four', 'five']]