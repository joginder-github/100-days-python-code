for i in range(1,6):
    k=1
    for j in range(1,9):
        if (j>=6-i and j<=4+i and k):
            print("*",end="\t")
        else:
            print(" ",end="\t")
        
