a=int(input("Saisir l'heure de début : "))
b=int(input("Saisir les minutes de début : "))
c=int(input("Saisir l'heure de fin : "))
d=int(input("Saisir les minutes de fin : "))
duréeHeures=c-a
duréeMinutes=d-b
if duréeMinutes < 0 :
    duréeHeures=duréeHeures-1
    duréeMinutes=60+duréeMinutes
print('La durée entre le début et la fin est de',duréeHeures,'h et',duréeMinutes,'min')      
