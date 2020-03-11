
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
def SuiteAliquote(nombre):
    resultat=[]
    resultat.append(nombre)
    while(nombre != 1 ):
        valeur=ListeDiviseur(nombre)
        print(valeur)
        nombre=SommeListe(valeur)
        if nombre == 6:
            return resultat
        resultat.append(SommeListe(valeur))
    return resultat
nombre=int(input("Choisissez un nombre : "))
résultatfinal=[]
résultatfinal=SuiteAliquote(nombre)
print(résultatfinal)


