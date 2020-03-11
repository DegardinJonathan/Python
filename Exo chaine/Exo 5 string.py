a=input("Saisissez une chaine : ")
c=len(a)
b=1
e=0
d=""
while c>0:
    d=d+a[-b]
    c=c-1
    b=b+1
b=1
while b<len(a):
    if d[b] == a[b]:
        b=b+1
        e=e+1
print(d)
print(a)
if e==len(a)-1:
    print("Votre phrase est bel et bien un palindrome")
if e!=len(a)-1:
    print("Votre phrase n est pas un palindrome")
    

