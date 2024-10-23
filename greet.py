import time
# h=int(time.strftime('%H'))

h=int(input("Enter hour (24 hour format):"))

if h<12:
    print("Good morning")
elif h<17:
    print("Good afternoon")
elif h<21:
    print("Good evening")
else:
    print("Good night")