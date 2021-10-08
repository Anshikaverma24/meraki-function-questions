# Question 3 (Part 1)

# Apko students naam ka ek function define karna hai or uss function mai list of students 
# name as a parameter pass karna hai(List ka use nahi karna hai)
# Question 3 (Part 2)

# Apko isGreaterThen20 naam ka function define karna hai jismai apko
#  function mai do parameter pass karane hai or first parameter by default 20 hi hona chahiye.

def students(*name):
    for name in name:
        print(name)

students("ansh","vish","shivi")

def isGreaterThen20(a=20,b=0):
    c=a-b
    print(c)

isGreaterThen20()