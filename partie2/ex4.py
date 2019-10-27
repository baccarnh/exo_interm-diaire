nombre=input("entrer un nombre")
def entier(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def fatorielle(nbr):
    fact = 1
    if (entier(nbr))==True:
        e = int(nbr)
        for k in range(1, e+1):
            fact = k * fact
        print(fact)
    else: print("le nombre n est pas entier")

fatorielle(nombre)

