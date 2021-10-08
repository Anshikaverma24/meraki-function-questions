# Question 1 (Part 1)

# ask_question naam ka Ek function likhiye jo yeh text ko "ek baar" print kare.
#  Fir iss function ko 5 baar call kar ke yeh text 5 baar print karvao.

# Question 1 (Part 2)

# Fir while loop ka use kar ke iss function ko 100 baar call karne ka code likho. 


def ask_question():
    print("ek bar")

# PART 1
ask_question()
ask_question()
ask_question()
ask_question()
ask_question()

# OR
i=1
while i<=5:
    ask_question()
    i+=1

#  PART 2

i=1
while i<=100:
 ask_question()
 i+=1