run = True

student_result = 10
presence = True

if student_result >= 10 or presence :
    print ('reussi')
elif student_result == 9:
    print('réussi si bon résultat toute l\'année')
else:
    print('raté')



verif = (student_result >= 10)

if verif:

    print ('reussi')
else:
    print('raté')

# NON(A OU B) ↔ (NON A) ET (NON B)
# NON(A ET B) ↔ (NON A) OU (NON B)

"""
météo :
A = il pleut = pluie
B = il neige = neige

S'il est faux (qu'il neige ou qu'il pleut)) -> Alors il fait beau
(S'il est faux qu'il pleut) et (qu'il est faux qu'il neige) -> Alors il fait beau

S'il est faux (qu'il neige et qu'il pleut) -> Alors il fait beau
(S'il est faux qu'il neige) ou (qu'il est faux qu'il pleut) -> Alors il fait beau aussi



"""

## Démo match case

# jour = int(input("Un jour de la semaine entre 1 et 7 : "))

# match jour :
#     case 1 : print("Lundi")
#     case 2 : print("Mardi")
#     case 3 : print("Mercredi")
#     case 4 : print("Jeudi")
#     case 5 : print("Vendredi")
#     case 6 : print("Samedi")
#     case 7 : print("Dimanche")
#     case _ : print("Le jour rentré n'existe pas dans la semaine")

# if jour == 1 :
#     print("Lundi")
# elif jour == 2 : 
#     print("Mardi")
# # .
# # . 
# else :
#     print("Le jour rentré n'existe pas dans la semaine")

## Démo Boucle While 

# compteur = 0

# while compteur < 10 :
#     print(f"{compteur}. yii")
#     # compteur = compteur + 1 même chose qu'en dessous (juste en forme non contractée)
#     compteur += 1


## Démo tableaux :

# mon_tableau = ["élément 1", "élément 2", 3]

# print(mon_tableau[1])

# mon_tableau.append("Vanessa")
# mon_tableau.append("Roméo")
# print(mon_tableau[4])
# print(mon_tableau)

# tb = ['AZE', 'AZE', 'AZE']
# size = 0

# tb.append('AZE')
# size += 1

# tb.append("Michel")
# size += 1

# print(tb, size)

# print(tb[size-1])

# tb[size-1] = "Plus michel"
# print(tb)
# print(tb.count("AZE"))



# tb = ['AZE', 'AZE', 'AZE']

# tb[1] = input("Entrez une valeur : ")
# print(tb)
    

## Démo boucle for

tb = ["a", "b", "c", "d"]

# Le nom element représente le réceptacle de chaque valeur présente dans la boucle spécifiée. Ne cherchez pas le nom de la variable élément ailleur dans le fichier, c'est nous qui déterminons le nom de la variable réceptacle au moment de la création de la boucle for
for element in tb:
    print(element)