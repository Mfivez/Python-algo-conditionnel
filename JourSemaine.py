# L'utilisateur saisie une date, le programme verifie la date.
# Si la date est valide, il indique le jour de la semaine.

# Pour l'exercice, ne pas utiliser les méthodes de python ;)

jour = int(input("Jour : "))
mois = int(input("Mois : "))
annee = int(input("Année : "))

#Definition du nombre de jour du mois
nb_jour = 30
if mois == 2:
    est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

    nb_jour = 29
    if not est_bissextile:
        nb_jour = 28

    #Ternaire => Une affection combiné a un "if"
    # nb_jour = 29 if est_bissextile else 28

elif (mois % 2 != 0 and mois < 8) or (mois % 2 == 0 and mois >= 8):
    nb_jour = 31


# Check erreur dans la date
erreur = False
if mois < 1 or mois > 12:
    print("Mois erroné")
    erreur = True
if jour < 1 or jour > nb_jour:
    print("Jour erroné")
    erreur = True

# Afficher le Jour de la semaine
if not erreur:

    if annee < 1583 or annee > 9999:
        print("Date non supportée")
    else:
        # https://fr.wikibooks.org/wiki/Curiosit%C3%A9s_math%C3%A9matiques/Trouver_le_jour_de_la_semaine_avec_une_date_donn%C3%A9e

        c = (14 - mois) // 12
        a = annee - c
        m = mois + 12 * c - 2

        j = (jour + a + a // 4 - a // 100 + a // 400 + (31 * m) // 12) % 7

        journee = "Dimanche"
        if j == 1:
            journee = "Lundi"
        elif j == 2:
            journee = "Mardi"
        elif j == 3:
            journee = "Mercredi"
        elif j == 4:
            journee = "Jeudi"
        elif j == 5:
            journee = "Vendredi"
        elif j == 6:
            journee = "Samedi"

        print("Cette date correspont au jour : \"",journee,"\"", sep="")