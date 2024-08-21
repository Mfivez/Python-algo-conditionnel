# exo12-Réalisez un algorithme utilisant le convertisseur de
# secondes, il reçoit deux durées (jours, heures, minutes et
# secondes) et calcule la différence entre ces dernières.


jours1 = int(input("Entrez le nombre de jours pour la première durée : "))
heures1 = int(input("Entrez le nombre d'heures pour la première durée : "))
minutes1 = int(input("Entrez le nombre de minutes pour la première durée : "))
secondes1 = int(input("Entrez le nombre de secondes pour la première durée : "))

jours2 = int(input("Entrez le nombre de jours pour la deuxième durée : "))
heures2 = int(input("Entrez le nombre d'heures pour la deuxième durée : "))
minutes2 = int(input("Entrez le nombre de minutes pour la deuxième durée : "))
secondes2 = int(input("Entrez le nombre de secondes pour la deuxième durée : "))

total_secondes1 = jours1 * 86400 + heures1 * 3600 + minutes1 * 60 + secondes1
total_secondes2 = jours2 * 86400 + heures2 * 3600 + minutes2 * 60 + secondes2

if total_secondes1 > total_secondes2 :
    difference_secondes = total_secondes1 - total_secondes2
else :
    difference_secondes = total_secondes2 - total_secondes1

jours_diff = difference_secondes // 86400
reste = difference_secondes % 86400
heures_diff = reste // 3600
reste = reste % 3600
minutes_diff = reste // 60
secondes_diff = reste % 60

print(f"La différence est de {jours_diff} jours, {heures_diff} heures, {minutes_diff} minutes et {secondes_diff} secondes.")