print ("Hello, in this code I can calculate cicle properties for you. I can also calculate surface area and volume of a cylindre.")
print ("Let's get started!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
elif Number != 1 or 2 or 3 or 4 or 5 or 6:
    print ("Sorry, This is not one of the options")
else:
    print ("Sorry, This is not one of the options")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("""Thank you for using my code! I hope that this helped you. Bye!""")
        
    


        







        
