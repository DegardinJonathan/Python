def MultiScalaire(matrice,a):
    résultat=matrice
    i=0
    j=0
    while i<len(matrice):
        while j<len(matrice):
            résultat[i][j]=matrice[i][j]*a
            j=j+1
        i=i+1
    return résultat
a=int(input("Choisissez un nombre allant multiplier votre matrice : "))
B=[[7,3],[4,2]]
print(MultiScalaire(B,a))
