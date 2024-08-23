# exo26-En considérant deux tableaux d'entiers (non triés), réalisez un algorithme qui place tous les éléments des deux tableaux dans un troisième. Ce dernier doit être trié une fois l'algorithme terminé. Notez que le tri doit être fait en même temps que la fusion des deux tableaux et pas après. (Indice : tab.reverse())

tb1 = [1, 5, 3]
tb2 = [2, 4, 6, 9, 5, 4]
tb3 = []

for element in tb1:
    i = 0
    while i < len(tb3) and tb3[i] < element:
        i += 1
    tb3.insert(i, element)

for element in tb2:
    i = 0
    while i < len(tb3) and tb3[i] < element:
        i += 1
    tb3.insert(i, element)

print(tb3)
