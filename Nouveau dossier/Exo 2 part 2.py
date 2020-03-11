def encadrer_rec(nbrcrochets,nombre):
    if nbrcrochets!=0:
        nombre=[nombre]
        nbrcrochets=nbrcrochets-1
        return encadrer_rec(nbrcrochets,nombre)
    else:
        return nombre
nbrcrochets=int(input("Combien de crochets souhaitez vous ? : "))
nombre=int(input("Choisissez un nombre : "))
print(encadrer_rec(nbrcrochets,nombre))
