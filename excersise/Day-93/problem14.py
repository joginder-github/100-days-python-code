# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
netAmount = 0
while True:
    s = input("Enter deposit amount withdrawal amount:")
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)


# Output:

# Enter deposit amount withdrawal amount:D 300
# Enter deposit amount withdrawal amount:D 300
# Enter deposit amount withdrawal amount:W 200
# Enter deposit amount withdrawal amount:D 100
# Enter deposit amount withdrawal amount:
# 500