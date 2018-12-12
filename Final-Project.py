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
if After == "y":
    J = 2
    A = int(input("Enter your next grade!   "))
    Q = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
    if Q == "y":
        J = 3
        B = input("Enter your next grade!   ").lower()
        Z = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
        if Z == "y":
            J = 4
            C = input("Enter your next grade!   ").lower()
            Y = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
            if Y == "y":
                J = 5
                D = input("Enter your next grade!   ").lower()
                X = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                if X == "y":
                    J = 6
                    E = input("Enter your next grade!   ").lower()
                    W = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                    if W == "y":
                        J = 7
                        I = input("Enter your next grade!   ").lower()
                        V = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                        if V == "y":
                            J = 8
                            F = input("Enter your next grade!   ").lower()
                            U = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                            if U == "y":
                                J = 9
                                G = input("Enter your next grade!   ").lower()
                                T = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
                                if T == "y":
                                    J = 10
                                    H = input("Enter your next grade!   ").lower()
elif After == "N":
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
Printed = Final/J
if Printed > 3.7:
    print("You are above average - your GPA is {0}!".format(Printed))
if Printed < 3.7:
    print("You are below average - your GPA is " + Printed + "!")

"""
Now, make a zip list compiling A:4,A-:3.67, etc,.
Then, have something with <Question> that makes the code know what weighted means and what unweighted means.
After, have something with <Then> that adds the numbers together and then divides them over how many grades there were.
Finally, have something with <After> that displays the GPA.
"""