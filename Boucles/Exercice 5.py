capital=int(input('Saisir votre capital initial : '))
année=int(input('Saisir le nombre d année : '))
résultat=0
a=0
i=int(input('Saisir le taux d intéret : '))
while a<=année:
        résultat=capital+capital*(i/100)
        a=a+1   
print('Le capital dont vous disposerez au bout de ',année,'année sera : ',résultat)

