import random
print("Bienvenue au juste prix")
keepon = True

def is_integer_between(nb, inf_inclusive=float('-inf'), sup_inclusive=float('inf')):
    """
    Vérifie si un nombre est compris entre deux bornes incluses.
 
    Args:
        nb (str ou int): Le nombre à vérifier.
        inf_inclusive (float, optionnel): La borne inférieure (par défaut -inf).
        sup_inclusive (float, optionnel): La borne supérieure (par défaut +inf).
 
    Returns:
        bool: True si le nombre est dans l'intervalle, False sinon.
    """
    try:
        int(nb)
        if(int(nb)>=inf_inclusive and int(nb)<=sup_inclusive):
            return True
        return False
    except ValueError:
        return False


while keepon:
    nb_chances_rest = 10
    choice=""
    while not is_integer_between(choice,1,3):
        choice = input(f"""
          Veuillez choisir un niveau: 
          Tapez 1 : niveau facile : un nombre entre 1 et 10
          Tapez 2 : niveau moyen : un nombre entre 1 et 100
          Tapez 3 : niveau difficile : un nombre entre 1 et 1000
          
          Vous avez {nb_chances_rest} chances
          """
          )
    match choice:
        case "1": 
            borne=10
        case "2":
            borne=100
        case "3":
            borne=1000
        case _:
            borne=1
    
    nb_to_find = random.randint(1,borne)
    win=False

    while nb_chances_rest>0 and not win:
        tentative=""
        while not is_integer_between(tentative,1,borne):
            tentative = input(f"Veuillez entrer un nombre entre 1 et {borne} : ")
        
        if int(tentative)<nb_to_find:
            nb_chances_rest= nb_chances_rest-1
            print(f"C'est +, il vous reste {nb_chances_rest} chances.")
        elif int(tentative)>nb_to_find:
            nb_chances_rest = nb_chances_rest-1
            print(f"C'est -, il vous reste {nb_chances_rest} chances.")
        else:
            print("Félicitations, vous avez trouvé!")
            win=True
    if not win:
        print("Vous avez perdu.")
        
    choice = ""
    while not is_integer_between(choice,1,2):
        choice = input(f"""
          Souhaitez-vous rejouer?
          Tapez 1 : oui
          Tapez 2 : non
          """
          )
    if choice=="1":
        keepon=True
    else:
        keepon=False