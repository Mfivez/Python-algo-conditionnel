# exo11-Note (Pseudo-Code + Python)
# Ecrire un algorithme qui met l'appréciation par rapport à des
# notes. Ces notes sont comprises entre 0 et 20.

# note = int(input("Entrez la note (entre 0 et 20) : "))

# if note < 0 or note > 20:
#     appreciation = "Note invalide."
# else:
#     if note >= 16:
#         appreciation = "Très bien"
#     elif note >= 12:
#         appreciation = "Assez bien"
#     elif note >= 10:
#         appreciation = "Passable"
#     else:
#         appreciation = "Insuffisant"

# print(f"Appréciation : {appreciation}")

note = int(input("Entrez une note (entre 0 et 20) :"))

if note < 0 or note > 20:
    appreciation = "Note invalide"
else :
    if note >= 10:
        appreciation = "Bien, tu as réussi"
    else:
        appreciation = "Pas bien, tu n'as pas réussi"

print(f"Appréciation pour la note de {note} : {appreciation}")