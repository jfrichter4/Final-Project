"""
Put the credit and stuff here:
"""
print("Welcome to the Oversimplified GPA Calc!")
"""
Question = input("Is your GPA weighted or unweighted?")
Then = input("Okay - I understand. Enter your grades in this form: 100; 95; 33")
"""
J = 1
ForNow = input("Enter your first grade here. If you have an A, enter: A. If you have an A-, enter: A-. If you have a B+, enter B+.     ")
After = input("Type 'Y' if you have another grade and if not, type something else.    ")
if After == "Y":
    J = 2
    A = input("Enter your next grade!   ")
    Q = input("Type 'Y' if you have another grade and if not, type something else.    ")
    if Q == "Y":
        J = 3
        B = input("Enter your next grade!   ")
        Z = input("Type 'Y' if you have another grade and if not, type something else.    ")
        if Z == "Y":
            J = 4
            C = input("Enter your next grade!   ")
            Y = input("Type 'Y' if you have another grade and if not, type something else.    ")
            if Y == "Y":
                J = 5
                D = input("Enter your next grade!   ")
                X = input("Type 'Y' if you have another grade and if not, type something else.    ")
                if X == "Y":
                    J = 6
                    E = input("Enter your next grade!   ")
                    W = input("Type 'Y' if you have another grade and if not, type something else.    ")
                    if W == "Y":
                        J = 7
                        I = input("Enter your next grade!   ")
                        V = input("Type 'Y' if you have another grade and if not, type something else.    ")
                        if V == "Y":
                            J = 8
                            F = input("Enter your next grade!   ")
                            U = input("Type 'Y' if you have another grade and if not, type something else.    ")
                            if U == "Y":
                                J = 9
                                G = input("Enter your next grade!   ")
                                T = input("Type 'Y' if you have another grade and if not, type something else.    ")
                                if T == "Y":
                                    J = 10
                                    H = input("Enter your next grade!   ")
elif After == "N":
    print("Thanks!")
"""
Zip1 = zip((A:100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50)

Zip1 = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F+", "F", "F-", "U", "N/A")
Zip2 = (4, 4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, .67, .33, 0)
Zip3 = zip(Zip1, Zip2)

Total = sum("A", "B", "C", "D", "E", "F", "G", "H")
"""
Total = {"A+":4, "A":4, "A-":3.67, "B+":3.33, "B":3, "B-":2.67, "C+":2.33, "C":2, "C-":1.67, "D+":1.33, "D":1, "D-":0.67, "F+":0.33, "F":0, "F-":0, "U":0, "N/A":0}

Final = sum(Total)
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