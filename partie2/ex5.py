facture=["jdhx", "gdehg", "ekjhckjh"]
facture1="hsdddegdz-dcercbrbcgev"

def tiret(chaine):
    if type(chaine) == str:
        chaine=chaine.replace("-", "\_")
        print("le resultat de tansformation de la facture est", chaine)
    else:
        print("erreur:", chaine, "ce n est pas une chaine", type(chaine))

tiret(facture)
tiret(facture1)