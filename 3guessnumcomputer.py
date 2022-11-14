import random
def computer_guess(x):

    low =1
    high = x
    feedback = " "
    while(feedback!= "c"):
        if low!= high:
            guess = random.randint(low,high)
        elif low==high:
            guess = low
        feedback = input(f"is {guess} too high (H), too low (L) or correct(C): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback =='l':
            low = guess + 1
    print("Yay , you've got it right!")

computer_guess(1000)
