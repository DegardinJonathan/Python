def TradBinaire(Valeur):
    code=[0]*(len(Valeur)*8)
    j=0
    k=0
    while j<len(Valeur):
        puissance=128
        test=ord(Valeur[j])
        i=0
        while i<8:
            if test>=puissance:
                code[k]=1
                i=i+1
                test=test-puissance
                puissance=puissance/2
                k=k+1
            else:
                puissance=puissance/2
                i=i+1
                k=k+1
            
        j=j+1
    return code
            
test=input("Saisissez un caractere : ")
print(TradBinaire(test))
