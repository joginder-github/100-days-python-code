for i in range(1,6):
    for j in range(1,10):
        if j >= 6-i and j <= 4+i:
            print(j," ",end="")
        else :
            print(" "," ",end="")    
    print(end="\n")  


# output:

#             5
#          4  5  6
#       3  4  5  6  7
#    2  3  4  5  6  7  8
# 1  2  3  4  5  6  7  8  9