Liste = [10,80,50,24,145,45,12,65,78,12,100,22,29]
a=0
recherche = int(input('Que cherchez vous ? '))
def search(tab,b):
  while b<=len(tab):
    if tab[b]==recherche:
        return b
    b=b+1
a = search(Liste,a)
print(a+1)
