# exo25-À l’aide des boucles, réalisez un algorithme permettant de trier un tableau d’entiers dans l’ordre croissant. Mettez-le ensuite en pratique avec le Python.

tb = [2, 4, 7, 3, 1]

for i in range(len(tb)-1):
    for j in range(len(tb)-1):
        if tb[j] > tb[j+1]:
            tb[j], tb[j+1] = tb[j+1], tb[j]

print(tb)