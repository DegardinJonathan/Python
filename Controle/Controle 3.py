a=input("Saisir une chaine de caractère : ")
b=input("Choisir un caractère : ")
d=0
e=0
while e<len(a):
    if a[e]==b:
        d=d+1
    e=e+1
print(d)
