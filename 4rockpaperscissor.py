import random
user_wins=0
computer_wins=0
tie = 0
while True:
    user = input("enter your choice in r,p,s to play or q to quit: ").lower()
    if user =="q":
        break
    elif (user in ['r','p','s']):
        computer = random.choice(['r','p','s'])
        print("The choice of computer is: ",computer)
        if user == computer:
            print('it\'s a tie')
            tie+=1
            print("The total number of ties are: ",tie)
        elif (user == 'r' and computer == 's') or (user == 's' and computer == "p") or (user == "p" and computer == "r"):
            print("user wins")
            user_wins+=1
            print("the total number of user wins are: ",user_wins)
        else:
            print("Computer wins")
            computer_wins += 1
            print("the total number of computer wins are: ", computer_wins)
    else:
        print("Please enter input in the 4 above mentioned characters")
        break
print("Goodday")

