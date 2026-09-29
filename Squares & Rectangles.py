print ("Hello,")
print ("""In this code I can calculate squares and rectangles. I can find the area and
perimeter of both squares and rectangles. I can also find surface area and
volume of cubes and rectangular prisms.""")
print ("Let's get started!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
        l=float(input("What is yoru lenght?"))
        w=float(input("What is your width?"))
        h=float(input("What is your height?"))
        messuerment=str(input("What is your unite of messerment?"))
        Answer_volume_rec=l*w*h
        print (Answer_volume_rec,messuerment,3)
    else:
        print ("................................")
        print ("Sorry, this was not an option. Please try again.")
else:
    print ("................................")
    print ("Sorry, this was not an option. Please try again.")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Thank you for using my code. Bye!")

        

    
