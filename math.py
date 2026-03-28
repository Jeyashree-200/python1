import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return 0
    else:
        return a/b
def mod(a,b):
    return a%b
def pow(a,b):
    return a**b
def square_root(a):
    return math.sqrt(a)
n1=int(input("enter a number"))
n2=int(input("enter another number"))
while(1):
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power\n7.Square\n8.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        print("Addition res:",add(n1,n2))
    elif ch==2:
        print("Subtraction res:",sub(n1,n2))
    elif ch==3:
        print("Multiplication res:",mul(n1,n2))
    elif ch==4:
        print("Division res:",div(n1,n2))
    elif ch==5:
        print("modulus res:",mod(n1,n2))
    elif ch==6:
        print("Power res:",pow(n1,n2))
    elif ch==7:
        print("Square root res:",square_root(n1))
    elif ch==8:
        print("Exit")
        break
    else:
        print("Invalid choice")
