# exo8-Lanceur de balles de tennis (Pseudo-Code + Python)
# (Indice : booleen = bool(int(input("Veuillez insérer : 1 = oui / 0 = non"))

# Réaliser l’algorithme d’un lanceur de balles de tennis. Ce lanceur possède deux états :
# – prêt : permet de savoir si le tennisman est prêt. Il ne faut pas lancer de balles dans le cas contraire
# – panier_vide : permet de savoir s’il y a encore des balles disponibles

# Le lanceur de balle possède l’opération « lancerBalle » qui, vous l’aurez compris, permet de lancer
# une balle.

# pret = bool(int(input("Le tennisman est-il prêt ? (1 = oui / 0 = non) : ")))

# panier_vide = bool(int(input("Le panier est-il vide ? (1 = oui / 0 = non) : ")))

# if pret and not panier_vide:
#     print("lancer balle")
# elif not pret and panier_vide:
#     print("Le tennisman n'est pas prêt et le panier est vide")
# elif not pret:
#     print("Le tennisman n'est pas prêt.")
# elif panier_vide:
#     print("Le panier est vide.")

# def lancerBalle():
#     print('Lancer balle')


pret = bool(int(input("Es-tu prêt : 1 = oui / 0 = non : ")))
panier_vide = bool(int(input("Le panier est-il vide : 1 = oui / 0 = non : ")))

if pret and not panier_vide :
    print("lancer balle")
elif not pret and panier_vide :
    print('ni le panier ni le joueur ne respecte les conditions pour lancer la balle')
elif not pret:
    print('Le joueur n\'est pas prêt')
else:
    print("Le panier est vide")