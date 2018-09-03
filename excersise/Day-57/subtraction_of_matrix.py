matrix1 = [[10, 11, 12],
	   [13, 14, 15],
	   [16, 17, 18]]
matrix2 = [[1, 2, 3],
	   [4, 5, 6],
	   [7, 8, 9]]
rmatrix = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]
print("Matix 1")
for i in matrix1:
    print(i)
print("Matix 2")
for j in matrix1:
    print(j)
print("Subtraction Of Two Matix")
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]
for r in rmatrix:
    print(r)


# output:

# Matix 1
# [10, 11, 12]
# [13, 14, 15]
# [16, 17, 18]
# Matix 2
# [10, 11, 12]
# [13, 14, 15]
# [16, 17, 18]
# Subtraction Of Two Matix
# [9, 9, 9]
# [9, 9, 9]
# [9, 9, 9]