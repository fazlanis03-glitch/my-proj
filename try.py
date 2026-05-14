#rock, paper, scissors game
#this is the first code we had before we decided to clean it up 

import random

while True:

    users_option = input("Do you want to choose rock, paper, or scissors (r, p, s): ").lower()

    Emojis = {
    "r" : "Rock 🪨", 
    "p" : "Paper 📄",
    "s" : "Scissors ✂️"

    }

    options = ('r', 'p', 's')

    computer_choice = random.choice(options) 

    if users_option not in options:
        print("Invalid Choice ")
        continue #makes sure i keeps running
    
    print("you chose:", Emojis.get(users_option, users_option)) #this shows the users pick

    print("Computer chose:",Emojis.get(computer_choice, computer_choice)) #this shows the computers pick


    if users_option == computer_choice:
        print("It's a Tie")
    elif users_option == 'r' and computer_choice == 's':
        print("You Win")
    elif users_option == 's' and computer_choice == 'p':
        print("You Win")    
    elif users_option == 'p' and computer_choice == 'r':
        print("You Win")
    else:
        print("You Lost")


#play again step

    Again = input("Continue (y/n): ").lower()
    if Again == 'y':
        continue 
    elif Again == 'n':
        break
    else:
        print("Invalid input, select (y,n)")