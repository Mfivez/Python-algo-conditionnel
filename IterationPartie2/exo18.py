# exo18-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme de la
# calculatrice afin qu’elle demande à l’utilisateur s’il veut faire un autre calcul (tant
# qu’il le désire).

run = True
while run :
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

    print(f"Le résultat : {resultat}")

    run = bool(int(input("Voulez-vous faire un autre calcul ? (1 = oui / 0 = non) : ")))

# run = True

# while run:
#     nombre1 = float(input("Entrez le premier nombre : "))
#     operateur = input("Entrez l'opérateur (+, -, *, /) : ")
#     nombre2 = float(input("Entrez le deuxième nombre : "))

#     if operateur == "+":
#         resultat = nombre1 + nombre2
#     elif operateur == "-":
#         resultat = nombre1 - nombre2
#     elif operateur == "*":
#         resultat = nombre1 * nombre2
#     elif operateur == "/":
#         if nombre2 != 0:
#             resultat = nombre1 / nombre2
#         else:
#             resultat = "Erreur : Division par zéro!"
#     else:
#         resultat = "Opérateur invalide!"

#     print(f"Le résultat est : {resultat}")

#     run = bool(int(input("Voulez-vous faire un autre calcul ? (1 = oui / 0 = non) : ")))