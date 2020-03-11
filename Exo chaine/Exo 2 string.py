a=input("Saisir une phrase : ")
b=input("Choisir un caractère : ")
c=0
d=len(a)
e=0
while d > 0:
    if a[e]==b:
        c=c+1
    d=d-1
    e=e+1
print("Il y a ",c," fois le caractère ",b,)
