# exo21-Améliorez le "C'est plus, c'est moins, c'est gagné" pour qu'il tourne en boucle tant que le juste_prix n'a pas été trouvé.
# L'ordinateur choisit un nombre aléatoirement entre 1 et 100. L'utilisateur est invité à entrer un nombre et l'algorithme nous
# répond "C'est plus" ou "C'est moins". Lorsqu'on a trouvé le bon nombre, l'algorithme affiche le nombre de tentatives
# effectuées pour trouver le résultat

import random as r

juste_prix = r.randint(1, 100)
nbr_tentatives = 0

run = True
while run :
    essai = int(input("Devinez le nombre entre 1 et 100 : "))
    nbr_tentatives += 1

    if essai < juste_prix:
        print("C'est plus")
    elif essai > juste_prix:
        print("C'est moins")
    else:
        print(f"Trouvé le juste prix en {nbr_tentatives} tentatives.")
        run = False
    

# import random

# juste_prix = random.randint(1, 100)
# tentatives = 0

# run = True
# while run:
#     essai = int(input("Devinez le nombre entre 1 et 100 : "))
#     tentatives += 1

#     if essai < juste_prix:
#         print("C'est plus")
#     elif essai > juste_prix:
#         print("C'est moins")
#     else:
#         print(f"Trouvé le juste prix en {tentatives} tentatives.")
#         run = False