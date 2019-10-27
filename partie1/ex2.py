age=input("entrer votre age")
def racine(age):
    age=int(age)
    car=pow(age, 0.5)
    x=int(car)
    y=car-x
    return y

age=input("votre age")
age=int(age)
if age>0:
    y=racine(age)
    if y<0.01:
        print ("l age est carré")
    else:
        print("l age n est pas carré")
    if age>21: print("acces autorisé")
    if age%2==0:  print ("age pair")
else: print("message d erreur: age négatif")

