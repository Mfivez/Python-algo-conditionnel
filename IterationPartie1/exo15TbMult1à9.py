# exo15-À l’aide de deux boucles, afficher les tables de
# multiplication de 1 à 9. Ensuite, coder votre algorithme en Python.


# i * 3 -> Si je suis dans la tb 3 ça sera toujours 3
i = 1
# while i <= 9:

#     print(f"Tb multiplication de {i} : ")
#     j = 1
#     while j <=10:
#         print(f"{i} x {j} = {i * j}")
#         j += 1
#     i += 1
#     print()

for i in range(1, 10):
    print(f"Tb multiplication de {i} : ")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# i = 1

# while i <= 9:
#     print(f"Table de multiplication de {i}:")
#     j = 1
#     while j <= 10:
#         print(f"{i} x {j} = {i * j}")
#         j += 1
#     print()
#     i += 1

# ou avec une boucle for

# for i in range(1, 10):
#     print(f"Table de multiplication de {i}:")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print() 