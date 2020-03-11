def fact(n):
    résultat = 1
    while n>0:
        résultat= résultat*n
        n=n-1
    return résultat   
n=int(input("Choisissez un nombre : "))
print(fact(n))

