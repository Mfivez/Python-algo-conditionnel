# exo16-Un algorithme reçoit deux nombres de l’utilisateur
# • (opération Lire) : a et b.
# • Il répond : « C’est plus » lorsque b est plus petit que a.
# • Et inversement, il répond : « C’est moins » lorsque b est plus grand que a.
# • Si a est égal à b, il répond : « C’est gagné ».

jeu_en_cours = True

while jeu_en_cours :
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))

    if b < a :
        print("C'est plus")
    elif b > a :
        print("c'est moins")
    else :
        print("Vous avez gagné")
        jeu_en_cours = False


# jeu_en_cours = True

# while jeu_en_cours:
#     a = int(input("Entrez le premier nombre (a) : "))
#     b = int(input("Entrez le deuxième nombre (b) : "))

#     if b < a:
#         print("C'est plus")
#     elif b > a:
#         print("C'est moins")
#     else:
#         print("C'est gagné")
#         jeu_en_cours = False 