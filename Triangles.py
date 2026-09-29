print ("""Hello, in this code I will find triangle properties for you. I can also
calculate triangular prism's.""")
print ("Let's get started!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Thank you for using my code! Bye!")
