# exo17-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme du distributeur
# de boissons pour qu’il demande au client s’il désire une autre boisson (Tant qu’il en a
# envie).




stock_coca = 3
stock_fanta = 1
stock_sprite = 0


run = True
while run :
    choix = int(input(f""" Choissisez votre boisson :
             1. Coca -> stock : {stock_coca}
             2. fanta -> stock : {stock_fanta}
             3. sprite -> stock : {stock_sprite}
         """))
    
    if choix == 1: #coca
        if stock_coca > 0:
            stock_coca -= 1
            # stock_coca = stock_coca - 1
            print("Voilà ton coca")
        else :
            print("Il n'y a plus de coca")

    if choix == 2: #fanta
        if stock_fanta > 0:
            stock_fanta -= 1
            print("Voilà ton fanta")
        else :
            print("Il n'y a plus de fanta")

    if choix == 3: #sprite
        if stock_sprite > 0:
            stock_sprite -=1
            print("Voilà ton sprite")
        else :
            print("Il n'y a plus de sprite")


    run = bool(int(input("Voulez-vous une autre boisson ? (1 = oui / 0 = non) : ")))



# run = True

# while run:
#     choix = int(input(f""" Choissisez votre boisson :
#             1. Coca -> stock : {stock_coca}
#             2. fanta -> stock : {stock_fanta}
#             3. sprite -> stock : {stock_sprite}
#         """))

#     if choix == 1:
#         if stock_coca > 0:
#             stock_coca -= 1
#             print("Voici votre Coca-Cola.")
#         else:
#             print("Désolé, Coca-Cola est en rupture de stock.")
#     elif choix == 2:
#         if stock_fanta > 0:
#             stock_fanta -= 1
#             print("Voici votre fanta.")
#         else:
#             print("Désolé, fanta est en rupture de stock.")
#     elif choix == 3:
#         if stock_sprite > 0:
#             stock_sprite -= 1
#             print("Voici votre sprite.")
#         else:
#             print("Désolé, sprite est en rupture de stock.")
#     else:
#         print("Choix invalide.")

#     run = bool(int(input("Voulez-vous une autre boisson ? (1 = oui / 0 = non) : ")))

