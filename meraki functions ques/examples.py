
def add_numbers(num1,num2):
    print("addition : ")
    print(num1+num2)

add_numbers(2,3)

def say_hello_people(name_x, name_y, name_z, name_a):

    print ("Namaste ", name_x) 

    print ("Alah hafiz ", name_y)

    print ("Bonjour ", name_z) 

    print ("Hello ", name_a)

say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")

say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")
# i got the desired output


def icecream(*flavours):

 for flavour in flavours:

  print("i love"+flavour)


icecream("chocolate", "butterscotch","vanilla","strawberry")
# i got the desired output

def attendance(name,status="absent"):

    print(name,"is",status," today")


attendance("kartik","present")

attendance("sonu")

attendance("vishal","present")

attendance("umesh")