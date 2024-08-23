# exo12-Réalisez un algorithme utilisant le convertisseur de
# secondes, il reçoit deux durées (jours, heures, minutes et
# secondes) et calcule la différence entre ces dernières.

jour1 = int(input("Nbr de jours pour la 1ère durée : "))
heure1 = int(input("Nbr d'heures pour la 1ère durée : "))
minute1 = int(input("Nbr de minutes pour la 1ère durée : "))
seconde1 = int(input("Nbr de secondes pour la 1ère durée : "))

jour2 = int(input("Nbr de jours pour la 2ème durée : "))
heure2 = int(input("Nbr d'heures pour la 2ème durée : "))
minute2 = int(input("Nbr de minutes pour la 2ème durée : "))
seconde2 = int(input("Nbr de secondes pour la 2ème durée : "))

total_seconde1 = jour1 * 86400 + heure1 * 3600 + minute1 * 60 + seconde1
total_seconde2 = jour2 * 86400 + heure2 * 3600 + minute2 * 60 + seconde2

if total_seconde1 > total_seconde2 :
    difference = total_seconde1 - total_seconde2
else:
    difference = total_seconde2 - total_seconde1

# difference = abs(total_seconde1 - total_seconde2)

jour_diff = difference // 86400
reste = difference % 86400
heure_diff = reste // 3600
reste = reste % 3600
minute_diff = reste // 60
seconde_diff = reste % 60

print(f"La différence est de {jour_diff} jours, {heure_diff} heures, {minute_diff} minutes et {seconde_diff} secondes.")












# jours1 = int(input("Nombre de jours pour la 1ère durée : "))
# heures1 = int(input("Nombre d'heures pour la 1ère durée : "))
# minutes1 = int(input("Nombre de minutes pour la 1ère durée : "))
# secondes1 = int(input("Nombre de secondes pour la 1ère durée : "))

# jours2 = int(input("Nombre de jours pour la 2ème durée : "))
# heures2 = int(input("Nombre d'heures pour la 2ème durée : "))
# minutes2 = int(input("Nombre de minutes pour la 2ème durée : "))
# secondes2 = int(input("Nombre de secondes pour la 2ème durée : "))

# total_secondes1 = jours1 * 86400 + heures1 * 3600 + minutes1 * 60 + secondes1
# total_secondes2 = jours2 * 86400 + heures2 * 3600 + minutes2 * 60 + secondes2

# if total_secondes1 > total_secondes2 :
#     difference_secondes = total_secondes1 - total_secondes2
# else :
#     difference_secondes = total_secondes2 - total_secondes1

# jours_diff = difference_secondes // 86400
# reste = difference_secondes % 86400
# heures_diff = reste // 3600
# reste = reste % 3600
# minutes_diff = reste // 60
# secondes_diff = reste % 60

# print(f"La différence est de {jours_diff} jours, {heures_diff} heures, {minutes_diff} minutes et {secondes_diff} secondes.")

