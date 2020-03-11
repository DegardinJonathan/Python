def ListeDiviseur(nombre):
    variable=[]
    i=1
    while(i<nombre):
        if(nombre%i == 0):
            variable.append(i)
        i=i+1
    return variable
def SommeListe(liste):
    i=0
    résultat = 0
    while(i<len(liste)):
        résultat = résultat + liste[i]
        i=i+1
    return résultat
L=[]
for i in range(1,1000):
    L.append(i)
i=1
T=[]
while(i<len(L)):
    test=[]
    test=ListeDiviseur(L[i])
    résultat=SommeListe(test)
    if(résultat == L[i]):
        T.append(L[i])
    i=i+1
print(T)

    
