import shutil
import random
import string

def Encode(a):
    if len(a)<=3:
        return a[::-1]
    else:
        return random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+a[1:]+a[0]+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)

def Decode(a):
    if len(a)<=3:
        return a[::-1]
    else:
        return a[-4]+a[3:-4]


terminal=shutil.get_terminal_size().columns
print('-'*terminal)

print("Welcome!!!")

while True:
    try:
        x=input("1.Encode a string\n2.Decode a string\n3.Exit\n\nEnter your choice: " )
        if int(x)==3:
            print("Thank you!!\n")
            break
        elif int(x)==1:
            str=input("Enter the input: ")
            print(f"Result of encoding: {Encode(str)}\n")
        elif int(x)==2:
            str=input("Enter the input: ")
            print(f"Result of decoding: {Decode(str)}\n")
        else:
            print("Invalid choice please try again!!!\n")
    except:
        print("Please enter a valid choice\n")
    finally:
        print('-'*terminal)