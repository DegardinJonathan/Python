def SommeDiag(matrice):
    résultat=0
    j=0
    i=len(matrice)-1
    while(i>=0):
        while(j<len(matrice)):
            résultat=résultat + matrice[i][j]
            i=i-1
            j=j+1
            print(résultat)
    return résultat
C=[[1,2,3,1],[3,5,8,2],[2,4,6,7],[1,2,3,4]]
print(SommeDiag(C))
    
