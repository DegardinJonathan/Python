Liste =[10,9,5,7,3]
a=0
b=0
c=0
def swap (Liste,b,c):
    d=Liste[c]
    Liste[b]=Liste[c]
    Liste[c]=d
while a<len(Liste):
    if Liste[a]<Liste[b]:
        c=Liste[a]
        if Liste[a]<c:
            c=Liste[a]
    a=a+1
    print(c)
    swap(Liste,b,c)
print(Liste)

    
