# Question 2

# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter
#  ko hume check karana hai ki vo perfect number hain ya nahi. Iske baad uss function ko 
# use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers ko print kare.
# [ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi factors ( including 
# 1 & excluding itself) ka sum uss number ke barabar hota hai. 

def perfect(m):
    # num=int(input("enter any number"))
    sum=0
    i=1
    while i<m:
     if m%i==0:
      sum=sum+i
     i+=1
    if m==sum:
     print(m,"perfect no.")
    else:
     print(m,"is not a perfect no.")


# perfect()

i=1
while i<=1000:
    perfect(i)
    i+=1