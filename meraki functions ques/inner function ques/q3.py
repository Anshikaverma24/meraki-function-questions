# Question 3

# Ek function banaiye jo 3 numbers ka sum aur average print kare.Hum user se 3 number
#  input karwayenge aur fir unn 3 numbers ka sum aur average print karwayenge 

def sum():
    num1=int(input("enter 1st no."))
    num2=int(input("enter 2nd no."))
    num3=int(input("enter 3rd no."))
    add=num1+num2+num3
    print (add)


sum()


def average():
    num1=int(input("enter 1st no."))
    num2=int(input("enter 2nd no."))
    num3=int(input("enter 3rd no."))
    avg=num1+num2+num3/3
    print(avg) 

average()