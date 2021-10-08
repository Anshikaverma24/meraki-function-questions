# Question 7

# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski
# length jyaada hogi use print karega aur agar dono strings ki length equal hui to 
# dono ko line by line print karega

def check(m,n):
    if len(m)>len(n):
        print(m)
    elif len(n)>len(m):
        print(n)
    elif len(m)==len(n):
        print(m,n)

string1=input("enter any string : ")
string2=input("enter any string : ")
check(string1,string2)