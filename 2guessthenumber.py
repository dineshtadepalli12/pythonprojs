import random

def guess(x):

    random_number = random.randint(1,x)
    guess = 0
    while (guess!= random_number):
        guess = int(input(f"enter a number 1 and {x}: "))
        if guess<random_number:
            print("Your guess is too low,try agian")
        elif guess>random_number:
            print("Your guess is too high,try again")
    print("You've got it right! Yay!")

guess(15)
