nbr_article=int(input("entrer le nombre de vos articles"))
liste_course=(list(range(1,nbr_article+1)))
x=len(liste_course)
print(len(liste_course))
print(liste_course)

#liste_course=list(chaine)

#liste_course[0]=input("entrer votre premier article")
for i in range(len(liste_course)):
    liste_course[i]= input("entrer votre article")
    #i+=
print(liste_course[0])
print(liste_course[-1])
print(liste_course[len(liste_course)-2])