# exo29-Refaites l'algorithme qui demande à l’utilisateur de taper 10 entiers et qui affiche le plus petit de ces entiers mais cette fois-ci à l'aide d'un tableau et sans retenir le minimum lors de la saisie.

tb = []

for i in range(10):
    tb.append(int(input("nbr : ")))

min = tb[0]

for v in tb[1:]:
    if v < min:
        min = v

print(f"{tb} => min : {min}")