import random

dice= input("Do you want to roll the dice?")
rolldice="Yes"

min=1
max=6

while dice=="y" or dice=="Yes":
    no=random.randint(min, max)
    if (no==1):
        print("[0]")
        dice=input("Press y to roll again and n to exit")
    elif (no==2):
        print("[0 0]")
        dice=input("Press y to roll again and n to exit")
    elif (no==3):
        print("[0 0 0]")
        dice=input("Press y to roll again and n to exit")
    elif (no==4):
        print("[0 0 0 0]")
        dice=input("Press y to roll again and n to exit")
    elif (no==5):
        print("[0 0 0 0 0]")
        dice=input("Press y to roll again and n to exit")
    else:
        print("[0 0 0 0 0 0]")
        dice=input("Press y to roll again and n to exit")

