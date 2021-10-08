# Question 5

# Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke beech
#  ke number jo ki 3 aur 5 ke multiples hain unka sum print karega.

def multiple(limit):
    sum=0
    i=0
    while i<=limit:
        if i%3==0 and i%5==0:
            sum=sum+i
            print(sum)
        i+=1

multiple(30)
