

long=int(input("donner la longueur de la piscine"))
larg=int(input("donner la largueur de la piscine"))
prof=int(input("donner la profodeur de la piscine"))
deb=int(input("donner le débit d'eau"))

def time(x, y, z, flow):
    print("le temps necessaire pour remplir la piscine est", x*z*y/flow, "minutes")

time(long, larg, prof, deb)