"""
Put the credit and stuff here:
"""
print("Welcome to the Oversimplified GPA Calc!")
"""
Question = input("Is your GPA weighted or unweighted?")
Then = input("Okay - I understand. Enter your grades in this form: 100; 95; 33")
"""
A=0
B=0
C=0
D=0
E=0
F=0
G=0
H=0
I=0
J=0
K=0
L=0
M=0
N=0
O=0
P=0
Q=0
R=0
S=0
T=0
U=0
V=0
W=0
X=0
Y=0
Z=0
J = 1
ForNow = int(input("Enter your first grade here. Follow this guide to know what each grade equates to:      "))
After = input("Type 'Y' if you have another grade and if not, type something else.      ").lower()
if ForNow > 92.49:
    ForNow = 4/4
elif ForNow > 89.49:
    ForNow = 3.67/4
elif ForNow > 86.49:
    ForNow = 3.33/4
elif ForNow > 82.49:
    ForNow = 3/4
elif ForNow > 79.49:
    ForNow = 2.67/4
elif ForNow > 76.49:
    ForNow = 2.33/4
elif ForNow > 72.49:
    ForNow = 2/4
elif ForNow > 69.49:
    ForNow = 1.67/4
elif ForNow > 66.49:
    ForNow = 1.33/4
elif ForNow > 62.49:
    ForNow = 1/4
elif ForNow > 59.49:
    ForNow = .67/4
else:
    ForNow = 0.00/4
if After == "y":
    J = 50
    A = int(input("Enter your next grade!   "))
    Q = input("Type 'Y' if you have another grade and if not, type something else.").lower()
    if A > 92.49:
        A = 4/4
    elif A > 89.49:
        A = 3.67/4
    elif A > 86.49:
        A = 3.33/4
    elif A > 82.49:
        A = 3/4
    elif A > 79.49:
        A = 2.67/4
    elif A > 76.49:
        A = 2.33/4
    elif A > 72.49:
        A = 2/4
    elif A > 69.49:
        A = 1.67/4
    elif A > 66.49:
        A = 1.33/4
    elif A > 62.49:
        A = 1/4
    elif A > 59.49:
        A = .67/4
    else:
        A = .00/4
    if Q == "y":
        J = 75
        B = int(input("Enter your next grade!   "))
        Z = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
        if B > 92.49:
            B = 4/4
        elif B > 89.49:
            B = 3.67/4
        elif B > 86.49:
            B = 3.33/4
        elif B > 82.49:
            B = 3/4
        elif B > 79.49:
            B = 2.67/4
        elif B > 76.49:
            B = 2.33/4
        elif B > 72.49:
            B = 2/4
        elif B > 69.49:
            B = 1.67/4
        elif B > 66.49:
            B = 1.33/4
        elif B > 62.49:
            B = 1/4
        elif B > 59.49:
            B = .67/4
        else:
            B = .00/4
        if Z == "y":
            J = 100
            C = int(input("Enter your next grade!   "))
            Y = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
            if C > 92.49:
                C = 4/4
            elif C > 89.49:
                C = 3.67/4
            elif C > 86.49:
                C = 3.33/4
            elif C > 82.49:
                C = 3/4
            elif C > 79.49:
                C = 2.67/4
            elif C > 76.49:
                C = 2.33/4
            elif C > 72.49:
                C = 2/4
            elif C > 69.49:
                C = 1.67/4
            elif C > 66.49:
                C = 1.33/4
            elif C > 62.49:
                C = 1/4
            elif C > 59.49:
                C = .67/4
            else:
                C = .00/4
            if Y == "y":
                J = 125
                D = int(input("Enter your next grade!   "))
                X = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                if D > 92.49:
                    D = 4/4
                elif D > 89.49:
                    D = 3.67/4
                elif D > 86.49:
                    D = 3.33/4
                elif D > 82.49:
                    D = 3/4
                elif D > 79.49:
                    D = 2.67/4
                elif D > 76.49:
                    D = 2.33/4
                elif D > 72.49:
                    D = 2/4
                elif D > 69.49:
                    D = 1.67/4
                elif D > 66.49:
                    D = 1.33/4
                elif D > 62.49:
                    D = 1/4
                elif D > 59.49:
                    D = .67/4
                else:
                    D = .00/4
                if X == "y":
                    J = 150
                    E = int(input("Enter your next grade!   "))
                    W = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                    if E > 92.49:
                        E = 4/4
                    elif E > 89.49:
                        E = 3.67/4
                    elif E > 86.49:
                        E = 3.33/4
                    elif E > 82.49:
                        E = 3/4
                    elif E > 79.49:
                        E = 2.67/4
                    elif E > 76.49:
                        E = 2.33/4
                    elif E > 72.49:
                        E = 2/4
                    elif E > 69.49:
                        E = 1.67/4
                    elif E > 66.49:
                        E = 1.33/4
                    elif E > 62.49:
                        E = 1/4
                    elif E > 59.49:
                        E = .67/4
                    else:
                        E = .00/4
                    if W == "y":
                        J = 175
                        F = int(input("Enter your next grade!   "))
                        V = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                        if F > 92.49:
                            F = 4/4
                        elif F > 89.49:
                            F = 3.67/4
                        elif F > 86.49:
                            F = 3.33/4
                        elif F > 82.49:
                            F = 3/4
                        elif F > 79.49:
                            F = 2.67/4
                        elif F > 76.49:
                            F = 2.33/4
                        elif F > 72.49:
                            F = 2/4
                        elif F > 69.49:
                            F = 1.67/4
                        elif F > 66.49:
                            F = 1.33/4
                        elif F > 62.49:
                            F = 1/4
                        elif F > 59.49:
                            F = .67/4
                        else:
                            F = .00/4
                        if V == "y":
                            J = 200
                            G = int(input("Enter your next grade!   "))
                            U = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                            if G > 92.49:
                                G = 4/4
                            elif G > 89.49:
                                G = 3.67/4
                            elif G > 86.49:
                                G = 3.33/4
                            elif G > 82.49:
                                G = 3/4
                            elif G > 79.49:
                                G = 2.67/4
                            elif G > 76.49:
                                G = 2.33/4
                            elif G > 72.49:
                                G = 2/4
                            elif G > 69.49:
                                G = 1.67/4
                            elif G > 66.49:
                                G = 1.33/4
                            elif G > 62.49:
                                G = 1/4
                            elif G > 59.49:
                                G = .67/4
                            else:
                                G = .00/4
                            if U == "y":
                                J = 225
                                H = int(input("Enter your next grade!   "))
                                T = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                                if H > 92.49:
                                    H = 4/4
                                elif H > 89.49:
                                    H = 3.67/4
                                elif H > 86.49:
                                    H = 3.33/4
                                elif H > 82.49:
                                    H = 3/4
                                elif H > 79.49:
                                    H = 2.67/4
                                elif H > 76.49:
                                    H = 2.33/4
                                elif H > 72.49:
                                    H = 2/4
                                elif H > 69.49:
                                    H = 1.67/4
                                elif H > 66.49:
                                    H = 1.33/4
                                elif H > 62.49:
                                    H = 1/4
                                elif H > 59.49:
                                    H = .67/4
                                else:
                                    H = .00/4
                                if T == "y":
                                    J = 250
                                    I = int(input("Enter your next grade!   "))
                                    if I > 92.49:
                                        I = 4/4
                                    elif I > 89.49:
                                        I = 3.67/4
                                    elif I > 86.49:
                                        I = 3.33/4
                                    elif I > 82.49:
                                        I = 3/4
                                    elif I > 79.49:
                                        I = 2.67/4
                                    elif I > 76.49:
                                        I = 2.33/4
                                    elif I > 72.49:
                                        I = 2/4
                                    elif I > 69.49:
                                        I = 1.67/4
                                    elif I > 66.49:
                                        I = 1.33/4
                                    elif I > 62.49:
                                        I = 1/4
                                    elif I > 59.49:
                                        I = .67/4
                                    else:
                                        I = .00/4
elif After == "n":
    print("Thanks!")
"""
Zip1 = zip((A:100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50)

Zip1 = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F+", "F", "F-", "U", "N/A")
Zip2 = (4, 4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, .67, .33, 0)
Zip3 = zip(Zip1, Zip2)

Total = sum("A", "B", "C", "D", "E", "F", "G", "H")
"""
if len(str(ForNow)) == 3 or 2 or 1:
    Final = (ForNow)
    if len(str(A)) == 3 or 2 or 1:
        Final = ((ForNow) + (A))
        if len(str(B)) == 3 or 2 or 1:
            Final = ((ForNow) + (A) + (B))
            if len(str(C)) == 3 or 2 or 1:
                Final = ((ForNow) + (A) + (B) + (C))
                if len(str(D)) == 3 or 2 or 1:
                    Final = ((ForNow) + (A) + (B) + (C) + (D))
                    if len(str(E)) == 3 or 2 or 1:
                        Final = ((ForNow) + (A) + (B) + (C) + (D) + (E))
                        if len(str(F)) == 3 or 2 or 1:
                            Final = ((ForNow) + (A) + (B) + (C) + (D) + (E) + (F))
                            if len(str(G)) == 3 or 2 or 1:
                                Final = ((ForNow) + (A) + (B) + (C) + (D) + (E) + (F) + (G))
                                if len(str(H)) == 3 or 2 or 1:
                                    Final = ((ForNow) + (A) + (B) + (C) + (D) + (E) + (F) + (G) + (H))
                                    if len(str(I)) == 3 or 2 or 1:
                                    Final = ((ForNow) + (A) + (B) + (C) + (D) + (E) + (F) + (G) + (H) + (I))
Printed = Final/J

if Printed > 3.7:
    print("You are above average - your GPA is {0}!".format(Printed))
if Printed < 3.7:
    print("You are below average - your GPA is {0}!".format(Printed))

"""
Now, make a zip list compiling A:4,A-:3.67, etc,.
Then, have something with <Question> that makes the code know what weighted means and what unweighted means.
After, have something with <Then> that adds the numbers together and then divides them over how many grades there were.
Finally, have something with <After> that displays the GPA.
"""