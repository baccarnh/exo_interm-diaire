nbcache=25
nbprop=int(input("donner un nombre entier de votre choix"))
diff = int(nbcache - nbprop)

while diff!=0:
    if diff > 0:
        print("le nombre à deviner est plus grand")
    elif diff < 0:
        print("le nombre à deviner est plus petit")

    nbprop = input("donner un nombre entier de votre choix")
    diff = int(nbcache - int(nbprop))

print("bravo vous avez gagné")

