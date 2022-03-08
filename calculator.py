#!/usr/bin/env python

#Python Calculator 
import sys
import math



#This defines a function as ADDITION
def add(n1, n2):
    return n1 + n2

#This defines a function as SUBTRACTION
def sub(n1, n2):
    return n1 - n2

#This defines a function as MULTIPLICATION
def mul(n1, n2):
    return n1 * n2

#This defines a function as DIVISION
def div(n1, n2):
    return n1 / n2

#This defines a function as SQUARE ROOT
def pwr(n1, n2):
    return n1 ** n2
def rad(deg):
    print(math.radians(deg))


print("welcome to multi-calcultor")

inf = 1
x = inf
while x == inf:
   
    fnct = ["+", "-", "*", "/", "**","sqrt","Ln","Log","rad","sin","cos","tan","asin","acos","atan"]
    print (fnct)
    select = input("Choose one of the calculation: ")
     
    if select == fnct[0]:
        num_1 = float(input("Enter the FIRST number: "))
        num_2 = float(input("Enter the SECOND number: "))
        print (add(num_1, num_2))

    elif select == fnct[1]:
        num_1 = float(input("Enter the FIRST number: "))
        num_2 = float(input("Enter the SECOND number: "))
        print (sub(num_1, num_2))

    elif select == fnct[2]:
        num_1 = float(input("Enter the FIRST number: "))
        num_2 = float(input("Enter the SECOND number: "))
        print (mul(num_1, num_2))

    elif select == fnct[3]:
        num_1 = float(input("Enter the FIRST number: "))
        num_2 = float(input("Enter the SECOND number: "))
        print (div(num_1, num_2))

    elif select == fnct[4]:
        num_1 = float(input("Enter the FIRST number: "))
        num_2 = float(input("Enter the SECOND number: "))
        print (pwr(num_1, num_2))
    
    elif select == fnct[5]:
        num = int(input("enter a number to take a square root: ")) 
        print(math.sqrt(num))
        
    elif select == fnct[6]:
        num = int(input("enter a number to take a natural log root: ")) 
        print(math.log(num))
        
    elif select == fnct[7]:
        num = int(input("enter a number to take a log base 10 root: ")) 
        print(math.log(num,10))
        
    elif select == fnct[8]:
        deg = float(input("enter degrees to convert to radians: "))
        rad(deg)
        
    elif select == fnct[9]:
        deg = float(input("enter the number for the trig function in degrees: "))
        print(math.sin(math.radians(deg)))

    elif select == fnct[10]:
        deg= float(input("enter the number for the trig function in degrees: "))
        print(math.cos(math.radians(deg)))
      
       
    elif select == fnct[11]:
        deg= float(input("enter the number for the trig function in degrees: "))
        print(math.tan(math.radians(deg)))
        
        
    elif select == fnct[12]:
        num= float(input("enter the number in the range of -1 to 1: "))
        option = str(input("how do you wamt the output enter deg for dgrees and rad for radians: ")).lower()
        if option == "rad":
            print(math.asin(num))
        else:
            print(math.degrees(math.asin(num)))
    
    elif select == fnct[13]:
        num= float(input("enter the number in the range of -1 to 1: "))
        option = str(input("how do you wamt the output enter deg for dgrees and rad for radians: ")).lower()
        if option == "rad":
            print(math.acos(num))
        else:
            print(math.degrees(math.acos(num)))
        
    elif select == fnct[14]:
      num= float(input("enter the number in the range of -1 to 1: "))
      option = str(input("how do you wamt the output enter deg for dgrees and rad for radians: ")).lower()
      if option == "rad":
          print(math.atan(num))
      else:
          print(math.degrees(math.atan(num)))
          
    else:
        print (f"Please select one of following: {fnct}")

    choice = str(input("Continue? y/n:")).lower()
    if choice == "n":
        print ("exit")
        break
    
    elif choice == "y":
        print ("return")
        continue
        
    else:
        print("not a valid response exiting program now")
        sys.exit()
