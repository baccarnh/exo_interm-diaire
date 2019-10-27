mat="abcd"
matrix=list(mat)
i=0
while i<4:
    for j in range(4):
        if j==i:
            matrix[j]=1
        else:
            matrix[j]=0
        print(matrix[j])
    i=i+1
    print("-------")