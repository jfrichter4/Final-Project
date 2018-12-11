"""
Put the credit and stuff here:
"""
print("Welcome to the Oversimplified GPA Calc!")
"""
Question = input("Is your GPA weighted or unweighted?")
Then = input("Okay - I understand. Enter your grades in this form: 100; 95; 33")
"""
J = 1
ForNow = input("Enter your first grade here. Follow this guide to know what each grade equates to: ").lower()
After = input("Type 'Y' if you have another grade and if not, type something else.    ").lower()
if After == "y":
    J = 2
    A = input("Enter your next grade!   ").lower()
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
if ForNow ==... :
    Final = sum(ForNow)
    if A == True:
        Final = sum(ForNow, A)
        if B == True:
            Final = sum(ForNow, A, B)
            if C == True:
                Final = sum(ForNow, A, B, C)
                if D == True:
                    Final = sum(ForNow, A, B, C, D)
                    if E == True:
                        Final = sum(ForNow, A, B, C, D, E)
                        if F == True:
                            Final = sum(ForNow, A, B, C, D, E, F)
                            if G == True:
                                Final = sum(ForNow, A, B, C, D, E, F)
                                if H == True:
                                    Final = sum(ForNow, A, B, C, D, E, F, G, H)
Printed = Final/J
if Final > 3.7:
    print("You are above average - your GPA is " + Printed + "!")
if Final < 3.7:
    print("You are below average - your GPA is " + Printed + "!")

"""
Now, make a zip list compiling A:4,A-:3.67, etc,.
Then, have something with <Question> that makes the code know what weighted means and what unweighted means.
After, have something with <Then> that adds the numbers together and then divides them over how many grades there were.
Finally, have something with <After> that displays the GPA.
"""