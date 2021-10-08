# Question (Part 1)

# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare 
# "Dono even hain" agar dono numbers even (2 se divide hote hain) nahi toh print
#  kare "Dono numbers even nahi hai"



def check_numbers(n,m):
    if n%2==0 and m%2==0:
        print("Dono even hain")
    else:
        print("Dono numbers even nahi hai")


check_numbers(2,2)

# Question (Part 2)

# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments 
# ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi. 
# Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo. 
 


def check_numbers_list(list1,list2):
    i=0
    while i<len(list1):
        j=0
        while j<len(list2):
         if list1[i]==list2[j]:
             print(list1[i])
         j+=1
        i+=1
        

check_numbers_list([1,2,3],[2,3,4])