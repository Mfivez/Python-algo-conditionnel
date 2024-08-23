# Écrire un algorithme demandant à l’utilisateur le nombre de joueurs (max 10 joueurs). Ensuite, l’algorithme doit demander à l’utilisateur le score de chaque joueur. Une fois ceci fini, il faut afficher la moyenne des scores. Faites de même en Python

notes = []
valide = False

while not valide :
    nbr_joueur = input("Entrez le nbr de joueurs : ")
    
    if nbr_joueur.isdigit() and int(nbr_joueur) <= 10:
        nbr_joueur = int(nbr_joueur)
        valide = True
    else:
        print("entrez une valeur valide")

for i in range(nbr_joueur):
    valide = False
    while not valide :
        note = input(f"Entrez la note du joueur {i+1} : ")

        if note.isdigit() :
            note = int(note)
            valide = True
            notes.append(note)
        else:
            print("entrez une valeur valide")

print(f"Moyenne : {sum(notes)/len(notes)}")
