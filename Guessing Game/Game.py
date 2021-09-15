import random

num = random.randint(0,100)

while True:
    value = int(input("Enter any Number between 0-100: "))
    if value > num:
        print("Guess Lower")
    elif value < num :
        print("Guess Higher")
    else :
        print("Correct Answer ")
        break

