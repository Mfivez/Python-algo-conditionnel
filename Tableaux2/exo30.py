# exo30-En considérant un tableau d'entiers trié dans l'ordre croissant, réaliser un algorithme étant capable d'insérer une nouvelle valeur dans le tableau de façon à ce que la tableau reste trié. Le but n'est évidemment pas d'insérer la valeur à la fin etde trier après mais bien de l'insérer au bon endroit directement.


tb = [1, 2, 3, 4, 5, 6, 7]
value = 10
index = len(tb)
find = False

for i,v in enumerate(tb):
    if value < v and not find:
        index = i
        find = True

## Sol 1 : 
# for i in range(index, len(tb)):
#     temp = tb[i]
#     tb[i] = value
#     value = temp
# tb.append(value)


# Sol 2 : 
tb.append(0)
for i in range(len(tb) - 1, index, -1):
    tb[i] = tb[i - 1]
tb[index] = value

print(tb)

# [3, 4, 5]
# stocker 4 mettre 3
# stocker 5 mettre 4 
# ajouter 5