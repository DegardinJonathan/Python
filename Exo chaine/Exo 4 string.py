a=input("Saisissez une chaine : ")
c=len(a)
b=1
d=""
while c>0:
    d=d+a[-b]
    c=c-1
    b=b+1
print (d)
