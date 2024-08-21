# exo10-Calculatrice (Pseudo-Code + Python)
# Réaliser l’algorithme d’une calculatrice basique. L’utilisateur
# est invité à saisir un nombre, un opérateur, et un deuxième
# nombre. La calculatrice affiche ensuite le résultat. (Gérer la
# division par 0)

nombre1 = float(input("Entrez le premier nombre : "))

operateur = input("Entrez l'opérateur (+, -, *, /) : ")

nombre2 = float(input("Entrez le deuxième nombre : "))

if operateur == "+":
    resultat = nombre1 + nombre2
elif operateur == "-":
    resultat = nombre1 - nombre2
elif operateur == "*":
    resultat = nombre1 * nombre2
elif operateur == "/":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        resultat = "Erreur : Division par zéro!"
else:
    resultat = "Opérateur invalide!"

print(f"Le résultat est : {resultat}")