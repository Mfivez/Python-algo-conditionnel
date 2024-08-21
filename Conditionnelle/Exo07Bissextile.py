# exo07-Année bissextile (Pseudo-Code + Python)

# Réaliser un petit algorithme qui sur base d’une année donnée va déterminer 
# s’il s’agit d’une année bissextile.
 
# Une année est bissextile si elle est divisible par 4, 
# mais non divisible par 100. Ou si elle est
# divisible par 400.

text = input("Une année : ")

if text.isdigit():
    annee = int(text)

    est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

    if est_bissextile:
        print(f"L'année {annee} est bissextile !")
    else:
        msg = f"L'année {annee} n'est pas bissextile !"
        print(msg)
else:
    print("Valeur erronée !")


