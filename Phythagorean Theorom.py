import math 
print ("Hello, in this code I will claculate the Pythagorean theorem.")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
    
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Thank you for using my code! See you next time!")
