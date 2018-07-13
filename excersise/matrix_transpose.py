# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# result = [[0,0,0], 
#           [0,0,0],
#           [0,0,0]]         
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         result[j][i]=matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = [[0,0,0],[0,0,0],[0,0,0]]         
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[j][i]=matrix[i][j]

print("Matrix")
for i in matrix:
    print(i)
print("\n")        

print("Transpose matrix")
for r in result:
    print(r)            