print("Enter 'x' for exit.")
ran = input("Upto how many line ? ")
if ran == 'x':
    exit()
else:
    rang = int(ran)
    k = 1
    for i in range(1, rang+1):
        for j in range(1, i+1):
            print(k, end=" ")
            k = k + 1
        print()


# output:

# Enter 'x' for exit.
# Upto how many line ? 10
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36
# 37 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54 55