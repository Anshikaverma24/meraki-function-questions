# PART 1

def calculator(number_x, number_y,operator):
    if operator == "add":
        calculation = number_x + number_y
    elif operator=="sub":
        calculation = number_x - number_y
    elif operator=="mul":
        calculation = number_x * number_y
    else:
        calculation = number_x / number_y
    return calculation


print(calculator([1,2,3],[4,3,7],"add"))

# # PART2

num1=int(input("enter first number"))
num2=int(input("enter second number"))
operator=input("enter the operator")
print(calculator(num1,num2,operator))

# PART3
def list_change(list1,list2):
    i=0
    while i<len(list1):
        j=0
        while j<len(list2):
            if i==j:
                print(list1[i]*list2[j])
            j+=1
        i+=1
(list_change([2,9,4],[2,3,4]))