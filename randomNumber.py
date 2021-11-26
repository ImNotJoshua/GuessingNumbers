import random

randomNumber=random.randint(1,9)
chance=0
while chance<5:
    
    Number= int(input("Write A Number"))
    if Number == randomNumber:
        print("Congragulations! You got it right")
        break
    elif Number > randomNumber:
        print("Too high try to guess a number a bit lower")
    elif Number < randomNumber:
        print("Too low try to guess a number a bit higher")
    chance=chance+1

if chance > 5:
    print("Looks like you have run out of chances, try again")
