Dégats=int(input('Saisissez le montant des dommages : '))
franchise= (Dégats/100)*10
if franchise>15 :
    if franchise<50 :
        print("L'assurance peut vous remboursez",franchise)
    else:
        print("Vous n'êtes pas remboursable")
else:
    print("Vous n'êtes pas remboursable")


