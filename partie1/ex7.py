r=int(input("donner le rayon du cercle en centimètre"))
import math
def perimetre(rayon):
    y=2 * rayon * math.pi
    y=round(y, 2)
    return y
def aire(rayon):
    z = rayon * rayon *math.pi
    z = round(z, 2)
    return z

print(perimetre(r), "centimètre carré \n",  aire(r), "centimètre cube")