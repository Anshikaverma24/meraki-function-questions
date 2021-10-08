# Question 4

# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter lega aur
#  0 se limit tak ke beech ke sabhi even aur odd numbers ko label ke saath print karega.


def shownumber(limit):
    i=0
    while i <=limit:
        if i%2==0:
            print("EVEN NUMBER : ", i)
        else:
            print("ODD NUMBER : ", i)
        i+=1

shownumber(20)