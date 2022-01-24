import os
# !/usr/bin/env python

# Python Calculator

# Available operators for inputting equations
fnct = ["+", "-", "*", "/", "**", "%", "//"]

# Contains the processing components for the calculator
while True:

    print(f"| Available operators: {fnct}\n")  # Prints list of operators
    in_equation = input("| Enter the equation: ")

    # Converts equation string to a mathematical expression, then solves it
    out_equation = eval(in_equation)
    print(f"\n > {out_equation}")

    # Keeps the terminal open. Allows reloading to enter more equations.
    close = input("\n| Press 'Enter' to reload. Input any key to terminate.\n")
    if close == "":
        os.system("cls")  # Clears the terminal log upon reloading
        continue
    else:
        quit()
