chf1 = int(input("premier chiffre"))
chf2 = int(input("deuxième chiffre"))
chf3 = int(input("troisième chiffre"))
chf4 = int(input("quatrième chiffre"))
#ajout integer car sans il prend que le premier chiffre ex(9>45??)
list = [chf1, chf2, chf3, chf4]
print(list)
if chf1 > chf2 and chf1 > chf3 and chf1 > chf4:
    print("la plus grande valeur est, ", chf1)
elif chf2 > chf1 and chf2 > chf3 and chf2 > chf4:
    print("la plus grande valeur est, ", chf2)
elif chf3 > chf2 and chf3 > chf1 and chf3 > chf4:
    print("la plus grande valeur est, ", chf3)
else:
    print("la plus grande valeur est, ", chf4)
# deuxieme façon for

max = list[0]
for i in range(4):
    if list[i] > max: max = list[i]

print("avec la méthode de la boucle for on obtient", max)
