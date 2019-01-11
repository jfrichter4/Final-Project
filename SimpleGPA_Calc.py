"""
Put the credit and stuff here:
"""
print("Welcome to the Oversimplified GPA Calc!")
"""
Question = input("Is your GPA weighted or unweighted?")
Then = input("Okay - I understand. Enter your grades in this form: 100; 95; 33")
"""

SW = 100
SH = 100
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
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
    ForNow = 4 
elif ForNow > 89.49:
    ForNow = 3.67 
elif ForNow > 86.49:
    ForNow = 3.33 
elif ForNow > 82.49:
    ForNow = 3 
elif ForNow > 79.49:
    ForNow = 2.67 
elif ForNow > 76.49:
    ForNow = 2.33 
elif ForNow > 72.49:
    ForNow = 2 
elif ForNow > 69.49:
    ForNow = 1.67 
elif ForNow > 66.49:
    ForNow = 1.33 
elif ForNow > 62.49:
    ForNow = 1 
elif ForNow > 59.49:
    ForNow = .67 
else:
    ForNow = 0.00 
if After == "y":
    J = 2
    A = int(input("Enter your next grade!   "))
    Q = input("Type 'Y', or something else:      ").lower()
    if A > 92.49:
        A = 4 
    elif A > 89.49:
        A = 3.67 
    elif A > 86.49:
        A = 3.33 
    elif A > 82.49:
        A = 3 
    elif A > 79.49:
        A = 2.67 
    elif A > 76.49:
        A = 2.33 
    elif A > 72.49:
        A = 2 
    elif A > 69.49:
        A = 1.67 
    elif A > 66.49:
        A = 1.33 
    elif A > 62.49:
        A = 1 
    elif A > 59.49:
        A = .67 
    else:
        A = .00 
    if Q == "y":
        J = 3
        B = int(input("Enter your next grade!   "))
        Z = input("Type 'Y', or something else:    ").lower()
        if B > 92.49:
            B = 4 
        elif B > 89.49:
            B = 3.67 
        elif B > 86.49:
            B = 3.33 
        elif B > 82.49:
            B = 3 
        elif B > 79.49:
            B = 2.67 
        elif B > 76.49:
            B = 2.33 
        elif B > 72.49:
            B = 2 
        elif B > 69.49:
            B = 1.67 
        elif B > 66.49:
            B = 1.33 
        elif B > 62.49:
            B = 1 
        elif B > 59.49:
            B = .67 
        else:
            B = .00 
        if Z == "y":
            J = 4
            C = int(input("Enter your next grade!   "))
            Y = input("Type 'Y', or something else:    ").lower()
            if C > 92.49:
                C = 4 
            elif C > 89.49:
                C = 3.67 
            elif C > 86.49:
                C = 3.33 
            elif C > 82.49:
                C = 3 
            elif C > 79.49:
                C = 2.67 
            elif C > 76.49:
                C = 2.33 
            elif C > 72.49:
                C = 2 
            elif C > 69.49:
                C = 1.67 
            elif C > 66.49:
                C = 1.33 
            elif C > 62.49:
                C = 1 
            elif C > 59.49:
                C = .67 
            else:
                C = .00 
            if Y == "y":
                J = 5
                D = int(input("Enter your next grade!   "))
                X = input("Type 'Y', or something else:    ").lower()
                if D > 92.49:
                    D = 4 
                elif D > 89.49:
                    D = 3.67 
                elif D > 86.49:
                    D = 3.33 
                elif D > 82.49:
                    D = 3 
                elif D > 79.49:
                    D = 2.67 
                elif D > 76.49:
                    D = 2.33 
                elif D > 72.49:
                    D = 2 
                elif D > 69.49:
                    D = 1.67 
                elif D > 66.49:
                    D = 1.33 
                elif D > 62.49:
                    D = 1 
                elif D > 59.49:
                    D = .67 
                else:
                    D = .00 
                if X == "y":
                    J = 6
                    E = int(input("Enter your next grade!   "))
                    W = input("Type 'Y', or something else:    ").lower()
                    if E > 92.49:
                        E = 4 
                    elif E > 89.49:
                        E = 3.67 
                    elif E > 86.49:
                        E = 3.33 
                    elif E > 82.49:
                        E = 3 
                    elif E > 79.49:
                        E = 2.67 
                    elif E > 76.49:
                        E = 2.33 
                    elif E > 72.49:
                        E = 2 
                    elif E > 69.49:
                        E = 1.67 
                    elif E > 66.49:
                        E = 1.33 
                    elif E > 62.49:
                        E = 1 
                    elif E > 59.49:
                        E = .67 
                    else:
                        E = .00 
                    if W == "y":
                        J = 7
                        F = int(input("Enter your next grade!   "))
                        V = input("Type 'Y', or something else:    ").lower()
                        if F > 92.49:
                            F = 4 
                        elif F > 89.49:
                            F = 3.67 
                        elif F > 86.49:
                            F = 3.33 
                        elif F > 82.49:
                            F = 3 
                        elif F > 79.49:
                            F = 2.67 
                        elif F > 76.49:
                            F = 2.33 
                        elif F > 72.49:
                            F = 2 
                        elif F > 69.49:
                            F = 1.67 
                        elif F > 66.49:
                            F = 1.33 
                        elif F > 62.49:
                            F = 1 
                        elif F > 59.49:
                            F = .67 
                        else:
                            F = .00 
                        if V == "y":
                            J = 8
                            G = int(input("Enter your next grade!   "))
                            U = input("Type 'Y', or something else:    ").lower()
                            if G > 92.49:
                                G = 4 
                            elif G > 89.49:
                                G = 3.67 
                            elif G > 86.49:
                                G = 3.33 
                            elif G > 82.49:
                                G = 3 
                            elif G > 79.49:
                                G = 2.67 
                            elif G > 76.49:
                                G = 2.33 
                            elif G > 72.49:
                                G = 2 
                            elif G > 69.49:
                                G = 1.67 
                            elif G > 66.49:
                                G = 1.33 
                            elif G > 62.49:
                                G = 1 
                            elif G > 59.49:
                                G = .67 
                            else:
                                G = .00 
                            if U == "y":
                                J = 9
                                H = int(input("Enter your next grade!   "))
                                T = input("Type 'Y', or something else:    ").lower()
                                if H > 92.49:
                                    H = 4 
                                elif H > 89.49:
                                    H = 3.67 
                                elif H > 86.49:
                                    H = 3.33 
                                elif H > 82.49:
                                    H = 3 
                                elif H > 79.49:
                                    H = 2.67 
                                elif H > 76.49:
                                    H = 2.33 
                                elif H > 72.49:
                                    H = 2 
                                elif H > 69.49:
                                    H = 1.67 
                                elif H > 66.49:
                                    H = 1.33 
                                elif H > 62.49:
                                    H = 1 
                                elif H > 59.49:
                                    H = .67 
                                else:
                                    H = .00 
                                if T == "y":
                                    J = 10
                                    I = int(input("Enter your next grade!   "))
                                    if I > 92.49:
                                        I = 4 
                                    elif I > 89.49:
                                        I = 3.67 
                                    elif I > 86.49:
                                        I = 3.33 
                                    elif I > 82.49:
                                        I = 3 
                                    elif I > 79.49:
                                        I = 2.67 
                                    elif I > 76.49:
                                        I = 2.33 
                                    elif I > 72.49:
                                        I = 2 
                                    elif I > 69.49:
                                        I = 1.67 
                                    elif I > 66.49:
                                        I = 1.33 
                                    elif I > 62.49:
                                        I = 1 
                                    elif I > 59.49:
                                        I = .67 
                                    else:
                                        I = .00 
elif After == "n":
    print("Thanks!")
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
if Printed >= 3.93:
    printed = TextAsset("Congratulations! Your GPA is within the top 10% of HHS students! Your GPA is {0}!".format(Printed), style="bold 15pt Times New Roman", width=10000000)
    Sprite(printed, (0, 0))
elif Printed >= 3.87:
    printed = TextAsset("Good Job! Your GPA is within the top 20% of HHS students. Your GPA is {0}.".format(Printed), style="bold 15pt Times New Roman", width=10000000)
    Sprite(printed, (0, 0))
elif Printed >= 3.8:
    printed = TextAsset("Fair. Your GPA is within the top 30% of HHS students. Your GPA is {0}.".format(Printed), style="bold 15pt Times New Roman", width=10000000)
    Sprite(printed, (0, 0))
elif Printed >= 3.68:
    printed = TextAsset("Alright... Your GPA is within the top 40% of HHS students. Your GPA is {0}.".format(Printed), style="bold 15pt Times New Roman", width=10000000)
    Sprite(printed, (0, 0))
elif Printed >= 3.58:
    printed = TextAsset("Okay... Your GPA is above the HHS average of 3.58. Your GPA is {0}!".format(Printed), style="bold 15pt Times New Roman", width=10000000)
    Sprite(printed, (0, 0))
elif Printed < 3.58:
    printed = TextAsset("Failure! Your GPA is below the HHS average of 3.58 - it's {0}!".format(Printed), style="bold 15pt Times New Roman", width=1000000000000)
    Sprite(printed, (0, 0))
myapp = App()
myapp.run()
