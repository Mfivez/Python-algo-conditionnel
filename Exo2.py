#Exo 2

# nom = input("Entrez votre nom : ")
# prenom = input("Entrez votre prénom : ")
# print(f"Bienvenue {prenom} {nom}")

#Exo 3
# Variable a, b, c, d, e : Entier
# Debut
# a ← 8 MOD 3
# b ← 4 + a
# c ← b * a
# d ← (c – a) * b
# e ← ((a + 7) * (d DIV a)) * 0
# Fin
# a = 8 % 3
# b = a + 4
# c = b * a
# d = (c - a) * b
# e = ( (a + 7) * (d // a)) * 0
# print(a, b, c, d, e, sep ="\n")


### Exo convertir temps
# temps = 4678 
# heure = 0
# minute = 0
# seconde = 0

# if temps >= 3600:
#     heure = temps // 3600 
#     temps = temps % 3600

# if temps >= 60:
#     minute = temps // 60 
#     temps = temps % 60 

# seconde = temps

# print(f"{heure}H{minute}Min{seconde}Sec")
#86400

temps = int(input("Le temps que vous souhaitez transformer : "))
journee = 0
heure = 0
minute = 0


if temps >= 86400: # journée
    journee = temps // 86400
    temps = temps % 86400

if temps >= 3600: # heure
    heure = temps // 3600
    temps = temps % 3600

if temps >= 60: # minute
    minute = temps // 60
    temps = temps % 60

print(f"{journee}J:{heure}H:{minute}M:{temps}S")
