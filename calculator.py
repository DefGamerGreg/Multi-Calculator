#!/usr/bin/env python

#Python Calculator 

#This defines a function as ADDITION
def add(n1, n2):
    return num_1 + num_2

#This defines a function as SUBTRACTION
def sub(n1, n2):
    return num_1 - num_2

#This defines a function as MULTIPLICATION
def mul(n1, n2):
    return num_1 * num_2

#This defines a function as DIVISION
def div(n1, n2):
    return num_1 / num_2

#This defines a function as SQUARE ROOT
def sqrt(n1, n2):
    return num_1 ** num_2


inf = 1
x = inf
while x == inf:

    num_1 = float(input("Enter the FIRST number: "))
    num_2 = float(input("Enter the SECOND number: "))

    fnct = ["+", "-", "*", "/", "**"]
    print ("+", "-", "*", "/", "**")
    selct = input("Choose one of the calculation: ")

    if selct == fnct[0]:
        print (add(num_1, num_2))

    elif selct == fnct[1]:
        print (sub(num_1, num_2))

    elif selct == fnct[2]:
        print (mul(num_1, num_2))

    elif selct == fnct[3]:
        print (div(num_1, num_2))

    elif selct == fnct[4]:
        print (div(num_1, num_2))

    else:
        print ("Please select one ""+", "-", "*", "/", "**""calculation variable!")

    input = str(input("Continue? y/n:")).lower()
    if input == "n":
        print ("exit")
        break
    
    elif ip == "y":
        print ("return")
        continue
        
    else:
    	quit()
