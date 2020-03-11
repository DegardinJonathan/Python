def livret_rec(n,livret,taux):
    if 0>(n-2019):
        livret=livret*(1+taux)
        n=n-1
        print(livret)
        return livret_rec(n,livret,taux)
    else:
        return livret
livret=1200
taux=0.05
n=int(input("Choisissez l'année : "))
print(livret_rec(n,livret,taux))
    
