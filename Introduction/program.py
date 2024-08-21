#exo 1
message = "Bienvenue"
print(message)

variable = 121231
variable = "variable"

# def addition(a, b):
#     print(a + b)

# addition(10, 12)

#exo 2
a = 5
b = 7
# a, b = 5, 7
print(f"valeur de a:{a} et de b:{b}")
a, b = b, a
print(f"valeur de a:{a} et de b:{b}")

print()
a = 12
print(id(a))
a = 13
print(id(a))
# comment créer un entier à partir de texte
entier_str = '12'
entier_str = int(entier_str)
print(type(entier_str))

lecture_reponse_utilisateur = int( input( "Entrez un chiffre : " ) ) 
print(lecture_reponse_utilisateur)
print(type(lecture_reponse_utilisateur))
