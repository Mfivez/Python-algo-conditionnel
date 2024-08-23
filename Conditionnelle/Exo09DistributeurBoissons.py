# exo09-Distributeur de boissons (Pseudo-Code + Python)
# Réaliser l’algorithme d’un distributeur de boissons. Ce dernier propose plusieurs boissons et
# l’utilisateur choisit celle qu’il désire en entrant le numéro correspondant. Ne pas oublier de vérifier
# s’il y a encore des boissons en stock.

stock_coca = 3
stock_fanta = 1
stock_sprite = 0

stock = {
    "coca": 3,
    "fanta": 2
}

choix = input(f""" Choissisez votre boisson : (son nom)
            1. Coca -> stock : {stock_coca}
            2. fanta -> stock : {stock_fanta}
            3. sprite -> stock : {stock_sprite}
        """)



def choisirBoissonDico(boisson_choisie):
    stock[boisson_choisie] = stock[boisson_choisie] - 1


choisirBoissonDico(choix)

print(stock["coca"])











def choisirBoisson(boisson_choisie):
    stock = 0
    stock_coca_modif = stock_coca
    stock_fanta_modif = stock_fanta
    stock_sprite_modif = stock_sprite

    if boisson_choisie == 1 :
        stock = stock_coca
        boisson_choisie = 'coca'
        stock_coca_modif = stock_coca - 1
    elif boisson_choisie == 2 :
        stock =stock_fanta
        boisson_choisie = 'fanta'
        stock_fanta_modif = stock_fanta - 1
    elif boisson_choisie == 3 :
        stock = stock_sprite
        boisson_choisie = 'sprite'
        stock_sprite_modif = stock_sprite - 1

    if stock > 0:
        print(f"Voilà ton {boisson_choisie}")
    else :
        print(f"Il n'y a plus de {boisson_choisie}")
    return stock_coca_modif, stock_fanta_modif, stock_sprite_modif

# stock_coca, stock_fanta, stock_sprite =  choisirBoisson(choix)
# print(stock_coca,stock_fanta, stock_sprite )

# if choix == 1: #coca
#     if stock_coca > 0:
#         print("Voilà ton coca")
#     else :
#         print("Il n'y a plus de coca")

# if choix == 2: #fanta
#     if stock_fanta > 0:
#         print("Voilà ton fanta")
#     else :
#         print("Il n'y a plus de fanta")

# if choix == 3: #sprite
#     if stock_sprite > 0:
#         print("Voilà ton sprite")
#     else :
#         print("Il n'y a plus de sprite")










# stock_coca = 5
# stock_pepsi = 3
# stock_eau = 0

# choix = int(input(f"""Entrez le numéro de la boisson souhaitée : 
#                         1. Coca-Cola (Stock: {stock_coca})
#                         2. Pepsi (Stock: {stock_pepsi})
#                         3. Eau (Stock: {stock_eau}
#                   """))

# if choix == 1:
#     if stock_coca > 0:
#         print("Voici votre Coca-Cola.")
#     else:
#         print("Désolé, Coca-Cola est en rupture de stock.")

# if choix == 2:
#     if stock_pepsi > 0:
#         print("Voici votre Pepsi.")
#     else:
#         print("Désolé, Pepsi est en rupture de stock.")

# if choix == 3:
#     if stock_eau > 0:
#         print("Voici votre Eau.")   
#     else:
#         print("Désolé, Eau est en rupture de stock.")
