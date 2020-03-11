a=input("Saisir une chaine : ")
minu=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
maj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0
j=0
L= []
while i < len(a):
    if a[i]== maj[j]:
        minu[i]=" "
        maj[i]=" "
        test=test+1
    i=i+1
    if j<len(maj):
        j=j+1
    else:
        j=0
i=0    
while i < len(a):
    if a[i] == minu[j]:
        minu[i]=" "
        test=test+1
    i=i+1
    if j<len(maj):
        j=j+1
    else:
        j=0
if test == 26:
    print("Ce texte est un pangramme")
else :
    print("Ce texte n'est pas un pangramme")
            
