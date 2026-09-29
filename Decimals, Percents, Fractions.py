choice=int(input('''What do you want to do?
Do you want to:
1. turn decimals to percents
2. turn decimals to fractions
3. turn fractions to decimals
4. turn fractions to percents
5. turn percents to frations
6. turn percents to decimlas.
Please enter the number.
Enter answer here:'''))

if choice == 1:
    print ('........................')
    decimal=float(input('''What is your decimal?
Enter answer here:'''))
    answer = decimal * 100
    print ('Your answer is :')
    print (answer)
elif choice == 2:
    print ('........................')
    decimal=float(input('''What is your decimal?
Enter answer here:'''))
    
elif choice == 3:
    print ('........................')
    fraction_top = float(input("""What is your numerator?
Enter number here:"""))
    fraction_bottom=float(input("""What is your denominatore?
Enter number here:"""))
    answer=fraction_top / fraction_bottom
    print ('''Your answer is''' , answer)
elif choice == 4:
    print ('........................')
    fraction_top = float(input("""What is your numerator?
Enter number here:"""))
    fraction_bottom=float(input("""What is your denominatore?
Enter number here:"""))
    part_1 =fraction_top / fraction_bottom
    answer = part_1 * 100
    print ('''Your answer is''' , answer)
elif choice == 5:
    print ('........................')
    percent = float(input("What is your percent. No percent symbole."))
    part_1 = percent / 100
    part_2 = 
    
    
    
