# exo27-Réalisez un algorithme nous permettant de déplacer un pion dans un tableau de 10 éléments. Au début, le pion se trouve dans la première case du tableau. Nous pouvons ensuite le déplacer par la gauche (g), par la droite (d) ou de stopper l'algorithme (q) (Indice : l'exo doit être exécuté dans la console Windows).

tb = ["🙎‍♂️"]+(["⬛"]*9)
posX = 0

run = True
while run :
    print("".join(tb))
    choix = input("G or D : ")

    match choix :
        case "G" :
            if posX == 0 :
                tb[posX] = "⬛"
                posX = (posX - 1) % len(tb)
                tb[posX] = "🙎‍♂️"
        case "D" :
            if posX == len(tb)-1 :
                tb[posX] = "⬛"
                posX = (posX + 1) % len(tb)
                tb[posX] = "🙎‍♂️"



