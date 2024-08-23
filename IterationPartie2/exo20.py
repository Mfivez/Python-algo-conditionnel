# exo20-Reprenez l’exercice précédent et modifiez-le pour que l’utilisateur entre
# également l’exposant qu’il désire calculer.

N = int(input("Entrez le nombre N : "))
exposant = int(input("Entrez l'exposant : "))

resultat = 1
compteur = 0

print()
print("cheminement : ")
while compteur < exposant: 
    print(f"{compteur+1}. resultat de {resultat}*{N} = {resultat*N}")
    resultat *= N
    compteur += 1

print(f"==> Le résultat de {N}^{exposant} est : {resultat}")