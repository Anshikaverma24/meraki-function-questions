# Question 1

# eligible_for_vote name ka function likho jo ki user ko bataye ki vo (he/she) 
# vote de sakta hai ya nahi. ( Consider minimum age of voting to be 18. )
#  Example:- Agar user input me 18 se kam deta hai to “not eligible “ 
# print kare aur agar user 18 ya 18 se jyaada input kare to “you are eligible” print kare. 


def vote_eligibility(age):
    if age>18:
        print("you are eligible")
    else:
        print("not eligible ")

age=int(input("enter your age"))
vote_eligibility(age)
