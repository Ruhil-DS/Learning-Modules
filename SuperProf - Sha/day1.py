F = 70
PE1 = 100
PE2 = 33.33
Qz1 = 76
Qz2 = 76
T = (0.1*100) + (0.3*F) + (0.2*max(PE1, PE2)) + (0.10*min(PE1, PE2)) + max(0.25*max(Qz1, Qz2), (0.15*Qz1) + (0.25*Qz2))
print(f'{T+5} is the final JAVA score')

F = 75
Qz1 = 63
Qz2 = 45
T = (0.1 * 100) + max(0.35*F + 0.25*Qz1 + 0.3*Qz2, 0.5*F + 0.3*max(Qz1, Qz2))

print(f'{T+5} is the final MAD2 score')