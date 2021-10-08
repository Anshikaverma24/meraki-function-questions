# # Question 1

# def greet(names):
#     for name in names:
#         print("Welcome", name)



# greet("Rinki", "Vishal", "Kartik", "Bijender")

# ANSWERS


def greet(names):
    for name in names:
        print("Welcome", names)



greet("Rinki")

# Question 2

# def info(name, age = ):
#    print(name + " is " + age + " years old")
# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

# ANSWER

def info(name, age ):
   print(name + " is " + age + " years old")
info("Sonu","16")
info("Sana", "17")
info("Umesh", "18")

# Question 3
# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop")

# ANSWER

def studentDetails(name,currentMilestone,mentorName):

    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)



studentDetails("Nilam","loop","sakshi")