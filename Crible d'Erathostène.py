N=int(input("Choisir un nombre : "))
test=int
test=3
b=0
from math import * 
L= []
for i in range(1,N+1):  
    L.append(i)
print(L)
if L[b]==0 & i!=2:
    L[b]=0
    b=b+1
if L[b]==1:
    L[b]=0
    b=b+1
while test<=sqrt(N):
    if L[b]%test==0:
        L[b]=0
    else:
        test=test+1
print(L)

