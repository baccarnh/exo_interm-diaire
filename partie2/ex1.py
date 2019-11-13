ligne="12345678"
colonne1=list(ligne)
colonne2=list(ligne)
repet=list(ligne)
a=str()


for i in range(8):
    if i%2==0:
        colonne1[i]=" "
        colonne2[i]="#"
    else:
        colonne1[i]="#"
        colonne2[i]=" "
    repet[i]=colonne1[i]+colonne2[i]
    a=repet[i]
    print(8*a)





