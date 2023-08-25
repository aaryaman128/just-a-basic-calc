import math

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b 
def product(a,b):
    return a*b
def divide(a,b):
    return a/b
def squareRoot(a):
    return math.sqrt(a)
def cubeRoot(a):
    return math.cbrt(a)

def menu():
    print("========== Welcome , What do you want to do today ? : ===============")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Square root")
    print("6.Cube root")
    print("=====================================================================")
menu()


    # Take input from the user

selection=input("Pick a number for selection : ")

print("=====================================================================")

if selection in ('1','2','3','4',):
    try:
        FirstNumber=float(input("Enter your first number of operation:"))
        SecondNumber=float(input("Enter your second number of operation:"))
    except :
        print("Invalid input , please enter a proper number again.. ")
            

if selection in ('1'):
    print(FirstNumber, "+", SecondNumber, "=", add(FirstNumber,SecondNumber))
       
if selection in ('2'):
    print(FirstNumber, "-", SecondNumber,"=",subtract(FirstNumber,SecondNumber))
      
if selection in ('3'):
    print(FirstNumber, "*" , SecondNumber, "=" ,product(FirstNumber,SecondNumber))
     
if selection in ('4'):
    print(FirstNumber, "Divided By " , SecondNumber, "=" ,divide(FirstNumber,SecondNumber))
    
if selection in ('5'):
    SquareNumber = float(input("Enter the Square , you want to find the root of : "))
    print("Square root of ", SquareNumber, "=" ,squareRoot(SquareNumber))
   
if selection in ('6'):
        CubeNumber=float(input("Enter the cube , you want to find the root of :"))
        print("Cube root of" , CubeNumber , "=" ,cubeRoot(CubeNumber))
    
 
