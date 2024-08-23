import random as r

nbr_tentatives = 0
run = True

while run :
    if nbr_tentatives == 0 :
        entree_invalide = True
        while entree_invalide:
            choix = input("""Choisissez votre niveau :
                                    1. facile : entre 1 et 10
                                    2. normal : entre 1 et 100
                                    3. difficile : entre 1 et 1000
                                """)
            if choix in ["1", "2", "3"]:
                entree_invalide = False
                choix = int(choix)
            else:
                print("Veuillez choisir un niveau valide (1, 2 ou 3).")

        match choix :
            case 1 : borne_sup = 10
            case 2 : borne_sup = 100
            case 3 : borne_sup = 1000
            case _ : borne_sup = 1

        juste_prix = r.randint(1, borne_sup)


    essai = int(input(f"Devinez le nombre entre 1 et {borne_sup} : "))
    nbr_tentatives += 1

    if essai < juste_prix:
        print("C'est plus")
    elif essai > juste_prix:
        print("C'est moins")
    elif essai == juste_prix:
        print(f"Vous avez trouvé le juste prix : {juste_prix} en {nbr_tentatives} tentatives.")
        run = bool(int(input("Voulez-vous rejouer ? 1 = oui / 0 = non")))
        nbr_tentatives = 0
    elif nbr_tentatives == 10 :
        print("tu as perdu ! ")
        run = bool(int(input("Voulez-vous rejouer ? 1 = oui / 0 = non")))
        nbr_tentatives = 0

        
    
            



# while run:
#     print(f'Nombre de tentatives : {nbr_tentatives}')

#     if nbr_tentatives == 0:
#         entree_invalide = True
#         while entree_invalide:
#             choix = input("""Choisissez votre niveau :
#                             1. facile : entre 1 et 10
#                             2. normal : entre 1 et 100
#                             3. difficile : entre 1 et 1000
#                         """)
#             if choix in ["1", "2", "3"]:
#                 entree_invalide = False
#                 choix = int(choix)
#             else:
#                 print("Veuillez choisir un niveau valide (1, 2 ou 3).")


#         match choix:
#             case 1:
#                 borne_supp = 10
#             case 2:
#                 borne_supp = 100
#             case 3:
#                 borne_supp = 1000

#         juste_prix = r.randint(1, borne_supp)
#         print("Le jeu commence !")

#     entree_invalide = True
#     while entree_invalide:
#         try:
#             essai = int(input(f"Devinez le nombre entre 1 et {borne_supp} : "))
#             if 1 <= essai <= borne_supp:
#                 entree_invalide = False
#             else:
#                 print(f"Veuillez entrer un nombre entre 1 et {borne_supp}.")
#         except ValueError:
#             print("Entrée invalide. Veuillez entrer un nombre.")

#     nbr_tentatives += 1

#     print()
#     if essai < juste_prix:
#         print("C'est plus")
#     elif essai > juste_prix:
#         print("C'est moins")
#     else:
#         print(f"Vous avez trouvé le juste prix: {juste_prix} en {nbr_tentatives} tentatives.")
#         while True:
#             try:
#                 rejouer = int(input("Voulez-vous rejouer ? (1: Oui, 0: Non) "))
#                 if rejouer in [0, 1]:
#                     run = bool(rejouer)
#                     break
#                 else:
#                     print("Veuillez entrer 1 pour Oui ou 0 pour Non.")
#             except ValueError:
#                 print("Entrée invalide. Veuillez entrer 1 ou 0.")
        
#         if run:
#             nbr_tentatives = 0

#     print()

#     if nbr_tentatives == 10 and run != False:
#         print("Vous avez perdu...")
#         entree_invalide = True
#         while entree_invalide:
#             try:
#                 rejouer = int(input("Voulez-vous rejouer ? (1: Oui, 0: Non) "))
#                 if rejouer in [0, 1]:
#                     run = bool(rejouer)
#                     entree_invalide = False
#                 else:
#                     print("Veuillez entrer 1 pour Oui ou 0 pour Non.")
#             except ValueError:
#                 print("Entrée invalide. Veuillez entrer 1 ou 0.")
        
#         if run:
#             nbr_tentatives = 0