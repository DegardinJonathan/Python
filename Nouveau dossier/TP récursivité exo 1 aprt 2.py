def fac_rec(n,resultat):
    if n>0:
        resultat=resultat*n
        n=n-1
        print(resultat)
        return fac_rec(n,resultat)
    else:
        return resultat
n=int(input("Choisissez un nombre : "))
résultat=1
print(fac_rec(n,résultat))

