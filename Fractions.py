print ("""Hello,today I will be calculating fractions. I can
turn decimals or percents to fractions. I can also add,
subtract, multiply and divide fractions. I can also turn
mixed number to improper fraction and the other way around.""")
print ("Let's get started!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Choice=int(input("""What do you want to do? Do you want, 1 to turn fractions
to percents or decimals,or 2 do you want to add, subtract, multiply and
divide fractions, or 3 turn mixed numbers to improper fractions and the
other way around? Please enter the number in front of the choice:""")) 
if Choice ==1:
    print ("......................................")
    print ("You are converting fractions to percents or dceimals:")
    print ("::::::::::::::::::::::::::::::::::::")
    choice=int(input("""Do you want to, 1 turn fractions to percents or
2  turn fractions to decimals? Please enter the number in front of the choice:"""))
    if choice == 1:
        print ("......................................")
        print ("You are turning fractions to percents:")
        top=int(input("What is your numeratore?:"))
        bottom=int(input("What is your denominatore?:"))
        decimal_number = top / bottom
        answer = decimal_number * 100
        print ("Your fraction is " ,top, '/', bottom)
        print ("The percent of it is:")
        print (answer, '%')
    elif choice == 2:
        print ("......................................")
        print ("You are turning fractions to decimals:")
        top=int(input("What is your numeratore?:"))
        bottom=int(input("What is your denominatore?:"))
        answer = top / bottom
        print ("Your fraction is " ,top, '/', bottom)
        print ("The decimal number of it is:")
        print (answer)
    else:
        print ("Sorry, this was not an option. Please try again")
elif Choice ==2:    
    print ("......................................")
    print ("You are adding, subtracting, multiplying or dividing fractions:")
    print ("::::::::::::::::::::::::::::::::::::")
    operation=int(input("""What is your opperation?  1 for adding, 2 for subtraction,
3 for multiplication, 4 for division. Please enter the number in front
of the choice:"""))
    print ("......................................")
    print ("This will be answers for first fraction:")
    numerator_1=int(input("What is your numeratore?:"))
    denominatore_1=int(input("What is your denominatore?:"))
    print ("......................................")
    print ("This will be answers for the second fraction:")
    numerator_2=int(input("What is your numeratore?:"))
    denominatore_2=int(input("What is your denominatore?:"))
    if operation ==1:
        if denominatore_1==denominatore_2:
            print ("~Solving fraction~:")
            final_deno=denominatore_1
            final_numerator=numerator_1+numerator_2
            print (Answer,'/',final_deno)
        elif denominatore_1 != denominatore_2:
            print ("~Solving fraction~:")
            final_deno = denominatore_1 * denominatore_2
            fraction_1 = denominatore_1 * numerator_2
            frcation_2 = denominatore_2 * numerator_1
            Answer = fraction_1 + frcation_2
            print (Answer,'/',final_deno)
    elif operation ==2:
        if denominatore_1==denominatore_2:
            print ("~Solving fraction~:")
            final_deno=denominatore_1
            final_numerator=numerator_1-numerator_2
            print (Answer,'/',final_deno)                
        elif denominatore_1 != denominatore_2:
            print ("~Solving fraction~:")
            final_deno = denominatore_1 * denominatore_2
            fraction_1 = denominatore_2 * numerator_1
            fraction_2 = denominatore_1 * numerator_2
            Answer = fraction_1 - fraction_2
            print (Answer,'/',final_deno)
    elif operation ==3:
         print ("~Solving fraction~:")
         final_deno= denominatore_1 * denominatore_2
         final_numo= numerator_1 * numerator_2
         print (final_numo, '/',final_deno)
    elif operation ==4:
        print ("~Solving fraction~:")
        numerator_2_0_2 = denominatore_2
        denomenatore_2_0_2 = numerator_2
        final_deno = denominatore_1 * denomenatore_2_0_2
        final_numo = numerator_1 * numerator_2_0_2
        print (final_numo,'/',final_deno)
    else:
        print ("Sorry, this was not an option. Please try again")
elif Choice ==3:
    print ("......................................")
    type_=int(input("""Do you want to, 1 change mixed number to improper fration
or 2 change improper fraction to mixed number? Please enter the number in
front of the choice:"""))
    if type_ ==1:
        print ("::::::::::::::::::::::::::::::::::::::::")
        print ("You are changing mixed number to improper fraction")
        print ("~Solving~")
        whole_number=int(input("What is your whole number?:"))
        numeratore=int(input("What is your numerator?:"))
        denominator=int(input("What is your denominator?:"))
        part1= denominator * whole_number
        part2= part1 + numeratore
        print (part2)
    elif type_ ==2:
        print ("::::::::::::::::::::::::::::::::::::::::")
        print ("You are changing improper fraction to mixed number")
        print ("~Solving~")
        numerator=int(input("What is your numerator?:"))
        denominator=int(input("What is your denominator?:"))
        reg_div=numerator/denominator
        div_rem=numerator%denominator
        print (reg_div, ',' , div_rem, '/',denominator)
        print ("(",reg_div,")", "Is the whole number. And ",div_rem,"/",denominator ,"Is the fraction")
    else:
        ("Sorry, this was not an option. Please try again")
else:
    print ("Sorry, this was not an option. Please try again")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Thank you for using my code! Bye!")
