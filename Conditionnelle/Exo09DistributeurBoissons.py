# exo09-Distributeur de boissons (Pseudo-Code + Python)
# Réaliser l’algorithme d’un distributeur de boissons. Ce dernier propose plusieurs boissons et
# l’utilisateur choisit celle qu’il désire en entrant le numéro correspondant. Ne pas oublier de vérifier
# s’il y a encore des boissons en stock.

stock_coca = 5
stock_pepsi = 3
stock_eau = 0



choix = int(input(f"""Entrez le numéro de la boisson souhaitée : 
                        1. Coca-Cola (Stock: {stock_coca})
                        2. Pepsi (Stock: {stock_pepsi})
                        3. Eau (Stock: {stock_eau}
                  """))

if choix == 1:
    if stock_coca > 0:
        print("Voici votre Coca-Cola.")
    else:
        print("Désolé, Coca-Cola est en rupture de stock.")

if choix == 2:
    if stock_pepsi > 0:
        print("Voici votre Pepsi.")
    else:
        print("Désolé, Pepsi est en rupture de stock.")

if choix == 3:
    if stock_eau > 0:
        print("Voici votre Eau.")   
    else:
        print("Désolé, Eau est en rupture de stock.")
