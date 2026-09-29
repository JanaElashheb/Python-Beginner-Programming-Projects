#for statement 
print ("""Hello,
in this code I will find out all the even and odd number from 1-10.
Then I will give you the sum of all the even number and the sum of all odd numbers.
Then I will give you all the prime numbers.""")
print ("By: Jana")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("       ~Eevn & Odd numbers~     ")
test =(input("Insert your number here. It has to be a number form 1-10"))
for d in test:
    if d == "1":
        print ("This is an odd number")
    elif d == "2":
        print ("This is an even number")
    elif d == "3":
        print ("This is an odd number")
    elif d == "4":
        print ("This is an even number")
    elif d == "5":
        print ("This is an odd number")
    elif d == "6":
        print ("This is an even number")
    elif d == "7":
        print ("This is an odd number")
    elif d == "8":
        print ("This is an even number")
    elif d == "9":
        print ("This is an odd number")
    elif d == "10":
        print ("This is an even number")
    print (d)
print ("     ")
print ("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print ("          ~Sum of even numbers 1-10     ")
sum_even = (2+4+6+8+10)
print ("Now I will give you the sum of all the even numbers in between 1 and 10")
print ("The sum is of even numbers is ", sum_even)
print ("        ")
print ("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("                ~Sum of odd numbers 1-10                                                   ")
odd_sum = (1+3+5+7+9)
print ("Now I will give you the sum of all the odd numbers in between 1 and 10")
print ("The sum of odd numbers is ", odd_sum)
print ("        ")
print ("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print ("                    ~Prime numbers~    ")
print ("Now I will give you all the prime numbers from 1-10")
test2= ["1" ,"2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]
for f in test2:
    if f == "1":
        continue
    elif f == "2":
        print ("2 is a prime number")
    elif f == "3":
        print ("3 is a prime number")
    elif f == "4":
        continue
    elif f == "5":
        print ("5 is a prime number")
    elif f == "6":
        continue
    elif f == "7":
        print ("7 is a prime number")
    elif f == "8":
        break
