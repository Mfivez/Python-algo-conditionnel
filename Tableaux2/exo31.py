# exo31-Réalisez un algorithme dans lequel nous devons rechercher une valeur (entrée par l'utilisateur) dans un tableau d'entiers.

tb = [10, 20, 30, 30, 40]

val = int(input("Entrez la valeur à chercher : "))

count = 0

for i in tb:
    if i == val:
        count += 1

match count:
    case 0 :print(f"La valeur {val} n'a pas été trouvée dans le tableau.")
    case _ : print(f"La valeur {val} a été trouvée {count}x dans le tableau.")
