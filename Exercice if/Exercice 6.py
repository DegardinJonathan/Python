def bissextile(an) :
    return False

mois=int(input("Saisir un mois : "))
jour=int(input("Saisir un jour : "))
année=int(input("Saisir une année : "))
if mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12 :
    if jour == 31:
        mois=mois+1
        jour=1
        if mois==13:
            année=année+1
            mois=1
    else :
        jour=jour+1
else :
    if mois==4 or mois==6 or mois==9 or mois==11 :
        if jour == 30 :
            mois=mois+1
            jour=1
        else:
            jour=jour+1
    else :
        if mois == 2:
            if bissextile :
                mois=mois+1
                jour=1
            else :
                jour=jour+1
print("Demain nous serons le",jour,"/",mois,"/",année)                
        
        
        
    
