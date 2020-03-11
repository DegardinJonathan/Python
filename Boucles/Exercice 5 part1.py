capital=int(input('Saisir votre capital initial : '))
résultat=capital
a=0
i=int(input('Saisir le taux d intéret : '))
while résultat<=capital*2:
    résultat=résultat+résultat*(i/100)
    a=a+1
print('Votre capital initial aura doublé au bout de ',a,'ans')    
    
