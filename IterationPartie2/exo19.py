# exo19-À l’aide de la boucle TantQue … Faire, réalisez un algorithme calculant le
# résultat de N10. N étant un nombre saisi par l’utilisateur.

N = int(input("Entrez un nombre : "))

i = 0 # compteur
puissance = 10
resultat = 1

print("cheminement : ")
while i < puissance :
    print(f"{i+1}. resultat de {resultat}*{N} = {resultat*N}")
    resultat *= N
    i += 1

print(f"Le résultat de {N}^10 est : {resultat}")

# N = int(input("Entrez le nombre N : "))

# resultat = 1
# puissance = 10
# compteur = 0

# print()
# print("cheminement : ")
# while compteur < puissance: # ou compteur < 10
#     print(f"{compteur+1}. resultat de {resultat}*{N} = {resultat*N}")
#     resultat *= N
#     compteur += 1

# print(f"==> Le résultat de {N}^10 est : {resultat}")