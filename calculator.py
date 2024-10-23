while True:
    b=[4,5,6]
    a=int(input("\nMENU:\n1.Addition\n2.Subtraction\n3.Multipllication\n4.Float Division\n5.Floor division\n6.Modulo\n7.Power\n8.Exit\n\n Enter your choice: "))
    
    if a==8:
        print("Thank you!!!")
        break
    if a<1 or a>8:
        print("Invalid input please try again")
        continue
    
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    if a in b and y==0:
        print("Divisor cannot be zero. Invalid input!!!")
        continue
    if a == 1:
        print("Sum is",x+y)
    elif a == 2:
        print("Difference is",x-y)
    elif a == 3:
        print("Product is",x*y)
    elif a == 4:
        print("Quotient is",x/y)
    elif a == 5:
        print("Quotient is",x//y)
    elif a == 6:
        print("Remainder is",x%y)
    elif a == 7:
        print("Power is",x**y)