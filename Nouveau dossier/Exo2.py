def encadrer(nbrcrochets,nombre):
    while nbrcrochets>0:
        nombre=[nombre]
        nbrcrochets=nbrcrochets-1
    return nombre
nbrcrochets=int(input("Combien de crochets souhaitez vous ? : "))
nombre=int(input("Choisissez un nombre : "))
print(encadrer(nbrcrochets,nombre))
