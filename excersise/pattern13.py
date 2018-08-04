for i in range(1,6):
    k=1
    for j in range(1,10):
        if j>=6-i and j<=4+i:
            
            print (k,end=" ")
            
            if j<5:
                 
                k=k+1
            else:
                k=k-1 
        else:
            print(" ",end=" ")


    print("\n")   

# output:

#         1

#       1 2 1

#     1 2 3 2 1

#   1 2 3 4 3 2 1

# 1 2 3 4 5 4 3 2 1
