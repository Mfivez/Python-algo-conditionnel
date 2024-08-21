A = 3
B = 9
C = False
D = not C
E = 9

print("1.", A > 8) # False
print("2.",B == 9) # True
print("3.",not(A != 3)) # True
print("4.",not(C)) # True
print("5.",(A < B) or C) # True
print("6.",not(A + B) != 12) # True
print("7.", ((B == 5) or ( (E > 10) and (A < 8) ) )) # False
print("8. ", ( ( ( ( B == 5 ) or ( (E > 10) and (A < 8) ) ) or (A < B) or C) and C )) # False