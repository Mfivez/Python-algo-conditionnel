# exo13-À l’aide d’une boucle, afficher la table de multiplication par
# 2. Ensuite, coder votre algorithme en Python.

# 2 * 1 = 2 le 2 est toujours en commun donc on peut jste en faire de l'affichage en console
# 2 * 2 = 4
# 2 * 3 = 6

compteur = 1
while compteur < 17:
    print(f"2 * {compteur} = {compteur * 2}")
    compteur += 1


# table_2 = 0
# while table_2 <= 12:
#       table_2 = table_2*2
#       print("la table de multiplication par 2 est",table_2)