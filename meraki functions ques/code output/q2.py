def primeorNot(num):     

    if num > 1:

        for i in range(2,num):

            if (num % i) == 0:

                print(num,"is not a prime number")

                print(i,"times",num//i,"is",num)

                break

            else:

                print(num,"is a prime number")


    else:

           print(num,"is not a prime number")

primeorNot(406)

# O/P WILL BE:
# 406 is not a prime no.
# 2 times 203 is 406