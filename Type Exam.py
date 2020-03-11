from random import *
secret=randrange(1,30)
i=0
while(i<10):
    if(i==10):
        print("Vous avez perdu le bon nombre etait ",secret)
        i=i+1
    if(i<10):
        Choix=int(input("Entrer un nombre entre 1 et 30 : "))
        if(Choix==secret):
            print("Bravo vous avez gagné il vous restait",10-i,"tentative")
            i=11
        else:
            i=i+1
            print("Ce n'est pas le bon nombre")
        if(i==10):
            print("Vous avez perdu le bon nombre etait",secret)

