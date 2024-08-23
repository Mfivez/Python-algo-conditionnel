# exo10-Calculatrice (Pseudo-Code + Python)
# Réaliser l’algorithme d’une calculatrice basique. L’utilisateur
# est invité à saisir un nombre, un opérateur, et un deuxième
# nombre. La calculatrice affiche ensuite le résultat. (Gérer la
# division par 0)

# nombre1 = float(input("Entrez le premier nombre : "))

# operateur = input("Entrez l'opérateur (+, -, *, /) : ")

# nombre2 = float(input("Entrez le deuxième nombre : "))

# if operateur == "+":
#     resultat = nombre1 + nombre2
# elif operateur == "-":
#     resultat = nombre1 - nombre2
# elif operateur == "*":
#     resultat = nombre1 * nombre2
# elif operateur == "/":
#     if nombre2 != 0:
#         resultat = nombre1 / nombre2
#     else:
#         resultat = "Erreur : Division par zéro!"
# else:
#     resultat = "Opérateur invalide!"

# print(f"Le résultat est : {resultat}")


nb1 = float(input("Entrez un nombre : "))
operateur = input("Entrez un opérateur (+, -, *, /) : ")
nb2 = float(input("Entrez un 2ème nombre : "))

if operateur == "+" :
    resultat = nb1 + nb2
elif operateur == "-":
    resultat = nb1 - nb2
elif operateur == "*":
    resultat = nb1 * nb2
elif operateur == "/":
    if nb2 != 0:
        resultat = nb1 / nb2
    else:
        resultat = "Erreur de division (division par 0)"
else:
    resultat = "opérateur invalide"

print(f"Le résultat du traitement est : {resultat}")