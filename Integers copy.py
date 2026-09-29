print (""" Hello, in this code I will calculate integers for you.""")
print ("Let's get started")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
number1=float(input("What is your first number?"))
number2=float(input ("What is your second number?"))
type_= int(input ("""What is your operation?
1: Adding,
2: Subtracting,
3: Multiplying,
4: Divison.
Enter number the in front of choice"""))


if type_ ==1:
    print ("Your equation looks like this:")
    print (number1, '+', number2)
    print ('***********************************')
    print ('Adding')
    print ('Answer:')
    answer = (number1 + number2)
    print (answer)
elif type_ == 2:
    print ("Your equation looks like this:")
    print (number1, '-', number2)
    print ('***********************************')
    print ('Subtracting')
    print ('Answer:')
    answer = number1 - number2
    print (answer)
elif type_ == 3:
    print ("Your equation looks like this:")
    print (number1, '*', number2)
    print ('***********************************')
    print ('Multypling')
    print ('Answer:')
    answer = number1 * number2
    print (answer)
   
elif type_ == 4:
    print ("Your equation looks like this:")
    print (number1, '/', number2)
    print ('***********************************')
    print ('Dividing')
    print ('Answer:')
    answer = number1 / number2
    print (answer)
else:
    print ('Sorry, this was not one of the options. Please try again')

print ('Thank you for using my code. See you next time.')
