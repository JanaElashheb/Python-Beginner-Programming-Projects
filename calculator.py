import math
operation=int(input('''What do you want to do?
1) Add
2) Subtracte
3) Multiply
4) Divide
5) Square root
6) Exponent
Please enter the number in front of the choice.
Enter number here:'''))
if operation == 1:
    print (':::::::::::::::::::::::::::::::::::::::')
    x=float(input("Insert your frist number here"))
    y=float(input("Insert your seconde number here"))
    answer=x+y
    print ('Your answer is ',answer)
elif operation == 2:
    print (':::::::::::::::::::::::::::::::::::::::')
    x=float(input("Insert your frist number here"))
    y=float(input("Insert your seconde number here"))
    answer=x-y
    print ('Your answer is ', answer)
elif operation == 3:
    print (':::::::::::::::::::::::::::::::::::::::')
    x=float(input("Insert your frist number here"))
    y=float(input("Insert your seconde number here"))
    answer=x*y
    print ('Your answer is ', answer)
elif operation == 4:
    print (':::::::::::::::::::::::::::::::::::::::')
    x=float(input("Insert your frist number here"))
    y=float(input("Insert your seconde number here"))
    answer=x/y
    print ('Your answer is ', answer)
elif operation ==5:
    print (':::::::::::::::::::::::::::::::::::::::')
    x=float(input("Number you want to squart root:"))
    answer = math.sqrt (x)
    print ('Your answer is', answer)
elif operation ==6:
    print (':::::::::::::::::::::::::::::::::::::::')
    x=float(input("Number:"))
    y=float(input('What is your exponenet?') 
    answer = x**y
    print ('Your answer is ' , answer)
else:
    print ("Sorry, this was not an option. Please try again")
