run = True

student_result = 10
presence = True

if student_result >= 10 or presence :
    print ('reussi')
elif student_result == 9:
    print('réussi si bon résultat toute l\'année')
else:
    print('raté')



verif = (student_result >= 10)

if verif:

    print ('reussi')
else:
    print('raté')

# NON(A OU B) ↔ (NON A) ET (NON B)
# NON(A ET B) ↔ (NON A) OU (NON B)

"""
météo :
A = il pleut = pluie
B = il neige = neige

S'il est faux (qu'il neige ou qu'il pleut)) -> Alors il fait beau
(S'il est faux qu'il pleut) et (qu'il est faux qu'il neige) -> Alors il fait beau

S'il est faux (qu'il neige et qu'il pleut) -> Alors il fait beau
(S'il est faux qu'il neige) ou (qu'il est faux qu'il pleut) -> Alors il fait beau aussi



"""