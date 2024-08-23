# exo24-Inverser un tableau : soit un tableau T. Saisir ce tableau. Changer de place les éléments de ce tableau de façon à ce que le nouveau tableau soit une sorte de miroir de l'ancien et afficher le nouveau tableau.

T = [1, 3, 2, 7, 2]
mirror_T = []

for i, val in enumerate(T) :
    print("i")
    mirror_T.append(T[-i - 1])

print(mirror_T)

