# exo22-BONUS : initialiser un tableau de 10 entiers avec
# les valeurs 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 à
# l’aide d’une boucle. Ensuite, à l’aide d’une boucle
# afficher la valeur de chaque cellule du tableau avec
# l’opération Ecrire().

i = 0
nbr = 1
tb = []
j = 0

################### Partie création #########################
# while i < 10:
#     nbr *= 2
#     tb.append(nbr)
#     i += 1
# print(f"Tableau : {tb}")

for i in range(10) :
    nbr *= 2
    tb.append(nbr)
print(f"Tableau : {tb}")

################### Partie affichage #########################

# while j < len(tb) :
#     print(f"Index : {j} | Valeur : {tb[j]}")
#     j += 1

# Avec des boucles for :
for index, element in enumerate(tb) :
    print(f"{index} : {element}")


# i = 0
# j = 0
# nbr = 1
# tb = []
# while i < 10:
#     nbr *= 2
#     tb.append(nbr)
#     i += 1
# print("tableau : ", tb)
# while j < len(tb) :
#     print(f"Index : {j} | Valeur : {tb[j]}")
#     j += 1