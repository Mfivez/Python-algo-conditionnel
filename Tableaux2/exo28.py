# exo28-Réalisez un algorithme permettant de rechercher une valeur dans un tableau. Si la valeur se trouve bien dans la tableau, nous affichons sa position.

tb = [3, 7, 9, 5, 0, 1, 3]

valeur = int(input("Quelle valeur cherches-tu ? "))
pos = []
for i, e in enumerate(tb) :
    if e == valeur :
        pos.append(i)

print(f"La valeur est dans le tableau. Pos : {pos}")
