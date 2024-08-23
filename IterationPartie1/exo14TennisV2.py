# exo14-Reprenez l’algorithme du lanceur de balles de tennis et
# faites en sorte qu’il lance une balle tant que le stock n’est pas vide.
# Il y a donc 2 variables stock_balles et pret


stock_balles = int(input("Entrez le nombre de balles qui se trouvent dans son stock : "))
pret = bool(int(input("Es-tu prêt : 1 = oui / 0 = non : ")))

while pret and stock_balles > 0 :
    stock_balles -= 1
    # stock_balles = stock_balles - 1 ## Même chose
    print(f"Lancer balle (sotck restant : {stock_balles})")


if not pret:
    print('Le joueur n\'est pas prêt')
if stock_balles == 0:
        print("Le panier est vide, remplissez-le")

# stock_balles = int(input("Entrez le nombre de balles dans le stock : "))
# pret = bool(int(input("Es-tu prêt : 1 = oui / 0 = non : ")))

# while pret and stock_balles > 0:
#     stock_balles -= 1 
#     print(f"Lancer balle (stock restant : {stock_balles})")

# if stock_balles == 0:
#     print("Le panier est vide.")
# if not pret:
#     print("Le joueur n'est pas prêt.")