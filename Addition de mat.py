def SommeMat(matriceA,matriceB):
    résultat=matriceA
    i=0
    j=0
    while i<len(matriceA):
        while j<len(matriceA):
            résultat[i][j]= matriceA[i][j] + matriceB[i][j]
            j=j+1
        i=i+1
        j=0
    print(résultat)
    return résultat
A=[[1,1,2],[4,6,8],[4,18,2]]
B=[[7,3,4],[1,2,4],[12,1,7]]
print(SommeMat(A,B))

