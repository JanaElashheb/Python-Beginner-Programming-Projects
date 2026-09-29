import math
print ('''Hello, in this code you can find differnet math properties calculator.
I have made many diffrent claculators for different properties anss now I am
putting it all in one code. I hope you find this code usefull. Bye!''')
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#STILL WORKING ON CODE FOR DECIMALS, PERCENTS, FRACTIONS
Math_Propertie = int(input('''Math properties:
1) Cartesian Coordinate System:
  - In this code you enter your x number and y number and it will tell you in
  witch quadrant it belongs in
2) Calculator:
  - In this code you can add, subtract, divide, multiply, find square root of
  a number and use exponenets
3) Circles:
  - In this code it can calculate different circle properties. It can calculate
  Diameter, Radius, Circumference, Area, Surface Area of cylinder, Volume of
  cylinder
4) Phythagorean Theorom:
  - In this code it can do the Phythagorean Theorom. It can solve for the C, A,
  and B side
5) Squares and Rectangles:
  -  In this code it can calculate the area and perimeter of both squares and
  rectangles. It can also find the surface area and volume of both cubes and
  rectangular prisims
6) Fractions:
  - In this code it can add, subtracte, multiply and divide fractions. It can
  also turn decimals and percents to fractions. Be aware that it can not turn
  fractions to decimals or percents. There is another section for that.You can
  do that on section 8. This code can also turn misied numbers to impoper
  fractions and the other way around
7) Integers:
  - In this code it can add, subtracte, multiply and divide integers.
8) Decimals, Percents, Fractions:
  - In this code it can convert between all three.
9) Triangles:
  - In this code it can find the area of a circle and find the surface area and
  volume of a triangular prisim.
Please enter the number in front of the section you want.
Enter number here: '''))
if Math_Propertie == 1:
    print ('::::::::::::::::::::::::::::::::')
    x=int(input("Please enter your x number"))
    y=int(input("Please enter your y number"))
    if x > 0:
        if y > 0:
          print("This belongs in Quadrant_I")
    if x < 0:
        if y > 0:
            print ("This belongs in Quadrant_II")
    if x < 0:
        if y < 0:
            print ("This belongs in Quadrant_III")
    if x > 0:
        if y < 0:
            print ("This belongs in Quadrant_IV")
    if x == 0:
        if y == 0:
            print ("This in the center point")
    if x > 0:
        if y == 0:
            print ("This is on the positive x axis")
    if x == 0:
        if y > 0:
            print ("This is on the positive y axis")
    if x < 0:
        if y == 0:
            print ("This is on the negative x axis")
    if x == 0:
        if y < 0:
            print ("This is on the negative y axis")
elif Math_Propertie == 2:
    print ('::::::::::::::::::::::::::::::::')
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
        y=float(input('What is your exponenet?')) 
        answer = x**y
        print ('Your answer is ' , answer)
    else:
        print ("Sorry, this was not an option. Please try again")
elif Math_Propertie == 3:
    print ('::::::::::::::::::::::::::::::::')
    Number=int(input("Do you want to look for, 1 radius, 2 diameter, 3 circumference, 4 area, 5 surface area or 6 volume? Please enter the number in front of the choice."))
#1 is radius
    if Number== 1:
        print ("You are looking for radius.")
        Choice_R =int(input("Do you want to find radius with, 1 dimater or 2 circumference? Please enter the number in front of the choice."))
    #1 == diameter
        if Choice_R ==1:
            choice_radius_diameter=float(input("What is your diameter?")) 
            Answer_radius_diameter=choice_radius_diameter/2
            print (Answer_radius_diameter)
        elif Choice_R ==2:
            choice_radius_circumference=float(input("What is your circumference?"))
            Answer_radius_circumference=choice_radius_circumference/2
            Answer_radius_circumference_2=Answer_radius_circumference*3.14
            print (Answer_radius_circumference_2)
        else:
            print ("Sorry, this is not one of the options")
    elif Number== 2:
        print ("You are looking for diameter")
        Choice_D= int(input("Do you want to find diameter with, 1 radius or 2 circumference? Please enter the number in front of the choice."))
        if Choice_D ==1:
            choice_diameter_radius=float(input("What is your radius?"))
            Answer_diameter_radius=choice_diameter_radius*2
            print (Answer_diameter_radius)
        elif Choice_D ==2:
            choice_diameter_circumference=float(input("What is your circumference?"))
            Answer_diameter_circumference=choice_diameter_circumference/3.14
            print(Answer_diameter_circumference)
        else:
            print ("Sorry, this is not one of the options")
    elif Number== 3:
        print ("You are looking for circumference.")
        Choice_C =int(input("Do you want to find circumference with, 1 radius, 2 diameter? Please enter the number in front of the choice."))
        if Choice_C ==1:
            choice_circumference_radius=float(input("What is your radius?"))
            Answer_circumference_radius=choice_circumference_radius*2*3.14
            print (Answer_circumference_radius)
        elif Choice_C ==2:
            choice_circumference_diameter=float(input("What is your diameter?"))
            Answer_circumference_diameter=choice_circumference_diameter*3.14
            print (Answer_circumference_diameter)
        else:
            print ("Sorry, this is not one of the options")
    elif Number== 4:
        print ("You are looking for area")
        Choice_A =int(input("Do you want to find arae with, 1 radius, 2 diameter or 3 circumference? Please enter the number in front of the choice."))
        if Choice_A ==1:
            choice_area_radius=float(input("What is your radius?"))
            Answer_area_radius=choice_area_radius*choice_area_radius*3.14
            print (Answer_area_radius)
        elif Choice_A ==2:
            choice_area_diameter=float(input("What is your diameter?"))
            Answer_area_diameter=0.25*choice_area_diameter*choice_area_diameter*3.14
            print (Answer_area_diameter)
        elif Choice_A ==3:
            choice_area_circumference=float(input("What is your circumference?"))
            Answer_area_circumference=choice_area_circumference*choice_area_circumference/12.56
            print (Answer_area_circumference)
        else:
            print ("Sorry, this is not one of the options")
    elif Number== 5:
        print ("You are looking for surface area.")
        Choice_SA =int(input("Do you want to find surface area with, 1 radius or 2 diameter? Please enter the number in front of the choice."))
        if Choice_SA ==1:
            choice_sa_radius=float(input("What is your radius?"))
            choice_sa_radius_height=float(input("What is your cylinders height."))
            Answer_sa_radius=2*3.14*choice_sa_radius*choice_sa_radius_height+2*3.14*choice_sa_radius*choice_sa_radius
            print (Answer_sa_radius)
        elif Choice_SA ==2:
            choice_sa_diameter=float(input("What is you diameter?"))
            choice_sa_diameter_height=float(input("What is your height?"))
            Answer_sa_diameter_D=choice_sa_diameter/2
            Answer_sa_diameter=2*3.14*Answer_sa_diameter_D*choice_sa_diameter_height+2*3.14*Answer_sa_diameter_D*Answer_sa_diameter_D
            print (Answer_sa_diameter)
        else:
            print ("Sorry, this is not one of the options")
    elif Number== 6:
        print ("You are looking for volume.")
        Choice_V=int(input("Do you want to find the volume with, 1 radius or 2 dimater? Please enter the number in front of the choice."))
        if Choice_V ==1:
            choice_volume_radius=float(input("What is your radius?"))
            choice_volume_radius_height=float(input("What is your height?"))
            Answer_volume_radius=choice_volume_radius*choice_volume_radius*3.14*choice_volume_radius_height
            print (Answer_volume_radius)
        elif Choice_V ==2:
            choice_volume_diameter=float(input("What is your diameter?"))
            choice_volume_diameter_height=float(input("What is your height?"))
            Answer_volume_diameter_D=choice_volume_diameter/2
            Answer_volume_diameter=Answer_volume_diameter_D*Answer_volume_diameter_D*3.14*choice_volume_diameter_height
            print (Answer_volume_diameter)
        else:
            print ("Sorry, this is not one of the options")
elif Math_Propertie == 4:
    print ('::::::::::::::::::::::::::::::::')
    Number=int(input("Are you looking for, 1 C side, 2 A side or 3 B side? Please wright the number in front of the choice"))
    if Number ==1:
        print ("You are looking for C.")
        A_side_C=float(input("What is your A side length?"))
        B_side_C=float(input("What is your B side length?"))
        C_Unite=str(input("What is your unite of measurement?"))
        A_squared_C=A_side_C*A_side_C
        B_squared_C=B_side_C*B_side_C
        C_squared=A_squared_C+B_squared_C
        Answer_C_side= math.sqrt (C_squared)
        print (Answer_C_side,C_Unite)   
    elif Number ==2:
        print ("You are looking for A")
        C_side_A=float(input("What is your C side length?"))
        B_side_A=float(input("What is your B side length?"))
        A_Unite=str(input("What is your unite of measurement?"))
        if B_side_A > C_side_A:
            print ("Sorry, your B side has to be shorter then your C side.")
        elif B_side_A == C_side_A:
            print ("Sorry, your B side has to be shorter then your C side.")
        elif C_side_A > B_side_A:
            C_squared_A= C_side_A**2
            B_squared_A= B_side_A**2
            A_squared_A= C_squared_A - B_squared_A
            Answer_A_side= math.sqrt (A_squared_A)
            print (Answer_A_side,A_Unite)
    elif Number ==3:
        print ("You are looking for B")
        C_side_B=float(input("What is your C side length?"))
        A_side_B=float(input("What is your A side length?"))
        B_unite=str(input("What is your unite of measurement."))
        if A_side_B > C_side_B:
            print ("Sorry, your A side has to be shorter then your C side.")
        elif A_side_B == C_side_B:
            print ("Sorry, your A side has to be shorter then your C side.")
        elif C_side_B > A_side_B:
            C_squared_B=C_side_B**2
            A_squared_B=A_side_B**2
            B_squared_B=C_squared_B-A_squared_B
            Answer_B_side= math.sqrt (B_squared_B)
            print (Answer_B_side,B_unite)
    else:   
        print ("Sorry, this is not one of the options. Please try again.")
elif Math_Propertie == 5:
    print ('::::::::::::::::::::::::::::::::')
    Option=int(input("""Do you want to work with, 1 squares or 2 rectagles?
Please enter the number in front of the choice."""))
    if Option ==1:
        print ("====================================")
        print ("You are working with squares.")
        Operation=int(input("""Do you want to look for, 1 area, 2 perimeter, 3 surface area or 4 volume.
Please enter the number in front of the choice."""))
        if Operation ==1:
            print ("................................")
            print ("You are finding area.")
            side_lenght_area_square=float(input("What is your side lenght?"))
            messurement_area_square=str(input("What is your unite of messuerment?"))
            Answer_area_square=side_lenght_area_square**2
            print (Answer_area_square,messurement_area_square,2)
        elif Operation==2:
            print("................................")
            print ("You are finding perimeter.")
            side_lenght_square=float(input("What is your side lenght?"))
            messurement_perimeter_square=str(input("What is your unite or messurment?"))
            Answer_perimeter_square=side_lenght_square*4
            print (Answer_perimeter_square,messurement_perimeter_square)
        elif Operation ==3:
            print ("You are finding surface area.")
            side_lenght_sa=float(input("What is your side lenght?"))
            messurment_sa_square=str(input("What is your unite of messurment?"))
            Answer_sa_square=side_lenght_sa**2*6
            print (Answer_sa_square,messurment_sa_square,2)
        elif Operation ==4:
            print("................................")
            print ("You are finding volume.")
            side_lenght_volume_square=float(input("What is your side lenght?"))
            messurment_volume_square=str(input("What is your unite of messurment."))
            Answer_volume_square=side_lenght_volume_square**3
            print (Answer_volume_square,messurment_volume_square,3)
        else:
            print("................................")
            print ("Sorry, this was not an option. Please try again.")
    elif Option ==2:
        print ("====================================")
        print ("You are working with rectangles.")
        Operation_2=int(input("""Do you want to look for, 1 area, 2 perimeter, 3 surface area or 4 volume.
Please enter the number in front of the choice."""))
        if Operation_2 ==1:
            print ("................................")
            print ("You are looking for area.")
            l=float(input("What is your lenght?"))
            w=float(input("What is your width?"))
            messurement_area_rec=str(input("What is your unite of messurment?"))
            Answer_area_rec=l*w
            print (Answer_area_rec,messurement_area_rec,2)
        elif Operation_2 ==2:
            print ("................................")
            print ("You are looking for perimeter.")
            l=float(input("What is your lenght?"))
            w=float(input("What is your width?"))
            messurment_perimeter_rec=str(input("What is your unite of messurement?"))
            Answer_perimeter_rec=(l+w)*2
            print (Answer_perimeter_rec,messurment_perimeter_rec)
        elif Operation_2 ==3:
            print ("................................")
            print ("You are looking for surface area.")
            l=float(input("What is your lenght?"))
            w=float(input("What is your width?"))
            h=float(input("What is your height?"))
            messerment=str(input("What is your messurment?"))
            Answer_sa_rec=(w*l+h*l+h*w)*2
            print (Answer_sa_rec,messerment,2)
        elif Operation_2 ==4:
            print ("................................")
            print ("You are looking for volume.")
            l=float(input("What is your lenght?"))
            w=float(input("What is your width?"))
            h=float(input("What is your height?"))
            messuerment=str(input("What is your unite of messerment?"))
            Answer_volume_rec=l*w*h
            print (Answer_volume_rec,messuerment,3)
        else:
            print ("................................")
            print ("Sorry, this was not an option. Please try again.")
elif Math_Propertie == 6:
    print ('::::::::::::::::::::::::::::::::')
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
            print ("Sorry, this was not an option. Please try again")
    else:
        print ("Sorry, this was not an option. Please try again")
elif Math_Propertie == 7:
    print ('::::::::::::::::::::::::::::::::')
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
elif Math_Propertie == 8:
    print ('::::::::::::::::::::::::::::::::')
    #STILL WORKING ON CODE
elif Math_Propertie == 9:
    print ('::::::::::::::::::::::::::::::::')
    Option=int(input("""What do you want to find? 1 area, 2 surface area,3 volume.
Please enter the number in front of the choice:"""))
    if Option ==1:
        print (".............................")
        print ("You are looking for area.")
        b=float(input("What is your triangles base?:"))
        h=float(input("What is your trangles height?:"))
        messeurement=str(input("What is your unite of messurment?:"))
        Answer=(b*h)/2
        print (Answer,messeurement,2)
    elif Option ==2:
        print (".............................")
        print ("You are looking for surface area")
        type_=int(input("""Witch kind of triangle do you have? 1 equlateral,
2 issosolies, 3 scalean or 4 right angle triangle? Please enter
the number in front of the choice:"""))
        if type_ ==1:
            print ("======================")
            print ("Type of triangel: Equlateral")
            b=float(input("What is your triangle's base?:"))
            h=float(input("What is your triangle's height?:"))
            l=float(input("What is your prism's lenght?:"))
            messuerment=str(input("What is your unite of messuerment?:"))
            Answer=(b*h)+(b*l)+(b*l)+(b*l)
            print (Answer,messuerment,2)
        elif type_ ==2:
            print ("======================")
            print ("Type of trinangle: Issosolies")
            b=float(input("What is your triangle's base?:"))
            h=float(input("What is your triangle's height?:"))
            l=float(input("What is your prism's lenght?:"))
            x=float(input("What is the other side lenght of your triangle? Not the base.:"))
            messuerment=str(input("What is your unite of messuerment?:"))
            Answer=(b*h)+(b*l)+(x*l)+(x*l)
            print (Answer,messuerment,2)
        elif type_ ==3:
            print ("======================")
            print ("Type of trinangle: Scalean")
            b=float(input("What is your triangle's base?"))
            h=float(input("What is your triangle's height?"))
            l=float(input("What is your prism's lenght?"))
            x=float(input("What is the other side lenght of your triangle? Not the base."))
            y=float(input("What is your last triangles side lenght?"))
            messuerment=str(input("What is your unite of messuerment?"))
            Answer=(b*h)+(b*l)+(x*l)+(y*l)
            print (Answer,messuerment,2)
        elif type_ ==4:
            print ("======================")
            print ("Type of trinangle: Right angle triangle")
            b=float(input("What is your triangle's base?:"))
            h=float(input("What is your triangle's height?:"))
            l=float(input("What is your prism's lenght?:"))
            x=float(input("What is the other side lenght of your triangle? Not the base or height."))
            messuerment=str(input("What is your unite of messuerment?:"))
            Answer=(b*h)+(b*l)+(x*l)+(h*l)
            print (Answer,messuerment,2)
        else:
            print ("Sorry, this was not an option. Please try again.")
    elif Option ==3:
        print (".............................")
        print ("You are looking for volume")
        b=float(input("What is your triangle's base?:"))
        h=float(input("What is your triangle's height?:"))
        l=float(input("What is your prism's lenght?:"))
        messerment=str(input("What is your unite of messurment?:"))
        Answer=(b*h)/2*l
        print (Answer,messerment,3)
    else:
        print ("Sorry, this was not an option. Please try again.")
else:
    print ("Sorry,this was not an option. Please try again")ii
