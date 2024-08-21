# exo11-Note (Pseudo-Code + Python)
# Ecrire un algorithme qui met l'appréciation par rapport à des
# notes. Ces notes sont comprises entre 0 et 20.

note = float(input("Entrez la note (entre 0 et 20) : "))

if note < 0 or note > 20:
    appreciation = "Note invalide."
else:
    if note >= 16:
        appreciation = "Très bien"
    elif note >= 14:
        appreciation = "Bien"
    elif note >= 12:
        appreciation = "Assez bien"
    elif note >= 10:
        appreciation = "Passable"
    else:
        appreciation = "Insuffisant"

print(f"Appréciation : {appreciation}")