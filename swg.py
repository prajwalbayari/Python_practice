import random as r
import shutil

l=[1,2,3]
print(shutil.get_terminal_size().columns*'-')
print("\nWelcome to Snake Water Gun Game!!\n")

while True:
    try:
        x=input("1.Snake\n2.Water\n3.Gun\n\nEnter your choice(Enter 0 to exit):")
        y=r.randint(1,3)
        if int(x)==0:
            print("Thank you\n")
            break    
        if(int(x) not in l):
            print("Invalid choice please try again!!\n\n")
        elif int(x)==y:
            print("It's a draw!!!\n")
        elif int(x)==(y+1)%3+1:
            print("You won!!!\n")
        elif (int(x)+1)%3+1==y:
            print("Computer won!!!\n")
    except:
        print("Please enter a valid choice!!\n")
    finally:
        print(shutil.get_terminal_size().columns*'-')