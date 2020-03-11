def pgcd(a,b):
    if a<b:
        c=a
        a=b
        b=c
    while b!= 0 :
        q=a//b
        r=a%b
        a=b
        b=r
    return a
a=int(input("Entrer un entier naturel : "))
b=int(input("Entrer un entier naturel : "))
p=pgcd(a,b)
print("Le PGCD de ",a," et ",b," est égal à ",p)
